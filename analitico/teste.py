import io
import zipfile
import requests
import pandas as pd


URL = (
    "https://data.binance.vision/data/spot/monthly/klines/"
    "JUVUSDT/1h/JUVUSDT-1h-2022-03.zip"
)


def main():

    print("Baixando ZIP original da Binance...")

    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:

        print("\n=== ARQUIVOS DENTRO DO ZIP ===")
        print(zip_file.namelist())

        csv_name = zip_file.namelist()[0]

        with zip_file.open(csv_name) as csv_file:

            df = pd.read_csv(
                csv_file,
                header=None
            )

    print("\n=== TOTAL DE LINHAS NO CSV ORIGINAL ===")
    print(len(df))

    print("\n=== OPEN_TIME ÚNICOS ===")
    print(df[0].nunique())

    print("\n=== DUPLICATAS ===")

    duplicados = (
        df.groupby(0)
        .size()
        .loc[lambda x: x > 1]
    )

    print(duplicados.head(20))

    print("\n=== RESUMO ===")
    print(f"Linhas:            {len(df)}")
    print(f"Open times únicos: {df[0].nunique()}")
    print(f"Excedentes:        {len(df) - df[0].nunique()}")


if __name__ == "__main__":
    main()