import duckdb,pandas as pd
import gc, plotly.express as px
import plotly.io as pio
import requests 
from class_query_router import QueryRouter
from paths import (
    PATH_BINANCE_PROCESSED
)  
from main import corr

pio.renderers.default = "png"
gc.collect()
# Montar df para volumetria
# Montar df para retorno

q = QueryRouter()
df = q.analitico()
df.shape

df.sort_values(["par","date_time_open"],inplace=True)

df["intervalo"] = (
    df.groupby("par")["date_time_open"]
      .diff()
)
print("pares analisados: ",df["par"].nunique())

print(df["intervalo"].value_counts().sort_index())

df_quali_gaps = df.loc[
    df["intervalo"] > pd.Timedelta(hours=1),
    ["par", "date_time_open", "intervalo"]
]

col_vol = "quote_asset_volume"
df_media_ativo = df.groupby("par")[col_vol].mean()

vol_medio_global = df[col_vol].mean()

print(f"""volume medio em valor de USDT por candle: {vol_medio_global}""")

analise_par = df.groupby("par").agg(
    maior_gap = ("intervalo","max"),
    quantidade_gaps = (
        "intervalo", 
        lambda x: (x > pd.Timedelta(1,'hour')).sum()
        ),
    volume_medio = (col_vol,'mean')
    )

analise_par['relacao_volume_global'] = analise_par["volume_medio"] / vol_medio_global *100

# NA ANÁLISE FOI NOTADA UMA FORTE RECORRENCIA DE ATIVOS COM GAP 
# MAXIMO DE 5 HORAS E 3 OCORRENCIAS DE GAPS, UMA ANALISE SERÁ DEDICADA A ISSO A FRENTE

picos_de_gaps = df_quali_gaps.groupby("date_time_open").size().sort_values(ascending=False)
print(picos_de_gaps)

# A analise confirma que a grande maioria de gaps ocorreram no mesmo horário
# OS GAPS COINCIDEM COM EVENTOS DE SUSPENÇÃO DO SPOT TRADING NA PLATAFORMA BINANCE

from pathlib import Path
path = Path(__file__).resolve().parent

# criação da matriz corr com base no top 20 volume de pares
selecao = analise_par.sort_values(by="relacao_volume_global",ascending=False).head(20)

str_pares = [ f"{valor}" for valor in selecao.index]
print(str_pares)

# %%
#  -----------------------------  #
# |     CORRELACAO DOS TOP 20   | #
#  -----------------------------  #
df_corr = corr(str_pares)
fig = px.imshow(
    df_corr,
    text_auto=".2f",
    color_continuous_scale="Spectral",
    zmin=-1,
    zmax=1,
    color_continuous_midpoint=0,
    title="Mapa de Calor de Correlação",
    aspect="equal"
)

fig.update_layout(
    width=1100,
    height=1000,
    margin=dict(
        l=120,
        r=80,
        t=80,
        b=140
    ),
    xaxis_title="",
    yaxis_title=""
)

fig.update_xaxes(
    tickangle=-45
)

fig.update_traces(
    textfont_size=11
)

fig.show()
analise_par.to_excel(path / 'analise_pares.xlsx')

#%%
#  -------------------------------  #
# | ESTATÍSTICAS DE RISCO-RETORNO | #
#  -------------------------------  #

estatisticas = (
    df.groupby("par")["retorno"]
      .agg(
          mu="mean",
          sigma="std"
      )
)

print(estatisticas)

import numpy as np

HORAS_ANO = 24 * 365

estatisticas["mu_anual"] = (
    estatisticas["mu"] * HORAS_ANO
)

estatisticas["sigma_anual"] = (
    estatisticas["sigma"] * np.sqrt(HORAS_ANO)
)

print('fim')
gc.collect()

#%%
import requests
#  -------------------------------  #
# |       INDICE DE SHARPE        | #
#  -------------------------------  #

# ENDPOINT SELIC: https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&dataInicial=01/01/2026&dataFinal=17/09/2026

selic = requests.get(
    url="https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&dataInicial=01/01/2026&dataFinal=17/09/2026"
)

selic = selic.json()[-1]["valor"]
print(selic)

# %%
