import duckdb,pandas as pd
import gc
gc.collect()

from paths import (
    PATH_BINANCE_PROCESSED
)  

# Montar df para volumetria
# Montar df para retorno

def gerar_df():

    path = PATH_BINANCE_PROCESSED
    duckdb.execute("SET enable_progress_bar = true;")       # Ativa o mecanismo
    duckdb.execute("SET enable_progress_bar_print = true;") # Garante o print no stdout
    duckdb.execute("SET progress_bar_time = 100;")         # Mostra se demorar mais de 100ms

    query = rf"""
    WITH 
    parametros AS (
        SELECT
            MAX(date_time_open) AS data_fim,
            MAX(date_time_open) - INTERVAL '5 YEARS' AS data_inicio
        FROM read_parquet(
            '{path}/*/*.parquet',
            hive_partitioning = true
        )
    ),
    historico AS (
        SELECT
            par,
            MIN(date_time_open) AS primeira_data,
            MAX(date_time_open) AS ultima_data
        FROM read_parquet(
            '{path}/*/*.parquet',
            hive_partitioning = true
        )
        GROUP BY par
    ),
    elegiveis AS (
        SELECT
            h.par
        FROM historico h
        CROSS JOIN parametros p
        WHERE
            h.primeira_data <= p.data_inicio
            AND h.ultima_data >= p.data_fim - INTERVAL '1 HOUR'
    ),
    base AS (
        SELECT
            d.par,
            d.date_time_open,
            d.open,
            d.high,
            d.low,
            d.close,
            d.volume,
            d.quote_asset_volume,
            d.number_of_trades,
            d.taker_buy_base_asset_volume,
            d.taker_buy_quote_asset_volume
        FROM read_parquet(
            '{path}/*/*.parquet',
            hive_partitioning = true
        ) d
        CROSS JOIN parametros p
        WHERE
            d.par IN (SELECT par FROM elegiveis)
            AND d.date_time_open BETWEEN p.data_inicio AND p.data_fim
    ),

    defasada AS (
        SELECT
            *,
            LAG(close) OVER (
                PARTITION BY par
                ORDER BY date_time_open
            ) AS close_anterior
        FROM base
    )

    SELECT
        par,
        date_time_open,
        open,
        high,
        low,
        close,
        volume,
        quote_asset_volume,
        number_of_trades,
        taker_buy_base_asset_volume,
        taker_buy_quote_asset_volume,
        LN(close / close_anterior) AS retorno
    FROM defasada;
        """
    q = duckdb.execute(query)
    return q.df()
    
df = gerar_df()
df.shape

df.sort_values(["par","date_time_open"],inplace=True)



df["intervalo"] = (
    df.groupby("par")["date_time_open"]
      .diff()
)
print("pares analisados: ",df["par"].nunique())

print(df["intervalo"].value_counts().sort_index())

df_quali_gaps = df.loc[
    df["intervalo"] > pd.Timedelta(hours=1),
    ["par", "date_time_open", "intervalo"]
]

col_vol = "quote_asset_volume"
df_media_ativo = df.groupby("par")[col_vol].mean()

vol_medio_global = df[col_vol].mean()

print(f"""volume medio em valor de USDT por candle: {vol_medio_global}""")

analise_par = df.groupby("par").agg(
    maior_gap = ("intervalo","max"),
    quantidade_gaps = (
        "intervalo", 
        lambda x: (x > pd.Timedelta(1,'hour')).sum()
        ),
    volume_medio = (col_vol,'mean')
    )

analise_par['relacao_volume_global'] = analise_par["volume_medio"] / vol_medio_global *100

# NA ANÁLISE FOI NOTADA UMA FORTE RECORRENCIA DE ATIVOS COM GAP 
# MAXIMO DE 5 HORAS E 3 OCORRENCIAS DE GAPS, UMA ANALISE SERÁ DEDICADA A ISSO A FRENTE

picos_de_gaps = df_quali_gaps.groupby("date_time_open").size().sort_values(ascending=False)
print(picos_de_gaps)

# A analise confirma que a grande maioria de gaps ocorreram no mesmo horário
# OS GAPS COINCIDEM COM EVENTOS DE SUSPENÇÃO DO SPOT TRADING NA PLATAFORMA BINANCE

from pathlib import Path
path = Path(__file__).resolve().parent
analise_par.to_excel(path / 'analise_pares.xlsx')
print('fim')
gc.collect()

