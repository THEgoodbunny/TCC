from pathlib import Path
import requests, warnings, io
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from zipfile import ZipFile

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

URL_AWS_BUCKET = (
    "https://s3-ap-northeast-1.amazonaws.com/"
    "data.binance.vision?"
    )
params = {
    "prefix":"data/spot/monthly/klines/",
    "list-type":"2",
    "delimiter":"/"
}
namespace = {"nmsp":"http://s3.amazonaws.com/doc/2006-03-01/"}

def listar_pares_aws(params):
    print("iniciada a listagem de pares...")
    keys = []
    cont = 0


    while True:
        cont+=1
        try:
            response = requests.get(
                URL_AWS_BUCKET, 
                params=params
            )
            response.raise_for_status()
            aws_xml = response.content
        except requests.exceptions.RequestException as e:
            print(f"Exceção na requisição: {e}")
            break
        parsed_xml = ET.fromstring(aws_xml)

        bool_trunc = parsed_xml.findtext("nmsp:IsTruncated",namespaces=namespace)

        continuation_token = parsed_xml.findtext("nmsp:NextContinuationToken",namespaces=namespace)  
        print(f"iteração {cont}... truncado: {bool_trunc}")

        key_list = parsed_xml.findall("nmsp:CommonPrefixes/nmsp:Prefix",namespaces=namespace)

        #estrutura das keys: data/spot/monthly/klines/ZRXBTC/
        key_pairs = [element.text.rsplit("/",2)[-2] for element in key_list if element.text and element.text.endswith("USDT/")] 

        keys.extend(key_pairs)

        #current_token = parsed_xml.findtext("nmsp:ContinuationToken",namespaces=namespace)


        if bool_trunc == "false":
            break
        params["continuation-token"] = continuation_token

    print("quantidade de iterações: ", cont)
    print("pares extraidos: ",len(keys))
    return(keys)

#REFERENCIA ENDPOINT ARQUIVOS: https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?prefix=data/spot/monthly/klines/BTCUSDT/1h/&list-type=2

def construir_prefixos(pares):
    dict_prefixos = {}
    std_uri = "data/spot/monthly/klines/"
    for par in pares:
         url = f"{std_uri}{par}/1h/"
         dict_prefixos[par] = url

    return dict_prefixos

def listar_zip_par(par, prefixo):
    zip_final_list= []
    dict_zip={}
    url = URL_AWS_BUCKET
    params = {
        "prefix": prefixo,
        "list-type":"2",
    }

    while True:
        try:
            response = requests.get(
                url=url,
                params=params
            )
            response.raise_for_status()
            aws_xml = response.content
        except requests.exceptions.RequestException as e:
            print(f"Exceção na requisição: {e}")
            break
        parsed_xml = ET.fromstring(aws_xml)

        bool_trunc = parsed_xml.findtext("nmsp:IsTruncated",namespaces=namespace)

        continuation_token = parsed_xml.findtext("nmsp:NextContinuationToken",namespaces=namespace)  

        zip_element = parsed_xml.findall("nmsp:Contents/nmsp:Key",namespaces=namespace)
   
        zip_list = [element.text for element in zip_element if element.text and element.text.endswith(".zip")]

        zip_final_list.extend(zip_list)

        #current_token = parsed_xml.findtext("nmsp:ContinuationToken",namespaces=namespace)

        params["continuation-token"] = continuation_token

        if bool_trunc == "false":
            break
    
    dict_zip[par] = zip_final_list

    print(f"{par}: {len(zip_final_list)} arquivos")

    return  dict_zip

def listar_zip(prefixos):
    with ThreadPoolExecutor() as threads:
        resultados = list(threads.map(
                listar_zip_par,prefixos.keys(),prefixos.values()
                ))
                
    print("quantidade de pares com arquivos zip: ",len(resultados))
    with open("output_zip.txt", "w",encoding="utf-8") as a:
        a.write(str(resultados))
    return resultados
   
def downloader(par,url):
    warnings.filterwarnings('ignore')
    prefixo = "http://data.binance.vision/" 
    path = PATH_BINANCE / par / "csv"
    path.mkdir(exist_ok=True,parents=True)
    url = prefixo + url
    download = requests.get(url,verify=False)
    buffer = io.BytesIO(download.content) #transforma em arquivo virtual de memoria
    arquivo = ZipFile(buffer)
    arquivo.extractall(path)
    print('processado: ', url)

def executor_threadpool(lista):
    with ThreadPoolExecutor() as threads:
        for dicionario in lista:
            for par,urls in dicionario.items():
                for url in urls:
                    threads.submit(downloader,par,url)

#def gerar_parquets(arquivos):

def main():
    pares = listar_pares_aws(params)
    prefixos = construir_prefixos(pares)
    lista_zip = listar_zip(prefixos)
    executor_threadpool(lista_zip)
    #gerar_parquets(arquivos)

if __name__ == "__main__":    
    main()