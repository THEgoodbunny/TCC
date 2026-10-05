# Complementação bibliográfica da Seção 3

## Estado atual da Seção 3

### Trabalhos atualmente citados

A leitura integral de `trabalhos-relacionados.tex` identificou 16 chaves únicas. Para esta análise, qualquer trabalho associado a uma dessas chaves foi tratado como **ARTIGO JÁ UTILIZADO**:

- `brauneis2019cryptocurrency` — Brauneis e Mestel, *Cryptocurrency-portfolios in a mean-variance framework* (2019).
- `chaweewanchon2022markowitz` — Chaweewanchon e Chaysiri, *Markowitz Mean-Variance Portfolio Optimization with Predictive Stock Selection Using Machine Learning* (2022).
- `chen2021mean` — Chen et al., *Mean-variance portfolio optimization using machine learning-based stock price prediction* (2021).
- `du2022mean` — Du, *Mean-variance portfolio optimization with deep learning based-forecasts for cointegrated stocks* (2022).
- `giantsidi2025deep` — Giantsidi e Tarantola, *Deep learning for financial forecasting: A review of recent trends* (2025).
- `jang2023deep` — Jang e Seong, *Deep reinforcement learning for stock portfolio optimization by connecting with modern portfolio theory* (2023).
- `jeleskovic2024cryptocurrency` — Jeleskovic et al., *Cryptocurrency portfolio optimization: Utilizing a GARCH-copula model within the Markowitz framework* (2024).
- `jiang2024deep` — Jiang, Olmo e Atwi, *Deep reinforcement learning for portfolio selection* (2024).
- `lopez2025enhancing` — López de Prado et al., *Enhancing Markowitz's portfolio selection paradigm with machine learning* (2025).
- `ma2021portfolio` — Ma, Han e Wang, *Portfolio optimization with return prediction using deep learning and machine learning* (2021).
- `padhi2022intelligent` — Padhi et al., *An Intelligent Fusion Model with Portfolio Selection and Machine Learning for Stock Market Prediction* (2022).
- `paiva2019decision` — Paiva et al., *Decision-making for financial trading: A fusion approach of machine learning and portfolio selection* (2019).
- `slusarczyk2025optimal` — Ślusarczyk e Ślepaczuk, *Optimal Markowitz portfolio using returns forecasted with time series and machine learning models* (2025).
- `sutiene2024enhancing` — Sutiene et al., *Enhancing portfolio management using artificial intelligence: literature review* (2024).
- `wang2020portfolio` — Wang et al., *Portfolio formation with preselection using deep learning from long-term financial data* (2020).
- `zouaoui2025portfolio` — Zouaoui e Naas, *Portfolio Optimization Based on MPT-LSTM Neural Networks: A case study of Cryptocurrency Markets* (2025).

Nenhuma dessas 16 chaves corresponde aos nove trabalhos publicados novos e válidos encontrados em `NOVOS SEC 3` na primeira execução.

### Resumo das quatro subseções atuais

- **Machine Learning aplicado à otimização de portfólios:** descreve previsão de retornos/preços e pré-seleção de ativos antes da alocação média-variância. A evidência é majoritariamente de ações e índices.
- **Média-variância e Markowitz em criptoativos:** discute diversificação, volatilidade, não normalidade, correlações instáveis e resultados em que 1/N pode superar carteiras MV; inclui uma aplicação MPT-LSTM já utilizada (`zouaoui2025portfolio`).
- **Estudos híbridos:** reúne ML/DL/RL com Markowitz, mas a maior parte dos exemplos desenvolvidos no texto atual é de mercados acionários ou financeiros tradicionais.
- **Síntese crítica:** contrapõe ganhos potenciais de modelos híbridos a turnover, custos, overfitting, sensibilidade paramétrica, risco de cauda e baixa interpretabilidade; encerra afirmando que permanece espaço para modelos híbridos em criptoativos.

### Lacunas identificadas antes da nova busca

- Pouca cobertura, no capítulo, de estudos publicados que integrem **no mesmo experimento** previsão/aprendizado, MV/Markowitz e carteiras de criptoativos.
- Ausência de trabalhos publicados sobre SVM com dados de sentimento, clustering como pré-seleção para MV, elastic net com fatores cripto, XGBoost em carteiras mistas, DRL com fronteiras MV/mean-CVaR e XAI aplicado à comparação de carteiras cripto.
- Discussão ainda limitada sobre quando maior sofisticação não melhora o desempenho, especialmente sob erro de estimação, risco de cauda, não estacionariedade e custos.
- A frase de que “parte relevante” dos estudos híbridos se concentra em mercados tradicionais era plausível com a bibliografia então usada, mas precisava ser testada contra literatura cripto mais recente.

## Principais resultados

- **Novos trabalhos distintos acumulados nas duas etapas:** 23 artigos publicados: 9 de Prioridade A, 4 de Prioridade B e 10 de Prioridade C.
- **Interseção completa MV + cripto + ML:** 9 trabalhos. A segunda etapa acrescentou Babaei, Giudici e Raffinetti (2022) aos oito estudos empíricos da primeira etapa.
- **Mais próximos do presente TCC:** Zhou et al. (2023), Xu et al. (2025), Han et al. (2024), Toscano et al. (2026) e Peykani, Sabour e Tanasescu (2026), porque usam previsões ou seleção algorítmica como entrada de modelos MV; Lorenzo e Arroyo (2023) são especialmente próximos no eixo pré-seleção→MV. Babaei, Giudici e Raffinetti (2022) acrescentam explicabilidade dos pesos, não previsão de retornos.
- **Diagnóstico executivo:** a lacuna ampla — “há poucos estudos que combinam MV, cripto e ML” — **não continua defensável sem qualificação**. A contribuição precisa ser delimitada pelo protocolo específico do TCC: modelos empregados, universo de ativos, horizonte e frequência, validação fora da amostra, retraining, custos, turnover, liquidez, restrições e estabilidade dos pesos.
- **Resultado específico da segunda etapa:** entre 50 PDFs físicos do acervo preexistente, foram identificados 43 estudos distintos, 14 novos e úteis, 16 já usados e 13 descartados por falta de aderência. Sete arquivos eram cópias ou versões do mesmo estudo.

## Prioridade A — MV + cripto + ML

### Multi-source data driven cryptocurrency price movement prediction and portfolio optimization

- **Classificação:** PRIORIDADE A.
- **Origem:** NOVOS SEC 3.
- **Autores:** Zhongbao Zhou; Zhengyang Song; Helu Xiao; Tiantian Ren.
- **Ano:** 2023.
- **Caminho do PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Multi-source data driven cryptocurrency price movement prediction and portfolio optimization.pdf`
- **DOI:** `10.1016/j.eswa.2023.119600`.
- **BibTeX:** existe — `zhou2023multisource`.
- **Mercado/dados:** sete criptomoedas (BTC, ETH, XRP, ADA, DOGE, DOT e LTC); dados de negociação, Google Trends e 28.799.774 tweets de 1/1/2021 a 30/6/2021; testes fora da amostra com horizontes de 1, 3 e 5 dias.
- **Componente MV/Markowitz:** modelo de variância mínima global modificado pela informação prevista; comparação com minimum variance, máximo Sharpe, 1/N, Black–Litterman, CRIX e outro método de pré-seleção.
- **Componente cripto:** previsão de movimentos e alocação exclusivamente entre criptomoedas.
- **Componente ML/DL/RL:** SVM para classificar a direção futura dos preços; VADER para extrair sentimento dos tweets.
- **Como os três componentes são integrados:** probabilidades/direções previstas pela SVM, construídas com dados de mercado, atenção e sentimento, modificam a função de otimização de variância mínima; a carteira é atualizada em janela móvel.
- **Principais resultados:** maior Sharpe, Sortino e retorno equivalente certo fora da amostra que a maioria dos benchmarks; resultado permanece em testes de robustez e, na maioria dos casos, após custo de transação de 0,1%.
- **Limitações:** apenas sete moedas e seis meses de dados; prevê direção, não magnitude; resultados dependem de janela e horizonte.
- **Citação literal 1:** “Third, we use SVM to forecast the movement of cryptocurrency prices based on the above multi-source data. Fourth, we propose a novel portfolio model by combining the forecasting results with the global minimum variance model, and the corresponding portfolio strategy is also derived.”
- **Página:** PDF 2; página impressa 2. Contexto: objetivo e desenho do estudo no corpo da introdução.
- **Tradução/síntese:** a previsão SVM alimenta explicitamente um modelo de variância mínima global.
- **Citação literal 2:** “The proposed strategy has a better out-of-sample Sharpe ratio, Sortino ratio, and Certainty-equivalent (CEQ) return than other strategies. More importantly, the robustness test further confirms the effectiveness of the proposed strategy. Finally, we discuss the case where there are transaction costs, and the results show that the strategy proposed in this paper outperforms other strategies even with transaction costs.”
- **Página:** PDF 2; página impressa 2. Contexto: síntese dos resultados próprios na introdução.
- **Tradução/síntese:** o método híbrido supera estratégias tradicionais em desempenho ajustado ao risco e mantém vantagem com custos.
- **Melhor local para inserir na Seção 3:** Estudos híbridos entre Markowitz, ML, deep learning e reinforcement learning.
- **Afirmação atual que pode reforçar:** previsões podem alimentar diretamente a alocação MV e melhorar desempenho fora da amostra.
- **Nova discussão que permite:** dados alternativos (sentimento e atenção), comparação com CRIX/1/N e efeito de custos de transação.
- **Relação específica com o presente TCC:** é um dos paralelos mais diretos: previsão de movimentos de criptoativos alimenta uma regra de variância mínima; difere pelo uso de SVM, tweets e Google Trends e por modificar o objetivo de variância mínima.
- **Impacto sobre a lacuna declarada no capítulo:** reduz fortemente a lacuna genérica; já havia, em 2023, integração explícita de ML + variância mínima + cripto. A lacuna deve ser deslocada para escolhas específicas de dados, modelos, período e robustez.

### Online risk-based portfolio allocation on subsets of crypto assets applying a prototype-based clustering algorithm

- **Classificação:** PRIORIDADE A.
- **Origem:** NOVOS SEC 3.
- **Autores:** Luis Lorenzo; Javier Arroyo.
- **Ano:** 2023.
- **Caminho do PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Online risk-based portfolio allocation on subsets of crypto assets applying a prototype-based clustering algorithm.pdf`
- **DOI:** `10.1186/s40854-022-00438-2`.
- **BibTeX:** existe — `lorenzo2023online`.
- **Mercado/dados:** mercado cripto completo com 534 ativos elegíveis e subconjuntos dos 175 e 250 maiores; simulação de janeiro de 2020 a maio de 2021, janela de estimação de dois anos, holding de 30 dias e 1.500 trajetórias de investimento.
- **Componente MV/Markowitz:** MV é aplicado somente ao cluster selecionado; MV integral, risk parity, hierarchical risk parity e CCI30 são benchmarks.
- **Componente cripto:** universo amplo de criptoativos, atualizado em janelas deslizantes.
- **Componente ML/DL/RL:** clustering não supervisionado CLARA/k-medoids, seleção automática do número de clusters e escolha do protótipo conforme perfil de risco/Sharpe.
- **Como os três componentes são integrados:** clustering pré-seleciona dinamicamente um subconjunto coerente com o perfil do investidor; MV calcula os pesos apenas nesse subconjunto.
- **Principais resultados:** estratégias de cluster por Sharpe e mean-risk melhoram retornos e Sharpe quando o universo cresce e evitam falhas de convergência do MV aplicado a todo o mercado; o MV clássico preserva vantagem em algumas métricas puras de risco.
- **Limitações:** maior drawdown/risco em algumas estratégias; sensibilidade ao número de moedas; fricções, liquidez, múltiplas exchanges e negociabilidade de todos os 534 ativos não foram incorporadas.
- **Citação literal 1:** “We propose enhancing the mean-variance (MV) model with a pre-selection stage that uses a prototype-based clustering algorithm to reduce the number of crypto assets considered at each investment period. [...] We then run the MV portfolio optimization with the crypto assets of the selected cluster.”
- **Página:** PDF 1; página impressa 1 de 40. Contexto: abstract do próprio estudo.
- **Tradução/síntese:** o algoritmo de clustering funciona como pré-seleção e o MV determina a carteira no cluster escolhido.
- **Citação literal 2:** “One of the drawbacks of the proposed strategies is the higher drawdown and risk compared with the classical MV, which is the more evident weakness of the proposed strategies, so it is comparable to the HRP model. We consider that SR and MR strategies independent of market size offer a good trade-off between returns, risk, and drawdown.”
- **Página:** PDF 36; página impressa 36 de 40. Contexto: conclusão e limitações reconhecidas pelos autores.
- **Tradução/síntese:** os ganhos não são absolutos: a seleção por clusters pode elevar drawdown e risco em comparação ao MV clássico.
- **Melhor local para inserir na Seção 3:** Estudos híbridos entre Markowitz, ML, deep learning e reinforcement learning.
- **Afirmação atual que pode reforçar:** ML também pode atuar na pré-seleção, antes da otimização matemática.
- **Nova discussão que permite:** redução de dimensionalidade e erro de covariância em universos cripto grandes, com trade-off entre retorno e drawdown.
- **Relação específica com o presente TCC:** compartilha a sequência seleção algorítmica→MV, mas usa clustering não supervisionado em vez de previsão de retornos e trabalha com um universo muito maior.

