# Mapa bibliográfico canônico da Seção 3

## Visão geral

| Subseção | Interseção | Objetivo | Estudos centrais |
|---|---|---|---|
| 3.1 | ML + MV/otimização de portfólios | Documentar o pipeline dados → previsão → estimativas → otimização → pesos → avaliação fora da amostra | Paiva et al.; Wang et al.; Ma et al.; Jensen et al. |
| 3.2 | ML + cripto | Reunir evidência direta sobre previsão, regimes, trading, deep learning e RL em cripto, inclusive resultados negativos | Lucarelli e Borrotti; Sebastião e Godinho; Chevallier et al.; Park e Yang |
| 3.3 | MV + cripto | Documentar diversificação, dependência dinâmica, risco de cauda, restrições e desempenho fora da amostra | Brauneis e Mestel; Guesmi et al.; Charfeddine et al.; Bakry et al.; Jeleskovic et al. |
| 3.4 | ML + MV + cripto | Reunir os trabalhos mais aderentes ao pipeline automatizado de previsão/seleção/interpretação e alocação | Zhou et al.; Lorenzo e Arroyo; Cui et al.; Han et al.; Xu et al.; Toscano et al.; Babaei et al. |
| 3.5 | síntese baseada em evidência | Apoiar a redação crítica por meio de surveys e resultados literais dos estudos originais | Demosthenous e Georgiou; Fang et al.; estudos empíricos das subseções anteriores |

### Convenções deste arquivo

- Este é o arquivo canônico de fichamento da SEC3. Ele funde o mapa por subseção com os dados de `CITACOES_COMPLEMENTARES_SEC3.md`, sem alterar o catálogo de origem.
- “Stack” significa o conjunto efetivamente informado no artigo: fontes de dados, variáveis, modelos de ML/DL/RL, estimadores de risco, otimizadores, validação e regras de rebalanceamento. Linguagem, biblioteca ou hardware só devem ser citados quando o artigo os declarar; ausência dessa informação não foi preenchida por inferência.
- As citações são transcrições dos artigos com extensão suficiente para preservar método, resultado e ressalvas relevantes. Não há limite artificial de tamanho: quando uma frase isolada impedir a reconstrução da ideia, conserva-se o conjunto de frases necessário. A página indicada é a página do PDF e, quando disponível, também a paginação impressa.
- “O que o trecho comprova” é apenas uma etiqueta de recuperação da evidência; não substitui a leitura do trecho literal.
- Trabalhos duplicados por título/DOI/autores aparecem uma única vez. Versões e cópias físicas são registradas na auditoria, não tratadas como estudos adicionais.
- A classificação do papel do ML em 3.4 segue: **A** fornece parâmetros/sinais ao MV; **B** seleciona ativos; **C** substitui a otimização por política aprendida; **D** interpreta resultados após a otimização.

## 3.1 Estudos sobre Machine Learning aplicado à otimização de portfólios

### Paiva et al. (2019) — Decision-making for financial trading: A fusion approach of machine learning and portfolio selection

