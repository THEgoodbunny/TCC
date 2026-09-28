# Levantamento bibliográfico — Machine Learning em Finanças

## Escopo e critério de uso

Este é um catálogo para consulta posterior, não uma redação da subseção. A triagem semântica considerou o texto integral dos PDFs e a validação abaixo foi feita no corpo dos artigos indicados. Revisões são usadas para mapear literatura e taxonomias; resultados numéricos de estudos citados por essas revisões não são tratados como resultados dos autores da revisão. Estudos centrados exclusivamente em criptoativos foram deliberadamente deixados fora do núcleo deste levantamento.

## 1. Histórico e evolução

### H1 — Crescimento documentado da pesquisa em IA aplicada ao mercado acionário

**Fonte:** Ferreira, F. G. D. C.; Gandomi, A. H.; Cardoso, R. T. N. (2021), *Artificial Intelligence Applied to Stock Market Trading: A Review*.

**BibTeX key:** `ferreira2021artificial`

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/Artificial_Intelligence_Applied_to_Stock_Market_Trading_A_Review.pdf`

**Página:** PDF 2 (página impressa 30899); Figura 2 na PDF 3 (impressa 30900).

**Trecho relevante:** “2,326 documents related to the application of Artificial Intelligence in the stock market were collected.”

**O que sustenta:** A revisão fez consulta no Scopus em 27/05/2020, para documentos de 1995–2019, e reporta crescimento exponencial das publicações no período. É uma evidência bibliométrica diretamente ligada a IA/ML e negociação em mercado acionário, útil para situar a expansão do campo desde os anos 1990.

**Observações/limitações:** Conta documentos indexados no Scopus e usa consulta/critério específicos; não mede adoção por instituições financeiras nem qualidade metodológica dos estudos.

---

### H2 — Panorama recente de deep learning para previsão financeira

**Fonte:** Giantsidi, S.; Tarantola, C. (2025), *Deep learning for financial forecasting: A review of recent trends*.

**BibTeX key:** `giantsidi2025deep`

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Deep learning for financial forecasting A review of recent trends.pdf`

**Página:** PDF 1–3; Figura 11 e Tabela 7 na PDF 30.

**Trecho relevante:** “This study offers a critical review of 187 Scopus-indexed studies published between 2020 and 2024.”

**O que sustenta:** Mapeia a fase recente da literatura de DL em previsão financeira: ações, índices, câmbio, commodities, títulos, criptoativos e volatilidade. A Figura 11 apresenta a distribuição anual das publicações no recorte 2020–2024.

**Observações/limitações:** É revisão focalizada em *deep learning* e previsão, não em toda a família de ML nem em todas as decisões financeiras.

## 2. Motivação para uso de ML em finanças

### M1 — Dados complexos, não estacionários e relações não lineares

**Fonte:** Giantsidi e Tarantola (2025).

**BibTeX key:** `giantsidi2025deep`

**PDF:** mesmo de H2.

**Página:** PDF 2.

**Trecho relevante:** “Financial markets generate massive streams of complex, non-stationary data.”

**O que sustenta:** A motivação para modelos de ML/DL decorre de relações não lineares, volatilidade e padrões temporais complexos para os quais modelos estatísticos/econométricos tradicionais podem ter dificuldade. Os autores descrevem DL como alternativa para aprender dependências complexas e se adaptar a dinâmicas de mercado.

**Observações/limitações:** É uma justificativa de revisão, não uma demonstração causal de superioridade universal de DL.

---

### M2 — Heterogeneidade de fontes e pipeline de previsão

**Fonte:** Ferreira, Gandomi e Cardoso (2021).

**BibTeX key:** `ferreira2021artificial`

**PDF:** mesmo de H1.

**Página:** PDF 9–12 (impressas 30906–30909); Figura 6 na PDF 9; Tabelas 10–11 na PDF 12.

**Trecho relevante:** “The next step is to acquire the data and treat it, transforming it, and reducing unnecessary noisy information.”

