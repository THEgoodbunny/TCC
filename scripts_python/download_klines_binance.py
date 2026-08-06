from pathlib import Path
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

#definindo os caminhos relativos e criando as pastas necessárias
PATH_PARENT = Path(__file__).resolve().parent.parent
PATH_DATA = PATH_PARENT / "data"
PATH_BINANCE = PATH_DATA / "binance"
PATH_KRAKEN = PATH_DATA / "kraken"
PATH_BINANCE.mkdir(exist_ok=True,parents=True)

# -----------------OS DADOS DA BINANCE SÃO ARMAZENADOS EM UM BUCKET DA AMAZON -------------------------------------
# https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?prefix=data/spot/monthly/klines/&list-type=2
# ESSE BUCKET CONTEM OS ENDEREÇOS DE PARES E ARQUIVOS ZIP
# O ENDEREÇO É PAGINADO E PARA CONTINUAR É NECESSÁRIO OBTER O TOKEN
# list-type=2 é importante para interceptar o token pelo XML

# https://data.binance.vision/?prefix=data/spot/monthly/klines

URL_BINANCE = "https://data.binance.vision/"

URL_AWS_BUCKET = (
    "https://s3-ap-northeast-1.amazonaws.com/"
    "data.binance.vision?"

    )

params = {
    "prefix":"data/spot/monthly/klines/",
    "list-type":"2",
    "delimiter":"/"
}
keys = []
while True:

    response = requests.get(
        URL_AWS_BUCKET, 
        params=params
    )
    aws_xml = response.content
    parsed_xml = ET.fromstring(aws_xml)
    namespace = {"nmsp":"http://s3.amazonaws.com/doc/2006-03-01/"}
    bool_trunc = parsed_xml.findtext("nmsp:IsTruncated",namespaces=namespace)
    key_list = parsed_xml.findall("nmsp:CommonPrefixes/nmsp:Prefix",namespaces=namespace)
    key_pairs = [element.text for element in key_list]
    keys.append(key_pairs)
    continuation_token = parsed_xml.findtext("nmsp:NextContinuationToken",namespaces=namespace)
    current_token = parsed_xml.findtext("nmsp:ContinuationToken",namespaces=namespace)
    params["continuation-token"] = continuation_token
    print(continuation_token,"\n",bool_trunc,"\n","-"*10,current_token,"-"*10,"\n")
    if bool_trunc == "false":
        break
    continuation_token = parsed_xml.findtext("nmsp:NextContinuationToken",namespaces=namespace)
    current_token = parsed_xml.findtext("nmsp:ContinuationToken",namespaces=namespace)
    params["continuation-token"] = continuation_token


print(keys)