### Portfolio constructions in cryptocurrency market: A CVaR-based deep reinforcement learning approach

- **Classificação:** PRIORIDADE A.
- **Origem:** NOVOS SEC 3.
- **Autores:** Tianxiang Cui; Shusheng Ding; Huan Jin; Yongmin Zhang.
- **Ano:** 2023.
- **Caminho do PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Portfolio constructions in cryptocurrency market - A CVaR-based deep reinforcement learning approach.pdf`
- **DOI:** `10.1016/j.econmod.2022.106078`.
- **BibTeX:** existe — `cui2023portfolio`.
- **Mercado/dados:** BTC, Dash, ETH, LTC, USDT e XRP; 2.199 observações diárias do Yahoo Finance, de 6/8/2015 a 6/8/2021; treino até 31/12/2019 e teste posterior.
- **Componente MV/Markowitz:** fronteira eficiente média-variância e função de recompensa baseada no objetivo MV; benchmark direto para a fronteira mean-CVaR.
- **Componente cripto:** carteiras compostas pelas seis criptomoedas.
- **Componente ML/DL/RL:** PPO com rede residual profunda; ações são vetores contínuos de pesos.
- **Como os três componentes são integrados:** agentes PPO são treinados tanto com recompensa MV quanto mean-CVaR, constroem as duas fronteiras e realocam pesos; os portfólios são comparados fora da amostra.
- **Principais resultados:** mean-CVaR domina MV: no teste, carteiras mean-CVaR apresentam retornos maiores e desvios-padrão menores; o estudo atribui a vantagem à representação do risco de cauda.
- **Limitações:** seis ativos e um único período de mercado; não há análise explícita de custos/slippage no experimento; parte da geração de cenários é descrita como in-sample; a superioridade observada é específica ao risco CVaR e desenho adotado.
- **Citação literal 1:** “The main contribution of this paper is to propose a new CVaR-based portfolio optimization model for cryptocurrency markets, which employs a DRL methodology. [...] We employ deep reinforcement learning to construct the portfolios and perform out-of-sample back testing to verify that the CVaR risk measure outperforms the variance risk measure.”
- **Página:** PDF 2; página impressa 2. Contexto: contribuição metodológica no corpo da introdução.
- **Tradução/síntese:** DRL constrói carteiras cripto sob objetivos mean-CVaR e MV, com teste fora da amostra.
- **Citação literal 2:** “We employ deep reinforcement learning to construct the portfolios according to the mean–variance and mean-CVaR mechanisms for out-of-sample back testing. [...] This indicates that the portfolios constructed under the mean-CVaR framework have higher returns with lower risk compared with the portfolios constructed under the mean–variance model.”
- **Página:** PDF 7; página impressa 7. Contexto: comparação empírica das fronteiras e dos portfólios.
- **Tradução/síntese:** o artigo não apenas menciona MV como benchmark: treina DRL sob ambos os mecanismos e mostra vantagem do mean-CVaR.
- **Melhor local para inserir na Seção 3:** Estudos híbridos entre Markowitz, ML, deep learning e reinforcement learning.
- **Afirmação atual que pode reforçar:** RL permite alocação dinâmica e incorporação explícita de risco na recompensa.
- **Nova discussão que permite:** risco de cauda como alternativa à variância e comparação de fronteiras eficientes geradas por DRL.
- **Relação específica com o presente TCC:** oferece benchmark metodológico alternativo ao pipeline predição→MV, pois aprende pesos sequencialmente e compara diretamente recompensas MV e mean-CVaR.
- **Impacto sobre a lacuna declarada no capítulo:** contradiz a impressão de que exemplos DRL relevantes estão restritos a ações: há experimento publicado especificamente em cripto com benchmark MV.

### Cryptocurrency Portfolio Optimisation Based on LSTM Time Series Forecasting

- **Classificação:** PRIORIDADE A.
- **Origem:** NOVOS SEC 3.
- **Autores:** Zhihan Xu; Xinyue Zhang; Zili Zhou.
- **Ano:** 2025.
- **Caminho do PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Cryptocurrency Portfolio Optimisation Based on LSTM Time Series Forecasting.pdf`
- **DOI:** `10.54254/2755-2721/2025.22255`.
- **BibTeX:** existe — `xu2025cryptocurrency`.
- **Mercado/dados:** BTC, ETH e LTC; seis anos de dados da Binance para treinamento; previsões e backtest de janeiro a junho de 2024, com otimização mensal.
- **Componente MV/Markowitz:** Markowitz estendido com short selling; maximização do Sharpe e cálculo mensal dos pesos.
- **Componente cripto:** carteira exclusivamente de BTC, ETH e LTC.
- **Componente ML/DL/RL:** LSTM com janela móvel para previsão de preços.
- **Como os três componentes são integrados:** dados históricos, dados novos e previsões LSTM são combinados como entradas do Markowitz estendido; os pesos resultantes são aplicados aos retornos reais e comparados com a janela móvel tradicional.
- **Principais resultados:** retorno ligeiramente maior, risco semelhante e Sharpe superior em quatro dos seis meses; o artigo conclui por maior retorno e melhor controle de risco no período.
- **Limitações:** apenas três moedas e seis meses de avaliação; short selling produz pesos negativos expressivos; acúmulo de erros e ausência de previsão de longo prazo; volatilidade não melhora em todos os meses.
- **Citação literal 1:** “This work investigates the optimization of cryptocurrency portfolios by combining Long Short-Term Memory (LSTM) time series forecasting with traditional portfolio optimization methods. [...] These predictions are subsequently incorporated into an extended Markowitz framework to optimize the portfolio on a monthly basis.”
- **Página:** PDF 1; página impressa 143. Contexto: abstract.
- **Tradução/síntese:** previsões LSTM de três criptomoedas alimentam mensalmente o Markowitz estendido.
- **Citação literal 2:** “As shown in Table 4 and Figure 4, Real Return in LSTM model exhibits slightly higher returns compared to the traditional model [...] The differences in volatility are relatively small, with the LSTM model demonstrating more stability in certain months, though it also exhibits higher volatility in others. And the Sharpe ratio of the LSTM model is superior in most month.”
- **Página:** PDF 7; página impressa 149. Contexto: resultados fora da amostra por mês.
- **Tradução/síntese:** a vantagem é moderada e heterogênea: Sharpe geralmente maior, mas volatilidade nem sempre menor.
- **Melhor local para inserir na Seção 3:** Estudos híbridos entre Markowitz, ML, deep learning e reinforcement learning.
- **Afirmação atual que pode reforçar:** LSTM pode fornecer entradas preditivas para os pesos MV em cripto.
- **Nova discussão que permite:** extensão do estudo já citado `zouaoui2025portfolio`, com comparação mensal entre otimização histórica e LSTM-enhanced.
- **Relação específica com o presente TCC:** é o paralelo mais próximo no desenho LSTM→Markowitz com carteira exclusivamente cripto; sua amostra de três moedas e seis meses ajuda a delimitar como o TCC pode avançar.
- **Impacto sobre a lacuna declarada no capítulo:** estreita a lacuna, mas sua amostra pequena deixa espaço para estudos com mais moedas, horizontes maiores, restrições realistas e custos.

### The diversification benefits of cryptocurrency factor portfolios: Are they there?

- **Classificação:** PRIORIDADE A.
- **Origem:** NOVOS SEC 3.
- **Autores:** Weihao Han; David Newton; Emmanouil Platanakis; Haoran Wu; Libo Xiao.
- **Ano:** 2024.
- **Caminho do PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/The diversification benefits of cryptocurrency factor portfolios - Are they there.pdf`
- **DOI:** `10.1007/s11156-024-01260-w`.
- **BibTeX:** existe — `han2024diversification`.
- **Mercado/dados:** mais de 2.000 criptomoedas do CoinGecko, janeiro de 2014 a junho de 2021, agregadas em 28 fatores de tamanho, momentum, volume e volatilidade; benchmark com S&P 500, Treasury de 10 anos e T-bill.
- **Componente MV/Markowitz:** MV com restrição de short sale, Bayes–Stein e Black–Litterman, além de variantes ML; 1/N como referência.
- **Componente cripto:** fatores cripto entram em carteiras tradicionais stock–bond; cada fator sintetiza um universo amplo de moedas.
- **Componente ML/DL/RL:** combination elastic net (C-ENet) prevê retornos dos fatores cripto.
- **Como os três componentes são integrados:** os retornos previstos por C-ENet substituem as médias históricas nos modelos MV, Bayes–Stein e Black–Litterman; pesos ótimos são recalculados fora da amostra.
- **Principais resultados:** fatores de tamanho e momentum geram benefícios significativos; estratégias com retornos previstos têm, em média, desempenho fora da amostra cerca de 4% maior; resultados resistem a custos, benchmark alternativo e janela móvel.
- **Limitações:** número limitado de técnicas de ML/otimização; covariâncias continuam históricas; possíveis erros de estimação em alta volatilidade; fatores baseados sobretudo em preço/mercado.
- **Citação literal 1:** “Second, we enhance the performance of optimised portfolios by combining the usage of traditional portfolio optimisation framework and machine learning, to mitigate the poor out-of-sample portfolio performance caused by estimation errors. [...] we leverage the power of machine learning to predict cryptocurrency factor’s one-period-ahead expected returns. Specifically, we employ the combination elastic net (C-ENet) approach.”
- **Página:** PDF 3; página impressa 471. Contexto: contribuição metodológica da introdução.
- **Tradução/síntese:** C-ENet prevê retornos de fatores cripto para reduzir erros de estimação na alocação tradicional.
- **Citação literal 2:** “Our empirical results demonstrate that, on average, the asset allocation strategies adopting forecasted expected returns have an approximate 4% higher out-of-sample performance than strategies that ignore the contribution of machine-learning techniques on predicting returns, especially for the momentum factors.”
- **Página:** PDF 4; página impressa 472. Contexto: síntese dos resultados empíricos.
- **Tradução/síntese:** a etapa preditiva melhora em aproximadamente 4% o desempenho médio fora da amostra.
- **Melhor local para inserir na Seção 3:** Estudos híbridos entre Markowitz, ML, deep learning e reinforcement learning.
- **Afirmação atual que pode reforçar:** previsões de retorno substituem entradas históricas do MV e podem reduzir erro de estimação.
- **Nova discussão que permite:** fatoração de milhares de criptomoedas, diversificação em carteiras mistas e diferenças por aversão ao risco.
- **Relação específica com o presente TCC:** substitui médias históricas por previsões C-ENet como entrada da alocação, mas usa fatores cripto em carteiras stock–bond, não ativos individuais numa carteira exclusivamente cripto.
- **Impacto sobre a lacuna declarada no capítulo:** é evidência robusta de integração completa, com grande universo e testes de custos; restringe a lacuna remanescente a carteiras cripto puras, ativos individuais e arquiteturas/objetivos específicos.

### When Richer Information Does Not Improve Allocation: Machine Learning and Portfolio Optimisation in NFT-Ecosystem Tokens

- **Classificação:** PRIORIDADE A.
- **Origem:** NOVOS SEC 3.
- **Autores:** David Toscano; Juan C. Roca; Francisco Jareño.
- **Ano:** 2026.
- **Caminho do PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/When Richer Information Does Not Improve Allocation - Machine Learning and Portfolio Optimisation in NFT-Ecosystem Tokens.pdf`
- **DOI:** `10.1007/s10614-026-11394-9`.
- **BibTeX:** existe — `toscano2026richer` (online first).
- **Mercado/dados:** 28 tokens do ecossistema NFT, com OHLC diário de janeiro de 2021 a março de 2024; comparação adicional com cinco criptomoedas maduras.
- **Componente MV/Markowitz:** MV clássico e modified mean-variance com covariância/volatilidade OHLC; 50.000 carteiras Monte Carlo por janela; pesos escolhidos pelo Sharpe.
- **Componente cripto:** tokens NFT/GameFi/metaverso, como SAND, MANA, AXS, GALA e THETA.
- **Componente ML/DL/RL:** Random Forest, Gradient Boosted Regression Trees, BPNN e rede neural; previsão de retornos com indicadores OHLC e técnicos.
- **Como os três componentes são integrados:** previsões ML são entradas exógenas comuns a MV, MMV e 1/N; isso separa o valor da previsão do valor do estimador de risco intradiário.
- **Principais resultados:** MV e MMV com ML superam 1/N, inclusive com custos; MV clássico geralmente tem Sharpe maior e menor volatilidade/risco de cauda que MMV; informação intradiária não melhora sistematicamente a alocação.
- **Limitações:** mercado muito específico e período curto; forte dependência de correlação e arquitetura; custos não incluem taxas de rede/slippage; simulação Monte Carlo aproxima a fronteira.
- **Citação literal 1:** “In the second stage, the predicted returns obtained from the ML models are treated as exogenous inputs to the portfolio optimization problem. Portfolio weights are computed using three alternative allocation strategies: the traditional MV framework, a MMV framework based on OHLC-derived volatility and covariance estimates and 1/N.”
- **Página:** PDF 14; página impressa mostra “13” no rodapé do arquivo (paginação interna anômala). Contexto: desenho experimental.
- **Tradução/síntese:** os mesmos retornos previstos alimentam três regras de alocação, permitindo isolar o efeito de MV/MMV.
- **Citação literal 2:** “Across all forecasting models, both optimization-based strategies (MMV and MV) substantially outperform the naïve 1/N benchmark in terms of cumulative returns and Sharpe ratios. Comparing MMV and MV, the classical MV strategy generally delivers higher Sharpe ratios and lower volatility.”
- **Página:** PDF 24; página impressa mostra “13” no rodapé do arquivo (paginação interna anômala). Contexto: resultados de alocação, antes da tabela 11.
- **Tradução/síntese:** o ganho vem da combinação previsão + otimização, mas o refinamento OHLC não supera consistentemente o MV clássico.
- **Melhor local para inserir na Seção 3:** Síntese crítica dos estudos relacionados.
- **Afirmação atual que pode reforçar:** sofisticação não garante ganho universal; qualidade preditiva e estrutura de correlação importam.
- **Nova discussão que permite:** distinguir valor econômico da previsão e valor incremental da medida de risco; incluir NFT tokens, custos e risco intradiário.
- **Relação específica com o presente TCC:** é próximo no pipeline previsão→MV e particularmente útil como contraprova: informação de risco mais rica não melhorou sistematicamente a alocação.
- **Impacto sobre a lacuna declarada no capítulo:** exige revisão direta. O estudo implementa exatamente ML + MV + cripto e mostra que a questão relevante já não é apenas “se combinar”, mas **quando** a combinação e cada refinamento geram valor.

