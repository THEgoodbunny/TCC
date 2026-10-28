import download_binance,processar_binance,sys, pandas as pd, duckdb,openpyxl, pathlib #pylint: disable=unused-import
from paths import (PATH_LOGS,PATH_BINANCE_PROCESSED)
import numpy as np
import plotly.express as px
from class_query_router import QueryRouter
from datetime import datetime

def corr(pares=[]) -> None: 
    now = datetime.now()
    f = now.strftime("%Y-%m-%d_%Hh%Mm%Ss")
    q = QueryRouter()
    print('matriz corr...')
    if not pares:
        df = q.retornos("ln")
        nome = "matriz_corr_pares"
    else:
        df = q.retornos("ln",pares)
        nome = "matriz_corr_completa"

    df = df.pivot(
        index="date_time_open",
        columns="par",
        values="retorno"
    )
    path = pathlib.Path(__file__).resolve().parent.parent
    df_corr = df.corr()
    df_corr.to_excel(path / f"{nome}-{f}.xlsx")
    print('exportado com sucesso\n')
    
    return df_corr
    
def hist(): 
    print("histograma correlações...")
    q = QueryRouter()
    df = q.retornos("ln")

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
            processo = int(input("selecione a opção: "))
            if not processo in range(0,5):
                raise ValueError #pylint: disable1=misplaced-bare-raise
            
        except:
            print("comando invalido ")
            continue

        match processo:
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