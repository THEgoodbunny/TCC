import duckdb
from paths import (PATH_LOGS,PATH_BINANCE_PROCESSED)
path = PATH_BINANCE_PROCESSED

query = fr"""
    DESCRIBE SELECT 
        *
    FROM read_parquet('{path}/*/*.parquet', hive_partitioning=true)
"""



query = rf"""
SELECT MIN(date_time_open)
FROM read_parquet('{path}/*/*.parquet', hive_partitioning=true)
WHERE date_time_open >= '2010-01-01'::TIMESTAMPTZ;

    """

query = rf"""
SELECT MIN(date_time_open)
FROM read_parquet('{path}/*/*.parquet', hive_partitioning=true)
WHERE ano = 2021

    """

query = rf"""
        SELECT MIN(date_time_open)
            
        FROM read_parquet('{path}/*/*.parquet', hive_partitioning=true)
        WHERE date_time_open >= CURRENT_DATE - INTERVAL '5 YEARS'
        
        
    """
duckdb.sql(query).show()