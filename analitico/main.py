import download_binance,processar_binance,sys, pandas as pd, duckdb,openpyxl
from paths import (PATH_LOGS,PATH_BINANCE_PROCESSED)


def query():
    path = PATH_BINANCE_PROCESSED
        
    duckdb.execute("SET enable_progress_bar = true;")       # Ativa o mecanismo
    duckdb.execute("SET enable_progress_bar_print = true;") # Garante o print no stdout
    duckdb.execute("SET progress_bar_time = 100;")         # Mostra se demorar mais de 100ms

    query = rf"""
        SELECT 
            *
        FROM read_parquet('{path}/*/*.parquet', hive_partitioning=true)
        ORDER BY par,open_time
        
    """
    return duckdb.execute(query)

def corr(): 
    tbl = query()

    df = tbl.df()

    df = df.pivot(
        index="open_time",
        columns="par",
        values="close"
    )

    df.corr().to_excel("matriz_corr.xlsx")

    main()


def atualizar():

    download_binance.atualizar_base()
    main()
def processar():
    processar_binance.processar_base()
    main()
    
def main():
    PATH_LOGS.mkdir(parents=True, exist_ok=True)

    print(
    """comandos: 
    0 - Sair
    1 - Matriz Correlação 
    2 - atualizar base (atualiza toda a base de dados 1h a partir do bucket AWS) 
    3 - processar base (executa processamento analítico) 

    -> PRIMEIRA EXECUÇÃO E AINDA NÃO TEM OS DADOS? ATUALIZE A BASE
    -> ATUALIZOU? PROCESSE A BASE
    """
    )

    while True:
        try:
            view = int(input("selecione a opção: "))
            if not view in range(0,4):
                raise
            break
        except:
            print("comando invalido ")

    match view:
        case 0:
            sys.exit()
        case 1:
            corr()
        case 2:
            atualizar()
        case 3:
            processar()


if __name__ == "__main__":    

   main()