### A machine learning framework for multi-market portfolio optimization: Evidence from U.S. stocks and cryptocurrencies

- **Classificação:** PRIORIDADE A.
- **Origem:** NOVOS SEC 3.
- **Autores:** Pejman Peykani; Daniyal Sabour; Cristina Tanasescu.
- **Ano:** 2026.
- **Caminho do PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/A machine learning framework for multi-market portfolio optimization - Evidence from U.S. stocks and cryptocurrencies.pdf`
- **DOI:** `10.36922/IJOCTA026240111`.
- **BibTeX:** existe — `peykani2026machine`.
- **Mercado/dados:** BTC, ETH, BNB, Microsoft e Tesla; preços diários de 20/3/2024 a 14/7/2025; teste final de 30 dias.
- **Componente MV/Markowitz:** MV, mean-semivariance e mean-absolute-deviation; carteiras de risco mínimo e tangência; 1/N como benchmark.
- **Componente cripto:** três criptomoedas dentro de carteira mista com ações norte-americanas.
- **Componente ML/DL/RL:** XGBoost para retornos diários, com otimização Bayesiana de hiperparâmetros e indicadores técnicos/macroeconômicos.
- **Como os três componentes são integrados:** previsões XGBoost substituem retornos esperados nos três modelos; os pesos e carteiras de tangência são avaliados fora da amostra.
- **Principais resultados:** todas as estratégias otimizadas reduzem risco para retorno-alvo semelhante; no buy-and-hold de 30 dias, 1/N retorna 6,6%, máximo Sharpe 7,2%, máximo Sortino 7,6% e máximo Sharpe-AD 10,2%.
- **Limitações:** apenas cinco ativos, teste de 30 dias e desenho estático de período único; sem testes formais de diferença de Sharpe/Sortino; custos, spread, slippage e estabilidade dos pesos não modelados; previsão tratada como determinística.
- **Citação literal 1:** “This study introduces an integrated framework linking XGBoost-based return forecasting with three distinct optimization models: MV, MSV, and MAD. The analysis applies these models jointly to a mixed portfolio containing both U.S. equities and cryptocurrencies.”
- **Página:** PDF 1; página impressa 1768. Contexto: introdução e contribuição do artigo.
- **Tradução/síntese:** o framework liga XGBoost a MV e medidas alternativas em uma carteira mista de ações e cripto.
- **Citação literal 2:** “The empirical results indicate that integrating machine-learning predictions with downside-focused optimization yields noticeable improvements over the baseline naïve portfolio. [...] The maximum-ratio configurations, particularly the Maximum Sharpe-AD and Maximum Sortino models, exhibited the most substantial efficiency gains and consistently outperformed both their minimum-risk counterparts and the equal-weighted baseline.”
- **Página:** PDF 11; página impressa 1778. Contexto: síntese dos resultados experimentais.
- **Tradução/síntese:** previsões combinadas a objetivos de risco produzem ganhos sobre 1/N, sobretudo nas carteiras de máxima razão.
- **Melhor local para inserir na Seção 3:** Estudos híbridos entre Markowitz, ML, deep learning e reinforcement learning.
- **Afirmação atual que pode reforçar:** ML pode atualizar retornos esperados usados por MV e por medidas downside.
- **Nova discussão que permite:** carteira multi-mercado e comparação entre variância, semivariância e desvio absoluto.
- **Relação específica com o presente TCC:** usa XGBoost para estimar retornos e calcular pesos MV, mas mistura ações e cripto e possui teste final de apenas 30 dias.
- **Impacto sobre a lacuna declarada no capítulo:** acrescenta evidência híbrida recente, embora em carteira mista e amostra pequena; a lacuna específica pode permanecer para universos cripto amplos e avaliação dinâmica longa.

### Integrating Choquet portfolios and machine learning interpretability for robust cryptocurrency investment strategies

- **Classificação:** PRIORIDADE A, com ressalva: ML é usado para **interpretar** carteiras e diferenças de retorno, não para prever diretamente os retornos que alimentam Markowitz.
- **Origem:** NOVOS SEC 3.
- **Autores:** João Pedro M. Franco; Márcio P. Laurini.
- **Ano:** 2025.
- **Caminho do PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Integrating Choquet portfolios and machine learning interpretability for robust cryptocurrency investment strategies.pdf`
- **DOI:** `10.1016/j.jfds.2025.100172`.
- **BibTeX:** existe — `franco2025integrating`.
- **Mercado/dados:** 15 criptomoedas do CoinMarketCap, de 22/5/2019 a 27/8/2025; janelas móveis e rebalanceamentos de 30, 90, 180 e 365 dias.
- **Componente MV/Markowitz:** carteira Markowitz é construída e comparada diretamente com Choquet, 1/N e Bitcoin; retorno-alvo anual uniforme de 10%.
- **Componente cripto:** BTC, ETH, XRP, BNB, DOGE, TRX, ADA, LINK, XLM, BCH, CRO, LEO, LTC, XMR e ETC.
- **Componente ML/DL/RL:** Random Forest de 500 árvores, Shapley values e LIME para explicar quais moedas impulsionam previsões/retornos das carteiras.
- **Como os três componentes são integrados:** Markowitz e Choquet geram pesos/retornos; um modelo explicável atribui a cada cripto a contribuição para as diferenças de retorno entre as estratégias.
- **Principais resultados:** Choquet melhora retorno cumulativo e mitigação de cauda, sobretudo em horizontes curtos; XAI identifica ADA, CRO e BNB como principais drivers de Markowitz, e CRO, ADA e TRX de Choquet; a vantagem decai em horizontes longos.
- **Limitações:** XAI é pós-alocação e não componente preditivo de Markowitz; o modelo assume i.i.d. dentro de cada janela; parâmetros perdem poder em holding longo; turnover/custos tornam estratégias simples competitivas.
- **Citação literal 1:** “This study further contributes by conducting a comparative analysis of the Markowitz mean-variance model and the Choquet portfolio. Machine Learning interpretability techniques are employed to elucidate the differences in portfolio returns, specifically identifying the cryptocurrencies that drive these divergences. In particular, Shapley Values [...] and Local Interpretable Model-Agnostic Explanations (LIME) [...] are utilized to augment the models’ transparency.”
- **Página:** PDF 2; página impressa 2. Contexto: contribuição declarada no corpo da introdução.
- **Tradução/síntese:** ML explicável é integrado à comparação de Markowitz e Choquet para mostrar quais criptoativos causam as diferenças.
- **Citação literal 2:** “This study contributes to the literature by applying the Choquet portfolio to cryptocurrency markets for the first time and juxtaposing it with the traditional Markowitz mean-variance model. Additionally, tools for the interpretability of Machine Learning, such as Shapley Values and LIME, are utilized to clarify distinctions in portfolio returns, thereby enhancing transparency and comprehension of the optimization process.”
- **Página:** PDF 16; página impressa 16. Contexto: conclusões.
- **Tradução/síntese:** o estudo usa XAI para abrir a caixa-preta das diferenças entre duas regras de carteira cripto.
- **Melhor local para inserir na Seção 3:** Síntese crítica dos estudos relacionados.
- **Afirmação atual que pode reforçar:** interpretabilidade é desafio relevante e pode ser tratada com ferramentas XAI específicas.
- **Nova discussão que permite:** explicar decisões/pesos, comparar Markowitz com risco de cauda e discutir transparência em robo-advisors.
- **Relação específica com o presente TCC:** aproxima-se pelo universo cripto e pelo benchmark Markowitz, mas o ML é uma camada explicativa posterior, não a fonte das estimativas usadas na otimização.
- **Impacto sobre a lacuna declarada no capítulo:** estreita a lacuna no eixo interpretabilidade, mas não elimina espaço para XAI incorporada ao próprio processo preditivo/alocativo, em vez de aplicada depois.

### Explainable artificial intelligence for crypto asset allocation

