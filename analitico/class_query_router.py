from paths import (PATH_LOGS,PATH_BINANCE_PROCESSED)
import duckdb, queries

class QueryExec:

    def __init__(self):
        self.conn = duckdb.connect()
        
        self.conn.execute("SET enable_progress_bar = true;")       # Ativa o mecanismo
        self.conn.execute("SET enable_progress_bar_print = true;") # Garante o print no stdout
        self.conn.execute("SET progress_bar_time = 100;")  
    
    def executar(self,sql,parametros=None):
        return self.conn.execute(sql,parametros or []).df()

    def fechar(self):
        self.conn.close()

class QueryRouter:

    def __init__(self):
        self.path = PATH_BINANCE_PROCESSED

    def retornos(self,tipo,pares=None):
        executor = QueryExec()
        try:
            resultado = executor.executar(
                queries.RETORNOS, 
                {
                    "path": str(self.path / "*" / "*.parquet"),
                    "pares": pares,
                    "tipo": tipo
                }
            )

            return resultado
        finally:
            executor.fechar()

    def analitico(self):
        executor = QueryExec()
        try:
            resultado = executor.executar(
                queries.ANALITICO,
                {
                    "path": str(self.path / "*" / "*.parquet")
                }
            )
            return resultado
        finally:
            executor.fechar()