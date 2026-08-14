from pathlib import Path
import requests, warnings, io, pyarrow.csv, pyarrow.parquet, shutil, time, concurrent.futures 
import xml.etree.ElementTree as ET
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from zipfile import ZipFile,BadZipFile
from datetime import datetime

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
    
    params = params.copy()

    cont = 0

    while True:
        cont+=1
        for tentativa in range(1,6):
            try:
                response = requests.get(
                    URL_AWS_BUCKET, 
                    params=params,
                    timeout=30
                )
                response.raise_for_status()
                aws_xml = response.content
                break

            except requests.exceptions.RequestException as e:
                print(
                    f"Erro na iteração {cont}, "
                    f"tentativa {tentativa}/5: {e}"                
                )

                if tentativa == 5:
                    raise

                time.sleep(2**(tentativa-1))

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
        for tentativa in range(1,6):
            try:
                response = requests.get(
                    url=url,
                    params=params,
                    timeout=30
                )
                response.raise_for_status()
                aws_xml = response.content
                break
            except requests.exceptions.RequestException as e:
                print(f"Exceção na requisição tentativa {tentativa}/5: {e}")

                if tentativa == 5:
                    raise
                
                time.sleep(2**(tentativa-1))

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

    with ThreadPoolExecutor(max_workers=32) as threads:
        resultados = list(threads.map(
                listar_zip_par,prefixos.keys(),prefixos.values()
                ))

    print("quantidade de pares com arquivos zip: ",len(resultados))
    with open("output_zip.txt", "w",encoding="utf-8") as a:
        a.write(str(resultados))
    return resultados
   
def downloader(par,url):
    warnings.filterwarnings('ignore')

    prefixo = "https://data.binance.vision/" 

    path = PATH_BINANCE / par / "csv"

    path.mkdir(exist_ok=True,parents=True)

    url = prefixo + url

    for tentativa in range(1,6):
        try:
            download = requests.get(url,timeout=30)

            download.raise_for_status()

            buffer = io.BytesIO(download.content) #transforma em arquivo virtual de memoria

            with ZipFile(buffer) as arquivo:
                arquivo.extractall(path)
            
            return
            
        except(requests.exceptions.RequestException, BadZipFile) as e:
            print(f"erro tentativa {tentativa}/5: {e}")

            if tentativa ==5:
                raise
            time.sleep(2**(tentativa-1))

def executor_threadpool(lista):
    futures = {}
    with ThreadPoolExecutor() as threads:
        for dicionario in lista:
            for par,urls in dicionario.items():
                for url in urls:
                    future = threads.submit(downloader,par,url)
                    futures[future] = (par,url)
        erros = []            
        for future in tqdm(
            concurrent.futures.as_completed(futures), 
            total=len(futures)
            ):
            try:
                future.result()
            except Exception as e:
                par,url = futures[future]
                erros.append((par,url,e))
    return erros

def gerar_parquets():
    
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
        "taker_buy_quote_asset_volume",
        "ignore",
    ]
    path_data = PATH_BINANCE
    for arquivo in path_data.glob("*/csv/*.csv"):

        final_path = arquivo.parent.parent

        csv = pyarrow.csv.read_csv(
            arquivo, read_options=pyarrow.csv.ReadOptions(column_names=COLUNAS)
        )
        
        pyarrow.parquet.write_table(csv, rf"{final_path}\{arquivo.stem}.parquet" ) 
        #"stem" pega somente a parte descritiva do nome antes da extensão
        
        print(arquivo.stem, "done")

def deletar_csv():
    for pasta in PATH_BINANCE.rglob("csv"):
        for item in pasta.iterdir():
            if item.is_file() or item.is_symlink():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)

def main():
    pares = listar_pares_aws(params)

    prefixos = construir_prefixos(pares)

    lista_zip = listar_zip(prefixos)

    erros = executor_threadpool(lista_zip)

    gerar_parquets()

    deletar_csv()
    if erros:
        print('arquivos que não baixaram: ',erros)
        now = datetime.now()
        format_time = now.strftime('%d-%m-%Y_%Hhr_%Mmin_%Sseg')
        log_path = Path(__file__).resolve().parent / f"erros_download{format_time}.log"
        with open(log_path, "w", encoding="utf-8") as arquivo:
            for par,url in erros.items():
                arquivo.write(f"{par}: {url}\n")

    else:
        print("sucesso (eu acho)")


if __name__ == "__main__":    

   main()
   #deletar_csv()