- **Classificação:** PRIORIDADE A, com ressalva: o ML explica os resultados da alocação Markowitz; não prevê retornos para alimentar a otimização.
- **Origem:** acervo preexistente.
- **Autores:** Golnoosh Babaei; Paolo Giudici; Emanuela Raffinetti.
- **Ano:** 2022.
- **Caminho:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/Explainable artificial intelligence for crypto asset allocation.pdf`.
- **Duplicata identificada:** cópia byte a byte em `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/3 parte intro - machine learning/Explainable artificial intelligence for crypto asset allocation.pdf`.
- **DOI:** `10.1016/j.frl.2022.102941`.
- **BibTeX:** existe — `babaei2022explainable`.
- **Mercado/dados:** BTC, ETH, XRP, BCH, LTC, BNB, EOS e XLM; 771 observações diárias de setembro de 2017 a outubro de 2019; 740 carteiras produzidas em janela móvel de 30 dias.
- **Componente MV/Markowitz:** alocação Markowitz de volatilidade mínima, recalculada diariamente com retornos e covariâncias dos 30 dias anteriores.
- **Componente cripto:** carteira exclusivamente formada pelas oito criptomoedas.
- **Componente ML/DL/RL:** Random Forest para modelar o Z-score risco-retorno da carteira e SHAP/Shapley values para explicar a influência de cada moeda.
- **Forma de integração:** o Markowitz gera pesos, risco e retorno; o Random Forest aprende a relação não linear entre Z-scores dos ativos e da carteira; SHAP atribui a contribuição de cada criptoativo à decisão resultante.
- **Principais resultados:** as carteiras dinâmicas apresentaram distribuição de risco inferior à estratégia estática de pesos iguais; XLM, seguida de BCH e XRP, explicou a maior parte das variações dos Z-scores e pesos.
- **Limitações:** a precisão preditiva do Random Forest não é avaliada porque não é o foco; o XAI é posterior à alocação; usa oito ativos, uma janela única de 30 dias e não modela custos, liquidez ou risco de cauda.
- **Citação literal 1:** “For this purpose, we apply Shapley values to the predictions generated by a machine learning model based on the results of a dynamic Markowitz portfolio optimization model and provide explanations for what is behind the selected portfolio weights.”
- **Página:** PDF 1; página impressa não exibida na primeira folha. Contexto: resumo do próprio estudo.
- **Citação literal 2:** “As explained in Section 2, the main goal of this paper is to propose an explainable portfolio management approach that has the ability to explain the weights assigned by a robot advisor that daily applied Markowitz’ asset allocation model to available cryptocurrencies.”
- **Página:** PDF 4; página impressa 4. Contexto: início dos resultados empíricos.
- **Tradução/síntese:** o artigo torna interpretáveis os pesos de uma carteira Markowitz dinâmica de criptoativos e identifica quais moedas mais explicam a variação das decisões.
- **Melhor local para inserção:** Síntese crítica dos estudos relacionados, após o parágrafo sobre baixa interpretabilidade; menção secundária na subseção de estudos híbridos.
- **Afirmação que pode sustentar:** XAI pode ser aplicada às decisões de alocação e aos pesos de carteiras cripto baseadas em Markowitz.
- **Relação específica com o presente TCC:** complementa diretamente a discussão de interpretabilidade, mas não concorre com o pipeline de previsão de retornos do TCC.
- **Impacto sobre a lacuna:** acrescenta outro exemplo publicado de integração efetiva dos três eixos; reduz a lacuna genérica, embora preserve espaço para explicabilidade integrada à previsão→otimização.

## Prioridade B — interseção de dois eixos

### Bitcoin and Portfolio Diversification: A Portfolio Optimization Approach

- **Classificação:** PRIORIDADE B — MV/otimização + cripto, sem ML.
- **Origem:** acervo preexistente.
- **Autores:** Walid Bakry; Audil Rashid; Somar Al-Mohamad; Nasser El-Kanj.
- **Ano:** 2021.
- **Caminho:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/4 parte intro - Teoria de Portifólio/Bitcoin and Portfolio Diversification A Portfolio Optimization Approach.pdf`.
- **DOI:** `10.3390/jrfm14070282`.
- **BibTeX:** existe — `bakry2021bitcoin`.
- **Mercado/dados:** Bitcoin e índices amplos de ações, câmbio, atividade econômica, energia, títulos corporativos e ouro; 508 observações semanais de agosto de 2011 a maio de 2021.
- **Componente MV/Markowitz:** média-variância e maximização do Sharpe sob oito cenários — pesos iguais, semirrestritos, restritos, risk parity e máximo Sharpe, com e sem short selling.
- **Componente cripto:** Bitcoin é incluído e retirado de cada carteira para medir seu efeito marginal.
- **Componente ML/DL/RL:** ausente.
- **Forma de integração:** a alocação otimiza pesos de cada classe e compara risco, retorno, Sharpe, VaR e CVaR de carteiras com e sem Bitcoin.
- **Principais resultados:** pequenas alocações em Bitcoin elevaram o Sharpe em vários cenários, mas exposição excessiva aumentou risco e CVaR; o melhor equilíbrio surgiu com restrições de peso.
- **Limitações:** apenas Bitcoin; avaliação histórica; variância–covariância e simulação Monte Carlo subestimaram perdas extremas; custos não são incorporados à otimização.
- **Citação literal 1:** “The study employs different constraining optimization frameworks that seek to maximize risk-adjusted returns (Sharpe ratio) of the portfolio by optimizing allocations to each asset class (asset allocation).”
- **Página:** PDF 1; página impressa 1 de 24. Contexto: resumo.
- **Citação literal 2:** “The results also revealed that increasing the weight of Bitcoin generated incremental returns, but the risk increased disproportionately, resulting in a decrease in the Sharpe ratio [...] including Bitcoin does not essentially increase the risk-adjusted performance of a portfolio unless carefully constrained.”
- **Página:** PDF 16; página impressa 16 de 24. Contexto: discussão dos cenários de otimização.
- **Tradução/síntese:** a inclusão de Bitcoin pode melhorar o retorno ajustado ao risco, mas somente com limites de alocação que contenham exposição e risco de cauda.
- **Melhor local para inserção:** Estudos sobre média-variância e Markowitz em criptoativos.
- **Afirmação que pode sustentar:** restrições nos pesos são decisivas para que a inclusão de cripto não deteriore o desempenho ajustado ao risco.
- **Relação específica com o presente TCC:** fornece benchmark para discutir restrições e risco de cauda, mas não usa previsão ou múltiplas criptomoedas.
- **Impacto sobre a lacuna:** não reduz a lacuna de ML; mostra que o componente de otimização cripto já possui evidência madura e que a contribuição precisa ir além de simplesmente incluir Bitcoin.

### Portfolio diversification with virtual currency: Evidence from bitcoin

- **Classificação:** PRIORIDADE B — MV/otimização + cripto, sem ML.
- **Origem:** acervo preexistente.
- **Autores:** Khaled Guesmi; Samir Saadi; Ilyes Abid; Zied Ftiti.
- **Ano:** 2019.
- **Caminho:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/Portfolio diversification with virtual currency Evidence from bitcoin.pdf`.
- **DOI:** `10.1016/j.irfa.2018.03.004`.
- **BibTeX:** **BIBTEX AUSENTE**. Metadados confirmados: *International Review of Financial Analysis*, v. 63, p. 431–437, 2019.
- **Mercado/dados:** Bitcoin, MSCI Emerging Markets, MSCI World, ouro, euro/dólar, WTI, VIX e yuan; dados diários de 1/1/2012 a 5/1/2018, 1.561 observações.
- **Componente MV/Markowitz:** pesos ótimos de carteiras bivariadas, sem short selling, pela minimização de variância sem reduzir retorno esperado, usando covariâncias condicionais.
- **Componente cripto:** Bitcoin é combinado com cada ativo/índice tradicional.
- **Componente ML/DL/RL:** ausente.
- **Forma de integração:** modelos VARMA-DCC-GJR-GARCH estimam volatilidade/covariância; essas estimativas determinam pesos e hedge ratios de média-variância.
- **Principais resultados:** a especificação VARMA-DCC-GJR-GARCH foi a mais adequada; estratégias com Bitcoin, ouro, petróleo e ações emergentes reduziram a variância relativamente às carteiras sem Bitcoin.
- **Limitações:** apenas Bitcoin; pares bivariados; dependência do modelo GARCH e do período; incerteza regulatória e hacking podem alterar pesos e eficácia.
- **Citação literal 1:** “Finally, hedging strategies involving gold, oil, equities and Bitcoin reduce considerably the portfolio's risk, as compared to the risk of the portfolio made up of gold, oil and equities only.”
- **Página:** PDF 1; página impressa 431. Contexto: resumo.
- **Citação literal 2:** “Our empirical results suggest VARMA (1,1)-DCC-GJR-GARCH as the best model specification to describe the joint dynamics of Bitcoin and different financial assets. [...] Taken together, our results show that Bitcoin may offer diversification and hedging benefits for investors.”
- **Página:** PDF 6; página impressa 436. Contexto: conclusão.
- **Tradução/síntese:** covariâncias condicionais alimentam pesos ótimos e indicam redução de risco ao incluir Bitcoin, embora sob um desenho bivariado.
- **Melhor local para inserção:** Estudos sobre média-variância e Markowitz em criptoativos.
- **Afirmação que pode sustentar:** estimativas dinâmicas de covariância podem alterar pesos e benefícios de diversificação envolvendo Bitcoin.
- **Relação específica com o presente TCC:** oferece alternativa econométrica às estimativas históricas usadas em MV, sem ML e sem carteira multimoedas.
- **Impacto sobre a lacuna:** reforça que a lacuna não está na aplicação de otimização a Bitcoin, mas na integração e comparação com previsões ML em universos cripto mais amplos.

### Investigating the dynamic relationship between cryptocurrencies and conventional assets: Implications for financial investors

- **Classificação:** PRIORIDADE B — média-variância + cripto, sem ML.
- **Origem:** acervo preexistente.
- **Autores:** Lanouar Charfeddine; Noureddine Benlagha; Youcef Maouchi.
- **Ano:** 2020.
- **Caminho:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/Investigating the dynamic relationship between cryptocurrencies and conventional assets Implications for financial investors.pdf`.
- **Duplicata/versão identificada:** outra cópia do mesmo artigo em `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/1 parte intro - decisoes de investimentos e tomada de decisao/Investigating the dynamic relationship between cryptocurrencies and.pdf`.
- **DOI:** `10.1016/j.econmod.2019.05.016`.
- **BibTeX:** existe — `charfeddine2020investigating`.
- **Mercado/dados:** BTC (18/7/2010–1/10/2018), ETH (1/9/2015–1/10/2018), S&P 500, ouro e petróleo bruto.
- **Componente MV/Markowitz:** função utilidade média-variância para pesos ótimos e hedge ratios, com covariâncias de copulas variantes no tempo e BEKK/DCC/ADCC-GARCH.
- **Componente cripto:** carteiras mistas BTC/ETH + ativos tradicionais e carteira exclusivamente BTC–ETH.
- **Componente ML/DL/RL:** ausente.
- **Forma de integração:** dependências e covariâncias dinâmicas determinam pesos que minimizam risco mantendo o retorno esperado.
- **Principais resultados:** correlações com ativos convencionais são fracas, porém variáveis no tempo; pequenas alocações digitais podem diversificar; a eficácia de hedge é baixa na maioria dos pares e sensível a choques externos.
- **Limitações:** apenas BTC e ETH; resultados dependem do modelo de dependência; carteiras bivariadas; não avalia custos nem previsão fora da amostra.
- **Citação literal 1:** “Assuming a mean-variance utility function, the optimal portfolio holdings of digital asset i is given by the following [...].”
- **Página:** PDF 17; página impressa 214. Contexto: método de pesos ótimos.
- **Citação literal 2:** “First, using time varying copula models, we find evidence of time varying dependence between all the different pairs considered. [...] Second, we show that for the case of portfolio with mixed assets, the level of dependence is very weak for all the seven examined pairs without exception, a result which suggests that Bitcoin and Ethereum can offer new opportunities for portfolio diversification.”
- **Página:** PDF 18; página impressa 215. Contexto: conclusão.
- **Tradução/síntese:** a diversificação existe, mas as correlações e os pesos ótimos mudam com o tempo e com choques, o que enfraquece estimativas estáticas.
- **Melhor local para inserção:** Estudos sobre média-variância e Markowitz em criptoativos.
- **Afirmação que pode sustentar:** correlações instáveis e choques externos limitam alocações MV estáticas em cripto.
- **Relação específica com o presente TCC:** justifica testar janelas móveis/retraining e estabilidade dos pesos; difere por usar copulas/GARCH, não ML.
- **Impacto sobre a lacuna:** desloca a contribuição para a capacidade do método do TCC de lidar, ou não, com dependências mutáveis.

### Are stablecoins truly diversifiers, hedges, or safe havens against traditional cryptocurrencies as their name suggests?