**O que sustenta:** Um fluxo de ML financeiro envolve seleção/aquisição de dados, tratamento e redução de ruído, treinamento, validação de hiperparâmetros e avaliação em teste. As tabelas da revisão listam preços, volume, indicadores técnicos e fundamentos como entradas frequentes; também mapeiam variáveis de saída de previsão.

**Observações/limitações:** O fluxograma é uma síntese dos autores; não substitui uma especificação de validação temporal ou uma escolha de dados para o projeto.

## 3. Principais aplicações

### Previsão de retornos e preços

**Fonte:** Giantsidi e Tarantola (2025).

**BibTeX key:** `giantsidi2025deep`

**PDF/Página:** PDF 19, Tabela 3.

**Trecho relevante:** “Stock price forecasting emerges as the most extensively studied application.”

**Utilidade:** A Tabela 3 organiza 75 estudos de previsão de preços de ações (com sobreposição entre categorias), com LSTM como modelo isolado predominante e combinações híbridas, além de documentar uso de preço, indicadores técnicos e sentimento.

**Observações:** É uma contagem dentro da amostra da revisão; não estabelece qual arquitetura é melhor em toda condição de mercado.

---

### Volatilidade

**Fonte:** Giantsidi e Tarantola (2025).

**BibTeX key:** `giantsidi2025deep`

**PDF/Página:** PDF 1–2 e PDF 30, Tabela 7.

**Trecho relevante:** “applications across [...] cryptocurrency, and volatility.”

**Utilidade:** A revisão inclui previsão de volatilidade como domínio específico e a Tabela 7 contabiliza 10 estudos de volatilidade no conjunto de 187. Serve para situar a volatilidade como caso de uso, sem afirmar desempenho quantitativo comum entre artigos.

---

### Gestão de risco, asset allocation e portfolio optimization

**Fonte:** Jiang, Y.; Olmo, J.; Atwi, M. (2024), *Deep reinforcement learning for portfolio selection*.

**BibTeX key:** `jiang2024deep`

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Deep reinforcement learning for portfolio selection.pdf`

**Página:** PDF 1–2 e 13.

**Trecho relevante:** “Investor risk aversion and transaction cost constraints are embedded using an extended Markowitz’s mean-variance reward function.”

**Utilidade:** Exemplo de aplicação de DL/RL à alocação dinâmica: TD3 usa recompensa média-variância estendida, com aversão ao risco e custos de transação; os experimentos usam os constituintes do DJIA e S&P 100.

**Observações:** Resultado de backtest; não é evidência de desempenho realizável sem ressalvas sobre custos, escolha de amostra e validação.

---

### Portfolio optimization com previsão/seleção de ativos

**Fonte:** Wang, W. et al. (2020), *Portfolio formation with preselection using deep learning from long-term financial data*.

**BibTeX key:** `wang2020portfolio`

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Portfolio formation with preselection using deep learning from long-term financial data.pdf`

**Página:** PDF 1 e 10–12.

**Trecho relevante:** “the pre-selected assets are then used in a mean-variance portfolio selection method.”

**Utilidade:** Exemplo explícito de integração ML–decisão: LSTM prevê/pré-seleciona ativos e a seleção alimenta a etapa média-variância. A amostra é composta pelas 100 ações da UK Stock Exchange, março de 1994 a março de 2019.

**Observações:** É um desenho aplicado a ações do Reino Unido; os ganhos e custos dependem da janela, cardinalidade e hipóteses de custo do estudo.

---

### Portfolio optimization com seleção preditiva por rede neural

**Fonte:** Chaweewanchon, A.; Chaysiri, R. (2022), *Markowitz Mean-Variance Portfolio Optimization with Predictive Stock Selection Using Machine Learning*.