- **Chave BibTeX:** `paiva2019decision`.
- **DOI/publicação:** [10.1016/j.eswa.2018.08.003](https://doi.org/10.1016/j.eswa.2018.08.003), *Expert Systems with Applications*.
- **Interseção:** ML + MV, sem cripto.
- **Mercado/universo:** ações do Ibovespa.
- **Período e frequência:** 3.716 pregões fora da amostra; janelas mensais compostas de janelas móveis diárias.
- **Stack e métodos usados pelo autor:** SVM classifica ativos com perspectiva de ganho; os ativos selecionados alimentam a alocação MV. O estudo compara 81 configurações de SVM+MV com SVM+1/N, Random+MV e Ibovespa.
- **Papel do ML:** prever/classificar e filtrar o universo elegível.
- **Papel do MV/Markowitz:** determinar a composição/pesos após a classificação.
- **Covariância prevista?:** não; o ML atua na seleção, não na previsão explícita da matriz de covariância.
- **Principais resultados:** a fusão apresentou resultados relevantes no protocolo testado, mas custos de corretagem e valor mínimo de operação restringiram a implementação.
- **Limitações:** mercado único, muitas configurações candidatas, alvo de classificação específico e sensibilidade a custos; o conjunto de configurações amplia o risco de seleção ex post.
- **Por que é útil nesta subseção:** explicita o encadeamento seleção por ML → MV → avaliação econômica e mostra que a etapa final, não a acurácia isolada, deve definir a utilidade.
- **Afirmações que pode sustentar no TCC:** ML pode entrar antes do MV como filtro de ativos; desempenho bruto pode desaparecer quando a estratégia exige muita negociação.
- **Relação com o presente TCC:** é um antecedente brasileiro e um benchmark de protocolo; difere por trabalhar com ações e SVM, não cripto e o conjunto de modelos do TCC.

#### Citações diretas verificadas

> “The experiments were formulated using historical data for 3716 trading days for the out-of-sample analysis. Simulations were conducted without including transaction costs and also with the inclusion of a proportion of such costs. We specifically analyzed the effect of brokerage costs on buying and selling stocks on the Brazilian market. This study also evaluated the classifier’s performance, portfolios’ cardinality, and models’ returns and risks. The proposed main model showed significant results, although demand for trading value can be a limiting factor for its implementation.”

- **Página:** PDF 1, resumo.
- **Contexto:** os autores qualificam a viabilidade da estratégia após custos.
- **O que o trecho comprova:** a qualidade do pipeline deve ser julgada pelo resultado líquido e executável, não apenas pelo retorno bruto.

> “This study proposes a unique decision-making model for day trading investments on the stock market. In this regard, the model was developed using a fusion approach of a classifier based on machine learning, with the support vector machine (SVM) method, and the mean-variance (MV) method for portfolio selection. Monthly rolling windows were used to choose the best-performing parameter sets (the in-sample phase) and testing (the out-of-sample phase).”

- **Página:** PDF 1, resumo.
- **Contexto:** descrição do pipeline, da combinação SVM–MV e do desenho temporal de validação.
- **O que o trecho comprova:** a proposta não é apenas um classificador; ela liga seleção por SVM, otimização MV e validação em janelas móveis dentro e fora da amostra.

---

### Wang et al. (2020) — Portfolio formation with preselection using deep learning from long-term financial data

- **Chave BibTeX:** `wang2020portfolio`.
- **DOI/publicação:** [10.1016/j.eswa.2019.112467](https://doi.org/10.1016/j.eswa.2019.112467), *Expert Systems with Applications*.
- **Interseção:** ML + MV, sem cripto.
- **Mercado/universo:** 100 ações da London Stock Exchange.
- **Período e frequência:** março de 1994 a março de 2019; séries de mercado com formação periódica de carteiras.
- **Stack e métodos usados pelo autor:** LSTM prevê retornos e pré-seleciona ativos; SVM, Random Forest, DNN e ARIMA são comparadores; o MV otimiza o subconjunto selecionado.
- **Papel do ML:** previsão e pré-seleção.
- **Papel do MV/Markowitz:** converter o subconjunto em pesos ótimos.
- **Covariância prevista?:** não; o componente preditivo se concentra em retornos/seleção.
- **Principais resultados:** LSTM+MV apresentou vantagem em parte dos cenários; para nove ativos, o artigo reporta retorno anualizado de 0,136 e Sharpe de 0,58 antes dos custos. As Tabelas 6–8 mostram mudança de classificação após custos.
- **Limitações:** sensibilidade à cardinalidade, à janela e à hipótese de custo; um mercado; não prova que LSTM domina em outros regimes.
- **Por que é útil nesta subseção:** estabelece a variante pré-seleção → MV e demonstra por que tamanho do universo e turnover fazem parte da comparação.
- **Afirmações que pode sustentar no TCC:** reduzir o universo com ML pode melhorar a qualidade das entradas do otimizador, mas o benefício depende do custo de alterar a composição.
- **Relação com o presente TCC:** fornece um desenho diretamente transferível para cripto, em que ativos previstos/ranqueados são filtrados antes do Markowitz.

#### Citações diretas verificadas

> “In the first stage, long short-term memory networks are used to forecast the return of assets and select assets with higher potential returns. After comparing the outcomes of the long short-term memory networks against support vector machine, random forest, deep neural networks, and autoregressive integrated moving average model, we discover that long short-term memory networks are appropriate for financial time-series forecasting, to beat the other benchmark models by a very clear margin. In the second stage, based on selected assets with higher returns, the mean-variance model is applied for portfolio optimisation.”

- **Página:** PDF 1, resumo.
- **Contexto:** definição do segundo estágio do método.
- **O que o trecho comprova:** o ML não substitui necessariamente o otimizador; pode apenas definir quais ativos chegam a ele.

> “The validation of this methodology is carried out by comparing the proposed model with the other five baseline strategies, to which the proposed model clearly outperforms others in terms of the cumulative return per year, Sharpe ratio per triennium as well as average return to the risk per month of each triennium.”

- **Página:** PDF 1, resumo.
- **Contexto:** síntese da comparação de LSTM+MV com cinco estratégias-base.
- **O que o trecho comprova:** a vantagem reportada é econômica e ajustada ao risco, não apenas preditiva.

---

### Ma et al. (2021) — Portfolio optimization with return prediction using deep learning and machine learning

- **Chave BibTeX:** `ma2021portfolio`.
- **DOI/publicação:** [10.1016/j.eswa.2020.113973](https://doi.org/10.1016/j.eswa.2020.113973), *Expert Systems with Applications*.
- **Interseção:** ML + MV/Omega, sem cripto.
- **Mercado/universo:** constituintes do China Securities 100.
- **Período e frequência:** 2007–2015; os quatro últimos anos são usados para avaliar as estratégias.
- **Stack e métodos usados pelo autor:** RF, SVR, LSTM, DMLP e CNN estimam retornos; ARIMA é benchmark; as previsões alimentam carteiras MV e Omega.
- **Papel do ML:** estimar retornos e apoiar pré-seleção.
- **Papel do MV/Markowitz:** transformar retornos esperados e risco estimado em pesos; Omega funciona como objetivo alternativo.
- **Covariância prevista?:** não foi identificada previsão ML da covariância; o ganho atribuído ao ML está na previsão de retorno.
- **Principais resultados:** RF+MV foi a melhor variante MV no experimento; o artigo relata que a alta rotatividade reduz aproximadamente metade do retorno total das estratégias líderes.
- **Limitações:** um índice/mercado, execução simulada e múltiplas combinações de modelos; a escolha do vencedor pode ser específica ao período.
- **Por que é útil nesta subseção:** compara algoritmos dentro do mesmo pipeline e mostra que o melhor preditor não precisa ser o mais complexo.
- **Afirmações que pode sustentar no TCC:** ganho preditivo deve ser convertido em retorno líquido; turnover pode inverter a conclusão econômica.
- **Relação com o presente TCC:** é um benchmark forte para comparar modelos sob a mesma regra de carteira, incluindo custos e um objetivo alternativo ao MV.

#### Citações diretas verificadas

> “This paper combines return prediction in portfolio formation with two machine learning models, i.e., random forest (RF) and support vector regression (SVR), and three deep learning models, i.e., LSTM neural network, deep multilayer perceptron (DMLP) and convolutional neural network. To be specific, this paper first applies these prediction models for stock preselection before portfolio formation. Then, this paper incorporates their predictive results in advancing mean–variance (MV) and omega portfolio optimization models.”

- **Página:** PDF 1, resumo.
- **Contexto:** descrição da stack preditiva e de como seus resultados entram nos modelos MV e Omega.
- **O que o trecho comprova:** o experimento mantém a camada de previsão separada da camada de otimização e compara cinco modelos preditivos alimentando dois objetivos de carteira.

> “Experimental results show that MV and omega models with RF return prediction, i.e., RF+MVF and RF+OF, outperform the other models. Further, RF+MVF is superior to RF+OF. Due to the high turnover of these two models, this paper discusses their performance after deducting the transaction fee caused by turnover. [...] Moreover, RF+MVF performs better than SVR+OF and high turnover erodes nearly half of their total returns especially for RF+OF and RF+MVF.”

- **Página:** PDF 1, resumo.
- **Contexto:** resultado líquido após deduzir as taxas associadas à rotatividade.
- **O que o trecho comprova:** o modelo vencedor em termos brutos pode perder aproximadamente metade do retorno quando o turnover é monetizado.

---

### Jensen et al. (2026) — Machine Learning and the Implementable Efficient Frontier

- **Chave BibTeX:** ausente no `.bib` consultado; sugestão, se futuramente autorizado: `jensen2026machine`.
- **DOI/publicação:** [10.1093/rfs/hhag022](https://doi.org/10.1093/rfs/hhag022), *The Review of Financial Studies*, 39(10), 3035–3078.
- **Interseção:** ML + escolha de carteira com custos; compara explicitamente Markowitz-ML.
- **Mercado/universo:** ações norte-americanas, com amostra-base de ações NYSE acima da mediana de capitalização.
- **Período e frequência:** 1981–2020; atualização mensal.
- **Stack e métodos usados pelo autor:** aprende diretamente pesos/portfólio sob objetivo econômico com custos e persistência dos sinais; compara Portfolio-ML, Multiperiod-ML, Static-ML, Markowitz-ML, fatores ML, minimum variance, 1/N e mercado.
- **Papel do ML:** na proposta principal, aprender a política de pesos consciente de custos; no benchmark Markowitz-ML, prever retornos e risco separadamente.
- **Papel do MV/Markowitz:** benchmark frictionless e componente teórico da fronteira; o artigo mostra que a fronteira relevante para implementação é líquida de custos.
- **Covariância prevista?:** o benchmark Markowitz-ML estima risco e retorno; a proposta evita tratar a previsão pontual de retorno como único objetivo.
- **Principais resultados:** Markowitz-ML tem Sharpe bruto de 2,06, mas retorno líquido altamente negativo devido à negociação agressiva; Portfolio-ML alcança Sharpe líquido de 1,33 no cenário-base de grande investidor.
- **Limitações:** ações grandes e infraestrutura de dados/execução incompatível com investidor pequeno; parâmetros de impacto e liquidez são específicos ao mercado acionário.
- **Por que é útil nesta subseção:** fornece o contraponto conceitual mais atual ao pipeline em duas etapas: otimizar acurácia primeiro e custos depois pode aprender sinais economicamente inúteis.
- **Afirmações que pode sustentar no TCC:** a fronteira eficiente implementável deve ser medida fora da amostra e líquida de custos; aprender pesos diretamente é uma alternativa ao ML que apenas fornece médias ao MV.
- **Relação com o presente TCC:** oferece um padrão de avaliação mais exigente. Mesmo que o TCC mantenha previsão→Markowitz, deve medir turnover, custos e persistência dos sinais.

#### Citações diretas verificadas

> “investors should focus on out-of-sample performance net of trading costs”

- **Página:** p. 3078, conclusão.
- **Contexto:** critério proposto para avaliar métodos de escolha de carteira.
- **O que o trecho comprova:** a fronteira ex ante e sem fricções não é evidência suficiente de valor econômico.

> “The superior net-of-cost performance is achieved by learning directly about portfolio weights using an economic objective.”

- **Página:** p. 3035, resumo.
- **Contexto:** distinção entre aprender pesos sob um objetivo econômico e prever parâmetros separadamente para um Markowitz sem fricções.
- **O que o trecho comprova:** o objetivo de treinamento e os custos devem fazer parte do problema de carteira, não apenas da avaliação posterior.

## 3.2 Estudos da aplicação de Machine Learning ao mercado de criptoativos

### Lucarelli e Borrotti (2020) — A deep Q-learning portfolio management framework for the cryptocurrency market

- **Chave BibTeX:** `lucarelli2020deepq`.
- **DOI/publicação:** [10.1007/s00521-020-05359-8](https://doi.org/10.1007/s00521-020-05359-8), *Neural Computing and Applications*.
- **Interseção:** ML/RL + cripto; não usa MV clássico.
- **Mercado/universo:** BTC, LTC, ETH e XRP.
- **Período e frequência:** dados horários de 1/7/2017 a 25/12/2018, cerca de 13 mil observações; dez testes consecutivos de 15 dias fora da amostra.
- **Stack e métodos usados pelo autor:** agentes DQN, Double DQN e Dueling Double DQN por ativo, coordenados por recompensa global de retorno ou retorno+Sharpe; compara pesos iguais e algoritmo genético.
- **Papel do ML:** decidir dinamicamente comprar, manter ou vender e a exposição; substitui a otimização MV.
- **Papel do MV/Markowitz:** ausente; é comparador conceitual de gestão dinâmica, não integração com Markowitz.
- **Principais resultados:** todos os frameworks foram lucrativos em média, mas nenhum foi positivo em todos os períodos; o melhor retorno diário médio reportado foi 4,67%, com alta variabilidade. Custos de 0,2% por compra e venda foram incorporados.
- **Limitações:** quatro ativos, somente fechamento, testes de 15 dias, ações discretizadas e alta dispersão; resultado de RL não identifica qual parte vem do sinal, recompensa ou regra de exposição.
- **Por que é útil nesta subseção:** representa a classe em que o ML substitui a camada de otimização e aprende pesos/ações diretamente.
- **Afirmações que pode sustentar no TCC:** RL permite decisão sequencial em mercado 24/7, mas desempenho médio positivo pode esconder instabilidade entre janelas.
- **Relação com o presente TCC:** serve como alternativa ao pipeline previsão→MV, não como trabalho metodologicamente equivalente.

#### Citações diretas verificadas

> “All deep Q-learning portfolio management frameworks are tested and compared by sampling 10 consecutive test periods, from 25 July 2018 to 25 December 2018. Each framework is run 5 times for each test period. Each test period is composed by 15 out-of-sample trading days for each framework. [...] In 80% of the cases the proposed frameworks have a higher daily returns with respect to the cryptocurrencies. No frameworks reach positive daily returns in all test periods.”

- **Página:** PDF 10; impressa 17238.
- **Contexto:** resultados dos dez períodos fora da amostra.
- **O que o trecho comprova:** a estratégia pode ser promissora em média sem ser estável entre regimes curtos.

> “On test period 8, DQN-RF2 gets an exceptional result obtaining daily returns equal to 24.781%. On the same test period, DDDQN-RF2 obtains the worst result (−12.052%). Daily returns values are positive for all frameworks on 40% of the test periods. On the remaining 60%, at least one framework gets negative performance. However, all frameworks obtain positive daily returns values on average. [...] DQN-RF2 reaches the highest value of average daily return, more precisely 4.67%.”

- **Página:** PDF 10; impressa 17238.
- **Contexto:** média dos dez períodos de teste de 15 dias, acompanhada no artigo por elevada dispersão do ROI.
- **O que o trecho comprova:** o maior retorno médio coexistiu com instabilidade entre subperíodos, por isso a média isolada não resume o risco do agente.

---

### Park e Yang (2023) — Intelligent cryptocurrency trading system using integrated AdaBoost-LSTM with market turbulence knowledge

- **Autores:** Sangjin Park; Jae-Suk Yang.
- **Ano:** 2023.
- **Caminho:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\2 parte intro - Cripto/Intelligent cryptocurrency trading system using integrated.pdf`.
- **Duplicata/versão identificada:** outra cópia em `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\3 parte intro - machine learning/Intelligent cryptocurrency trading system using integrated.pdf`.
- **DOI:** `10.1016/j.asoc.2023.110568`.
- **BibTeX:** existe — `park2023intelligent`.
- **Mercado/dados:** Bitcoin diário de 1/6/2016 a 30/4/2022; treino, validação e teste, com teste de 1/4/2021 a 30/4/2022.
- **Metodologia:** AdaBoost-LSTM para direção do preço, Markov regime-switching para turbulência e regra long-only com horizontes de 1, 3 e 5 dias.
- **Papel para portfólios:** não aloca entre ativos; fornece um modelo de sinal e filtro de risco potencialmente utilizável antes da otimização.
- **Principais resultados:** turbulência prolongada por 21 dias ou mais sinaliza alto risco; estratégia integrada apresentou retornos e Sharpes superiores aos indicadores técnicos de referência, especialmente nos horizontes de 3 e 5 dias.
- **Limitações:** único ativo; backtest de um ano; regras regulatórias e CBDCs podem gerar volatilidade não capturada; desempenho da negociação não demonstra benefício em carteira MV.
#### Citações diretas verificadas

- **Citação literal 1:** “We propose a fusion approach combining technology with economic knowledge to achieve accurate predictions. Firstly, we provide an ensemble prediction framework that integrates the AdaBoost algorithm with the LSTM deep learning model [...]. Secondly [...] we combine the econometrics Markov regime-switching model with the AdaBoost-LSTM model.”
- **Página:** PDF 1; página impressa 1. Contexto: resumo.
- **Citação literal 2:** “The simulation of our trading system for one year (from April 1, 2021 to April 30, 2022) showed cumulative returns and Sharpe ratios that greatly exceeded those of other trading strategies such as the stochastic oscillator and MACD.”
- **Página:** PDF 19; página impressa 19. Contexto: conclusão.
- **O que o trecho comprova:** combinar previsão DL com informação de regime melhora sinais e controle de risco, mas ainda não demonstra como esses sinais afetam pesos MV.
- **Afirmações que pode sustentar no TCC:** regimes de turbulência e overfitting precisam ser considerados na etapa preditiva.
- **Relação específica com o presente TCC:** sugere incluir variáveis/regimes de mercado ou testar estabilidade entre regimes; não é comparador direto de carteira.
- **Por que é útil nesta subseção:** regimes de turbulência e overfitting precisam ser considerados na etapa preditiva.

---

### Sebastião e Godinho (2021) — Forecasting and trading cryptocurrencies with machine learning under changing market conditions

- **Autores:** Helder Sebastião; Pedro Godinho.
- **Ano:** 2021.
- **Caminho:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\3 parte intro - machine learning/Forecasting and trading cryptocurrencies.pdf`.
- **Duplicata identificada:** cópia byte a byte em `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\2 parte intro - Cripto/s40854-020-00217-x (1).pdf`.
- **DOI:** `10.1186/s40854-020-00217-x`.
- **BibTeX:** existe — `sebastiao2021forecasting`.
- **Mercado/dados:** BTC, ETH e LTC; variáveis de negociação e atividade de rede de 15/8/2015 a 3/3/2019; teste começa em 13/4/2018.
- **Metodologia:** modelos lineares, Random Forest e SVM em classificação/regressão, janela móvel e ensembles por concordância; estratégias long-only com custo round-trip de 0,5%.
- **Papel para portfólios:** não define pesos multivariados; avalia sinais que poderiam fornecer retornos previstos a uma camada de alocação.
- **Principais resultados:** não há modelo individual universalmente superior; Ensemble 5 em ETH e LTC obteve Sharpe anualizado de 80,17% e 91,35%, mas tail risk e drawdown permanecem altos e custos tornam cinco estratégias negativas.
- **Limitações:** estratégia por ativo, short selling proibido, baixo desempenho preditivo individual e forte dependência do regime e do critério econômico de seleção.
#### Citações diretas verificadas

- **Citação literal 1:** “The models are validated in a period characterized by unprecedented turmoil and tested in a period of bear markets, allowing the assessment of whether the predictions are good even when the market direction changes between the validation and test periods.”
- **Página:** PDF 1; página impressa 1 de 30. Contexto: resumo.
- **Citação literal 2:** “Additionally, these trading strategies are subjected to a high tail risk, with CVaRs at 1% between 3.88% and 13.40% and maximum drawdown between 11.15% and 48.06%.”
- **Página:** PDF 27; página impressa 27 de 30. Contexto: conclusão.
- **O que o trecho comprova:** resultados positivos de ML podem coexistir com baixa acurácia, alto risco de cauda, drawdowns e sensibilidade a custos/regimes.
- **Afirmações que pode sustentar no TCC:** avaliar apenas retorno ou acurácia não basta; custos e perdas extremas podem mudar a conclusão.
- **Relação específica com o presente TCC:** oferece um protocolo de robustez útil para a etapa preditiva, mas não determina pesos de carteira.
- **Por que é útil nesta subseção:** avaliar apenas retorno ou acurácia não basta; custos e perdas extremas podem mudar a conclusão.

---

### Chevallier et al. (2021) — Is It Possible to Forecast the Price of Bitcoin?

- **Autores:** Julien Chevallier; Dominique Guégan; Stéphane Goutte.
- **Ano:** 2021.
- **Caminho:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\2 parte intro - Cripto/forecasting-03-00024-v2.pdf`.
- **DOI:** `10.3390/forecast3020024`.
- **BibTeX:** existe — `chevallier2021forecast`.
- **Mercado/dados:** Bitcoin spot e futuros, 17 criptomoedas e ativos de ações, títulos, câmbio e commodities; 57 séries diárias entre 13/1/2015 e 31/12/2020, 2.070 observações.
- **Metodologia:** ANN, SVM, Random Forest, kNN, AdaBoost e Ridge, com AR(1) e buy-and-hold como referências; análises de subperíodos e negociação.
- **Papel para portfólios:** estuda informação cruzada entre classes e previsão de Bitcoin, mas não calcula pesos ou fronteira eficiente.
- **Principais resultados:** outras criptomoedas melhoram a previsão; AdaBoost/Random Forest se destacam em parte dos testes, mas buy-and-hold vence as regras de negociação em geral.
- **Limitações:** um ativo-alvo; resultados variam por período e conjunto de atributos; boa acurácia não se converte automaticamente em ganho econômico.
#### Citações diretas verificadas

- **Citação literal 1:** “The main contribution is to use these data analytics techniques with great caution in the parameterization, instead of classical parametric modelings (AR), to disentangle the non-stationary behavior of the data.”
- **Página:** PDF 1; página impressa 377. Contexto: resumo.
- **Citação literal 2:** “Across the trading strategies, we have documented that (i) machine learning algorithms (configured as bots following buy/sell signals) do not teach how to trade, (ii) the buy-and-hold strategy appears the best [...].”
- **Página:** PDF 39; página impressa 415. Contexto: conclusão.
- **O que o trecho comprova:** previsão estatisticamente útil não garante estratégia economicamente superior; não estacionariedade e parametrização exigem cautela.
- **Afirmações que pode sustentar no TCC:** ganho preditivo não implica, por si só, ganho de carteira ou de negociação.
- **Relação específica com o presente TCC:** reforça a necessidade de avaliar a carteira final fora da amostra, além das métricas do preditor.
- **Por que é útil nesta subseção:** ganho preditivo não implica, por si só, ganho de carteira ou de negociação.

---

### Hamayel e Owda (2021) — A Novel Cryptocurrency Price Prediction Model Using GRU, LSTM and bi-LSTM Machine Learning Algorithms

- **Autores:** Mohammad J. Hamayel; Amani Yousef Owda.
- **Ano:** 2021.
- **Caminho:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\3 parte intro - machine learning/A Novel Cryptocurrency Price Prediction Model Using GRU, LSTM and bi-LSTM Machine Learning Algorithms.pdf`.
- **DOI:** `10.3390/ai2040030`.
- **BibTeX:** existe — `hamayel2021novel`.
- **Mercado/dados:** BTC, ETH e LTC; treino de 22/1/2018 a 22/10/2020 e teste de 22/10/2020 a 30/6/2021.
- **Metodologia:** GRU, LSTM e BiLSTM univariadas, avaliadas por MAPE e RMSE.
- **Papel para portfólios:** apenas previsão de preços; não seleciona ativos nem calcula pesos.
- **Principais resultados:** GRU obteve os menores MAPEs nas três moedas; BiLSTM foi a menos precisa; os autores propõem incluir notícias, tweets e volume em trabalhos futuros.
- **Limitações:** somente preço histórico, três ativos, divisão temporal única e ausência de teste econômico/custos; erro de preço não prova utilidade para retornos ou pesos.
#### Citações diretas verificadas

- **Citação literal 1:** “This paper proposes three types of recurrent neural network (RNN) algorithms used to predict the prices of three types of cryptocurrencies, namely Bitcoin (BTC), Litecoin (LTC), and Ethereum (ETH).”
- **Página:** PDF 1; página impressa 477. Contexto: resumo.
- **Citação literal 2:** “The results show that GRU outperformed the other algorithms with a MAPE of 0.2454%, 0.8267%, and 0.2116% for BTC, ETH, and LTC, respectively.”
- **Página:** PDF 18; página impressa 494. Contexto: conclusão.
- **O que o trecho comprova:** GRU foi superior no experimento, mas o estudo não demonstra se essas previsões melhoram uma alocação MV.
- **Afirmações que pode sustentar no TCC:** arquiteturas recorrentes não são intercambiáveis; desempenho depende da moeda e do modelo.
- **Relação específica com o presente TCC:** útil para justificar a comparação GRU/LSTM/BiLSTM, se esses modelos fizerem parte do experimento; não é trabalho relacionado de otimização por si só.
- **Por que é útil nesta subseção:** arquiteturas recorrentes não são intercambiáveis; desempenho depende da moeda e do modelo.

---

### Derbentsev et al. (2021) — Comparative Performance of Machine Learning Ensemble Algorithms for Forecasting Cryptocurrency Prices

- **Autores:** V. Derbentsev; V. Babenko; K. Khrustalev; H. Obruch; S. Khrustalova.
- **Ano:** 2021.
- **Caminho:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\3 parte intro - machine learning/Comparative Performance of Machine Learning Ensemble Algorithms for.pdf`.
- **DOI:** `10.5829/ije.2021.34.01a.16`.
- **BibTeX:** existe — `derbentsev2021comparative`.
- **Mercado/dados:** BTC e XRP de 1/1/2015 a 31/12/2019 (1.826 observações) e ETH de 7/8/2015 a 31/12/2019 (1.608); 92 observações finais fora da amostra.
- **Metodologia:** Random Forest e Stochastic Gradient Boosting Machine, com defasagens, médias móveis e volume.
- **Papel para portfólios:** prevê preços um passo à frente; não avalia carteira, pesos ou retorno econômico.
- **Principais resultados:** MAPE fora da amostra entre 0,92% e 2,61%; atributos adicionais melhoraram a precisão em 1%–3% em média.
- **Limitações:** teste curto, apenas três moedas, foco em erro de preço e ausência de custos/backtest; seleção de atributos e modelos adicionais ficam para pesquisa futura.
#### Citações diretas verificadas

- **Citação literal 1:** “To check the effectiveness of these models we made an out-of-sample forecast for selected time series by using the one step ahead technique.”
- **Página:** PDF 1; página impressa 140. Contexto: resumo.
- **Citação literal 2:** “According to our results, the out of sample accuracy of short-term forecasting daily prices obtained by SGBM and RF in terms of MAPE for three of the most capitalized cryptocurrencies (BTC, ETH, and XRP) was within 0.92-2.61 %.”
- **Página:** PDF 7; página impressa 146. Contexto: conclusão.
- **O que o trecho comprova:** ensembles de árvores conseguem baixo erro de preço no teste adotado, sem evidência de que isso resulte em melhores pesos ou Sharpe.
- **Afirmações que pode sustentar no TCC:** Random Forest/boosting são alternativas relevantes para previsão cripto fora da amostra.
- **Relação específica com o presente TCC:** pode justificar modelos candidatos e atributos, mas precisa ser conectado a uma avaliação de carteira no TCC.
- **Por que é útil nesta subseção:** Random Forest/boosting são alternativas relevantes para previsão cripto fora da amostra.

---

### Livieris et al. (2020) — Ensemble Deep Learning Models for Forecasting Cryptocurrency Time-Series

- **Autores:** Ioannis E. Livieris; Emmanuel Pintelas; Stavros Stavroyiannis; Panagiotis Pintelas.
- **Ano:** 2020.
- **Caminho:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\3 parte intro - machine learning/Ensemble Deep Learning Models for Forecasting.pdf`.
- **DOI:** `10.3390/a13050121`.
- **BibTeX:** existe — `livieris2020ensemble`.
- **Mercado/dados:** preços horários de BTC, ETH e XRP de 1/1/2018 a 31/8/2019; treino com 10.177 pontos e teste com 4.415.
- **Metodologia:** averaging, bagging e stacking sobre combinações CNN, LSTM e BiLSTM; tarefas de regressão e direção do preço.
- **Papel para portfólios:** o artigo motiva a previsão por sua utilidade potencial à otimização, mas não realiza alocação ou backtest de carteira.
- **Principais resultados:** ensembles geralmente melhoram modelos isolados; stacking com kNN foi considerado o melhor compromisso, enquanto bagging teve resíduos autocorrelacionados.
- **Limitações:** alto custo computacional, sensibilidade a hiperparâmetros e configuração; avaliação de lucro/retorno é deixada para trabalho futuro.
#### Citações diretas verificadas

- **Citação literal 1:** “The main contribution of this research is the combination of three of the most widely employed ensemble learning strategies: ensemble-averaging, bagging and stacking with advanced deep learning models for forecasting major cryptocurrency hourly prices.”
- **Página:** PDF 1; página impressa 1 de 21. Contexto: resumo.
- **Citação literal 2:** “The incorporation of deep learning models (which are by nature computational inefficient) in an ensemble learning approach, would lead the total training and prediction computation time to be considerably increased.”
- **Página:** PDF 19; página impressa 19 de 21. Contexto: limitação declarada.
- **O que o trecho comprova:** ensembles DL podem elevar precisão e robustez, mas custam mais e ainda precisam demonstrar valor econômico numa carteira.
- **Afirmações que pode sustentar no TCC:** arquiteturas mais complexas impõem trade-off entre precisão, confiabilidade e custo computacional.
- **Relação específica com o presente TCC:** alerta para comparar ganho de carteira com custo e complexidade, não só erro preditivo.
- **Por que é útil nesta subseção:** arquiteturas mais complexas impõem trade-off entre precisão, confiabilidade e custo computacional.

## 3.3 Estudos de MV aplicados ao mercado de criptoativos

### Brauneis e Mestel (2019) — Cryptocurrency-portfolios in a mean-variance framework

- **Chave BibTeX:** `brauneis2019cryptocurrency`.
- **DOI/publicação:** [10.1016/j.frl.2018.05.008](https://doi.org/10.1016/j.frl.2018.05.008), *Finance Research Letters*.
- **Interseção:** MV + cripto, sem ML.
- **Mercado/universo:** 500 criptomoedas; em cada data, o universo investível é restringido às mais líquidas.
- **Período e frequência:** dados diários de 1/1/2015 a 31/12/2017; avaliação fora da amostra com custos.
- **Stack e métodos usados pelo autor:** oito estratégias long-only, incluindo 1/N, tangência, minimum variance e outras parametrizações MV; CRIX e criptoativos individuais como referências.
- **Papel do ML:** ausente.
- **Papel do MV/Markowitz:** núcleo da alocação, com médias e covariâncias estimadas por janela.
- **Principais resultados:** carteiras reduzem risco em relação a moedas isoladas, mas 1/N supera os ativos individuais e mais de 75% das carteiras MV em Sharpe e retorno equivalente certo.
- **Limitações:** período inicial do mercado, elevada mortalidade/seleção do universo e sensibilidade a janela/liquidez; o resultado não isola todos os vieses de disponibilidade histórica.
- **Por que é útil nesta subseção:** é o benchmark obrigatório contra a alegação de que otimização sofisticada sempre supera diversificação ingênua.
- **Afirmações que pode sustentar no TCC:** diversificar cripto reduz risco, mas erro de estimação pode fazer 1/N superar MV fora da amostra.
- **Relação com o presente TCC:** o ML só agrega valor se superar, de forma líquida e robusta, esse benchmark simples.

#### Citações diretas verificadas

> “Table 3 presents our results. In line with our previous considerations the 1/N portfolios outperform mean-variance optimal portfolios as well as individual CC. It turns out that the minimum Sharpe ratio of all 1/N portfolios exceeds the Sharpe ratios of more than 75% of the optimized portfolios. The average Sharpe ratio of the 1/N investments of 0.1865 is also higher than that of the CRIX (SRCRIX = 0.1596). The same conclusions may be drawn from certainty equivalent returns.”

- **Página:** PDF 1; impressa 259, resumo.
- **Contexto:** resultado principal fora da amostra.
- **O que o trecho comprova:** a diversificação é útil, mas a otimização baseada em parâmetros ruidosos não garante melhor Sharpe.

> “The 1/N portfolios seem to have superior risk-return patterns compared to the optimized portfolios. Following DeMiguel et al. (2009), we further investigate this point by comparing the Sharpe ratios as well as the certainty equivalent returns of all portfolio strategies in the different parameterizations outlined above. [...] The average Sharpe ratio of the 1/N investments of 0.1865 is also higher than that of the CRIX (SRCRIX = 0.1596).”

- **Página:** PDF 4; impressa 262.
- **Contexto:** comparação fora da amostra entre 1/N, CRIX, carteiras MV e criptomoedas individuais.
- **O que o trecho comprova:** o benchmark ingênuo supera inclusive o índice cripto no Sharpe médio reportado.

---

### Bakry et al. (2021) — Bitcoin and Portfolio Diversification: A Portfolio Optimization Approach

- **Autores:** Walid Bakry; Audil Rashid; Somar Al-Mohamad; Nasser El-Kanj.
- **Ano:** 2021.
- **Caminho:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\4 parte intro - Teoria de Portifólio/Bitcoin and Portfolio Diversification A Portfolio Optimization Approach.pdf`.
- **DOI:** `10.3390/jrfm14070282`.
- **BibTeX:** existe — `bakry2021bitcoin`.
- **Mercado/dados:** Bitcoin e índices amplos de ações, câmbio, atividade econômica, energia, títulos corporativos e ouro; 508 observações semanais de agosto de 2011 a maio de 2021.
- **Stack de otimização/risco:** média-variância e maximização do Sharpe sob oito cenários — pesos iguais, semirrestritos, restritos, risk parity e máximo Sharpe, com e sem short selling.
- **Componente cripto:** Bitcoin é incluído e retirado de cada carteira para medir seu efeito marginal.
- **Stack e métodos de ML/DL/RL:** ausente.
- **Integração da stack:** a alocação otimiza pesos de cada classe e compara risco, retorno, Sharpe, VaR e CVaR de carteiras com e sem Bitcoin.
- **Principais resultados:** pequenas alocações em Bitcoin elevaram o Sharpe em vários cenários, mas exposição excessiva aumentou risco e CVaR; o melhor equilíbrio surgiu com restrições de peso.
- **Limitações:** apenas Bitcoin; avaliação histórica; variância–covariância e simulação Monte Carlo subestimaram perdas extremas; custos não são incorporados à otimização.
#### Citações diretas verificadas

- **Citação literal 1:** “The study employs different constraining optimization frameworks that seek to maximize risk-adjusted returns (Sharpe ratio) of the portfolio by optimizing allocations to each asset class (asset allocation).”
- **Página:** PDF 1; página impressa 1 de 24. Contexto: resumo.
- **Citação literal 2:** “The results also revealed that increasing the weight of Bitcoin generated incremental returns, but the risk increased disproportionately, resulting in a decrease in the Sharpe ratio [...] including Bitcoin does not essentially increase the risk-adjusted performance of a portfolio unless carefully constrained.”
- **Página:** PDF 16; página impressa 16 de 24. Contexto: discussão dos cenários de otimização.
- **O que o trecho comprova:** a inclusão de Bitcoin pode melhorar o retorno ajustado ao risco, mas somente com limites de alocação que contenham exposição e risco de cauda.
- **Afirmações que pode sustentar no TCC:** restrições nos pesos são decisivas para que a inclusão de cripto não deteriore o desempenho ajustado ao risco.
- **Relação específica com o presente TCC:** fornece benchmark para discutir restrições e risco de cauda, mas não usa previsão ou múltiplas criptomoedas.
- **Por que é útil nesta subseção:** restrições nos pesos são decisivas para que a inclusão de cripto não deteriore o desempenho ajustado ao risco.

---

### Guesmi et al. (2019) — Portfolio diversification with virtual currency: Evidence from bitcoin

- **Autores:** Khaled Guesmi; Samir Saadi; Ilyes Abid; Zied Ftiti.
- **Ano:** 2019.
- **Caminho:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\2 parte intro - Cripto/Portfolio diversification with virtual currency Evidence from bitcoin.pdf`.
- **DOI:** `10.1016/j.irfa.2018.03.004`.
- **BibTeX:** **BIBTEX AUSENTE**. Metadados confirmados: *International Review of Financial Analysis*, v. 63, p. 431–437, 2019.
- **Mercado/dados:** Bitcoin, MSCI Emerging Markets, MSCI World, ouro, euro/dólar, WTI, VIX e yuan; dados diários de 1/1/2012 a 5/1/2018, 1.561 observações.
- **Stack de otimização/risco:** pesos ótimos de carteiras bivariadas, sem short selling, pela minimização de variância sem reduzir retorno esperado, usando covariâncias condicionais.
- **Componente cripto:** Bitcoin é combinado com cada ativo/índice tradicional.
- **Stack e métodos de ML/DL/RL:** ausente.
- **Integração da stack:** modelos VARMA-DCC-GJR-GARCH estimam volatilidade/covariância; essas estimativas determinam pesos e hedge ratios de média-variância.
- **Principais resultados:** a especificação VARMA-DCC-GJR-GARCH foi a mais adequada; estratégias com Bitcoin, ouro, petróleo e ações emergentes reduziram a variância relativamente às carteiras sem Bitcoin.
- **Limitações:** apenas Bitcoin; pares bivariados; dependência do modelo GARCH e do período; incerteza regulatória e hacking podem alterar pesos e eficácia.
#### Citações diretas verificadas

- **Citação literal 1:** “Finally, hedging strategies involving gold, oil, equities and Bitcoin reduce considerably the portfolio's risk, as compared to the risk of the portfolio made up of gold, oil and equities only.”
- **Página:** PDF 1; página impressa 431. Contexto: resumo.
- **Citação literal 2:** “Our empirical results suggest VARMA (1,1)-DCC-GJR-GARCH as the best model specification to describe the joint dynamics of Bitcoin and different financial assets. [...] Taken together, our results show that Bitcoin may offer diversification and hedging benefits for investors.”
- **Página:** PDF 6; página impressa 436. Contexto: conclusão.
- **O que o trecho comprova:** covariâncias condicionais alimentam pesos ótimos e indicam redução de risco ao incluir Bitcoin, embora sob um desenho bivariado.
- **Afirmações que pode sustentar no TCC:** estimativas dinâmicas de covariância podem alterar pesos e benefícios de diversificação envolvendo Bitcoin.
- **Relação específica com o presente TCC:** oferece alternativa econométrica às estimativas históricas usadas em MV, sem ML e sem carteira multimoedas.
- **Por que é útil nesta subseção:** estimativas dinâmicas de covariância podem alterar pesos e benefícios de diversificação envolvendo Bitcoin.

---

### Charfeddine et al. (2020) — Investigating the dynamic relationship between cryptocurrencies and conventional assets: Implications for financial investors

- **Autores:** Lanouar Charfeddine; Noureddine Benlagha; Youcef Maouchi.
- **Ano:** 2020.
- **Caminho:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\2 parte intro - Cripto/Investigating the dynamic relationship between cryptocurrencies and conventional assets Implications for financial investors.pdf`.
- **Duplicata/versão identificada:** outra cópia do mesmo artigo em `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\1 parte intro - decisoes de investimentos e tomada de decisao/Investigating the dynamic relationship between cryptocurrencies and.pdf`.
- **DOI:** `10.1016/j.econmod.2019.05.016`.
- **BibTeX:** existe — `charfeddine2020investigating`.
- **Mercado/dados:** BTC (18/7/2010–1/10/2018), ETH (1/9/2015–1/10/2018), S&P 500, ouro e petróleo bruto.
- **Stack de otimização/risco:** função utilidade média-variância para pesos ótimos e hedge ratios, com covariâncias de copulas variantes no tempo e BEKK/DCC/ADCC-GARCH.
- **Componente cripto:** carteiras mistas BTC/ETH + ativos tradicionais e carteira exclusivamente BTC–ETH.
- **Stack e métodos de ML/DL/RL:** ausente.
- **Integração da stack:** dependências e covariâncias dinâmicas determinam pesos que minimizam risco mantendo o retorno esperado.
- **Principais resultados:** correlações com ativos convencionais são fracas, porém variáveis no tempo; pequenas alocações digitais podem diversificar; a eficácia de hedge é baixa na maioria dos pares e sensível a choques externos.
- **Limitações:** apenas BTC e ETH; resultados dependem do modelo de dependência; carteiras bivariadas; não avalia custos nem previsão fora da amostra.
#### Citações diretas verificadas

- **Citação literal 1:** “Assuming a mean-variance utility function, the optimal portfolio holdings of digital asset i is given by the following [...].”
- **Página:** PDF 17; página impressa 214. Contexto: método de pesos ótimos.
- **Citação literal 2:** “First, using time varying copula models, we find evidence of time varying dependence between all the different pairs considered. [...] Second, we show that for the case of portfolio with mixed assets, the level of dependence is very weak for all the seven examined pairs without exception, a result which suggests that Bitcoin and Ethereum can offer new opportunities for portfolio diversification.”
- **Página:** PDF 18; página impressa 215. Contexto: conclusão.
- **O que o trecho comprova:** a diversificação existe, mas as correlações e os pesos ótimos mudam com o tempo e com choques, o que enfraquece estimativas estáticas.
- **Afirmações que pode sustentar no TCC:** correlações instáveis e choques externos limitam alocações MV estáticas em cripto.
- **Relação específica com o presente TCC:** justifica testar janelas móveis/retraining e estabilidade dos pesos; difere por usar copulas/GARCH, não ML.
- **Por que é útil nesta subseção:** correlações instáveis e choques externos limitam alocações MV estáticas em cripto.

---

### Wang et al. (2020) — Are stablecoins truly diversifiers, hedges, or safe havens against traditional cryptocurrencies as their name suggests?

- **Autores:** Gang-Jin Wang; Xin-yu Ma; Hao-yu Wu.
- **Ano:** 2020.
- **Caminho:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\2 parte intro - Cripto/Are stablecoins truly diversifiers, hedges, or safe havens against traditional cryptocurrencies as their name suggests.pdf`.
- **DOI:** `10.1016/j.ribaf.2020.101225`.
- **BibTeX:** existe — `wang2020stablecoins`.
- **Mercado/dados:** Tether, BitUSD, NuBits, DGD, HGT, XAUR, BTC, LTC e XRP; dados diários até 20/3/2019, com início em 6/3/2015 para stablecoins em dólar e 13/10/2017 para as lastreadas em ouro.
- **Stack de otimização/risco:** pesos de uma carteira bivariada obtida minimizando risco sem reduzir retorno esperado, usando variâncias e covariâncias DCC-GARCH; comparação com 50/50.
- **Componente cripto:** carteiras stablecoin–criptomoeda tradicional, avaliadas também por VaR e ES.
- **Stack e métodos de ML/DL/RL:** ausente.
- **Integração da stack:** DCC-GARCH e copulas produzem dependência dinâmica; os pesos são calculados e o risco extremo das carteiras é comparado.
- **Principais resultados:** stablecoins em dólar dispersam melhor o risco que as lastreadas em ouro; Tether é o caso mais forte; o papel de safe haven varia por condição de mercado e algumas combinações falham em caudas extremas.
- **Limitações:** carteiras bivariadas; amostras com inícios distintos; resultados específicos a stablecoins antigas; não modela custos ou liquidez.
#### Citações diretas verificadas

- **Citação literal 1:** “First, we consider a portfolio, called portfolio 1, obtained by minimizing the risk of a cryptocurrency-stablecoin portfolio without reducing the expected return.”
- **Página:** PDF 13; página impressa 13. Contexto: construção da carteira.
- **Citação literal 2:** “Comparing the results of full-period analysis with the subperiod one, we find that the market condition matters to the risk-dispersion effectiveness of USD-pegged stablecoins.”
- **Página:** PDF 16; página impressa 16. Contexto: conclusão.
- **O que o trecho comprova:** a diversificação e a redução de perdas dependem do ativo e do regime; pesos ótimos não devem ser interpretados como invariantes.
- **Afirmações que pode sustentar no TCC:** risco de cauda e mudanças de regime exigem cautela ao interpretar carteiras cripto otimizadas por variância.
- **Relação específica com o presente TCC:** amplia o universo potencial com stablecoins e fornece comparação 50/50, mas não usa ML nem carteira multivariada ampla.
- **Por que é útil nesta subseção:** risco de cauda e mudanças de regime exigem cautela ao interpretar carteiras cripto otimizadas por variância.

---

### Goodell e Goutte (2021) — Diversifying equity with cryptocurrencies during COVID-19

- **Autores:** John W. Goodell; Stephane Goutte.
- **Ano:** 2021.
- **Caminho:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\1 parte intro - decisoes de investimentos e tomada de decisao/Diversifying equity with cryptocurrencies during COVID-19.pdf`.
- **DOI:** `10.1016/j.irfa.2021.101781`.
- **BibTeX:** existe — `goodell2021diversifying`.
- **Mercado/dados:** BTC, ETH, LTC e Tether contra sete índices acionários e VIX; 28/2/2019–9/2/2021.
- **Metodologia:** correlações/heatmaps, coerência wavelet e redes neurais para co-movimentos antes e durante a COVID-19.
- **Papel para portfólios:** testa se as criptomoedas oferecem diversificação em regimes normais e de crise; não calcula carteira ótima.
- **Principais resultados:** co-movimentos aumentam com a pandemia; BTC, ETH e LTC oferecem pouco benefício para ações; Tether exibe co-movimento negativo relevante e comportamento de safe haven.
- **Limitações:** período centrado numa crise única; quatro moedas; inferência de diversificação por co-movimento, sem backtest de pesos, custos ou restrições.
#### Citações diretas verificadas

- **Citação literal 1:** “We find co-movements between cryptocurrencies and equity indices gradually increased as COVID-19 progressed. However, most of these co-movements are either modestly positively correlated, or minimal, suggesting cryptocurrencies in general do not provide a diversification benefit during either normal times or downturns.”
- **Página:** PDF 1; página impressa não exibida. Contexto: resumo.
- **Citação literal 2:** “The latter three cryptocurrencies offer little diversification benefit for equity investors. On the other hand, tether [...] manifests pronounced negative co-movements with equity indices, both in normal times, and especially during the COVID-19 period.”
- **Página:** PDF 8; página impressa 8. Contexto: discussão e conclusão.
- **O que o trecho comprova:** o benefício de diversificação é heterogêneo por moeda e regime; stablecoins podem se comportar de modo distinto de BTC, ETH e LTC.
- **Afirmações que pode sustentar no TCC:** correlações e benefícios de diversificação mudam em crises e entre tipos de criptoativo.
- **Relação específica com o presente TCC:** motiva avaliação por regimes e inclusão/controle de stablecoins, mas não é estudo de otimização.
- **Por que é útil nesta subseção:** correlações e benefícios de diversificação mudam em crises e entre tipos de criptoativo.

---

### Fakhfekh e Jeribi (2020) — Volatility dynamics of crypto-currencies’ returns: Evidence from asymmetric and long memory GARCH models

- **Autores:** Mohamed Fakhfekh; Ahmed Jeribi.
- **Ano:** 2020.
- **Caminho:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\2 parte intro - Cripto/Volatility dynamics of crypto-currencies’ returns.pdf`.
- **DOI:** `10.1016/j.ribaf.2019.101075`.
- **BibTeX:** existe — `fakhfekh2020volatility`.
- **Mercado/dados:** 16 criptomoedas de maior capitalização/volume; séries de retornos com tamanhos distintos conforme a história de negociação.
- **Metodologia:** 14 especificações das famílias FIGARCH, FIEGARCH, EGARCH, PGARCH e TGARCH com diferentes distribuições de erro.
- **Papel para portfólios:** não forma carteira; testa heterogeneidade, memória longa e assimetria da volatilidade que afetam a estimação de risco MV.
- **Principais resultados:** TGARCH com distribuição dupla exponencial foi a melhor para várias moedas; volatilidade respondeu mais a choques positivos, diferentemente do padrão típico de ações.
- **Limitações:** ajuste in-sample e escolha por likelihood/AIC/BIC; não mede previsão fora da amostra nem efeito em pesos; resultados variam por moeda.
#### Citações diretas verificadas

- **Citação literal 1:** “The objective of this paper is to select the most optimum model or set of models useful for modeling sixteen of the most popular crypto-currencies associated volatility.”
- **Página:** PDF 1; página impressa não exibida. Contexto: resumo.
- **Citação literal 2:** “In addition, it has also been discovered that volatility tends to increase as a response to positive shocks rather than to negative shocks, reflecting an asymmetric effect that differs noticeably from that often observed in stock markets.”
- **Página:** PDF 9; página impressa 9. Contexto: conclusão.
- **O que o trecho comprova:** o processo de volatilidade é assimétrico e heterogêneo entre moedas, o que questiona uma única estimativa histórica de variância.
- **Afirmações que pode sustentar no TCC:** volatilidade cripto pode apresentar memória longa, assimetria e distribuição não gaussiana, afetando estimativas de risco.
- **Relação específica com o presente TCC:** fundamenta testes de robustez para estimadores de risco e janelas; não é comparador de alocação.
- **Por que é útil nesta subseção:** volatilidade cripto pode apresentar memória longa, assimetria e distribuição não gaussiana, afetando estimativas de risco.

---

### Jeleskovic et al. (2024) — Cryptocurrency portfolio optimization: Utilizing a GARCH-copula model within the Markowitz framework

- **Chave BibTeX:** `jeleskovic2024cryptocurrency`.
- **DOI/publicação:** [10.1002/jcaf.22721](https://doi.org/10.1002/jcaf.22721), *Journal of Corporate Accounting & Finance*.
- **Interseção:** MV + cripto + covariâncias dinâmicas, sem ML.
- **Mercado/universo:** carteira tradicional; dez criptomoedas selecionadas entre as 200 maiores (PIVX, ETH, XRP, XLM, NEO, DCR, WAVES, XVG, UNO e GRS); carteira mista.
- **Período e frequência:** retornos de 1/1/2017 a 31/12/2018 para estimação; horizonte simulado de 90 dias, janela/rebalanceamento de 30 dias.
- **Stack e métodos usados pelo autor:** ARMA-GARCH para marginais, Copula e Vine Copula para dependência; maximização do Sharpe via Markowitz, long-only (`0 ≤ w_i ≤ 1`).
- **Papel do ML:** ausente.
- **Papel do MV/Markowitz:** pesos ótimos sob matrizes de risco geradas pelas estruturas GARCH-copula.
- **Principais resultados:** a carteira mista apresenta Sharpe ex post mais alto e desempenho ex ante mais estável; carteira apenas cripto é inferior às carteiras tradicional e mista em parte das comparações.
- **Limitações:** seleção ex post das dez moedas de melhor desempenho, amostra curta e dependência de simulação/modelo; isso cria risco de seleção e reduz validade externa.
- **Por que é útil nesta subseção:** exemplifica a separação entre estimador de dependência e regra de alocação.
- **Afirmações que pode sustentar no TCC:** covariâncias dinâmicas/copulas podem tornar o risco mais realista, mas não eliminam viés de seleção nem tornam carteira cripto pura superior.
- **Relação com o presente TCC:** é benchmark econométrico para a matriz de risco; o TCC deve declarar se melhora apenas retorno esperado ou também risco/covariância.

#### Citações diretas verificadas

> “For these purposes, the classic variance-covariance approach is applied where the calculation of the risk structure is done via the GARCH-Copula and GARCH-Vine Copula approaches. The optimal weights of the assets in the optimized portfolios are determined through Markowitz optimization problem. The analysis mainly showed that the portfolio composed of cryptocurrency and traditional assets has a higher Sharpe index, from an ex-post perspective, and more stable performances, from an ex-ante perspective.”

- **Página:** PDF 1; impressa 139, resumo.
- **Contexto:** distinção entre modelagem GARCH-copula do risco e otimização dos pesos.
- **O que o trecho comprova:** o modelo de dependência fornece entradas; Markowitz continua sendo a camada decisória.

> “The analysis is carried out from an ex-post perspective, evaluating the performance achieved in a certain period by three different portfolios. These are the one composed only of equities, bonds and commodities, the second one only of cryptocurrencies, and the third one is a combination of these both ones and thus made up of all considered ‘traditional’ assets and the most performing cryptocurrency of the second portfolio. [...] The analysis mainly showed that the portfolio composed of cryptocurrency and traditional assets has a higher Sharpe index, from an ex-post perspective, and more stable performances, from an ex-ante perspective.”

- **Página:** PDF 1; impressa 139, resumo.
- **Contexto:** principal comparação entre carteira tradicional, carteira apenas cripto e carteira mista.
- **O que o trecho comprova:** a vantagem observada está na combinação de classes, não na superioridade de uma carteira exclusivamente cripto.

## 3.4 Estudos híbridos Machine Learning e MV aplicados ao mercado de criptoativos

### Zhou et al. (2023) — Multi-source data driven cryptocurrency price movement prediction and portfolio optimization
- **Classificação do papel do ML:** **A — fornece parâmetros/sinais ao MV**.

- **Autores:** Zhongbao Zhou; Zhengyang Song; Helu Xiao; Tiantian Ren.
- **Ano:** 2023.
- **Caminho do PDF:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\NOVOS SEC 3/Multi-source data driven cryptocurrency price movement prediction and portfolio optimization.pdf`
- **DOI:** `10.1016/j.eswa.2023.119600`.
- **BibTeX:** existe — `zhou2023multisource`.
- **Mercado/dados:** sete criptomoedas (BTC, ETH, XRP, ADA, DOGE, DOT e LTC); dados de negociação, Google Trends e 28.799.774 tweets de 1/1/2021 a 30/6/2021; testes fora da amostra com horizontes de 1, 3 e 5 dias.
- **Stack de otimização/risco:** modelo de variância mínima global modificado pela informação prevista; comparação com minimum variance, máximo Sharpe, 1/N, Black–Litterman, CRIX e outro método de pré-seleção.
- **Componente cripto:** previsão de movimentos e alocação exclusivamente entre criptomoedas.
- **Stack e métodos de ML/DL/RL:** SVM para classificar a direção futura dos preços; VADER para extrair sentimento dos tweets.
- **Integração da stack:** probabilidades/direções previstas pela SVM, construídas com dados de mercado, atenção e sentimento, modificam a função de otimização de variância mínima; a carteira é atualizada em janela móvel.
- **Principais resultados:** maior Sharpe, Sortino e retorno equivalente certo fora da amostra que a maioria dos benchmarks; resultado permanece em testes de robustez e, na maioria dos casos, após custo de transação de 0,1%.
- **Limitações:** apenas sete moedas e seis meses de dados; prevê direção, não magnitude; resultados dependem de janela e horizonte.
#### Citações diretas verificadas

- **Citação literal 1:** “Third, we use SVM to forecast the movement of cryptocurrency prices based on the above multi-source data. Fourth, we propose a novel portfolio model by combining the forecasting results with the global minimum variance model, and the corresponding portfolio strategy is also derived.”
- **Página:** PDF 2; página impressa 2. Contexto: objetivo e desenho do estudo no corpo da introdução.
- **O que o trecho comprova:** a previsão SVM alimenta explicitamente um modelo de variância mínima global.
- **Citação literal 2:** “The proposed strategy has a better out-of-sample Sharpe ratio, Sortino ratio, and Certainty-equivalent (CEQ) return than other strategies. More importantly, the robustness test further confirms the effectiveness of the proposed strategy. Finally, we discuss the case where there are transaction costs, and the results show that the strategy proposed in this paper outperforms other strategies even with transaction costs.”
- **Página:** PDF 2; página impressa 2. Contexto: síntese dos resultados próprios na introdução.
- **O que o trecho comprova:** o método híbrido supera estratégias tradicionais em desempenho ajustado ao risco e mantém vantagem com custos.
- **Afirmações que pode sustentar no TCC:** previsões podem alimentar diretamente a alocação MV e melhorar desempenho fora da amostra.
- **Relação específica com o presente TCC:** é um dos paralelos mais diretos: previsão de movimentos de criptoativos alimenta uma regra de variância mínima; difere pelo uso de SVM, tweets e Google Trends e por modificar o objetivo de variância mínima.
- **Por que é útil nesta subseção:** previsões podem alimentar diretamente a alocação MV e melhorar desempenho fora da amostra.

---

### Lorenzo e Arroyo (2023) — Online risk-based portfolio allocation on subsets of crypto assets applying a prototype-based clustering algorithm
- **Classificação do papel do ML:** **B — seleciona ativos antes do MV**.

- **Autores:** Luis Lorenzo; Javier Arroyo.
- **Ano:** 2023.
- **Caminho do PDF:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\NOVOS SEC 3/Online risk-based portfolio allocation on subsets of crypto assets applying a prototype-based clustering algorithm.pdf`
- **DOI:** `10.1186/s40854-022-00438-2`.
- **BibTeX:** existe — `lorenzo2023online`.
- **Mercado/dados:** mercado cripto completo com 534 ativos elegíveis e subconjuntos dos 175 e 250 maiores; simulação de janeiro de 2020 a maio de 2021, janela de estimação de dois anos, holding de 30 dias e 1.500 trajetórias de investimento.
- **Stack de otimização/risco:** MV é aplicado somente ao cluster selecionado; MV integral, risk parity, hierarchical risk parity e CCI30 são benchmarks.
- **Componente cripto:** universo amplo de criptoativos, atualizado em janelas deslizantes.
- **Stack e métodos de ML/DL/RL:** clustering não supervisionado CLARA/k-medoids, seleção automática do número de clusters e escolha do protótipo conforme perfil de risco/Sharpe.
- **Integração da stack:** clustering pré-seleciona dinamicamente um subconjunto coerente com o perfil do investidor; MV calcula os pesos apenas nesse subconjunto.
- **Principais resultados:** estratégias de cluster por Sharpe e mean-risk melhoram retornos e Sharpe quando o universo cresce e evitam falhas de convergência do MV aplicado a todo o mercado; o MV clássico preserva vantagem em algumas métricas puras de risco.
- **Limitações:** maior drawdown/risco em algumas estratégias; sensibilidade ao número de moedas; fricções, liquidez, múltiplas exchanges e negociabilidade de todos os 534 ativos não foram incorporadas.
#### Citações diretas verificadas

- **Citação literal 1:** “We propose enhancing the mean-variance (MV) model with a pre-selection stage that uses a prototype-based clustering algorithm to reduce the number of crypto assets considered at each investment period. [...] We then run the MV portfolio optimization with the crypto assets of the selected cluster.”
- **Página:** PDF 1; página impressa 1 de 40. Contexto: abstract do próprio estudo.
- **O que o trecho comprova:** o algoritmo de clustering funciona como pré-seleção e o MV determina a carteira no cluster escolhido.
- **Citação literal 2:** “One of the drawbacks of the proposed strategies is the higher drawdown and risk compared with the classical MV, which is the more evident weakness of the proposed strategies, so it is comparable to the HRP model. We consider that SR and MR strategies independent of market size offer a good trade-off between returns, risk, and drawdown.”
- **Página:** PDF 36; página impressa 36 de 40. Contexto: conclusão e limitações reconhecidas pelos autores.
- **O que o trecho comprova:** os ganhos não são absolutos: a seleção por clusters pode elevar drawdown e risco em comparação ao MV clássico.
- **Afirmações que pode sustentar no TCC:** ML também pode atuar na pré-seleção, antes da otimização matemática.
- **Relação específica com o presente TCC:** compartilha a sequência seleção algorítmica→MV, mas usa clustering não supervisionado em vez de previsão de retornos e trabalha com um universo muito maior.
- **Por que é útil nesta subseção:** ML também pode atuar na pré-seleção, antes da otimização matemática.

---

### Cui et al. (2023) — Portfolio constructions in cryptocurrency market: A CVaR-based deep reinforcement learning approach
- **Classificação do papel do ML:** **C — substitui a otimização estática por política de alocação**.

- **Autores:** Tianxiang Cui; Shusheng Ding; Huan Jin; Yongmin Zhang.
- **Ano:** 2023.
- **Caminho do PDF:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\NOVOS SEC 3/Portfolio constructions in cryptocurrency market - A CVaR-based deep reinforcement learning approach.pdf`
- **DOI:** `10.1016/j.econmod.2022.106078`.
- **BibTeX:** existe — `cui2023portfolio`.
- **Mercado/dados:** BTC, Dash, ETH, LTC, USDT e XRP; 2.199 observações diárias do Yahoo Finance, de 6/8/2015 a 6/8/2021; treino até 31/12/2019 e teste posterior.
- **Stack de otimização/risco:** fronteira eficiente média-variância e função de recompensa baseada no objetivo MV; benchmark direto para a fronteira mean-CVaR.
- **Componente cripto:** carteiras compostas pelas seis criptomoedas.
- **Stack e métodos de ML/DL/RL:** PPO com rede residual profunda; ações são vetores contínuos de pesos.
- **Integração da stack:** agentes PPO são treinados tanto com recompensa MV quanto mean-CVaR, constroem as duas fronteiras e realocam pesos; os portfólios são comparados fora da amostra.
- **Principais resultados:** mean-CVaR domina MV: no teste, carteiras mean-CVaR apresentam retornos maiores e desvios-padrão menores; o estudo atribui a vantagem à representação do risco de cauda.
- **Limitações:** seis ativos e um único período de mercado; não há análise explícita de custos/slippage no experimento; parte da geração de cenários é descrita como in-sample; a superioridade observada é específica ao risco CVaR e desenho adotado.
#### Citações diretas verificadas

- **Citação literal 1:** “The main contribution of this paper is to propose a new CVaR-based portfolio optimization model for cryptocurrency markets, which employs a DRL methodology. [...] We employ deep reinforcement learning to construct the portfolios and perform out-of-sample back testing to verify that the CVaR risk measure outperforms the variance risk measure.”
- **Página:** PDF 2; página impressa 2. Contexto: contribuição metodológica no corpo da introdução.
- **O que o trecho comprova:** DRL constrói carteiras cripto sob objetivos mean-CVaR e MV, com teste fora da amostra.
- **Citação literal 2:** “We employ deep reinforcement learning to construct the portfolios according to the mean–variance and mean-CVaR mechanisms for out-of-sample back testing. [...] This indicates that the portfolios constructed under the mean-CVaR framework have higher returns with lower risk compared with the portfolios constructed under the mean–variance model.”
- **Página:** PDF 7; página impressa 7. Contexto: comparação empírica das fronteiras e dos portfólios.
- **O que o trecho comprova:** o artigo não apenas menciona MV como benchmark: treina DRL sob ambos os mecanismos e mostra vantagem do mean-CVaR.
- **Afirmações que pode sustentar no TCC:** RL permite alocação dinâmica e incorporação explícita de risco na recompensa.
- **Relação específica com o presente TCC:** oferece benchmark metodológico alternativo ao pipeline predição→MV, pois aprende pesos sequencialmente e compara diretamente recompensas MV e mean-CVaR.
- **Por que é útil nesta subseção:** RL permite alocação dinâmica e incorporação explícita de risco na recompensa.

---

### Xu et al. (2025) — Cryptocurrency Portfolio Optimisation Based on LSTM Time Series Forecasting
- **Classificação do papel do ML:** **A — fornece parâmetros/sinais ao MV**.

- **Autores:** Zhihan Xu; Xinyue Zhang; Zili Zhou.
- **Ano:** 2025.
- **Caminho do PDF:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\NOVOS SEC 3/Cryptocurrency Portfolio Optimisation Based on LSTM Time Series Forecasting.pdf`
- **DOI:** `10.54254/2755-2721/2025.22255`.
- **BibTeX:** existe — `xu2025cryptocurrency`.
- **Mercado/dados:** BTC, ETH e LTC; seis anos de dados da Binance para treinamento; previsões e backtest de janeiro a junho de 2024, com otimização mensal.
- **Stack de otimização/risco:** Markowitz estendido com short selling; maximização do Sharpe e cálculo mensal dos pesos.
- **Componente cripto:** carteira exclusivamente de BTC, ETH e LTC.
- **Stack e métodos de ML/DL/RL:** LSTM com janela móvel para previsão de preços.
- **Integração da stack:** dados históricos, dados novos e previsões LSTM são combinados como entradas do Markowitz estendido; os pesos resultantes são aplicados aos retornos reais e comparados com a janela móvel tradicional.
- **Principais resultados:** retorno ligeiramente maior, risco semelhante e Sharpe superior em quatro dos seis meses; o artigo conclui por maior retorno e melhor controle de risco no período.
- **Limitações:** apenas três moedas e seis meses de avaliação; short selling produz pesos negativos expressivos; acúmulo de erros e ausência de previsão de longo prazo; volatilidade não melhora em todos os meses.
#### Citações diretas verificadas

- **Citação literal 1:** “This work investigates the optimization of cryptocurrency portfolios by combining Long Short-Term Memory (LSTM) time series forecasting with traditional portfolio optimization methods. [...] These predictions are subsequently incorporated into an extended Markowitz framework to optimize the portfolio on a monthly basis.”
- **Página:** PDF 1; página impressa 143. Contexto: abstract.
- **O que o trecho comprova:** previsões LSTM de três criptomoedas alimentam mensalmente o Markowitz estendido.
- **Citação literal 2:** “As shown in Table 4 and Figure 4, Real Return in LSTM model exhibits slightly higher returns compared to the traditional model [...] The differences in volatility are relatively small, with the LSTM model demonstrating more stability in certain months, though it also exhibits higher volatility in others. And the Sharpe ratio of the LSTM model is superior in most month.”
- **Página:** PDF 7; página impressa 149. Contexto: resultados fora da amostra por mês.
- **O que o trecho comprova:** a vantagem é moderada e heterogênea: Sharpe geralmente maior, mas volatilidade nem sempre menor.
- **Afirmações que pode sustentar no TCC:** LSTM pode fornecer entradas preditivas para os pesos MV em cripto.
- **Relação específica com o presente TCC:** é o paralelo mais próximo no desenho LSTM→Markowitz com carteira exclusivamente cripto; sua amostra de três moedas e seis meses ajuda a delimitar como o TCC pode avançar.
- **Por que é útil nesta subseção:** LSTM pode fornecer entradas preditivas para os pesos MV em cripto.

---

### Han et al. (2024) — The diversification benefits of cryptocurrency factor portfolios: Are they there?
- **Classificação do papel do ML:** **A — fornece parâmetros/sinais ao MV**.

- **Autores:** Weihao Han; David Newton; Emmanouil Platanakis; Haoran Wu; Libo Xiao.
- **Ano:** 2024.
- **Caminho do PDF:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\NOVOS SEC 3/The diversification benefits of cryptocurrency factor portfolios - Are they there.pdf`
- **DOI:** `10.1007/s11156-024-01260-w`.
- **BibTeX:** existe — `han2024diversification`.
- **Mercado/dados:** mais de 2.000 criptomoedas do CoinGecko, janeiro de 2014 a junho de 2021, agregadas em 28 fatores de tamanho, momentum, volume e volatilidade; benchmark com S&P 500, Treasury de 10 anos e T-bill.
- **Stack de otimização/risco:** MV com restrição de short sale, Bayes–Stein e Black–Litterman, além de variantes ML; 1/N como referência.
- **Componente cripto:** fatores cripto entram em carteiras tradicionais stock–bond; cada fator sintetiza um universo amplo de moedas.
- **Stack e métodos de ML/DL/RL:** combination elastic net (C-ENet) prevê retornos dos fatores cripto.
- **Integração da stack:** os retornos previstos por C-ENet substituem as médias históricas nos modelos MV, Bayes–Stein e Black–Litterman; pesos ótimos são recalculados fora da amostra.
- **Principais resultados:** fatores de tamanho e momentum geram benefícios significativos; estratégias com retornos previstos têm, em média, desempenho fora da amostra cerca de 4% maior; resultados resistem a custos, benchmark alternativo e janela móvel.
- **Limitações:** número limitado de técnicas de ML/otimização; covariâncias continuam históricas; possíveis erros de estimação em alta volatilidade; fatores baseados sobretudo em preço/mercado.
#### Citações diretas verificadas

- **Citação literal 1:** “Second, we enhance the performance of optimised portfolios by combining the usage of traditional portfolio optimisation framework and machine learning, to mitigate the poor out-of-sample portfolio performance caused by estimation errors. [...] we leverage the power of machine learning to predict cryptocurrency factor’s one-period-ahead expected returns. Specifically, we employ the combination elastic net (C-ENet) approach.”
- **Página:** PDF 3; página impressa 471. Contexto: contribuição metodológica da introdução.
- **O que o trecho comprova:** C-ENet prevê retornos de fatores cripto para reduzir erros de estimação na alocação tradicional.
- **Citação literal 2:** “Our empirical results demonstrate that, on average, the asset allocation strategies adopting forecasted expected returns have an approximate 4% higher out-of-sample performance than strategies that ignore the contribution of machine-learning techniques on predicting returns, especially for the momentum factors.”
- **Página:** PDF 4; página impressa 472. Contexto: síntese dos resultados empíricos.
- **O que o trecho comprova:** a etapa preditiva melhora em aproximadamente 4% o desempenho médio fora da amostra.
- **Afirmações que pode sustentar no TCC:** previsões de retorno substituem entradas históricas do MV e podem reduzir erro de estimação.
- **Relação específica com o presente TCC:** substitui médias históricas por previsões C-ENet como entrada da alocação, mas usa fatores cripto em carteiras stock–bond, não ativos individuais numa carteira exclusivamente cripto.
- **Por que é útil nesta subseção:** previsões de retorno substituem entradas históricas do MV e podem reduzir erro de estimação.

---

### Toscano et al. (2026) — When Richer Information Does Not Improve Allocation: Machine Learning and Portfolio Optimisation in NFT-Ecosystem Tokens
- **Classificação do papel do ML:** **A — fornece retornos previstos às regras de alocação**.

- **Autores:** David Toscano; Juan C. Roca; Francisco Jareño.
- **Ano:** 2026.
- **Caminho do PDF:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\NOVOS SEC 3/When Richer Information Does Not Improve Allocation - Machine Learning and Portfolio Optimisation in NFT-Ecosystem Tokens.pdf`
- **DOI:** `10.1007/s10614-026-11394-9`.
- **BibTeX:** existe — `toscano2026richer` (online first).
- **Mercado/dados:** 28 tokens do ecossistema NFT, com OHLC diário de janeiro de 2021 a março de 2024; comparação adicional com cinco criptomoedas maduras.
- **Stack de otimização/risco:** MV clássico e modified mean-variance com covariância/volatilidade OHLC; 50.000 carteiras Monte Carlo por janela; pesos escolhidos pelo Sharpe.
- **Componente cripto:** tokens NFT/GameFi/metaverso, como SAND, MANA, AXS, GALA e THETA.
- **Stack e métodos de ML/DL/RL:** Random Forest, Gradient Boosted Regression Trees, BPNN e rede neural; previsão de retornos com indicadores OHLC e técnicos.
- **Integração da stack:** previsões ML são entradas exógenas comuns a MV, MMV e 1/N; isso separa o valor da previsão do valor do estimador de risco intradiário.
- **Principais resultados:** MV e MMV com ML superam 1/N, inclusive com custos; MV clássico geralmente tem Sharpe maior e menor volatilidade/risco de cauda que MMV; informação intradiária não melhora sistematicamente a alocação.
- **Limitações:** mercado muito específico e período curto; forte dependência de correlação e arquitetura; custos não incluem taxas de rede/slippage; simulação Monte Carlo aproxima a fronteira.
#### Citações diretas verificadas

- **Citação literal 1:** “In the second stage, the predicted returns obtained from the ML models are treated as exogenous inputs to the portfolio optimization problem. Portfolio weights are computed using three alternative allocation strategies: the traditional MV framework, a MMV framework based on OHLC-derived volatility and covariance estimates and 1/N.”
- **Página:** PDF 14; página impressa mostra “13” no rodapé do arquivo (paginação interna anômala). Contexto: desenho experimental.
- **O que o trecho comprova:** os mesmos retornos previstos alimentam três regras de alocação, permitindo isolar o efeito de MV/MMV.
- **Citação literal 2:** “Across all forecasting models, both optimization-based strategies (MMV and MV) substantially outperform the naïve 1/N benchmark in terms of cumulative returns and Sharpe ratios. Comparing MMV and MV, the classical MV strategy generally delivers higher Sharpe ratios and lower volatility.”
- **Página:** PDF 24; página impressa mostra “13” no rodapé do arquivo (paginação interna anômala). Contexto: resultados de alocação, antes da tabela 11.
- **O que o trecho comprova:** o ganho vem da combinação previsão + otimização, mas o refinamento OHLC não supera consistentemente o MV clássico.
- **Afirmações que pode sustentar no TCC:** sofisticação não garante ganho universal; qualidade preditiva e estrutura de correlação importam.
- **Relação específica com o presente TCC:** é próximo no pipeline previsão→MV e particularmente útil como contraprova: informação de risco mais rica não melhorou sistematicamente a alocação.
- **Por que é útil nesta subseção:** sofisticação não garante ganho universal; qualidade preditiva e estrutura de correlação importam.

---

### Peykani et al. (2026) — A machine learning framework for multi-market portfolio optimization: Evidence from U.S. stocks and cryptocurrencies
- **Classificação do papel do ML:** **A — fornece parâmetros ao MV e a objetivos downside**.

- **Autores:** Pejman Peykani; Daniyal Sabour; Cristina Tanasescu.
- **Ano:** 2026.
- **Caminho do PDF:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\NOVOS SEC 3/A machine learning framework for multi-market portfolio optimization - Evidence from U.S. stocks and cryptocurrencies.pdf`
- **DOI:** `10.36922/IJOCTA026240111`.
- **BibTeX:** existe — `peykani2026machine`.
- **Mercado/dados:** BTC, ETH, BNB, Microsoft e Tesla; preços diários de 20/3/2024 a 14/7/2025; teste final de 30 dias.
- **Stack de otimização/risco:** MV, mean-semivariance e mean-absolute-deviation; carteiras de risco mínimo e tangência; 1/N como benchmark.
- **Componente cripto:** três criptomoedas dentro de carteira mista com ações norte-americanas.
- **Stack e métodos de ML/DL/RL:** XGBoost para retornos diários, com otimização Bayesiana de hiperparâmetros e indicadores técnicos/macroeconômicos.
- **Integração da stack:** previsões XGBoost substituem retornos esperados nos três modelos; os pesos e carteiras de tangência são avaliados fora da amostra.
- **Principais resultados:** todas as estratégias otimizadas reduzem risco para retorno-alvo semelhante; no buy-and-hold de 30 dias, 1/N retorna 6,6%, máximo Sharpe 7,2%, máximo Sortino 7,6% e máximo Sharpe-AD 10,2%.
- **Limitações:** apenas cinco ativos, teste de 30 dias e desenho estático de período único; sem testes formais de diferença de Sharpe/Sortino; custos, spread, slippage e estabilidade dos pesos não modelados; previsão tratada como determinística.
#### Citações diretas verificadas

- **Citação literal 1:** “This study introduces an integrated framework linking XGBoost-based return forecasting with three distinct optimization models: MV, MSV, and MAD. The analysis applies these models jointly to a mixed portfolio containing both U.S. equities and cryptocurrencies.”
- **Página:** PDF 1; página impressa 1768. Contexto: introdução e contribuição do artigo.
- **O que o trecho comprova:** o framework liga XGBoost a MV e medidas alternativas em uma carteira mista de ações e cripto.
- **Citação literal 2:** “The empirical results indicate that integrating machine-learning predictions with downside-focused optimization yields noticeable improvements over the baseline naïve portfolio. [...] The maximum-ratio configurations, particularly the Maximum Sharpe-AD and Maximum Sortino models, exhibited the most substantial efficiency gains and consistently outperformed both their minimum-risk counterparts and the equal-weighted baseline.”
- **Página:** PDF 11; página impressa 1778. Contexto: síntese dos resultados experimentais.
- **O que o trecho comprova:** previsões combinadas a objetivos de risco produzem ganhos sobre 1/N, sobretudo nas carteiras de máxima razão.
- **Afirmações que pode sustentar no TCC:** ML pode atualizar retornos esperados usados por MV e por medidas downside.
- **Relação específica com o presente TCC:** usa XGBoost para estimar retornos e calcular pesos MV, mas mistura ações e cripto e possui teste final de apenas 30 dias.
- **Por que é útil nesta subseção:** ML pode atualizar retornos esperados usados por MV e por medidas downside.

---

### Franco e Laurini (2025) — Integrating Choquet portfolios and machine learning interpretability for robust cryptocurrency investment strategies
- **Classificação do papel do ML:** **D — interpreta resultados após a otimização**.

- **Autores:** João Pedro M. Franco; Márcio P. Laurini.
- **Ano:** 2025.
- **Caminho do PDF:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\NOVOS SEC 3/Integrating Choquet portfolios and machine learning interpretability for robust cryptocurrency investment strategies.pdf`
- **DOI:** `10.1016/j.jfds.2025.100172`.
- **BibTeX:** existe — `franco2025integrating`.
- **Mercado/dados:** 15 criptomoedas do CoinMarketCap, de 22/5/2019 a 27/8/2025; janelas móveis e rebalanceamentos de 30, 90, 180 e 365 dias.
- **Stack de otimização/risco:** carteira Markowitz é construída e comparada diretamente com Choquet, 1/N e Bitcoin; retorno-alvo anual uniforme de 10%.
- **Componente cripto:** BTC, ETH, XRP, BNB, DOGE, TRX, ADA, LINK, XLM, BCH, CRO, LEO, LTC, XMR e ETC.
- **Stack e métodos de ML/DL/RL:** Random Forest de 500 árvores, Shapley values e LIME para explicar quais moedas impulsionam previsões/retornos das carteiras.
- **Integração da stack:** Markowitz e Choquet geram pesos/retornos; um modelo explicável atribui a cada cripto a contribuição para as diferenças de retorno entre as estratégias.
- **Principais resultados:** Choquet melhora retorno cumulativo e mitigação de cauda, sobretudo em horizontes curtos; XAI identifica ADA, CRO e BNB como principais drivers de Markowitz, e CRO, ADA e TRX de Choquet; a vantagem decai em horizontes longos.
- **Limitações:** XAI é pós-alocação e não componente preditivo de Markowitz; o modelo assume i.i.d. dentro de cada janela; parâmetros perdem poder em holding longo; turnover/custos tornam estratégias simples competitivas.
#### Citações diretas verificadas

- **Citação literal 1:** “This study further contributes by conducting a comparative analysis of the Markowitz mean-variance model and the Choquet portfolio. Machine Learning interpretability techniques are employed to elucidate the differences in portfolio returns, specifically identifying the cryptocurrencies that drive these divergences. In particular, Shapley Values [...] and Local Interpretable Model-Agnostic Explanations (LIME) [...] are utilized to augment the models’ transparency.”
- **Página:** PDF 2; página impressa 2. Contexto: contribuição declarada no corpo da introdução.
- **O que o trecho comprova:** ML explicável é integrado à comparação de Markowitz e Choquet para mostrar quais criptoativos causam as diferenças.
- **Citação literal 2:** “This study contributes to the literature by applying the Choquet portfolio to cryptocurrency markets for the first time and juxtaposing it with the traditional Markowitz mean-variance model. Additionally, tools for the interpretability of Machine Learning, such as Shapley Values and LIME, are utilized to clarify distinctions in portfolio returns, thereby enhancing transparency and comprehension of the optimization process.”
- **Página:** PDF 16; página impressa 16. Contexto: conclusões.
- **O que o trecho comprova:** o estudo usa XAI para abrir a caixa-preta das diferenças entre duas regras de carteira cripto.
- **Afirmações que pode sustentar no TCC:** interpretabilidade é desafio relevante e pode ser tratada com ferramentas XAI específicas.
- **Relação específica com o presente TCC:** aproxima-se pelo universo cripto e pelo benchmark Markowitz, mas o ML é uma camada explicativa posterior, não a fonte das estimativas usadas na otimização.
- **Por que é útil nesta subseção:** interpretabilidade é desafio relevante e pode ser tratada com ferramentas XAI específicas.

---

### Babaei et al. (2022) — Explainable artificial intelligence for crypto asset allocation
- **Classificação do papel do ML:** **D — interpreta resultados após a otimização**.

- **Autores:** Golnoosh Babaei; Paolo Giudici; Emanuela Raffinetti.
- **Ano:** 2022.
- **Caminho:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\2 parte intro - Cripto/Explainable artificial intelligence for crypto asset allocation.pdf`.
- **Duplicata identificada:** cópia byte a byte em `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\3 parte intro - machine learning/Explainable artificial intelligence for crypto asset allocation.pdf`.
- **DOI:** `10.1016/j.frl.2022.102941`.
- **BibTeX:** existe — `babaei2022explainable`.
- **Mercado/dados:** BTC, ETH, XRP, BCH, LTC, BNB, EOS e XLM; 771 observações diárias de setembro de 2017 a outubro de 2019; 740 carteiras produzidas em janela móvel de 30 dias.
- **Stack de otimização/risco:** alocação Markowitz de volatilidade mínima, recalculada diariamente com retornos e covariâncias dos 30 dias anteriores.
- **Componente cripto:** carteira exclusivamente formada pelas oito criptomoedas.
- **Stack e métodos de ML/DL/RL:** Random Forest para modelar o Z-score risco-retorno da carteira e SHAP/Shapley values para explicar a influência de cada moeda.
- **Integração da stack:** o Markowitz gera pesos, risco e retorno; o Random Forest aprende a relação não linear entre Z-scores dos ativos e da carteira; SHAP atribui a contribuição de cada criptoativo à decisão resultante.
- **Principais resultados:** as carteiras dinâmicas apresentaram distribuição de risco inferior à estratégia estática de pesos iguais; XLM, seguida de BCH e XRP, explicou a maior parte das variações dos Z-scores e pesos.
- **Limitações:** a precisão preditiva do Random Forest não é avaliada porque não é o foco; o XAI é posterior à alocação; usa oito ativos, uma janela única de 30 dias e não modela custos, liquidez ou risco de cauda.

- **Variável prevista e algoritmo:** o Random Forest modela o Z-score risco-retorno da carteira; SHAP/Shapley values explicam a contribuição dos ativos. O modelo não prevê retornos usados pelo Markowitz.
- **Validação:** análise diária das 740 carteiras geradas; a precisão preditiva do Random Forest não é a pergunta principal do artigo.
- **Modelo de otimização:** Markowitz de volatilidade mínima recalculado diariamente com 30 dias de retornos e covariâncias.
- **Restrições e rebalanceamento:** rebalanceamento diário; janela fixa de 30 dias.
- **Custos:** não modelados.
- **Métricas:** distribuição de risco e explicação dos Z-scores/pesos.
- **Desempenho fora da amostra:** as carteiras dinâmicas apresentam risco inferior ao 1/N estático no período; XLM, BCH e XRP explicam grande parte da variação.
- **Principal limitação:** XAI é posterior; não demonstra ganho preditivo/alocativo, usa uma janela e ignora custos, liquidez e risco de cauda.

#### Citações diretas verificadas

- **Citação literal 1:** “For this purpose, we apply Shapley values to the predictions generated by a machine learning model based on the results of a dynamic Markowitz portfolio optimization model and provide explanations for what is behind the selected portfolio weights.”
- **Página:** PDF 1; página impressa não exibida na primeira folha. Contexto: resumo do próprio estudo.
- **Citação literal 2:** “As explained in Section 2, the main goal of this paper is to propose an explainable portfolio management approach that has the ability to explain the weights assigned by a robot advisor that daily applied Markowitz’ asset allocation model to available cryptocurrencies.”
- **Página:** PDF 4; página impressa 4. Contexto: início dos resultados empíricos.
- **O que o trecho comprova:** o artigo torna interpretáveis os pesos de uma carteira Markowitz dinâmica de criptoativos e identifica quais moedas mais explicam a variação das decisões.
- **Afirmações que pode sustentar no TCC:** XAI pode ser aplicada às decisões de alocação e aos pesos de carteiras cripto baseadas em Markowitz.
- **Relação específica com o presente TCC:** complementa diretamente a discussão de interpretabilidade, mas não concorre com o pipeline de previsão de retornos do TCC.
- **Por que é útil nesta subseção:** XAI pode ser aplicada às decisões de alocação e aos pesos de carteiras cripto baseadas em Markowitz.

## 3.5 Síntese crítica dos estudos relacionados

### Demosthenous e Georgiou (2026) — Portfolio Optimization Methods for the Digital Asset Market: A Comprehensive Survey

- **Autores:** Giorgos Demosthenous; Chrysis Georgiou.
- **Ano:** 2026.
- **Caminho do PDF:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\NOVOS SEC 3/Portfolio Optimization Methods for the Digital Asset Market - A Comprehensive Survey.pdf`
- **DOI:** `10.1145/3819577`.
- **BibTeX:** existe — `demosthenous2026portfolio`.
- **Mercado/dados:** revisão sistemática de 119 publicações de 2017–2025 sobre portfólios exclusivamente de ativos digitais.
- **Stack de otimização/risco:** identifica MVO como método mais frequente e discute pressupostos, erro de estimação e benchmarks.
- **Componente cripto:** foco integral em digital-asset-only portfolios.
- **Stack e métodos de ML/DL/RL:** categorias próprias de ML/DL e RL; descreve forecasting→allocation, clustering, DRL e limitações de adaptação.
- **Integração da stack:** síntese e classificação da literatura, não uma integração experimental própria.
- **Principais resultados:** literatura cresce 37,8% ao ano, mas permanece fragmentada; MVO é o método mais usado; estudos ML/DL frequentemente seguem previsão e alocação em duas fases; comportamento estático e falta de retreinamento são fragilidades.
- **Limitações:** cobertura termina em 2025; como revisão, resultados empíricos são de trabalhos secundários e não devem ser citados como experimentos próprios dos autores.
#### Citações diretas verificadas

- **Citação literal 1:** “Although the portfolio optimization problem for traditional markets (stocks, commodities, etc.) is well researched and documented in the literature, studies on optimizing digital-asset-only portfolios are still sparse, fragmented and undocumented.”
- **Página:** PDF 2; página impressa 342:2. Contexto: introdução e justificativa da revisão.
- **O que o trecho comprova:** a literatura existe e cresce, mas ainda é dispersa e pouco consolidada; isso é diferente de dizer que quase não há estudos híbridos.
- **Citação literal 2:** “A major drawback of the existing literature within this category is the assumption of time-invariant and static model behavior. Usually, models are trained once and their parameters are only tuned during the building phase and are never updated, which can lead to a failure to adapt to non-stationary market dynamics.”
- **Página:** PDF 22; página impressa 342:22. Contexto: conclusão da categoria ML/DL em portfólios digitais.
- **O que o trecho comprova:** a revisão aponta falta de adaptação/retreinamento como lacuna mais específica da literatura ML/DL cripto.
- **Afirmações que pode sustentar no TCC:** modelos cripto enfrentam não normalidade, não estacionariedade, turnover, custos e dificuldade de adaptação.
- **Relação específica com o presente TCC:** oferece o enquadramento global mais amplo para situar o pipeline do TCC e, sobretudo, para justificar lacunas de validação dinâmica e adaptação, não uma alegação de inexistência de estudos.
- **Por que é útil nesta subseção:** modelos cripto enfrentam não normalidade, não estacionariedade, turnover, custos e dificuldade de adaptação.

---

### Fang et al. (2022) — Cryptocurrency trading: a comprehensive survey

- **Autores:** Fan Fang; Carmine Ventre; Michail Basios; Leslie Kanthan; David Martinez-Rego; Fan Wu; Lingbo Li.
- **Ano:** 2022.
- **Caminho:** `C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\2 parte intro - Cripto/Cryptocurrency trading a comprehensive survey.pdf`.
- **DOI:** `10.1186/s40854-021-00321-6`.
- **BibTeX:** existe — `fang2022cryptocurrency`.
- **Mercado/dados:** revisão de 146 trabalhos publicados entre 2013 e junho de 2021.
- **Metodologia:** taxonomia de sistemas de negociação, estratégias sistemáticas, ML, portfólios, condições extremas, datasets e tendências.
- **Papel para portfólios:** mapeia a construção de carteiras cripto, mas não executa uma otimização própria.
- **Principais resultados:** documenta rápido crescimento e diversidade de métodos/dados; identifica como oportunidades redes de transação, mudanças em tempo real e risco de dissipação de alphas.
- **Limitações:** revisão encerrada em 2021; inclui literatura heterogênea e alguns preprints em seu universo; seus achados secundários não substituem validação dos artigos originais.
#### Citações diretas verificadas

- **Citação literal 1:** “This paper provides a comprehensive survey of cryptocurrency trading research, by covering 146 research papers on various aspects of cryptocurrency trading (e.g., cryptocurrency trading systems, bubble and extreme condition, prediction of volatility and return, crypto-assets portfolio construction and crypto-assets, technical trading and others).”
- **Página:** PDF 1; página impressa 1 de 59. Contexto: resumo.
- **Citação literal 2:** “We further summarised the datasets used for experiments and analysed the research trends and opportunities in cryptocurrency trading.”
- **Página:** PDF 51; página impressa 51 de 59. Contexto: conclusão.
- **O que o trecho comprova:** a revisão demonstra que previsão, risco e construção de carteiras cripto já formavam uma literatura ampla até 2021.
- **Afirmações que pode sustentar no TCC:** há diversidade metodológica e forte crescimento da literatura cripto, o que exige delimitar a contribuição por desenho, não por ausência ampla de estudos.
- **Relação específica com o presente TCC:** serve como mapa histórico e fonte de terminologia, mas não evidencia desempenho de um modelo específico.
- **Por que é útil nesta subseção:** há diversidade metodológica e forte crescimento da literatura cripto, o que exige delimitar a contribuição por desenho, não por ausência ampla de estudos.

### Banco de evidências para a síntese crítica

O texto final da subseção 3.5 deve ser escrito a partir das citações literais e dos resultados quantitativos registrados acima. As proposições abaixo são índices de evidência, não conclusões independentes:

| Questão de redação | Evidência primária a citar | Contraponto obrigatório |
|---|---|---|
| ML melhora MV? | Han et al. reportam aproximadamente 4% de melhora média fora da amostra; Zhou et al. reportam Sharpe, Sortino e CEQ superiores | Toscano et al. mostram que informação mais rica não melhora sistematicamente a alocação; Jensen et al. mostram reversão após custos em uma implementação Markowitz-ML |
| Ganho preditivo vira ganho econômico? | Paiva et al., Wang et al., Sebastião e Godinho e Jensen et al. ligam desempenho à inclusão de custos | Chevallier et al. encontram buy-and-hold como melhor resultado global; Lucarelli e Borrotti não obtêm lucro em todos os subperíodos |
| Variância é suficiente em cripto? | Brauneis e Mestel mostram valor do MV, sobretudo no portfólio 1/N; Jeleskovic et al. modelam dependência com GARCH-cópulas | Cui et al. reportam vantagem de mean-CVaR sobre MV; Fakhfekh e Jeribi documentam assimetria e longa memória |
| Universos grandes favorecem pré-seleção? | Lorenzo e Arroyo usam CLARA/k-medoids antes do MV em até 534 ativos | Os próprios autores registram maior drawdown/risco em parte das estratégias |
| XAI equivale a previsão? | Babaei et al. e Franco e Laurini usam RF/SHAP/LIME para explicar pesos ou diferenças após a carteira | Esses estudos não demonstram que XAI fornece retornos previstos ao Markowitz |
| Qual lacuna permanece? | Comparar o protocolo concreto do TCC com universo, horizonte, restrições, custos, turnover, liquidez, retraining e estabilidade informados em cada ficha | Evitar a alegação genérica de inexistência de ML + MV + cripto, refutada pelos estudos de 3.4 |

### Avaliação da necessidade da subseção 3.2

- **O que acrescenta:** evidencia se previsões, regimes, sentimento, RL e relações não lineares funcionam no mercado cripto antes de serem convertidos em parâmetros de carteira.
- **O que se perderia se removida:** resultados negativos e limites próprios da camada preditiva, como buy-and-hold superior em Chevallier et al. e ausência de lucro universal em Lucarelli e Borrotti.
- **O que pode ser absorvido em 3.4:** apenas trabalhos em que a previsão, seleção ou política de ML é efetivamente ligada a uma regra de alocação multiativo.
- **Função argumentativa:** separar capacidade preditiva de ganho econômico e impedir que precisão de previsão seja tratada como prova automática de melhoria da carteira.

# Trabalhos essenciais por subseção

| Subseção | Núcleo empírico | Contrapontos |
|---|---|---|
| 3.1 | Paiva; Wang; Ma; Jensen | custos, turnover e instabilidade podem eliminar ganho bruto |
| 3.2 | Sebastião e Godinho; Park e Yang; Lucarelli e Borrotti | Chevallier et al. e os subperíodos negativos |
| 3.3 | Brauneis e Mestel; Charfeddine; Bakry; Jeleskovic | CVaR, não normalidade, assimetria e dependência dinâmica |
| 3.4 | Zhou; Lorenzo; Han; Xu; Toscano | Cui para RL/CVaR; Babaei e Franco para XAI posterior |
| 3.5 | Demosthenous e Georgiou; Fang et al. | resultados originais das subseções 3.1–3.4 |

# Matriz de cobertura

| Trabalho | 3.1 | 3.2 | 3.3 | 3.4 | 3.5 |
|---|:---:|:---:|:---:|:---:|:---:|
| Paiva et al. (2019) | ✓ |  |  |  | ✓ |
| Wang et al. (2020) | ✓ |  |  |  | ✓ |
| Ma et al. (2021) | ✓ |  |  |  | ✓ |
| Jensen et al. (2026) | ✓ |  |  |  | ✓ |
| Lucarelli e Borrotti (2020) |  | ✓ |  |  | ✓ |
| Sebastião e Godinho (2021) |  | ✓ |  |  | ✓ |
| Chevallier et al. (2021) |  | ✓ |  |  | ✓ |
| Park e Yang (2023) |  | ✓ |  |  | ✓ |
| Brauneis e Mestel (2019) |  |  | ✓ |  | ✓ |
| Charfeddine et al. (2020) |  |  | ✓ |  | ✓ |
| Bakry et al. (2021) |  |  | ✓ |  | ✓ |
| Jeleskovic et al. (2024) |  |  | ✓ |  | ✓ |
| Zhou et al. (2023) |  | ✓ | ✓ | ✓ | ✓ |
| Lorenzo e Arroyo (2023) |  | ✓ | ✓ | ✓ | ✓ |
| Cui et al. (2023) |  | ✓ | ✓ | ✓ | ✓ |
| Han et al. (2024) |  | ✓ | ✓ | ✓ | ✓ |
| Xu et al. (2025) |  | ✓ | ✓ | ✓ | ✓ |
| Toscano et al. (2026) |  | ✓ | ✓ | ✓ | ✓ |
| Peykani et al. (2026) |  | ✓ | ✓ | ✓ | ✓ |
| Franco e Laurini (2025) |  | ✓ | ✓ | ✓ | ✓ |
| Babaei et al. (2022) |  | ✓ | ✓ | ✓ | ✓ |
| Demosthenous e Georgiou (2026) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Fang et al. (2022) |  | ✓ |  |  | ✓ |

# Lacunas bibliográficas remanescentes

- Evidência com universo cripto amplo, teste fora da amostra longo e comparação uniforme entre previsões ML e médias históricas.
- Estudos que reportem simultaneamente custos, turnover, spread/slippage, liquidez, restrições, estabilidade dos pesos e significância estatística.
- Separação explícita entre erro de previsão de retornos e erro de estimação de covariâncias.
- Protocolos walk-forward com retraining documentado e múltiplos regimes de mercado.
- Comparação direta entre ganho preditivo, ganho econômico bruto e ganho econômico líquido.
- Evidência sobre AdaBoost alimentando diretamente um otimizador MV multiativo de cripto; no acervo incorporado, AdaBoost aparece em previsão/trading, não nessa combinação específica.

# Implicações para a redação da SEC3

## Para 3.1

- Apresentar primeiro o pipeline completo e os pontos de erro.
- Usar Paiva, Wang e Ma para dados, previsão, MV, turnover e custos.
- Usar Jensen como contraponto entre Sharpe bruto e implementabilidade líquida.
- Não equiparar acurácia preditiva a ganho de carteira.

## Para 3.2

- Organizar por previsão/direção, regimes, trading e RL.
- Registrar resultados negativos com o mesmo destaque dos positivos.
- Usar Chevallier e Lucarelli e Borrotti como contrapontos.
- Não antecipar MV quando o estudo não faz alocação multiativo.

## Para 3.3

- Separar limitação conceitual da variância, erro de estimação e característica específica do mercado cripto.
- Apoiar correlação dinâmica em GARCH/cópulas e não normalidade em estudos de volatilidade.
- Comparar MV com 1/N, CVaR e restrições de short selling.
- Não chamar qualquer método risco-retorno de Markowitz sem função objetivo compatível.

## Para 3.4

- Organizar os estudos pelos papéis A/B/C/D do ML.
- Começar pelos pipelines em que a previsão fornece parâmetros ao MV.
- Tratar pré-seleção, RL e XAI como funções metodologicamente distintas.
- Informar universo, janela, rebalanceamento, custos e avaliação fora da amostra em cada comparação.

## Para 3.5

- Construir cada conclusão a partir das citações e números das fichas.
- Confrontar evidências positivas com resultados nulos ou dependentes de custos.
- Formular a lacuna pelo protocolo ainda não testado, não pela suposta ausência de estudos híbridos.
- Distinguir ganho preditivo, ganho bruto de alocação e ganho líquido implementável.

# Auditoria de incorporação

- Fonte complementar preservada: C:\Pessoal\GIT\TCC\REPOSITORIO\TRABALHOS_REFERENCIA\CITACOES_COMPLEMENTARES_SEC3.md.
- Entradas completas incorporadas do catálogo complementar: **23**.
- Entradas completas exclusivas do mapa anterior preservadas: **7**.
- Total de fichas completas no canônico: **30**, sem contar linhas de matriz.
- Cada ficha oriunda do catálogo complementar conserva DOI/publicação, chave BibTeX, universo, período, métodos, resultados, limitações e as duas citações literais paginadas disponíveis.
- Citações excessivamente telegráficas do mapa anterior foram ampliadas com o parágrafo metodológico ou de resultados do próprio artigo; o critério é suficiência contextual, não brevidade.
- Cópias físicas e versões do mesmo DOI não foram contadas como estudos novos.
- Os falsos positivos registrados no catálogo complementar permanecem excluídos do corpo de evidências; o caso de título Empirical evidence on deep learning-enhanced portfolio optimization... continua marcado como não verificável no acervo original.