- **Classificação:** PRIORIDADE B — otimização risco-retorno baseada em variância/covariância + cripto, sem ML.
- **Origem:** acervo preexistente.
- **Autores:** Gang-Jin Wang; Xin-yu Ma; Hao-yu Wu.
- **Ano:** 2020.
- **Caminho:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/Are stablecoins truly diversifiers, hedges, or safe havens against traditional cryptocurrencies as their name suggests.pdf`.
- **DOI:** `10.1016/j.ribaf.2020.101225`.
- **BibTeX:** existe — `wang2020stablecoins`.
- **Mercado/dados:** Tether, BitUSD, NuBits, DGD, HGT, XAUR, BTC, LTC e XRP; dados diários até 20/3/2019, com início em 6/3/2015 para stablecoins em dólar e 13/10/2017 para as lastreadas em ouro.
- **Componente MV/Markowitz:** pesos de uma carteira bivariada obtida minimizando risco sem reduzir retorno esperado, usando variâncias e covariâncias DCC-GARCH; comparação com 50/50.
- **Componente cripto:** carteiras stablecoin–criptomoeda tradicional, avaliadas também por VaR e ES.
- **Componente ML/DL/RL:** ausente.
- **Forma de integração:** DCC-GARCH e copulas produzem dependência dinâmica; os pesos são calculados e o risco extremo das carteiras é comparado.
- **Principais resultados:** stablecoins em dólar dispersam melhor o risco que as lastreadas em ouro; Tether é o caso mais forte; o papel de safe haven varia por condição de mercado e algumas combinações falham em caudas extremas.
- **Limitações:** carteiras bivariadas; amostras com inícios distintos; resultados específicos a stablecoins antigas; não modela custos ou liquidez.
- **Citação literal 1:** “First, we consider a portfolio, called portfolio 1, obtained by minimizing the risk of a cryptocurrency-stablecoin portfolio without reducing the expected return.”
- **Página:** PDF 13; página impressa 13. Contexto: construção da carteira.
- **Citação literal 2:** “Comparing the results of full-period analysis with the subperiod one, we find that the market condition matters to the risk-dispersion effectiveness of USD-pegged stablecoins.”
- **Página:** PDF 16; página impressa 16. Contexto: conclusão.
- **Tradução/síntese:** a diversificação e a redução de perdas dependem do ativo e do regime; pesos ótimos não devem ser interpretados como invariantes.
- **Melhor local para inserção:** Estudos sobre média-variância e Markowitz em criptoativos.
- **Afirmação que pode sustentar:** risco de cauda e mudanças de regime exigem cautela ao interpretar carteiras cripto otimizadas por variância.
- **Relação específica com o presente TCC:** amplia o universo potencial com stablecoins e fornece comparação 50/50, mas não usa ML nem carteira multivariada ampla.
- **Impacto sobre a lacuna:** não cobre a integração com ML; ajuda a tornar mais específica a lacuna sobre regimes, caudas e composição do universo de ativos.

## Prioridade C — complementares

### Portfolio Optimization Methods for the Digital Asset Market: A Comprehensive Survey

- **Classificação:** PRIORIDADE C — revisão sistemática; não é um novo experimento de carteira.
- **Origem:** NOVOS SEC 3.
- **Autores:** Giorgos Demosthenous; Chrysis Georgiou.
- **Ano:** 2026.
- **Caminho do PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Portfolio Optimization Methods for the Digital Asset Market - A Comprehensive Survey.pdf`
- **DOI:** `10.1145/3819577`.
- **BibTeX:** existe — `demosthenous2026portfolio`.
- **Mercado/dados:** revisão sistemática de 119 publicações de 2017–2025 sobre portfólios exclusivamente de ativos digitais.
- **Componente MV/Markowitz:** identifica MVO como método mais frequente e discute pressupostos, erro de estimação e benchmarks.
- **Componente cripto:** foco integral em digital-asset-only portfolios.
- **Componente ML/DL/RL:** categorias próprias de ML/DL e RL; descreve forecasting→allocation, clustering, DRL e limitações de adaptação.
- **Como os três componentes são integrados:** síntese e classificação da literatura, não uma integração experimental própria.
- **Principais resultados:** literatura cresce 37,8% ao ano, mas permanece fragmentada; MVO é o método mais usado; estudos ML/DL frequentemente seguem previsão e alocação em duas fases; comportamento estático e falta de retreinamento são fragilidades.
- **Limitações:** cobertura termina em 2025; como revisão, resultados empíricos são de trabalhos secundários e não devem ser citados como experimentos próprios dos autores.
- **Citação literal 1:** “Although the portfolio optimization problem for traditional markets (stocks, commodities, etc.) is well researched and documented in the literature, studies on optimizing digital-asset-only portfolios are still sparse, fragmented and undocumented.”
- **Página:** PDF 2; página impressa 342:2. Contexto: introdução e justificativa da revisão.
- **Tradução/síntese:** a literatura existe e cresce, mas ainda é dispersa e pouco consolidada; isso é diferente de dizer que quase não há estudos híbridos.
- **Citação literal 2:** “A major drawback of the existing literature within this category is the assumption of time-invariant and static model behavior. Usually, models are trained once and their parameters are only tuned during the building phase and are never updated, which can lead to a failure to adapt to non-stationary market dynamics.”
- **Página:** PDF 22; página impressa 342:22. Contexto: conclusão da categoria ML/DL em portfólios digitais.
- **Tradução/síntese:** a revisão aponta falta de adaptação/retreinamento como lacuna mais específica da literatura ML/DL cripto.
- **Melhor local para inserir na Seção 3:** Síntese crítica dos estudos relacionados.
- **Afirmação atual que pode reforçar:** modelos cripto enfrentam não normalidade, não estacionariedade, turnover, custos e dificuldade de adaptação.
- **Nova discussão que permite:** substituir uma lacuna quantitativa vaga por lacunas de adaptação, dados on-chain, objetivos ligados ao desempenho e transformers.
- **Relação específica com o presente TCC:** oferece o enquadramento global mais amplo para situar o pipeline do TCC e, sobretudo, para justificar lacunas de validação dinâmica e adaptação, não uma alegação de inexistência de estudos.
- **Impacto sobre a lacuna declarada no capítulo:** sustenta que o campo ainda é fragmentado, mas sua amostra de 119 trabalhos impede afirmar, sem qualificação, que a interseção é quase inexistente.

### Diversifying equity with cryptocurrencies during COVID-19

- **Classificação:** PRIORIDADE C — cripto + análise não linear de diversificação, sem MV e sem alocação de pesos.
- **Origem:** acervo preexistente.
- **Autores:** John W. Goodell; Stephane Goutte.
- **Ano:** 2021.
- **Caminho:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/1 parte intro - decisoes de investimentos e tomada de decisao/Diversifying equity with cryptocurrencies during COVID-19.pdf`.
- **DOI:** `10.1016/j.irfa.2021.101781`.
- **BibTeX:** existe — `goodell2021diversifying`.
- **Mercado/dados:** BTC, ETH, LTC e Tether contra sete índices acionários e VIX; 28/2/2019–9/2/2021.
- **Metodologia:** correlações/heatmaps, coerência wavelet e redes neurais para co-movimentos antes e durante a COVID-19.
- **Papel para portfólios:** testa se as criptomoedas oferecem diversificação em regimes normais e de crise; não calcula carteira ótima.
- **Principais resultados:** co-movimentos aumentam com a pandemia; BTC, ETH e LTC oferecem pouco benefício para ações; Tether exibe co-movimento negativo relevante e comportamento de safe haven.
- **Limitações:** período centrado numa crise única; quatro moedas; inferência de diversificação por co-movimento, sem backtest de pesos, custos ou restrições.
- **Citação literal 1:** “We find co-movements between cryptocurrencies and equity indices gradually increased as COVID-19 progressed. However, most of these co-movements are either modestly positively correlated, or minimal, suggesting cryptocurrencies in general do not provide a diversification benefit during either normal times or downturns.”
- **Página:** PDF 1; página impressa não exibida. Contexto: resumo.
- **Citação literal 2:** “The latter three cryptocurrencies offer little diversification benefit for equity investors. On the other hand, tether [...] manifests pronounced negative co-movements with equity indices, both in normal times, and especially during the COVID-19 period.”
- **Página:** PDF 8; página impressa 8. Contexto: discussão e conclusão.
- **Tradução/síntese:** o benefício de diversificação é heterogêneo por moeda e regime; stablecoins podem se comportar de modo distinto de BTC, ETH e LTC.
- **Melhor local para inserção:** Estudos sobre média-variância e Markowitz em criptoativos, como qualificação externa à evidência MV.
- **Afirmação que pode sustentar:** correlações e benefícios de diversificação mudam em crises e entre tipos de criptoativo.
- **Relação específica com o presente TCC:** motiva avaliação por regimes e inclusão/controle de stablecoins, mas não é estudo de otimização.
- **Impacto sobre a lacuna:** ajuda a especificar a lacuna de robustez temporal; não altera a contagem de interseção completa.

### Cryptocurrency trading: a comprehensive survey

- **Classificação:** PRIORIDADE C — survey de negociação, previsão, risco e construção de portfólios cripto.
- **Origem:** acervo preexistente.
- **Autores:** Fan Fang; Carmine Ventre; Michail Basios; Leslie Kanthan; David Martinez-Rego; Fan Wu; Lingbo Li.
- **Ano:** 2022.
- **Caminho:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/Cryptocurrency trading a comprehensive survey.pdf`.
- **DOI:** `10.1186/s40854-021-00321-6`.
- **BibTeX:** existe — `fang2022cryptocurrency`.
- **Mercado/dados:** revisão de 146 trabalhos publicados entre 2013 e junho de 2021.
- **Metodologia:** taxonomia de sistemas de negociação, estratégias sistemáticas, ML, portfólios, condições extremas, datasets e tendências.
- **Papel para portfólios:** mapeia a construção de carteiras cripto, mas não executa uma otimização própria.
- **Principais resultados:** documenta rápido crescimento e diversidade de métodos/dados; identifica como oportunidades redes de transação, mudanças em tempo real e risco de dissipação de alphas.
- **Limitações:** revisão encerrada em 2021; inclui literatura heterogênea e alguns preprints em seu universo; seus achados secundários não substituem validação dos artigos originais.
- **Citação literal 1:** “This paper provides a comprehensive survey of cryptocurrency trading research, by covering 146 research papers on various aspects of cryptocurrency trading (e.g., cryptocurrency trading systems, bubble and extreme condition, prediction of volatility and return, crypto-assets portfolio construction and crypto-assets, technical trading and others).”
- **Página:** PDF 1; página impressa 1 de 59. Contexto: resumo.
- **Citação literal 2:** “We further summarised the datasets used for experiments and analysed the research trends and opportunities in cryptocurrency trading.”
- **Página:** PDF 51; página impressa 51 de 59. Contexto: conclusão.
- **Tradução/síntese:** a revisão demonstra que previsão, risco e construção de carteiras cripto já formavam uma literatura ampla até 2021.
- **Melhor local para inserção:** Síntese crítica dos estudos relacionados.
- **Afirmação que pode sustentar:** há diversidade metodológica e forte crescimento da literatura cripto, o que exige delimitar a contribuição por desenho, não por ausência ampla de estudos.
- **Relação específica com o presente TCC:** serve como mapa histórico e fonte de terminologia, mas não evidencia desempenho de um modelo específico.
- **Impacto sobre a lacuna:** enfraquece narrativas genéricas de escassez; a revisão mais recente de Demosthenous e Georgiou (2026) deve ter precedência para o estado atual.

### Intelligent cryptocurrency trading system using integrated AdaBoost-LSTM with market turbulence knowledge