**BibTeX key:** `chaweewanchon2022markowitz`

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Markowitz Mean-Variance Portfolio Optimization with Predictive Stock Selection Using Machine Learning.pdf`

**Página:** PDF 1, 13–17.

**Trecho relevante:** “R-CNN-BiLSTM is used to select stocks and Markowitz’s mean-variance method is then used to optimize the portfolio.”

**Utilidade:** Demonstra a divisão funcional entre ML para seleção/predição e MV para pesos. O estudo trabalha com ações tailandesas e compara R-CNN-BiLSTM, LSTM, CNN-BiLSTM e BiLSTM na etapa de previsão.

**Observações:** Os próprios autores limitam a generalização ao mercado tailandês e registram ausência de variáveis exógenas, análise de complexidade e busca sistemática de hiperparâmetros.

---

### Trading quantitativo e decisões dinâmicas de carteira

**Fonte:** Jang, J.; Seong, N. Y. (2023), *Deep reinforcement learning for stock portfolio optimization by connecting with modern portfolio theory*.

**BibTeX key:** `jang2023deep`

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Deep reinforcement learning for stock portfolio optimization by connecting with modern portfolio theory.pdf`

**Página:** PDF 1 e 10–11.

**Trecho relevante:** “The proposed model dynamically determines the portfolio weights.”

**Utilidade:** Exemplo de RL conectado à MPT para rebalanceamento/decisão de pesos, avaliado contra estratégias de referência em ações.

**Observações:** A comparação é de backtest em janelas específicas e os autores observam complexidade do modelo e não determinismo do treinamento de RL.

---

### Sentimento e dados alternativos

**Fonte:** Ferreira, Gandomi e Cardoso (2021).

**BibTeX key:** `ferreira2021artificial`

**PDF/Página:** PDF 12 (impressa 30909) e PDF 17 (impressa 30914).

**Trecho relevante:** “Financial sentiment analysis applies the techniques from the area of Natural Language Processing.”

**Utilidade:** A revisão identifica notícias, redes sociais, fóruns e blogs como fontes de texto para inferir sentimento, e separa a análise de sentimento como uma das quatro grandes categorias de IA no trading acionário.

**Observações:** Os percentuais de retorno/acurácia descritos na seção são resumos de artigos referenciados pela revisão; para uso empírico, deve-se consultar os originais.

## 4. Limitações e desafios

### L1 — Não estacionariedade, ruído e quebras estruturais

**Fonte:** Giantsidi e Tarantola (2025).

**BibTeX key:** `giantsidi2025deep`

**PDF/Página:** PDF 37.

**Trecho relevante:** “Regime shifts and structural breaks often lead to poor generalization.”

**O que sustenta:** Mercados não estacionários, voláteis e ruidosos dificultam a estabilidade de modelos treinados em regimes anteriores.

---

### L2 — Overfitting, validação temporal e vieses de dados

**Fonte:** Giantsidi e Tarantola (2025).

**BibTeX key:** `giantsidi2025deep`

**PDF/Página:** PDF 36–37.

**Trecho relevante:** “random splits can introduce look-ahead bias.”

**O que sustenta:** Diferenças de conjunto de dados, pré-processamento e validação comprometem comparabilidade; os autores destacam risco de *look-ahead bias*, sobreajuste, *survivorship bias* e uso de dados revisados.

**Observações/limitações:** É diagnóstico de revisão; não quantifica a incidência de cada viés na literatura.

---

### L3 — Interpretabilidade e robustez em condições extremas

**Fonte:** Giantsidi e Tarantola (2025).

**BibTeX key:** `giantsidi2025deep`

**PDF/Página:** PDF 2, 35 e 37.

**Trecho relevante:** “Interpretability remains a major barrier.”

**O que sustenta:** Modelos de DL podem operar como caixas-pretas; a revisão identifica falta de testes de estresse, fragilidade em extremos e barreiras de implantação computacional/tempo real.

---

### L4 — Custos de transação, risco e seleção da amostra em RL

**Fonte:** Jiang, Olmo e Atwi (2024).

**BibTeX key:** `jiang2024deep`

**PDF/Página:** PDF 2 e 9–13.

**Trecho relevante:** “transaction costs and risk aversion should be considered.”

**O que sustenta:** Em portfolio RL, omitir custos e preferências de risco pode tornar o objetivo pouco realista; os resultados também dependem da seleção de dados históricos para treinamento/validação/teste.

## 5. Evidências quantitativas

### Q1 — Mapeamento recente por domínio e métricas de previsão

**Fonte:** Giantsidi e Tarantola (2025).

