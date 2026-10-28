#RETORNOS_LOGARITMICOS: variaveis de entrada: 

# {
#   "pares":{pares}, #pares a serem retornados (vazio=todos)
#   "path":path, #caminho
#   "tipo": p | ln #tipo de retorno % ou log
#}
RETORNOS = rf"""
    WITH 
    parametros AS (
        SELECT
            MAX(date_time_open) AS data_fim,
            MAX(date_time_open) - INTERVAL '5 YEARS' AS data_inicio
        FROM read_parquet(
            $path,
            hive_partitioning = true
        )
    ),
    historico AS (
        SELECT
            par,
            MIN(date_time_open) AS primeira_data,
            MAX(date_time_open) AS ultima_data
        FROM read_parquet(
            $path,
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
            AND (
                $pares IS NULL
                OR h.par IN (
                    SELECT par 
                    FROM UNNEST(CAST($pares AS VARCHAR[])) AS t(par)
            )
        )
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
            $path,
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
        CASE
            WHEN $tipo = 'p' THEN (close / close_anterior) * 100
            WHEN $tipo = 'ln' THEN LN(close / close_anterior) 
        END AS retorno
    FROM defasada;
    """
# {
#   "path":path, #caminho
#}
ANALITICO = rf"""
    WITH 
    parametros AS (
        SELECT
            MAX(date_time_open) AS data_fim,
            MAX(date_time_open) - INTERVAL '5 YEARS' AS data_inicio
        FROM read_parquet(
            $path,
            hive_partitioning = true
        )
    ),
    historico AS (
        SELECT
            par,
            MIN(date_time_open) AS primeira_data,
            MAX(date_time_open) AS ultima_data
        FROM read_parquet(
            $path,
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
            $path,
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
        (close / close_anterior) - 1 AS retorno_simples,
        LN(close / close_anterior) AS retorno
    FROM defasada;
        
"""