- **Classificação:** PRIORIDADE C — cripto + ML/DL e regimes; negociação de um ativo, sem MV.
- **Origem:** acervo preexistente.
- **Autores:** Sangjin Park; Jae-Suk Yang.
- **Ano:** 2023.
- **Caminho:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/Intelligent cryptocurrency trading system using integrated.pdf`.
- **Duplicata/versão identificada:** outra cópia em `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/3 parte intro - machine learning/Intelligent cryptocurrency trading system using integrated.pdf`.
- **DOI:** `10.1016/j.asoc.2023.110568`.
- **BibTeX:** existe — `park2023intelligent`.
- **Mercado/dados:** Bitcoin diário de 1/6/2016 a 30/4/2022; treino, validação e teste, com teste de 1/4/2021 a 30/4/2022.
- **Metodologia:** AdaBoost-LSTM para direção do preço, Markov regime-switching para turbulência e regra long-only com horizontes de 1, 3 e 5 dias.
- **Papel para portfólios:** não aloca entre ativos; fornece um modelo de sinal e filtro de risco potencialmente utilizável antes da otimização.
- **Principais resultados:** turbulência prolongada por 21 dias ou mais sinaliza alto risco; estratégia integrada apresentou retornos e Sharpes superiores aos indicadores técnicos de referência, especialmente nos horizontes de 3 e 5 dias.
- **Limitações:** único ativo; backtest de um ano; regras regulatórias e CBDCs podem gerar volatilidade não capturada; desempenho da negociação não demonstra benefício em carteira MV.
- **Citação literal 1:** “We propose a fusion approach combining technology with economic knowledge to achieve accurate predictions. Firstly, we provide an ensemble prediction framework that integrates the AdaBoost algorithm with the LSTM deep learning model [...]. Secondly [...] we combine the econometrics Markov regime-switching model with the AdaBoost-LSTM model.”
- **Página:** PDF 1; página impressa 1. Contexto: resumo.
- **Citação literal 2:** “The simulation of our trading system for one year (from April 1, 2021 to April 30, 2022) showed cumulative returns and Sharpe ratios that greatly exceeded those of other trading strategies such as the stochastic oscillator and MACD.”
- **Página:** PDF 19; página impressa 19. Contexto: conclusão.
- **Tradução/síntese:** combinar previsão DL com informação de regime melhora sinais e controle de risco, mas ainda não demonstra como esses sinais afetam pesos MV.
- **Melhor local para inserção:** Estudos sobre Machine Learning aplicado à otimização de portfólios, como antecedente de previsão cripto, com ressalva explícita de que não há otimização.
- **Afirmação que pode sustentar:** regimes de turbulência e overfitting precisam ser considerados na etapa preditiva.
- **Relação específica com o presente TCC:** sugere incluir variáveis/regimes de mercado ou testar estabilidade entre regimes; não é comparador direto de carteira.
- **Impacto sobre a lacuna:** delimita uma lacuna de integração sinal/regime→pesos, não uma lacuna de previsão cripto.

### Forecasting and trading cryptocurrencies with machine learning under changing market conditions

- **Classificação:** PRIORIDADE C — cripto + ML com validação por regime e custos; sem MV.
- **Origem:** acervo preexistente.
- **Autores:** Helder Sebastião; Pedro Godinho.
- **Ano:** 2021.
- **Caminho:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/3 parte intro - machine learning/Forecasting and trading cryptocurrencies.pdf`.
- **Duplicata identificada:** cópia byte a byte em `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/s40854-020-00217-x (1).pdf`.
- **DOI:** `10.1186/s40854-020-00217-x`.
- **BibTeX:** existe — `sebastiao2021forecasting`.
- **Mercado/dados:** BTC, ETH e LTC; variáveis de negociação e atividade de rede de 15/8/2015 a 3/3/2019; teste começa em 13/4/2018.
- **Metodologia:** modelos lineares, Random Forest e SVM em classificação/regressão, janela móvel e ensembles por concordância; estratégias long-only com custo round-trip de 0,5%.
- **Papel para portfólios:** não define pesos multivariados; avalia sinais que poderiam fornecer retornos previstos a uma camada de alocação.
- **Principais resultados:** não há modelo individual universalmente superior; Ensemble 5 em ETH e LTC obteve Sharpe anualizado de 80,17% e 91,35%, mas tail risk e drawdown permanecem altos e custos tornam cinco estratégias negativas.
- **Limitações:** estratégia por ativo, short selling proibido, baixo desempenho preditivo individual e forte dependência do regime e do critério econômico de seleção.
- **Citação literal 1:** “The models are validated in a period characterized by unprecedented turmoil and tested in a period of bear markets, allowing the assessment of whether the predictions are good even when the market direction changes between the validation and test periods.”
- **Página:** PDF 1; página impressa 1 de 30. Contexto: resumo.
- **Citação literal 2:** “Additionally, these trading strategies are subjected to a high tail risk, with CVaRs at 1% between 3.88% and 13.40% and maximum drawdown between 11.15% and 48.06%.”
- **Página:** PDF 27; página impressa 27 de 30. Contexto: conclusão.
- **Tradução/síntese:** resultados positivos de ML podem coexistir com baixa acurácia, alto risco de cauda, drawdowns e sensibilidade a custos/regimes.
- **Melhor local para inserção:** Síntese crítica, junto às limitações de custos, generalização e risco de cauda.
- **Afirmação que pode sustentar:** avaliar apenas retorno ou acurácia não basta; custos e perdas extremas podem mudar a conclusão.
- **Relação específica com o presente TCC:** oferece um protocolo de robustez útil para a etapa preditiva, mas não determina pesos de carteira.
- **Impacto sobre a lacuna:** fortalece a lacuna específica de integrar previsões avaliadas sob mudança de regime a uma alocação MV realista.

### Is It Possible to Forecast the Price of Bitcoin?

- **Classificação:** PRIORIDADE C — previsão ML de Bitcoin, sem otimização de carteira.
- **Origem:** acervo preexistente.
- **Autores:** Julien Chevallier; Dominique Guégan; Stéphane Goutte.
- **Ano:** 2021.
- **Caminho:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/forecasting-03-00024-v2.pdf`.
- **DOI:** `10.3390/forecast3020024`.
- **BibTeX:** existe — `chevallier2021forecast`.
- **Mercado/dados:** Bitcoin spot e futuros, 17 criptomoedas e ativos de ações, títulos, câmbio e commodities; 57 séries diárias entre 13/1/2015 e 31/12/2020, 2.070 observações.
- **Metodologia:** ANN, SVM, Random Forest, kNN, AdaBoost e Ridge, com AR(1) e buy-and-hold como referências; análises de subperíodos e negociação.
- **Papel para portfólios:** estuda informação cruzada entre classes e previsão de Bitcoin, mas não calcula pesos ou fronteira eficiente.
- **Principais resultados:** outras criptomoedas melhoram a previsão; AdaBoost/Random Forest se destacam em parte dos testes, mas buy-and-hold vence as regras de negociação em geral.
- **Limitações:** um ativo-alvo; resultados variam por período e conjunto de atributos; boa acurácia não se converte automaticamente em ganho econômico.
- **Citação literal 1:** “The main contribution is to use these data analytics techniques with great caution in the parameterization, instead of classical parametric modelings (AR), to disentangle the non-stationary behavior of the data.”
- **Página:** PDF 1; página impressa 377. Contexto: resumo.
- **Citação literal 2:** “Across the trading strategies, we have documented that (i) machine learning algorithms (configured as bots following buy/sell signals) do not teach how to trade, (ii) the buy-and-hold strategy appears the best [...].”
- **Página:** PDF 39; página impressa 415. Contexto: conclusão.
- **Tradução/síntese:** previsão estatisticamente útil não garante estratégia economicamente superior; não estacionariedade e parametrização exigem cautela.
- **Melhor local para inserção:** Síntese crítica dos estudos relacionados.
- **Afirmação que pode sustentar:** ganho preditivo não implica, por si só, ganho de carteira ou de negociação.
- **Relação específica com o presente TCC:** reforça a necessidade de avaliar a carteira final fora da amostra, além das métricas do preditor.
- **Impacto sobre a lacuna:** sustenta uma lacuna de avaliação econômica integrada, não de disponibilidade de algoritmos preditivos.

### A Novel Cryptocurrency Price Prediction Model Using GRU, LSTM and bi-LSTM Machine Learning Algorithms

- **Classificação:** PRIORIDADE C — comparação DL para previsão cripto, sem alocação.
- **Origem:** acervo preexistente.
- **Autores:** Mohammad J. Hamayel; Amani Yousef Owda.
- **Ano:** 2021.
- **Caminho:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/3 parte intro - machine learning/A Novel Cryptocurrency Price Prediction Model Using GRU, LSTM and bi-LSTM Machine Learning Algorithms.pdf`.
- **DOI:** `10.3390/ai2040030`.
- **BibTeX:** existe — `hamayel2021novel`.
- **Mercado/dados:** BTC, ETH e LTC; treino de 22/1/2018 a 22/10/2020 e teste de 22/10/2020 a 30/6/2021.
- **Metodologia:** GRU, LSTM e BiLSTM univariadas, avaliadas por MAPE e RMSE.
- **Papel para portfólios:** apenas previsão de preços; não seleciona ativos nem calcula pesos.
- **Principais resultados:** GRU obteve os menores MAPEs nas três moedas; BiLSTM foi a menos precisa; os autores propõem incluir notícias, tweets e volume em trabalhos futuros.
- **Limitações:** somente preço histórico, três ativos, divisão temporal única e ausência de teste econômico/custos; erro de preço não prova utilidade para retornos ou pesos.
- **Citação literal 1:** “This paper proposes three types of recurrent neural network (RNN) algorithms used to predict the prices of three types of cryptocurrencies, namely Bitcoin (BTC), Litecoin (LTC), and Ethereum (ETH).”
- **Página:** PDF 1; página impressa 477. Contexto: resumo.
- **Citação literal 2:** “The results show that GRU outperformed the other algorithms with a MAPE of 0.2454%, 0.8267%, and 0.2116% for BTC, ETH, and LTC, respectively.”
- **Página:** PDF 18; página impressa 494. Contexto: conclusão.
- **Tradução/síntese:** GRU foi superior no experimento, mas o estudo não demonstra se essas previsões melhoram uma alocação MV.
- **Melhor local para inserção:** Estudos sobre Machine Learning aplicado à otimização de portfólios, apenas como evidência de seleção do preditor antes da camada de alocação.
- **Afirmação que pode sustentar:** arquiteturas recorrentes não são intercambiáveis; desempenho depende da moeda e do modelo.
- **Relação específica com o presente TCC:** útil para justificar a comparação GRU/LSTM/BiLSTM, se esses modelos fizerem parte do experimento; não é trabalho relacionado de otimização por si só.
- **Impacto sobre a lacuna:** não reduz a lacuna de integração, mas mostra que a etapa preditiva isolada já é bem explorada.

### Comparative Performance of Machine Learning Ensemble Algorithms for Forecasting Cryptocurrency Prices