**Problema:** panorama de DL para previsão financeira.

**Amostra/período:** 187 estudos Scopus, 2020–2024.

**Modelo:** revisão sistemática de estudos de DL.

**Benchmark:** não aplicável; é contagem de literatura.

**Métrica:** frequência de domínios, arquiteturas, entradas e métricas reportadas.

**Resultado:** Tabela 7: 75 estudos de previsão de preços de ações, 83 de índices, 11 de câmbio, 8 de commodities, 2 de títulos, 23 de cripto e 10 de volatilidade (há sobreposição de aplicações). Tabela 3: entre estudos de preço de ações, RMSE aparece em 42/75 (56%), MAE em 35/75 (47%), MAPE em 29/75 (39%) e R² em 22/75 (29%).

**Página:** PDF 19 (Tabela 3) e PDF 30 (Tabela 7).

**Interpretação correta:** Mostra predominância temática e heterogeneidade de avaliação no corpus, não desempenho médio de uma técnica.

**Limitações:** Recorte Scopus e 2020–2024; categorias podem se sobrepor.

---

### Q2 — LSTM + média-variância em ações do Reino Unido

**Fonte:** Wang et al. (2020).

**Problema:** pré-seleção preditiva de ativos seguida de carteira MV.

**Amostra/período:** 100 ações da UK Stock Exchange; março de 1994 a março de 2019.

**Modelo:** LSTM para pré-seleção e otimização média-variância; comparação com SVM, random forest, DNN, ARIMA e estratégias equiponderadas.

**Benchmark:** variantes ML+MV e 1/N.

**Métrica:** retorno anualizado, Sharpe e custo de transação.

**Resultado:** Para carteira de nove ativos antes dos custos, o texto reporta retorno anualizado de 0,136 e Sharpe de 0,58 para LSTM+MV. As Tabelas 6–8 mostram que a classificação pode se alterar quando se incorporam os custos de transação.

**Página:** PDF 10–12, especialmente Tabelas 6–8.

**Interpretação correta:** É evidência de que previsão/seleção e MV podem ser integradas e avaliadas conjuntamente; não demonstra superioridade independente de custos ou fora do mercado/janela estudados.

**Limitações:** Backtest específico; sensível a custo, número de ativos e mercado.

---

### Q3 — Seleção R-CNN-BiLSTM + Markowitz no mercado tailandês

**Fonte:** Chaweewanchon e Chaysiri (2022).

**Problema:** seleção preditiva de ações e otimização MV.

**Amostra/período:** ações do mercado tailandês; o artigo usa dados do Yahoo Finance e descreve a amostra/metodologia nas seções empíricas.

**Modelo:** R-CNN-BiLSTM + Markowitz, comparado a LSTM, CNN-BiLSTM, BiLSTM e seleções aleatórias.

**Benchmark:** modelos de previsão alternativos e carteiras aleatórias/MV/1/N.

**Métrica:** MAE, MSE, SMAPE, retorno, risco e Sharpe.

**Resultado:** Tabela 2: R-CNN-BiLSTM obteve MAE 1,4582, MSE 1,8081 e SMAPE 2,3332, versus MAE 1,7219 no LSTM. Na Tabela 3, a carteira de cinco ativos R-CNN-BiLSTM+MV apresenta Sharpe 2,62; esses valores são do desenho experimental do artigo, não estimativas gerais de mercado.

**Página:** PDF 13–15, Tabelas 2–3.

**Interpretação correta:** Dá exemplo mensurável de pipeline seleção por ML → pesos por Markowitz e de comparação com baselines.

**Limitações:** Autores registram generalização limitada ao mercado tailandês, ausência de variáveis exógenas, busca manual de hiperparâmetros e falta de análise de tempo computacional (PDF 17).

---

### Q4 — RL com recompensa média-variância versus Max-Sharpe e MV

**Fonte:** Jiang, Olmo e Atwi (2024).

**Problema:** alocação dinâmica de carteira por DRL com risco e custos.

**Amostra/período:** preços diários de fechamento de 30 ações do DJIA e 100 do S&P 100, 01/04/2010–09/03/2023; treino 01/04/2010–02/01/2020 e validação 03/01/2020–29/04/2021.

