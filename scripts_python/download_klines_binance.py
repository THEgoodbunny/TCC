from pathlib import Path
import requests
from bs4 import BeautifulSoup


#definindo os caminhos relativos e criando as pastas necessárias
PATH_PARENT = Path(__file__).resolve().parent.parent
PATH_DATA = PATH_PARENT / "data"
PATH_BINANCE = PATH_DATA / "binance"
PATH_KRAKEN = PATH_DATA / "kraken"
PATH_BINANCE.mkdir(exist_ok=True,parents=True)

# https://data.binance.vision/?prefix=data/spot/monthly/klines
URL_BINANCE = "https://data.binance.vision/"

response = requests.get(
    URL_BINANCE,
    params= {"prefix": "data/spot/monthly/klines"}
)

# <a href="https://data.binance.vision/?prefix=data/spot/monthly/klines/0GFDUSD/">0GFDUSD/</a> — estrutura HTML Binance Data

soup = BeautifulSoup(response.content,features="html.parser")
print(soup.prettify())