- **Classificação:** PRIORIDADE C — ensembles ML para preços cripto, sem alocação.
- **Origem:** acervo preexistente.
- **Autores:** V. Derbentsev; V. Babenko; K. Khrustalev; H. Obruch; S. Khrustalova.
- **Ano:** 2021.
- **Caminho:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/3 parte intro - machine learning/Comparative Performance of Machine Learning Ensemble Algorithms for.pdf`.
- **DOI:** `10.5829/ije.2021.34.01a.16`.
- **BibTeX:** existe — `derbentsev2021comparative`.
- **Mercado/dados:** BTC e XRP de 1/1/2015 a 31/12/2019 (1.826 observações) e ETH de 7/8/2015 a 31/12/2019 (1.608); 92 observações finais fora da amostra.
- **Metodologia:** Random Forest e Stochastic Gradient Boosting Machine, com defasagens, médias móveis e volume.
- **Papel para portfólios:** prevê preços um passo à frente; não avalia carteira, pesos ou retorno econômico.
- **Principais resultados:** MAPE fora da amostra entre 0,92% e 2,61%; atributos adicionais melhoraram a precisão em 1%–3% em média.
- **Limitações:** teste curto, apenas três moedas, foco em erro de preço e ausência de custos/backtest; seleção de atributos e modelos adicionais ficam para pesquisa futura.
- **Citação literal 1:** “To check the effectiveness of these models we made an out-of-sample forecast for selected time series by using the one step ahead technique.”
- **Página:** PDF 1; página impressa 140. Contexto: resumo.
- **Citação literal 2:** “According to our results, the out of sample accuracy of short-term forecasting daily prices obtained by SGBM and RF in terms of MAPE for three of the most capitalized cryptocurrencies (BTC, ETH, and XRP) was within 0.92-2.61 %.”
- **Página:** PDF 7; página impressa 146. Contexto: conclusão.
- **Tradução/síntese:** ensembles de árvores conseguem baixo erro de preço no teste adotado, sem evidência de que isso resulte em melhores pesos ou Sharpe.
- **Melhor local para inserção:** Estudos sobre Machine Learning aplicado à otimização de portfólios, como antecedente preditivo secundário.
- **Afirmação que pode sustentar:** Random Forest/boosting são alternativas relevantes para previsão cripto fora da amostra.
- **Relação específica com o presente TCC:** pode justificar modelos candidatos e atributos, mas precisa ser conectado a uma avaliação de carteira no TCC.
- **Impacto sobre a lacuna:** confirma maturidade da previsão isolada e reforça que a contribuição precisa estar na integração e validação econômica.

### Ensemble Deep Learning Models for Forecasting Cryptocurrency Time-Series

- **Classificação:** PRIORIDADE C — ensemble DL para previsão cripto, sem otimização efetiva.
- **Origem:** acervo preexistente.
- **Autores:** Ioannis E. Livieris; Emmanuel Pintelas; Stavros Stavroyiannis; Panagiotis Pintelas.
- **Ano:** 2020.
- **Caminho:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/3 parte intro - machine learning/Ensemble Deep Learning Models for Forecasting.pdf`.
- **DOI:** `10.3390/a13050121`.
- **BibTeX:** existe — `livieris2020ensemble`.
- **Mercado/dados:** preços horários de BTC, ETH e XRP de 1/1/2018 a 31/8/2019; treino com 10.177 pontos e teste com 4.415.
- **Metodologia:** averaging, bagging e stacking sobre combinações CNN, LSTM e BiLSTM; tarefas de regressão e direção do preço.
- **Papel para portfólios:** o artigo motiva a previsão por sua utilidade potencial à otimização, mas não realiza alocação ou backtest de carteira.
- **Principais resultados:** ensembles geralmente melhoram modelos isolados; stacking com kNN foi considerado o melhor compromisso, enquanto bagging teve resíduos autocorrelacionados.
- **Limitações:** alto custo computacional, sensibilidade a hiperparâmetros e configuração; avaliação de lucro/retorno é deixada para trabalho futuro.
- **Citação literal 1:** “The main contribution of this research is the combination of three of the most widely employed ensemble learning strategies: ensemble-averaging, bagging and stacking with advanced deep learning models for forecasting major cryptocurrency hourly prices.”
- **Página:** PDF 1; página impressa 1 de 21. Contexto: resumo.
- **Citação literal 2:** “The incorporation of deep learning models (which are by nature computational inefficient) in an ensemble learning approach, would lead the total training and prediction computation time to be considerably increased.”
- **Página:** PDF 19; página impressa 19 de 21. Contexto: limitação declarada.
- **Tradução/síntese:** ensembles DL podem elevar precisão e robustez, mas custam mais e ainda precisam demonstrar valor econômico numa carteira.
- **Melhor local para inserção:** Síntese crítica, no parágrafo sobre custo computacional e diferenças de validação.
- **Afirmação que pode sustentar:** arquiteturas mais complexas impõem trade-off entre precisão, confiabilidade e custo computacional.
- **Relação específica com o presente TCC:** alerta para comparar ganho de carteira com custo e complexidade, não só erro preditivo.
- **Impacto sobre a lacuna:** ajuda a definir a lacuna de avaliação ponta a ponta previsão→alocação.

### Volatility dynamics of crypto-currencies’ returns: Evidence from asymmetric and long memory GARCH models