**Modelo:** RTC-CNN-TD3, com recompensa média-variância estendida, aversão ao risco e custo de transação.

**Benchmark:** Max-Sharpe, MV e variantes DRL.

**Métrica:** retorno anual/cumulativo, volatilidade anual, Sharpe, maximum drawdown e Calmar.

**Resultado:** Para DJIA, com β=0,005 e custo ξ=0,05%, Tabela 2: RTC-CNN-TD3 teve retorno anual 26,91%, volatilidade 22,01%, Sharpe 1,19 e MDD 19,11%; Max-Sharpe: 2,62%, 19,97%, 0,23 e 21,38%; MV: 3,25%, 13,42%, 0,31 e 16,01%. Para S&P 100 sob o mesmo cenário, Tabela 6: RTC-CNN-TD3 teve retorno anual 36,92% e Sharpe 1,39; Max-Sharpe 10,25% e 0,48; MV 3,08% e 0,09.

**Página:** PDF 7 (dados), PDF 9 (Tabela 2) e PDF 12 (Tabela 6).

**Interpretação correta:** No backtest e nos parâmetros especificados, o método proposto superou os dois benchmarks no retorno/Sharpe, mas também apresentou volatilidade e drawdown que devem ser lidos junto dos retornos.

**Limitações:** Resultados dependem de dados, parâmetros β/ξ, período e protocolo de treino; não provam desempenho futuro.

---

### Q5 — RL conectado à MPT em duas janelas de ações

**Fonte:** Jang e Seong (2023).

**Problema:** otimização de carteira de ações via DRL e MPT.

**Amostra/período:** duas janelas de teste reportadas: 2017-01–2018-06 e 2018-07–2019-12.

**Modelo:** método proposto de DRL conectado à MPT; resultados médios de 10 execuções.

**Benchmark:** 1/N e métodos de RL anteriores.

**Métrica:** Sharpe, maximum drawdown (MDD) e valor final de carteira (fAPV).

**Resultado:** Tabela 4 (2017-01–2018-06): método proposto, Sharpe 2,1092, MDD 7,00 e fAPV 1,3629; 1/N, Sharpe 1,9884, MDD 7,05 e fAPV 1,3118. Tabela 5 (2018-07–2019-12): proposto, Sharpe 1,9365, MDD 8,05 e fAPV 1,4150; 1/N, Sharpe 1,3770, MDD 10,75 e fAPV 1,2559.

**Página:** PDF 10, Tabelas 4–5.

**Interpretação correta:** Os números corroboram desempenho relativo nas duas janelas testadas, não uma dominância de DRL em todos os mercados/regimes.

**Limitações:** Os autores assinalam complexidade e estocasticidade de RL; a replicabilidade requer atenção às execuções e aos dados.

## 6. Figuras e tabelas candidatas

### V1 — Crescimento anual de documentos de IA no mercado acionário

**Fonte:** Ferreira, Gandomi e Cardoso (2021).

**Página:** PDF 3 (impressa 30900).

**Figura/Tabela:** Figura 2.

**Caption:** “Documents by year.”

**Conteúdo:** Série bibliométrica de documentos da busca Scopus sobre IA e mercado acionário, 1995–2019.

**Por que pode ser útil:** Referência visual direta para evolução da literatura financeira, desde que a legenda deixe claros base, consulta e período.

---

### V2 — Fluxo geral de previsão financeira por IA

**Fonte:** Ferreira, Gandomi e Cardoso (2021).

**Página:** PDF 9 (impressa 30906).

**Figura/Tabela:** Figura 6.

**Caption:** “Flowchart for general financial forecasting with Artificial Intelligence model predictions.”

**Conteúdo:** Dados → tratamento/redução de ruído → treinamento → validação de hiperparâmetros → teste/avaliação.

**Por que pode ser útil:** Ajuda a orientar visualmente o ciclo de modelagem, especialmente a separação validação/teste.

---

### V3 — Mapa quantitativo de DL por mercado financeiro

**Fonte:** Giantsidi e Tarantola (2025).

