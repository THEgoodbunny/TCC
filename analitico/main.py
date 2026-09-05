import download_binance,processar_binance,sys, pandas as pd, duckdb,openpyxl, pathlib #pylint: disable=unused-import
from paths import (PATH_LOGS,PATH_BINANCE_PROCESSED)
import numpy as np
import plotly.express as px


def query(pares=None):
    path = PATH_BINANCE_PROCESSED        
    duckdb.execute("SET enable_progress_bar = true;")       # Ativa o mecanismo
    duckdb.execute("SET enable_progress_bar_print = true;") # Garante o print no stdout
    duckdb.execute("SET progress_bar_time = 100;")         # Mostra se demorar mais de 100ms
    if pares is None:
        query = rf"""
            WITH parametros AS (
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
            
            cobertura AS (
                SELECT
                    d.par,
                    COUNT(DISTINCT d.date_time_open) AS qtd_candles
                FROM read_parquet(
                    '{path}/*/*.parquet',
                    hive_partitioning = true
                ) d
                CROSS JOIN parametros p
                WHERE d.date_time_open BETWEEN p.data_inicio AND p.data_fim
                GROUP BY d.par
            ),
            
            elegiveis AS (
                SELECT
                    h.par
                FROM historico h
                JOIN cobertura c USING (par)
                CROSS JOIN parametros p
                WHERE
                    h.primeira_data <= p.data_inicio
                    AND h.ultima_data >= p.data_fim - INTERVAL '1 HOUR'
                    AND c.qtd_candles >=
                        0.99 * (
                            DATE_DIFF('hour', p.data_inicio, p.data_fim) + 1
                        )
            ),
            base AS (
                SELECT
                    d.par,
                    d.date_time_open,
                    CAST(d.close AS DOUBLE) AS close
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
                LN(close / close_anterior) AS retorno
            FROM defasada
            WHERE close_anterior IS NOT NULL;
        """
        query = duckdb.execute(query)
    else:
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
            WHERE 1=1
                AND h.primeira_data <= p.data_inicio
                AND h.ultima_data >= p.data_fim - INTERVAL '1 HOUR'
                AND h.par IN (SELECT par FROM UNNEST(?) as t(par))
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
        query = duckdb.execute(query, [pares])
    return query

def corr(pares=[]) -> None: 
    print('matriz corr...')
    if not pares:
        tbl = query()
    else:
        tbl = query(pares)

    df = tbl.df()
    df = df.pivot(
        index="date_time_open",
        columns="par",
        values="retorno"
    )
    path = pathlib.Path(__file__).resolve().parent
    df_corr = df.corr()
    df_corr.to_excel(path / "matriz_corr{pares}.xlsx")
    print('exportado com sucesso\n')
    
    return df_corr
def hist(): 
    print("histograma correlações...")

    df = query().df()

    retornos = df.pivot(
        index="date_time_open",
        columns="par",
        values="retorno"
    )

    matriz = retornos.corr()

    mask = np.triu(
        np.ones(matriz.shape, dtype=bool),
        k=1
    )

    correlacoes = (
        matriz
        .where(mask)
        .rename_axis(index="ativo_1", columns="ativo_2")
        .stack()
        .reset_index(name="correlacao")
    )

    fig = px.histogram(
        correlacoes,
        x="correlacao",
        nbins=20,
        title="Distribuição das correlações entre retornos"
    )

    fig.update_layout(
        xaxis_title="Correlação",
        yaxis_title="Quantidade de pares"
    )
    fig.show()

def atualizar():
    download_binance.atualizar_base()

def processar():
    processar_binance.processar_base()
    
def main():
    PATH_LOGS.mkdir(parents=True, exist_ok=True)

    while True:
        
        print(
        """comandos: 
        0 - Sair
        1 - Matriz Correlação 
        2 - atualizar base (atualiza toda a base de dados 1h a partir do bucket AWS) 
        3 - processar base (executa processamento analítico) 
        4 - vizualizar histograma de correlação
        -> PRIMEIRA EXECUÇÃO E AINDA NÃO TEM OS DADOS? ATUALIZE A BASE
        -> ATUALIZOU? PROCESSE A BASE
        """
        )
            
        try:
            view = int(input("selecione a opção: "))
            if not view in range(0,5):
                raise ValueError #pylint: disable1=misplaced-bare-raise
            
        except:
            print("comando invalido ")
            continue

        match view:
            case 0:
                break
            case 1:
                corr()
            case 2:
                atualizar()
            case 3:
                processar()
            case 4:
                hist()

if __name__ == "__main__":    
    main()