- **Classificação:** PRIORIDADE C — modelagem de volatilidade cripto útil para discutir limitações da variância estática.
- **Origem:** acervo preexistente.
- **Autores:** Mohamed Fakhfekh; Ahmed Jeribi.
- **Ano:** 2020.
- **Caminho:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/Volatility dynamics of crypto-currencies’ returns.pdf`.
- **DOI:** `10.1016/j.ribaf.2019.101075`.
- **BibTeX:** existe — `fakhfekh2020volatility`.
- **Mercado/dados:** 16 criptomoedas de maior capitalização/volume; séries de retornos com tamanhos distintos conforme a história de negociação.
- **Metodologia:** 14 especificações das famílias FIGARCH, FIEGARCH, EGARCH, PGARCH e TGARCH com diferentes distribuições de erro.
- **Papel para portfólios:** não forma carteira; testa heterogeneidade, memória longa e assimetria da volatilidade que afetam a estimação de risco MV.
- **Principais resultados:** TGARCH com distribuição dupla exponencial foi a melhor para várias moedas; volatilidade respondeu mais a choques positivos, diferentemente do padrão típico de ações.
- **Limitações:** ajuste in-sample e escolha por likelihood/AIC/BIC; não mede previsão fora da amostra nem efeito em pesos; resultados variam por moeda.
- **Citação literal 1:** “The objective of this paper is to select the most optimum model or set of models useful for modeling sixteen of the most popular crypto-currencies associated volatility.”
- **Página:** PDF 1; página impressa não exibida. Contexto: resumo.
- **Citação literal 2:** “In addition, it has also been discovered that volatility tends to increase as a response to positive shocks rather than to negative shocks, reflecting an asymmetric effect that differs noticeably from that often observed in stock markets.”
- **Página:** PDF 9; página impressa 9. Contexto: conclusão.
- **Tradução/síntese:** o processo de volatilidade é assimétrico e heterogêneo entre moedas, o que questiona uma única estimativa histórica de variância.
- **Melhor local para inserção:** Estudos sobre média-variância e Markowitz em criptoativos, como evidência de cautela metodológica.
- **Afirmação que pode sustentar:** volatilidade cripto pode apresentar memória longa, assimetria e distribuição não gaussiana, afetando estimativas de risco.
- **Relação específica com o presente TCC:** fundamenta testes de robustez para estimadores de risco e janelas; não é comparador de alocação.
- **Impacto sobre a lacuna:** sustenta uma lacuna específica de tratamento de volatilidade, sem aumentar a contagem de estudos híbridos.

## Artigos já utilizados

Os 16 trabalhos citados no capítulo foram reencontrados no acervo preexistente e **não foram contabilizados como novos**:

- `brauneis2019cryptocurrency` — Brauneis e Mestel (2019), *Cryptocurrency-portfolios in a mean-variance framework*.
- `chaweewanchon2022markowitz` — Chaweewanchon e Chaysiri (2022), *Markowitz Mean-Variance Portfolio Optimization with Predictive Stock Selection Using Machine Learning*; duas cópias byte a byte.
- `chen2021mean` — Chen et al. (2021), *Mean-variance portfolio optimization using machine learning-based stock price prediction*.
- `du2022mean` — Du (2022), *Mean-variance portfolio optimization with deep learning based-forecasts for cointegrated stocks*.
- `giantsidi2025deep` — Giantsidi e Tarantola (2025), *Deep learning for financial forecasting: A review of recent trends*.
- `jang2023deep` — Jang e Seong (2023), *Deep reinforcement learning for stock portfolio optimization by connecting with modern portfolio theory*.
- `jeleskovic2024cryptocurrency` — Jeleskovic et al. (2024), *Cryptocurrency portfolio optimization: Utilizing a GARCH-copula model within the Markowitz framework*; o acervo também contém a versão de trabalho *Optimization of portfolios with cryptocurrencies: Markowitz and GARCH-Copula model approach*, tratada como o mesmo estudo, não como artigo novo.
- `jiang2024deep` — Jiang, Olmo e Atwi (2024), *Deep reinforcement learning for portfolio selection*.
- `lopez2025enhancing` — López de Prado et al. (2025), *Enhancing Markowitz's portfolio selection paradigm with machine learning*.
- `ma2021portfolio` — Ma, Han e Wang (2021), *Portfolio optimization with return prediction using deep learning and machine learning*.
- `padhi2022intelligent` — Padhi et al. (2022), *An Intelligent Fusion Model with Portfolio Selection and Machine Learning for Stock Market Prediction*.
- `paiva2019decision` — Paiva et al. (2019), *Decision-making for financial trading: A fusion approach of machine learning and portfolio selection*; duas cópias byte a byte.
- `slusarczyk2025optimal` — Ślusarczyk e Ślepaczuk (2025), *Optimal Markowitz portfolio using returns forecasted with time series and machine learning models*.
- `sutiene2024enhancing` — Sutiene et al. (2024), *Enhancing portfolio management using artificial intelligence: literature review*.
- `wang2020portfolio` — Wang et al. (2020), *Portfolio formation with preselection using deep learning from long-term financial data*.
- `zouaoui2025portfolio` — Zouaoui e Naas (2025), *Portfolio Optimization Based on MPT-LSTM Neural Networks: A case study of Cryptocurrency Markets*.

Esses 16 estudos correspondem a 19 PDFs físicos: as duplicações/versões de Chaweewanchon, Paiva e Jeleskovic explicam os três arquivos adicionais. Nenhum dos nove trabalhos válidos de `NOVOS SEC 3` foi reencontrado como PDF fora daquela pasta.

## Falsos positivos descartados

### Empirical evidence on deep learning-enhanced portfolio optimization: integrating CNN-LSTM forecasts with mean-variance theory in cryptocurrency markets

- **Motivo do descarte:** preprint SSRN explicitamente identificado no PDF como “This preprint research paper has not been peer reviewed”. O usuário determinou excluir preprints.
- **Elementos aparentemente presentes:** CNN-LSTM, otimização média-variância, criptoativos e backtest.
- **Por que não entra como trabalho válido:** ausência de revisão por pares/publicação acadêmica final confirmada no arquivo. A entrada `dunsin2025empirical` no `.bib` também está tipada como `@Misc` e marcada “Preprint”.
- **PDFs afetados:**
  - `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Empirical evidence on deep learning-enhanced portfolio optimization - integrating CNN-LSTM forecasts with mean-variance theory in cryptocurrency markets.pdf`
  - `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Empirical evidence on deep learning-enhanced portfolio woptimization - theory in cryptocurrency integrating CNN-LSTM markets forecasts with mean-variance.pdf`
- **Observação:** os dois arquivos têm SHA-256 idêntico (`fdad4521b20e967d3c761fc21e0e7c7210a9cf6b10699e8681c8379dec0a6265`); são cópias byte a byte do mesmo preprint, não dois trabalhos.

### Descartes da segunda etapa

- **Behavioral Finance Factors and Investment Decisions: A Mediating Role of Risk Perception** — parecia pertinente por “risco” e “decisão de investimento”, mas é estudo comportamental com investidores; não contém cripto, otimização de carteira ou ML.
- **Bitcoin: A safe haven asset and a winner amid political and economic uncertainties in the US?** — contém Bitcoin, diversificação/safe haven e métodos econométricos; não usa MV/Markowitz, ML nem seleção/alocação de carteira.
- **How financial literacy moderate the association between behaviour biases and investment decision?** — termos de investimento aparecem, mas o objeto é letramento financeiro e vieses; nenhum dos três eixos metodológicos.
- **Is there a risk-return trade-off in cryptocurrency markets? The case of Bitcoin** — contém risco, retorno, volatilidade e Bitcoin; investiga prêmio de risco por GARCH, sem carteira, pesos, MV ou ML.
- **Portfolio optimization with robust stochastic dominance testing: A genetic algorithm approach** — contém otimização e algoritmo genético, mas o estudo é de dominância estocástica em ativos tradicionais; não envolve cripto nem MV/ML na interseção requerida.
- **A crypto safe haven against Bitcoin** — contém cripto e safe haven; compara Tether e Bitcoin sem otimização, Markowitz ou ML.
- **Testing for herding in the cryptocurrency market** — contém cripto e comportamento coletivo, mas não seleção de carteira, MV ou ML.
- **The contagion effects of the COVID-19 pandemic: Evidence from gold and cryptocurrencies** — contém cripto, ouro, correlação e crise; não executa otimização de carteira nem usa ML.
- **Class-imbalanced dynamic financial distress prediction based on AdaBoost-SVM ensemble combined with SMOTE and time weighting** — contém ML e previsão financeira, mas o alvo é distress corporativo; não há cripto ou carteira.
- **Crude oil price prediction: A comparison between AdaBoost-LSTM and AdaBoost-GRU for improving forecasting performance** — contém DL e previsão de preços, mas somente petróleo; não há cripto nem carteira.
- **Artificial Intelligence Applied to Stock Market Trading: A Review** — revisão de IA em negociação de ações; não é cripto e não fornece integração própria com MV.
- **Financial Planning Behaviour: A Systematic Literature Review and New Theory Development** — planejamento financeiro pessoal; nenhum dos três eixos.
- **Mapping Financial Literacy: A Systematic Literature Review of Determinants and Recent Trends** — letramento financeiro; ocorrências financeiras não sustentam o problema de carteira pesquisado.

A versão de trabalho *Optimization of portfolios with cryptocurrencies: Markowitz and GARCH-Copula model approach* também não foi contabilizada como nova: além de não trazer ML, corresponde ao estudo posteriormente publicado de Jeleskovic et al. (2024), já citado no capítulo. Assim, a segunda etapa teve **13 falsos positivos distintos**; essa versão duplicada foi contabilizada entre duplicatas/artigos já usados, não como um 14º descarte.

## Mapa de inserção na Seção 3

### Estudos sobre Machine Learning aplicado à otimização de portfólios

- **Zhou et al. (2023):** previsão SVM com sentimento e atenção; acrescentaria um exemplo cripto no qual o sinal previsto modifica diretamente a variância mínima. Melhor posição: após o parágrafo que descreve previsão→otimização.
- **Xu et al. (2025):** LSTM→Markowitz mensal; acrescentaria o paralelo empírico mais direto ao projeto. Melhor posição: após Wang et al. (2020), antes da discussão de pré-seleção.
- **Han et al. (2024):** C-ENet prevê fatores cripto usados por MV/Bayes–Stein/Black–Litterman; acrescentaria escala e erro de estimação. Melhor posição: após Ma et al. (2021).
- **Toscano et al. (2026):** vários preditores alimentam MV/MMV; acrescentaria a constatação de que informação de risco mais rica não garante melhor alocação. Melhor posição: no fechamento de desempenho/limitações.
- **Peykani, Sabour e Tanasescu (2026):** XGBoost→MV/MSV/MAD; acrescentaria comparação entre medidas de risco. Melhor posição: após os exemplos de Random Forest/XGBoost.
- **Park e Yang (2023), Sebastião e Godinho (2021), Chevallier et al. (2021), Hamayel e Owda (2021), Derbentsev et al. (2021) e Livieris et al. (2020):** antecedentes de previsão cripto. Devem entrar, no máximo, em bloco breve, deixando explícito que não otimizam carteiras.

### Estudos sobre média-variância e Markowitz em criptoativos

- **Bakry et al. (2021):** restrições de peso e risco de cauda na inclusão de Bitcoin; acrescentaria que exposição excessiva pode reduzir Sharpe. Melhor posição: após a discussão de benefícios de diversificação.
- **Guesmi et al. (2019):** pesos MV com covariâncias GARCH; acrescentaria risco dinâmico e carteiras mistas. Melhor posição: após Jeleskovic et al. (2024).
- **Charfeddine et al. (2020):** dependências variantes no tempo e quebras; acrescentaria evidência direta à afirmação de correlações instáveis. Melhor posição: no parágrafo de limitações da aplicação de Markowitz.
- **Wang, Ma e Wu (2020):** stablecoins, pesos de risco mínimo, VaR e ES; acrescentaria heterogeneidade entre tipos de cripto e regimes. Melhor posição: após a discussão de risco de cauda.
- **Goodell e Goutte (2021):** correlações em crise e comportamento distinto de Tether; acrescentaria qualificação sobre benefícios de diversificação. Melhor posição: no fechamento da subseção.
- **Fakhfekh e Jeribi (2020):** memória longa e assimetria da volatilidade; acrescentaria base empírica para questionar variância histórica estática. Melhor posição: junto às premissas/limitações do MV.

### Estudos híbridos entre Markowitz, Machine Learning, deep learning e reinforcement learning

- **Zhou et al. (2023), Lorenzo e Arroyo (2023), Cui et al. (2023), Xu et al. (2025), Han et al. (2024), Toscano et al. (2026) e Peykani, Sabour e Tanasescu (2026):** devem formar o núcleo novo da subseção, pois integram os três eixos na metodologia.
- **Babaei, Giudici e Raffinetti (2022) e Franco e Laurini (2025):** acrescentariam XAI dos pesos/retornos; devem ser apresentados separadamente dos modelos preditivos porque o ML é explicativo e posterior à alocação.
- **Ordem aproximada:** começar com previsão→MV (Zhou, Xu, Han, Toscano, Peykani), seguir com pré-seleção (Lorenzo), decisão sequencial/risco de cauda (Cui) e terminar com interpretabilidade (Babaei; Franco e Laurini).

### Síntese crítica dos estudos relacionados

- **Demosthenous e Georgiou (2026):** fornece o diagnóstico mais abrangente: campo crescente, mas fragmentado e frequentemente estático.
- **Fang et al. (2022):** mostra que previsão, risco e construção de carteiras cripto já formavam literatura extensa até 2021.
- **Toscano et al. (2026) e Chevallier et al. (2021):** sustentam que complexidade ou ganho preditivo não asseguram melhor resultado econômico.
- **Sebastião e Godinho (2021):** acrescenta custos, drawdown e CVaR como contrapeso a Sharpe/retorno.
- **Babaei et al. (2022) e Franco e Laurini (2025):** permitem substituir a alegação genérica de “caixa-preta” por uma discussão sobre onde a explicabilidade é aplicada e o que ela efetivamente explica.

## Diagnóstico final da lacuna

1. **A alegação atual continua defensável?** Apenas em sentido restrito. É defensável dizer que vários artigos atualmente citados pelo capítulo tratam de ações/índices. Não é defensável concluir daí que faltam aplicações de MV + cripto + ML: as duas buscas localizaram nove estudos publicados nessa interseção.
2. **Quantos trabalhos combinam efetivamente os três eixos?** Nove: Zhou et al. (2023), Lorenzo e Arroyo (2023), Cui et al. (2023), Xu et al. (2025), Han et al. (2024), Toscano et al. (2026), Peykani, Sabour e Tanasescu (2026), Franco e Laurini (2025) e Babaei, Giudici e Raffinetti (2022). Os dois últimos empregam ML/XAI como explicação pós-alocação, ressalva que deve acompanhar a classificação.
3. **Em que diferem do presente TCC?** Sem inventar detalhes ainda não declarados sobre o experimento do TCC, o contraste comprovável é metodológico: os estudos usam SVM com dados alternativos, clustering, PPO/DRL, LSTM, C-ENet sobre fatores, múltiplos ensembles em tokens NFT, XGBoost em carteira mista e XAI posterior. Diferem também em universo (3 moedas, 7 moedas, 15 moedas, fatores de mais de 2.000 moedas, NFT tokens ou carteira mista), horizonte, risco (variância, CVaR, semivariância, MAD, Choquet) e protocolo de teste.
4. **Existe lacuna mais específica e defensável?** Sim, se corresponder ao desenho efetivo do TCC: comparação reproduzível de modelos preditivos sob o mesmo protocolo; avaliação walk-forward com retreinamento em múltiplos regimes; universo exclusivamente cripto e suficientemente amplo; custos, turnover, spread, slippage, liquidez e restrições; incerteza das previsões e estabilidade dos pesos; comparação de variância e risco de cauda; e explicabilidade integrada ao pipeline. O texto deve selecionar somente os itens que o experimento realmente cobre.
5. **Quais alegações precisam ser revistas?** A frase “como parte relevante dos estudos híbridos analisados se concentra em ações, índices ou mercados financeiros tradicionais, permanece espaço...” deve deixar de fundamentar uma lacuna ampla. O fechamento “essa diversidade metodológica oferece base para investigar modelos híbridos também no contexto de carteiras de criptoativos” também precisa reconhecer que essa investigação já existe. A afirmação de que o anteprojeto “se insere nessa lacuna” deve indicar a diferença experimental concreta, não apenas a combinação ML + Markowitz + cripto.

Em suma, o conjunto encontrado não invalida o tema do TCC; ele exige uma contribuição mais estreita e verificável. A literatura já cobre a combinação geral. O espaço remanescente está em **como** o pipeline é construído, validado e comparado sob condições realistas.

## Top trabalhos para adicionar imediatamente

1. **Zhou et al. (2023), *Multi-source data driven cryptocurrency price movement prediction and portfolio optimization*.** É o paralelo mais direto e bem validado de previsão cripto alimentando variância mínima, com benchmarks, teste fora da amostra e custos.
2. **Lorenzo e Arroyo (2023), *Online risk-based portfolio allocation on subsets of crypto assets...*.** Acrescenta pré-seleção por clustering e um universo de 534 ativos; é crucial para discutir dimensionalidade, covariância e seleção antes do MV.
3. **Cui et al. (2023), *Portfolio constructions in cryptocurrency market...*.** Mostra DRL aplicado diretamente a cripto e compara mecanismos MV e mean-CVaR, corrigindo a impressão de que a evidência DRL está restrita a ações.
4. **Han et al. (2024), *The diversification benefits of cryptocurrency factor portfolios...*.** Oferece grande universo, previsão fora da amostra, custos e múltiplos modelos de alocação; é forte para erro de estimação e generalização.
5. **Xu et al. (2025), *Cryptocurrency Portfolio Optimisation Based on LSTM Time Series Forecasting*.** É metodologicamente muito próximo de um pipeline LSTM→Markowitz e permite comparação direta, embora sua amostra seja pequena.
6. **Toscano et al. (2026), *When Richer Information Does Not Improve Allocation...*.** Fortalece a síntese crítica ao mostrar que um refinamento de risco e maior riqueza informacional não melhoram necessariamente o resultado.
7. **Babaei, Giudici e Raffinetti (2022), *Explainable artificial intelligence for crypto asset allocation*.** Deve entrar no debate de interpretabilidade porque explica pesos Markowitz reais em cripto, com a ressalva de que ML não prevê retornos.
8. **Demosthenous e Georgiou (2026), *Portfolio Optimization Methods for the Digital Asset Market: A Comprehensive Survey*.** É a melhor âncora para atualizar o estado da arte e formular uma lacuna mais específica sem depender de enumeração impressionista.

Como segunda linha de inclusão, Peykani, Sabour e Tanasescu (2026) acrescentam XGBoost e riscos downside; Bakry et al. (2021) e Charfeddine et al. (2020) fortalecem restrições, caudas e correlações dinâmicas.

## Resumo final da busca

- **PDFs examinados nesta execução:** 50, todos os PDFs fora de `NOVOS SEC 3`.
- **PDFs examinados na primeira execução:** 11, conforme registrado no relatório anterior.
- **Total aproximado de PDFs examinados nas duas etapas:** 61.
- **Estudos distintos representados nas duas etapas:** 53.
- **Novos trabalhos distintos encontrados nesta execução:** 14 publicados e válidos.
- **Novos trabalhos distintos acumulados:** 23.
- **Quantidade final de PRIORIDADE A:** 9.
- **Quantidade final de PRIORIDADE B:** 4.
- **Quantidade final de PRIORIDADE C:** 10.
- **Duplicatas identificadas:** 7 arquivos/versões redundantes nesta execução e 1 cópia redundante na primeira; 8 redundâncias físicas no total. A deduplicação considerou SHA-256, título, DOI, autores/ano e conteúdo.
- **Falsos positivos descartados:** 13 estudos distintos nesta execução; 14 acumulados ao incluir o preprint único da primeira etapa. O preprint da primeira etapa estava em dois PDFs idênticos e foi excluído conforme solicitado.
- **Trabalhos já utilizados reencontrados:** 16 estudos distintos, representados por 19 PDFs nesta execução.
- **BibTeX ausente entre os 14 novos da segunda etapa:** 1 — Guesmi et al. (2019). Os outros 13 possuem chave em `referencias.bib`.
- **Método:** leitura integral do capítulo e do relatório anterior; extração dos 50 PDFs com `pdftotext -layout`; triagem combinada de termos MV/Markowitz, cripto e ML; conferência por página de método, dados, resultados e limitações; descarte de ocorrências em referências; verificação de publicação/preprint; deduplicação por hash, título, DOI e conteúdo; e confronto com as quatro subseções atuais.
