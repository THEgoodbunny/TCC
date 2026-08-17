import duckdb, os,pandas as pd
from tqdm import tqdm
from zipfile import ZipFile,BadZipFile
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache
from paths import (
    PATH_BINANCE_RAW,
    PATH_BINANCE_PROCESSED
)  

# o processamento unifica os pares em tabelas long particionados em anos
#  
COLUNAS = [
        "open_time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "quote_asset_volume",
        "number_of_trades",
        "taker_buy_base_asset_volume",
        "taker_buy_quote_asset_volume"
    ]

def processar_base():
    raw = PATH_BINANCE_RAW
    separador = os.sep
    colunas = ", ".join(COLUNAS)
    processed = PATH_BINANCE_PROCESSED
    processed.mkdir(exist_ok=True,parents=True)
    
    duckdb.execute("SET enable_progress_bar = true;")       # Ativa o mecanismo
    duckdb.execute("SET enable_progress_bar_print = true;") # Garante o print no stdout
    duckdb.execute("SET progress_bar_time = 100;")         # Mostra se demorar mais de 100ms

    query = rf"""
    COPY(
        SELECT DISTINCT
            {colunas}, 
            split(filename, '{separador}')[-2] AS par,
            split(filename, '-')[-2] AS ano,
            to_timestamp(open_time/1000000) AS date_time_open
        FROM read_parquet('{raw}/*/*.parquet', filename=true)
        ORDER BY par,open_time
        )
    TO '{processed}'
    (FORMAT parquet, PARTITION_BY(ano), OVERWRITE)
    """
    duckdb.execute(query)
    print('processo encerrado')    

def main():
    processar_base()

    
if __name__ == "__main__":    
    
   main()