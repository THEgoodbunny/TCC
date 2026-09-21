from pathlib import Path
import argparse
import json
import unicodedata

import numpy as np
import pymupdf
from sentence_transformers import SentenceTransformer


ROOT = Path(
    "/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA"
)

INDEX_DIR = Path.home() / ".cache" / "tcc-semantic"

MODEL_NAME = "intfloat/multilingual-e5-small"

EMBEDDINGS_FILE = INDEX_DIR / "embeddings.npy"
METADATA_FILE = INDEX_DIR / "metadata.json"


def chunk_text(text, chunk_words=180, overlap_words=40):
    words = text.split()

    if not words:
        return []

    chunks = []
    step = chunk_words - overlap_words

    for start in range(0, len(words), step):
        chunk = words[start:start + chunk_words]

        if len(chunk) < 40:
            continue

        chunks.append(" ".join(chunk))

    return chunks


def normalize_lexical(text):
    """Normaliza texto para comparação lexical simples e tolerante a acentos."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return " ".join(text.casefold().split())


def build_index():
    INDEX_DIR.mkdir(parents=True, exist_ok=True)

    model = SentenceTransformer(MODEL_NAME)

    texts = []
    metadata = []

    pdfs = sorted(ROOT.rglob("*.pdf"))

    print(f"{len(pdfs)} PDFs encontrados.")

    for i, pdf in enumerate(pdfs, start=1):
        print(f"[{i}/{len(pdfs)}] {pdf.relative_to(ROOT)}")

        try:
            with pymupdf.open(pdf) as doc:
                for page_number, page in enumerate(doc, start=1):
                    text = page.get_text(
                        "text",
                        sort=True,
                    ).strip()

                    if not text:
                        continue

                    for chunk in chunk_text(text):
                        texts.append("passage: " + chunk)

                        metadata.append({
                            "file": str(pdf.relative_to(ROOT)),
                            "page": page_number,
                            "text": chunk,
                        })

        except Exception as exc:
            print(f"ERRO: {pdf}: {exc}")

    if not texts:
        raise RuntimeError("Nenhum texto foi extraído.")

    print(f"\nGerando embeddings de {len(texts)} trechos...")

    embeddings = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=True,
        normalize_embeddings=True,
    )

    np.save(
        EMBEDDINGS_FILE,
        embeddings.astype("float32"),
    )

    METADATA_FILE.write_text(
        json.dumps(
            metadata,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"\nÍndice salvo em: {INDEX_DIR}")


def load_index():
    if not EMBEDDINGS_FILE.exists() or not METADATA_FILE.exists():
        raise RuntimeError(
            "Índice não encontrado. Execute primeiro o comando 'index'."
        )

    embeddings = np.load(EMBEDDINGS_FILE)
    metadata = json.loads(
        METADATA_FILE.read_text(encoding="utf-8")
    )

    if len(embeddings) != len(metadata):
        raise RuntimeError(
            "Índice inconsistente: embeddings e metadados têm tamanhos diferentes. "
            "Reconstrua com o comando 'index'."
        )

    return embeddings, metadata


def semantic_scores(query, embeddings):
    model = SentenceTransformer(MODEL_NAME)

    query_embedding = model.encode(
        ["query: " + query],
        normalize_embeddings=True,
    )[0]

    return embeddings @ query_embedding


def select_results(order, scores, metadata, top_k=10, per_file=1):
    """Seleciona os melhores chunks, limitando quantos podem vir de cada PDF."""
    results = []
    count_by_file = {}

    for idx in order:
        idx = int(idx)
        item = metadata[idx]
        filename = item["file"]

        count = count_by_file.get(filename, 0)
        if count >= per_file:
            continue

        results.append((float(scores[idx]), item))
        count_by_file[filename] = count + 1

        if len(results) >= top_k:
            break

    return results


def print_results(results):
    if not results:
        print("Nenhum resultado encontrado.")
        return

    for rank, (score, item) in enumerate(results, start=1):
        snippet = " ".join(item["text"].split())[:700]

        print()
        print(
            f"{rank:02d}. {score:.4f} | "
            f"{item['file']} | pág. {item['page']}"
        )
        print(f"    {snippet}")


def search(query, top_k=10, per_file=1):
    embeddings, metadata = load_index()
    scores = semantic_scores(query, embeddings)
    order = np.argsort(scores)[::-1]

    results = select_results(
        order,
        scores,
        metadata,
        top_k=top_k,
        per_file=per_file,
    )
    print_results(results)


def hybrid_search(
    query,
    terms,
    top_k=10,
    per_file=1,
    require_all=False,
):
    """
    Primeiro filtra chunks por termos literais; depois os ordena semanticamente.

    Por padrão, basta um dos termos aparecer no chunk. Com --all-terms,
    todos os termos precisam aparecer no mesmo chunk.
    """
    embeddings, metadata = load_index()

    normalized_terms = [
        normalize_lexical(term)
        for term in terms
        if term.strip()
    ]

    if not normalized_terms:
        raise ValueError("Informe ao menos um termo em --terms.")

    candidate_indices = []

    for idx, item in enumerate(metadata):
        text = normalize_lexical(item["text"])
        matches = [term in text for term in normalized_terms]

        accepted = all(matches) if require_all else any(matches)
        if accepted:
            candidate_indices.append(idx)

    candidate_files = {
        metadata[idx]["file"]
        for idx in candidate_indices
    }

    mode = "TODOS" if require_all else "QUALQUER"
    print(
        f"Filtro lexical ({mode} dos termos): "
        f"{len(candidate_indices)} chunks em {len(candidate_files)} PDFs."
    )

    if not candidate_indices:
        print("Nenhum chunk passou pelo filtro lexical.")
        return

    scores = semantic_scores(query, embeddings)

    # Ordena somente os chunks que passaram pelo filtro lexical.
    order = sorted(
        candidate_indices,
        key=lambda idx: float(scores[idx]),
        reverse=True,
    )

    results = select_results(
        order,
        scores,
        metadata,
        top_k=top_k,
        per_file=per_file,
    )
    print_results(results)


def add_common_result_args(parser):
    parser.add_argument(
        "-n",
        "--top",
        type=int,
        default=10,
        help="Quantidade total de trechos exibidos (padrão: 10).",
    )
    parser.add_argument(
        "--per-file",
        type=int,
        default=1,
        help="Máximo de trechos exibidos por PDF (padrão: 1).",
    )


def main():
    parser = argparse.ArgumentParser(
        description="Busca semântica e híbrida no repositório de PDFs do TCC."
    )

    sub = parser.add_subparsers(
        dest="command",
        required=True,
    )

    sub.add_parser(
        "index",
        help="Extrai os PDFs e reconstrói o índice vetorial.",
    )

    search_parser = sub.add_parser(
        "search",
        help="Busca puramente semântica.",
    )
    search_parser.add_argument("query")
    add_common_result_args(search_parser)

    hybrid_parser = sub.add_parser(
        "hybrid",
        help="Filtra por termos literais e depois ordena semanticamente.",
    )
    hybrid_parser.add_argument("query")
    hybrid_parser.add_argument(
        "--terms",
        nargs="+",
        required=True,
        help=(
            "Termos/frases do filtro lexical. Coloque expressões com espaços "
            "entre aspas. Por padrão, basta um termo aparecer."
        ),
    )
    hybrid_parser.add_argument(
        "--all-terms",
        action="store_true",
        help="Exige que todos os termos apareçam no mesmo chunk.",
    )
    add_common_result_args(hybrid_parser)

    args = parser.parse_args()

    if args.command == "index":
        build_index()

    elif args.command == "search":
        search(
            args.query,
            top_k=args.top,
            per_file=args.per_file,
        )

    elif args.command == "hybrid":
        hybrid_search(
            args.query,
            terms=args.terms,
            top_k=args.top,
            per_file=args.per_file,
            require_all=args.all_terms,
        )


if __name__ == "__main__":
    main()