**Página:** PDF 30.

**Figura/Tabela:** Tabela 7 e Figura 11.

**Caption:** Tabela 7: síntese de domínios/modelos; Figura 11: “Annual distribution of publication count (2020–2024).”

**Conteúdo:** Contagens de estudos por mercado/aplicação e distribuição anual do corpus de 187 artigos.

**Por que pode ser útil:** Situa a extensão de aplicações de DL sem converter a subseção em uma lista de algoritmos.

---

### V4 — Taxonomia de entradas e saídas em previsão acionária

**Fonte:** Ferreira, Gandomi e Cardoso (2021).

**Página:** PDF 12 (impressa 30909).

**Figura/Tabela:** Tabelas 10 e 11.

**Caption:** tabelas de *input data* e *output variables* para previsão de mercado acionário.

**Conteúdo:** Organiza preços, volume, indicadores técnicos, fundamentos e variáveis de previsão.

**Por que pode ser útil:** Referência para classificar dados financeiros e alvos preditivos; melhor como inspiração para tabela própria, com escopo explicitado.

## 7. Referências mais úteis encontradas

- **Ferreira, Gandomi e Cardoso (2021)** — histórico bibliométrico, taxonomia de aplicações, previsão, sentimento e workflow; revisão geral de IA no trading acionário.
- **Giantsidi e Tarantola (2025)** — motivação com dados financeiros, panorama recente de DL, domínios de aplicação, métricas recorrentes e limitações metodológicas.
- **Jiang, Olmo e Atwi (2024)** — portfolio/asset allocation, RL, integração explícita de risco e custo de transação, e comparação quantitativa com Max-Sharpe/MV.
- **Wang et al. (2020)** — arquitetura prática ML para pré-seleção + média-variância; previsão e portfolio.
- **Chaweewanchon e Chaysiri (2022)** — seleção por ML seguida de Markowitz, métricas preditivas e de carteira, com limitações declaradas.
- **Jang e Seong (2023)** — RL conectado à MPT, pesos dinâmicos e métricas de risco-retorno.

## 8. Possível organização temática

1. Evolução da adoção/pesquisa em ML financeiro e transição metodológica.
2. Propriedades dos dados financeiros que motivam ML: não linearidade, não estacionariedade, ruído, múltiplas fontes e alta dimensionalidade.
3. Casos de uso por objetivo: previsão de retorno/preço e volatilidade; sentimento/dados alternativos; gestão de risco; trading; seleção, alocação e otimização de carteiras.
4. Integração previsão/seleção → decisão de carteira, distinguindo modelos preditivos, otimizadores e RL.
5. Avaliação e limitações: separação temporal e fora da amostra, leakage, custos, risco, mudanças de regime, interpretabilidade e reprodutibilidade.

## 9. Resultados rejeitados

- **Artigos de previsão, trading ou alocação exclusivamente em criptomoedas** — encontrados na busca textual (por exemplo, *Cryptocurrency trading: a comprehensive survey*, *Forecasting and trading cryptocurrencies* e *A Novel Cryptocurrency Price Prediction Model Using GRU, LSTM and bi-LSTM*), mas não entram no núcleo pois a finalidade desta subseção é ML em finanças gerais; a interseção cripto deve permanecer em Trabalhos Relacionados.
- **Explainable artificial intelligence for crypto asset allocation** — potencialmente útil para a seção específica de cripto, mas não como base geral sem deslocar o foco temático.
- **Class-imbalanced dynamic financial distress prediction based on Adaboost-SVM ensemble combined with SMOTE and time weighting** — aplicação bancária/risco de crédito muito especializada para o objetivo atual; pode ser fonte secundária para “outras aplicações”, mas não é prioritária para previsão, trading, risco de mercado ou portfolios.
- **Crude oil price prediction: A comparison between AdaBoost-LSTM and AdaBoost-GRU for improving forecasting performance** — é previsão de commodity pontual; não foi incluído porque as revisões selecionadas já cobrem previsão financeira em escopo mais amplo e porque o estudo isolado não fundamenta, por si, uma visão geral de ML em finanças.

