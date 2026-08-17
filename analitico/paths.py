from pathlib import Path

#definindo os caminhos relativos

PATH_ANALITICO = Path(__file__).resolve().parents[0]
PATH_ROOT = PATH_ANALITICO.parent

PATH_LOGS = PATH_ANALITICO / "logs"

PATH_DATA = PATH_ROOT / "data"

PATH_BINANCE = PATH_DATA / "binance" 
PATH_BINANCE_RAW = PATH_BINANCE / "raw"
PATH_BINANCE_PROCESSED = PATH_BINANCE / "processed"

#VAI SER IMPLEMENTADO QUANDO PRECISAR DE PAREAR 1:1 COM O USD
PATH_KRAKEN = PATH_DATA / "kraken"