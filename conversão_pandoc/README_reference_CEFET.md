# Referência Pandoc CEFET-MG

## Base normativa analisada

`Manual-de-Normas_2024.pdf`, CEFET-MG, 2024, 145 páginas. As regras aplicáveis a TCC foram consolidadas especialmente das pp. 40-56 (apresentação geral), 85-100 (citações e referências), com os elementos acadêmicos definidos nas pp. 13-39.

## O que o `reference.docx` aplica automaticamente

| Elemento | Configuração incorporada |
|---|---|
| Página | A4; margens: superior/esquerda 3 cm, inferior/direita 2 cm. |
| Texto normal (`Normal`, `Body Text`) | Arial 12, preta, justificada, sem hifenização como orientação de uso, 1,5 linha, primeira linha 1,25 cm, sem espaço extra entre parágrafos. Times New Roman 12 também é permitida pelo manual, mas Arial foi a escolha fixa do modelo. |
| Seção primária (`Heading 1`) | Arial 12, negrito, caixa alta, à esquerda, início em nova página e 1,5 linha após o título. |
| Seções secundária a quinária (`Heading 2` a `Heading 5`) | Arial 12, negrito, à esquerda, sem caixa alta forçada, 1,5 linha antes e depois. |
| Título não numerado (`CEFET Unnumbered Heading`) | Arial 12, negrito, caixa alta, centralizado, em nova página. Aplicável, por exemplo, a REFERÊNCIAS, SUMÁRIO, RESUMO, APÊNDICES e ANEXOS. |
| Citação longa (`Block Text`, `Quote`) | Arial 10, simples, justificada, recuo esquerdo de 4 cm, sem aspas. |
| Legenda/fonte de ilustração (`Caption`, `Image Caption`, `CEFET Source and Legend`) | Arial 10, simples, à esquerda. O título da ilustração fica acima; fonte obrigatória, legenda e notas ficam abaixo. |
| Título de tabela (`Table Caption`) | Arial 12, 1,5 linha, à esquerda. A estrutura gráfica da tabela segue IBGE e depende do conteúdo. |
| Notas de rodapé (`Footnote Text`) | Arial 10, simples, sem espaço; recuo pendente de 0,5 cm para destacar o número e alinhar as linhas seguintes ao texto. |
| Referências (`Bibliography`, `References`) | Arial 12, à esquerda, simples, uma linha simples em branco entre referências (12 pt depois do parágrafo). A normalização bibliográfica continua sendo ABNT NBR 6023:2020. |
| Cabeçalho/página | Estilo de cabeçalho Arial 10 e campo PAGE, à direita; margem direita e distância do cabeçalho configuradas em 2 cm. |

## Regras editoriais que continuam obrigatórias

- TCC em anverso, A4, texto preto (ilustrações podem ser coloridas).
- Citações diretas curtas: dentro do parágrafo, aspas duplas e autoria/título, data e página/localização. Citações diretas longas: mais de três linhas, sem aspas, recuo de 4 cm e corpo 10.
- O CEFET-MG exige o sistema autor-data de chamada. Citações indiretas dispensam página; em citações diretas, página/localização, volume, tomo ou seção é obrigatório conforme aplicável.
- Ilustração: identificação acima, à esquerda, no formato `Figura N - Título`; fonte abaixo é obrigatória, inclusive quando a produção é do autor; legenda/notas também abaixo, se existirem. Deve ser mencionada e ficar próxima ao trecho a que se refere.
- Tabela: identificação no topo como `Tabela N - Título`; fonte no rodapé; notas geral e específica após a fonte quando necessárias; ao menos os três traços horizontais recomendados pelo IBGE (topo, cabeçalho e rodapé).
- Referências: ordem alfabética porque o sistema adotado é autor-data; alinhamento à esquerda; simples; uma linha em branco entre itens; consistência de destaque tipográfico segundo a NBR 6023.
- Alíneas usam letras minúsculas seguidas de `)`; subalíneas usam travessão e espaço. Títulos com mais de uma linha devem ter continuação sob a primeira letra da primeira palavra do título.

## Limitações do `reference.docx` e pós-processamento recomendado

Um arquivo de referência é um conjunto de propriedades e estilos OOXML. O Pandoc o usa como matriz de estilo, mas não consegue inferir a semântica institucional de uma estrutura LaTeX arbitrária. Assim, as regras abaixo não ficam plenamente garantidas só por estilos:

1. **Paginação correta.** O manual conta a partir da folha de rosto, mas mostra o número somente na primeira folha textual. O modelo contém campo PAGE em 10 pt, à direita. Após a conversão, um script deve inserir uma quebra de seção imediatamente antes da primeira seção textual, ocultar o cabeçalho da seção pré-textual e definir `PAGE` com o deslocamento correspondente às folhas já contadas.
2. **Numeração e recuo de títulos.** O Word/Pandoc pode receber o número no próprio texto ou em uma lista automática. Para reproduzir títulos longos, o pós-processador deve aplicar recuo pendente calculado após o indicativo (por exemplo, `2.3 `), preservar até a seção quinária e validar ausência de ponto/hífen entre o número e o título.
3. **Caixa alta somente na seção primária.** O estilo garante `Heading 1` em caixa alta; a regra não deve ser aplicada a `Heading 2`-`Heading 5`. A conversão deve mapear `\\chapter`/seção primária para `Heading 1` e as demais seções aos estilos seguintes.
4. **Cabeçalhos de figuras e tabelas.** Pandoc nem sempre distingue título de tabela, título de figura, fonte, legenda e nota. Um filtro Lua deve emitir classes/estilos explícitos: `Table Caption`, `Image Caption` e `CEFET Source and Legend`.
5. **Filete e separação da nota de rodapé.** O Word gera o separador de notas como parte especial de `footnotes.xml`; Pandoc pode recriá-lo ao escrever as notas. O pós-processador deve substituir o separador por um filete de 5 cm, manter uma linha simples entre texto e nota e validar que não há espaço entre notas.
6. **Referências ABNT.** Estilo controla apenas aparência. Use um arquivo CSL compatível com ABNT, a base bibliográfica e validação humana para autores, títulos, datas, URLs, destaques e casos especiais da NBR 6023.
7. **Hifenização, campos e atualização.** O modelo não ativa hifenização. Campos de página e referências cruzadas devem ser atualizados no Word antes da entrega final.

### Fluxo automatizado sugerido

1. Converter com Pandoc usando `--reference-doc=reference.docx` e um filtro Lua que aplique os estilos explícitos para citação longa, título/fonte/legenda de figura, título/fonte/notas de tabela e títulos não numerados.
2. Rodar um pós-processador OOXML (Python com `python-docx` e `lxml`) para: localizar a primeira seção textual; criar a quebra de seção e paginação; aplicar os recuos pendentes dos títulos; ajustar `footnotes.xml`; e normalizar tabela/legendas.
3. Abrir no Word, atualizar todos os campos (`Ctrl+A`, `F9`) e fazer inspeção visual. Confirmar especialmente a primeira página textual, cada nota de rodapé, tabela dividida, figura/legenda e a lista de referências.
