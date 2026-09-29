# Mineração bibliográfica expandida — Machine Learning em Finanças

**Data da busca:** 28/09/2026  
**Arquivo-base lido integralmente:** `CITACOES_ML_FINANCAS.md`  
**Finalidade:** catálogo bibliográfico rastreável; não é redação da subseção do TCC.  
**Arquivo-base preservado:** nenhuma alteração foi feita no levantamento original.

## 0. Método, cobertura e limites

Foram usados seis artigos-semente do catálogo original. A mineração combinou: (i) leitura das bibliografias extraídas dos PDFs locais; (ii) normalização de títulos e DOI; (iii) referências retrospectivas; (iv) trabalhos posteriores que citam as sementes; (v) uma segunda rodada a partir de cinco nós centrais; e (vi) validação direta no artigo, na página oficial do periódico ou no texto integral quando acessível.

### Cobertura rastreada

- 6 sementes;
- 481 relações retrospectivas de primeiro nível, correspondentes a 452 trabalhos únicos com metadados recuperados;
- 481 relações prospectivas de primeiro nível, correspondentes a 455 trabalhos únicos;
- 492 relações retrospectivas e 500 prospectivas na expansão de segundo nível;
- 1.760 trabalhos únicos no grafo combinado antes da triagem temática e de qualidade;
- 51 referências mantidas no catálogo: 18 de alta prioridade, 22 de prioridade média, 6 de baixa prioridade e 5 específicas de cripto;
- 12 referências ou classes de referência registradas como rejeitadas.

Esses números descrevem o grafo recuperável no OpenAlex na data da busca, não a totalidade universal das citações. Diferenças de cobertura entre Scopus, Web of Science, Crossref, OpenAlex e Google Scholar são esperadas.

### Regra de evidência

- **Validada diretamente:** resumo, texto integral ou página oficial do artigo foi consultado.
- **Validada bibliograficamente:** autoria, título, periódico, ano e DOI foram conferidos, mas o resultado empírico detalhado não estava acessível; nesses casos não se atribui resultado numérico.
- **Descoberta por revisão:** a revisão é usada para localizar o original; o resultado empírico é atribuído ao original, não à revisão.
- Trechos entre aspas são deliberadamente curtos. Quando não há paginação HTML, registra-se a seção (`Abstract`, `Introduction`, `Results` etc.).

### Verificação contra o repositório local

Os títulos e DOIs foram comparados com os nomes dos PDFs em `TRABALHOS_REFERENCIA` e subpastas. Foram localizados como já existentes, entre outros: Paiva et al. (2019); Ma, Han e Wang (2021); Chen et al. (2021); Du (2022); Cui et al. (2023); Zhou et al. (2023). A ausência indicada abaixo significa “não localizado por nome/DOI no inventário de 28/09/2026”, não prova de inexistência fora da pasta inventariada.

## 1. Artigos-semente utilizados

| Seed | Referência | DOI | Papel na cadeia |
|---|---|---|---|
| S1 | Ferreira, F. G. D. C.; Gandomi, A. H.; Cardoso, R. T. N. (2021). *Artificial Intelligence Applied to Stock Market Trading: A Review*. IEEE Access, 9, 30898–30917. | [10.1109/ACCESS.2021.3058133](https://doi.org/10.1109/ACCESS.2021.3058133) | Histórico, previsão, sentimento e portfolio optimization. |
| S2 | Giantsidi, S.; Tarantola, C. (2025). *Deep learning for financial forecasting: A review of recent trends*. International Review of Economics & Finance, 104719. | [10.1016/j.iref.2025.104719](https://doi.org/10.1016/j.iref.2025.104719) | Previsão recente, volatilidade, validação e limitações. |
| S3 | Jiang, Y.; Olmo, J.; Atwi, M. (2024). *Deep reinforcement learning for portfolio selection*. Global Finance Journal, 62, 101016. | [10.1016/j.gfj.2024.101016](https://doi.org/10.1016/j.gfj.2024.101016) | RL, risco, custos e alocação dinâmica. |
| S4 | Wang, W.; Li, W.; Zhang, N.; Liu, K. (2020). *Portfolio formation with preselection using deep learning from long-term financial data*. Expert Systems with Applications, 143, 113042. | [10.1016/j.eswa.2019.113042](https://doi.org/10.1016/j.eswa.2019.113042) | Integração previsão/pré-seleção com média-variância. |
| S5 | Chaweewanchon, A.; Chaysiri, R. (2022). *Markowitz Mean-Variance Portfolio Optimization with Predictive Stock Selection Using Machine Learning*. International Journal of Financial Studies, 10(3), 64. | [10.3390/ijfs10030064](https://doi.org/10.3390/ijfs10030064) | Seleção preditiva e otimização de carteira. |
| S6 | Jang, J.; Seong, N. Y. (2023). *Deep reinforcement learning for stock portfolio optimization by connecting with modern portfolio theory*. Expert Systems with Applications, 218, 119556. | [10.1016/j.eswa.2023.119556](https://doi.org/10.1016/j.eswa.2023.119556) | RL conectado à MPT e rebalanceamento dinâmico. |

## 2. Cadeias de citação exploradas e sinais de saturação

### 2.1 Cadeias principais

1. **S4/S5/S1 → Fischer e Krauss (2018) → Krauss, Do e Huck (2017) e literatura de asset pricing por ML.** A cadeia separa previsão direcional, retorno econômico e efeito de custos.
2. **S4/S5/S1 → Paiva et al. (2019), Ma et al. (2021), Chen et al. (2021) e Ta et al. (2020).** É o núcleo mais diretamente aderente a “previsão/seleção por ML → otimização de carteira”.
3. **S3/S6/S4/S5 → Almahdi e Yang (2017) → Moody e Saffell (2001), DeMiguel et al. (2009) e literatura de risco/custos.** É o núcleo histórico e metodológico de RL para trading/carteiras.
4. **S3/S6 → Aboussalah e Lee (2020), Park et al. (2020), Wang e Zhou (2020).** Expande o RL para ações contínuas, múltiplos ativos, MDP e média-variância em tempo contínuo.
5. **S2 → Olorunnimbe e Viktor (2023) → Arnott, Harvey e Markowitz (2019), Fabozzi e López de Prado (2018) e validação temporal.** É a cadeia mais útil para backtesting, overfitting e reprodutibilidade.
6. **S3 → Goodell et al. (2021) → Gu, Kelly e Xiu (2020), Tetlock (2007), Tetlock et al. (2008), Loughran e McDonald (2011), Harvey et al. (2016).** Conecta o levantamento a asset pricing, texto/sentimento e múltiplos testes.
7. **Forward de S4/S5 → Ma et al. (2023), Chen et al. (2022), Du (2022), Ngo et al. (2023).** Mostra a evolução recente de pipelines “predict-then-optimize” e comparações RL × DL × modelos tradicionais.

### 2.2 Referências recorrentes em sementes independentes

| Ocorrências | Trabalho | Sementes |
|---:|---|---|
| 4 | Almahdi e Yang (2017), RRL com expected maximum drawdown | S3, S4, S5, S6 |
| 3 | Fischer e Krauss (2018), LSTM para previsão financeira | S1, S4, S5 |
| 3 | Paiva et al. (2019), SVM + média-variância | S1, S4, S5 |
| 3 | Ta, Liu e Tadesse (2020), LSTM + portfolio optimization | S2, S3, S5 |
| 3 | Long, Lu e Cui (2019), feature engineering por DL | S1, S2, S4 |
| 3 | Kara, Boyacioglu e Baykan (2011), ANN × SVM | S1, S4, S6 |
| 2 | Ma, Han e Wang (2021), previsão + MV/Omega | S2, S5; também citação posterior de S4 |
| 2 | Aboussalah e Lee (2020), controle contínuo por RRL | S3, S6 |
| 2 | Park, Sim e Choi (2020), deep Q-learning de carteira | S3, S6 |
| 2 | Kolm, Tütüncü e Fabozzi (2014), 60 anos de otimização | S4, S5 |

O segundo nível voltou repetidamente a Fama (1970), random forests, Cavalcante et al. (2016), Krauss et al. (2017), Tetlock et al. (2008), DeMiguel et al. (2009) e problemas de validação. O ganho marginal passou a ser sobretudo de aplicações muito específicas ou incrementos arquiteturais, caracterizando saturação temática suficiente para encerrar esta rodada.

## 3. Alta prioridade

### A1 — Fischer e Krauss (2018): LSTM com universo sem survivorship bias e custos

**Referência:** Fischer, T.; Krauss, C. (2018). *Deep learning with long short-term memory networks for financial market predictions*. European Journal of Operational Research, 270(2), 654–669.  
**DOI/publisher:** [10.1016/j.ejor.2017.11.054](https://doi.org/10.1016/j.ejor.2017.11.054)  
**Descoberta/relação:** referência citada por S1, S4 e S5; nó recorrente de primeiro nível.  
**Tema/tipo:** previsão de retorno direcional; estudo empírico/benchmark.  
**Dados/amostra:** constituintes históricos do S&P 500, 1992–2015; listas mensais de composição para reduzir survivorship bias.  
**Modelo e benchmark:** LSTM versus random forest, DNN e regressão logística; previsão fora da amostra; estratégia long-short.  
**Métricas/resultado:** retorno diário, Sharpe, acurácia e teste de Diebold–Mariano. O resumo reporta 0,46% ao dia e Sharpe 5,8 antes de custos; após 2010, o excesso de retorno do LSTM oscila em torno de zero depois dos custos.  
**Afirmação sustentada:** modelos complexos podem superar baselines em uma amostra longa, mas a vantagem econômica pode desaparecer em subperíodos recentes e após custos.  
**Localizador/trecho curto:** Abstract e seções *Data*, *Results* e *Conclusion*: “profitability fluctuating around zero after transaction costs.”  
**Limitações:** estratégia e parâmetros específicos; resultado bruto muito alto; sensível a custos, microestrutura e período.  
**Repositório:** não localizado. **Baixar:** sim, prioridade máxima.

### A2 — Gu, Kelly e Xiu (2020): benchmark moderno de asset pricing por ML

**Referência:** Gu, S.; Kelly, B.; Xiu, D. (2020). *Empirical Asset Pricing via Machine Learning*. The Review of Financial Studies, 33(5), 2223–2273.  
**DOI/publisher:** [10.1093/rfs/hhaa009](https://doi.org/10.1093/rfs/hhaa009)  
**Descoberta/relação:** S3 → Goodell et al. (2021) → artigo original; segundo nível.  
**Tema/tipo:** previsão de prêmios de risco e retornos; benchmark empírico.  
**Dados/amostra:** ações norte-americanas; previsão agregada e cross-section com grande conjunto de características e interações.  
**Modelo e benchmark:** regressões lineares/regularizadas, árvores, random forests, gradient boosting e redes neurais; avaliação fora da amostra e carteiras.  
**Métricas/resultado:** R² fora da amostra e Sharpe. O artigo reporta Sharpe anualizado 0,77 para timing do S&P 500 por rede neural versus 0,51 buy-and-hold; long-short por decis de previsão chega a 1,35. Árvores e redes obtêm os melhores resultados, associados a interações não lineares.  
**Afirmação sustentada:** ML pode acrescentar valor econômico em previsão de retornos quando comparado de forma homogênea a métodos tradicionais, sem que isso identifique por si só mecanismos econômicos.  
**Localizador/trecho curto:** Abstract e seção 2: “trees and neural networks” são os métodos de melhor desempenho.  
**Limitações:** mercado dos EUA; forte dependência de universo, características e desenho de carteira; previsão não equivale a explicação causal.  
**Repositório:** não localizado. **Baixar:** sim, prioridade máxima.

### A3 — Leippold, Wang e Zhou (2022): generalização para mercado chinês e custos

**Referência:** Leippold, M.; Wang, Q.; Zhou, W. (2022). *Machine learning in the Chinese stock market*. Journal of Financial Economics, 145(2), 64–82.  
**DOI/publisher:** [10.1016/j.jfineco.2021.08.017](https://doi.org/10.1016/j.jfineco.2021.08.017)  
**Descoberta/relação:** S3 → Goodell → Gu; trabalho posterior conectado a Gu.  
**Tema/tipo:** asset pricing, seleção de ativos, mercado emergente; estudo empírico.  
**Dados/amostra:** mais de 3.900 ações A-share de Xangai e Shenzhen, janeiro/2000–junho/2020; 94 características, 11 variáveis macro e dummies setoriais.  
**Modelo e benchmark:** métodos lineares/regularizados, árvores e redes neurais; R² OOS, testes de capacidade preditiva e carteiras long-short/long-only.  
**Resultado:** liquidez é o preditor dominante; árvores e redes superam regressões em vários recortes; desempenho econômico permanece significativo após custos, mas sofre em choques sistemáticos inesperados.  
**Afirmação sustentada:** a utilidade de ML varia com estrutura de mercado, horizonte, tamanho e custos; resultados dos EUA não devem ser generalizados automaticamente.  
**Localizador/trecho curto:** Abstract, seções 2–5: “performance can be vulnerable to unexpected systematic risk.”  
**Limitações:** dados proprietários; instituições e restrições de short selling chinesas; comparação internacional não é experimento controlado.  
**Repositório:** não localizado. **Baixar:** sim.

### A4 — Paiva et al. (2019): SVM + média-variância no Ibovespa

**Referência:** Paiva, F. D.; Cardoso, R. T. N.; Hanaoka, G. P.; Duarte, W. M. (2019). *Decision-making for financial trading: A fusion approach of machine learning and portfolio selection*. Expert Systems with Applications, 115, 635–655.  
**DOI/publisher:** [10.1016/j.eswa.2018.08.003](https://doi.org/10.1016/j.eswa.2018.08.003)  
**Descoberta/relação:** citado por S1, S4 e S5.  
**Tema/tipo:** integração previsão/classificação → otimização MV; estudo empírico brasileiro.  
**Dados/amostra:** ações do Ibovespa; 3.716 pregões fora da amostra; janelas mensais compostas de janelas diárias móveis.  
**Modelo e benchmark:** SVM+MV versus SVM+1/N, Random+MV e Ibovespa; 81 configurações do modelo principal.  
**Métricas/resultado:** desempenho do classificador, cardinalidade, retorno e risco, com e sem corretagem. A fusão apresenta resultados significativos, mas os custos e o valor mínimo por operação restringem a viabilidade.  
**Afirmação sustentada:** a integração ML–MV deve ser avaliada fora da amostra e líquida de custos; ganho preditivo isolado não basta.  
**Localizador/trecho curto:** Abstract: “brokerage costs can be a strong constraint.”  
**Limitações:** mercado, período e alvo de ganho específicos; muitas configurações elevam risco de seleção.  
**Repositório:** já existe como `Paiva2019.pdf` e em `5 parte intro - estudos relacionados`. **Baixar:** não; apenas consolidar uma cópia canônica.

### A5 — Ma, Han e Wang (2021): RF/SVR/DL + MV/Omega com custos

**Referência:** Ma, Y.; Han, R.; Wang, W. (2021). *Portfolio optimization with return prediction using deep learning and machine learning*. Expert Systems with Applications, 165, 113973.  
**DOI/publisher:** [10.1016/j.eswa.2020.113973](https://doi.org/10.1016/j.eswa.2020.113973)  
**Descoberta/relação:** citado por S2 e S5; citação posterior de S4.  
**Tema/tipo:** previsão de retornos, pré-seleção, MV/Omega; benchmark empírico.  
**Dados/amostra:** constituintes do China Securities 100, 2007–2015; últimos quatro anos usados para medir estratégias.  
**Modelo e benchmark:** RF, SVR, LSTM, DMLP e CNN; ARIMA como benchmark; carteiras MV e Omega.  
**Resultado:** RF+MV apresenta o melhor resultado entre as variantes MV; alta rotatividade reduz aproximadamente metade do retorno total de estratégias líderes.  
**Afirmação sustentada:** o algoritmo preditivo “vencedor” depende da função de decisão e do custo; neste estudo, RF supera DL no pipeline de carteira.  
**Localizador/trecho curto:** Abstract: “high turnover erodes nearly half of their total returns.”  
**Limitações:** um índice/mercado; custos modelados, mas sem execução real; risco de escolha ex post entre muitos modelos.  
**Repositório:** já existe em `5 parte intro - estudos relacionados`. **Baixar:** não.

### A6 — Chen et al. (2021): XGBoost otimizado + média-variância

**Referência:** Chen, W.; Zhang, H.; Mehlawat, M. K.; Jia, L. (2021). *Mean–variance portfolio optimization using machine learning-based stock price prediction*. Applied Soft Computing, 100, 106943.  
**DOI/publisher:** [10.1016/j.asoc.2020.106943](https://doi.org/10.1016/j.asoc.2020.106943)  
**Descoberta/relação:** citado por S5 e trabalho posterior que cita S4.  
**Tema/tipo:** seleção por ML + Markowitz; estudo empírico.  
**Dados/amostra:** Shanghai Stock Exchange.  
**Modelo e benchmark:** XGBoost com hiperparâmetros otimizados por improved firefly algorithm (IFAXGBoost), seguido por MV; compara métodos sem previsão e outros preditores.  
**Resultado:** o pipeline de dois estágios supera benchmarks em retorno e risco no experimento.  
**Afirmação sustentada:** previsões podem alimentar diretamente retorno esperado/pré-seleção antes da otimização MV.  
**Localizador/trecho curto:** Abstract: “two stages are involved: stock prediction and portfolio selection.”  
**Limitações:** complexidade de meta-heurística, risco de otimização excessiva e baixa transferibilidade entre mercados.  
**Repositório:** já existe em `5 parte intro - estudos relacionados`. **Baixar:** não.

### A7 — Almahdi e Yang (2017): RL com downside risk e custos

**Referência:** Almahdi, S.; Yang, S. Y. (2017). *An adaptive portfolio trading system: A risk-return portfolio optimization using recurrent reinforcement learning with expected maximum drawdown*. Expert Systems with Applications, 87, 267–279.  
**DOI/publisher:** [10.1016/j.eswa.2017.06.023](https://doi.org/10.1016/j.eswa.2017.06.023)  
**Descoberta/relação:** citado por S3, S4, S5 e S6; referência mais recorrente do primeiro nível.  
**Tema/tipo:** RL, alocação dinâmica, drawdown, custos; estudo empírico.  
**Dados/amostra:** carteira de ETFs líquidos; experimento de cinco anos.  
**Modelo e benchmark:** recurrent reinforcement learning, objetivo Calmar/E(MDD); compara Sharpe e Sterling, pesos variáveis e iguais, custos distintos e hedge-fund benchmarks.  
**Resultado:** E(MDD) melhora a geração de sinais e pesos no desenho testado; o mecanismo adaptativo responde melhor a custos e regimes de volatilidade.  
**Afirmação sustentada:** recompensas de RL podem incorporar downside risk e custos, em vez de maximizar somente lucro ou Sharpe.  
**Localizador/trecho curto:** Abstract: “responds to transaction cost effects better.”  
**Limitações:** cinco anos e universo de ETFs; backtest dependente de objetivo, retreinamento e regime; sem garantia de estabilidade futura.  
**Repositório:** não localizado. **Baixar:** sim.

### A8 — Aboussalah e Lee (2020): ações contínuas e múltiplos ativos

**Referência:** Aboussalah, A. M.; Lee, C.-G. (2020). *Continuous control with Stacked Deep Dynamic Recurrent Reinforcement Learning for portfolio optimization*. Expert Systems with Applications, 140, 112891.  
**DOI/publisher:** [10.1016/j.eswa.2019.112891](https://doi.org/10.1016/j.eswa.2019.112891)  
**Descoberta/relação:** citado por S3 e S6.  
**Tema/tipo:** DRL contínuo, cardinalidade, online learning; metodologia/empírico.  
**Dados/amostra:** dez ações do S&P 500, 01/01/2013–31/07/2017; 20 rodadas sucessivas de treino/teste online.  
**Modelo e benchmark:** SDDRRL com otimização bayesiana de arquitetura; rolling MVO, risk parity e uniform buy-and-hold.  
**Resultado:** desempenho superior aos três benchmarks no experimento.  
**Afirmação sustentada:** RL contínuo pode tratar simultaneamente pesos multiativos e restrições de carteira.  
**Localizador/trecho curto:** Abstract: “continuous investment actions for each asset.”  
**Limitações:** só dez ações e período curto; busca de arquitetura e avaliação no mesmo ambiente elevam risco de sobreajuste.  
**Repositório:** não localizado. **Baixar:** sim.

### A9 — Park, Sim e Choi (2020): deep Q-learning para trading de carteira

**Referência:** Park, H.; Sim, M. K.; Choi, D. G. (2020). *An intelligent financial portfolio trading strategy using deep Q-learning*. Expert Systems with Applications, 158, 113573.  
**DOI/publisher:** [10.1016/j.eswa.2020.113573](https://doi.org/10.1016/j.eswa.2020.113573)  
**Descoberta/relação:** citado por S3 e S6.  
**Tema/tipo:** DRL, decisões discretas, turnover; estudo empírico.  
**Dados/amostra:** dois casos de carteira; backtest multiativo.  
**Modelo e benchmark:** MDP + deep Q-learning, espaço combinatório discreto e função que mapeia ações inviáveis; estratégias tradicionais como benchmarks.  
**Resultado:** desempenho relativo superior nos dois casos testados; o desenho busca controlar ações inviáveis e giro excessivo.  
**Afirmação sustentada:** espaço de ação e restrições operacionais são componentes estruturais do RL financeiro, não meros detalhes de implementação.  
**Localizador/trecho curto:** Abstract: “adopts a discrete combinatorial action space.”  
**Limitações:** poucos casos; quantidade limitada de dados para treinar o agente; resultado depende da discretização e do simulador.  
**Repositório:** não localizado. **Baixar:** sim.

### A10 — Wang e Zhou (2020): média-variância em tempo contínuo por RL

**Referência:** Wang, H.; Zhou, X. Y. (2020). *Continuous-time mean–variance portfolio selection: A reinforcement learning framework*. Mathematical Finance, 30(4), 1273–1308.  
**DOI/publisher:** [10.1111/mafi.12281](https://doi.org/10.1111/mafi.12281)  
**Descoberta/relação:** citado por S3.  
**Tema/tipo:** RL e média-variância; metodologia teórica com simulação/empírico.  
**Modelo e benchmark:** controle estocástico relaxado com regularização por entropia; política ótima Gaussiana; algoritmo RL versus métodos tradicionais e redes profundas.  
**Resultado:** os autores provam teorema de melhoria de política e reportam superioridade do algoritmo e variante em simulações e estudo empírico.  
**Afirmação sustentada:** a integração RL–média-variância possui formulação matemática além de heurísticas de backtest.  
**Localizador/trecho curto:** Abstract: “optimal feedback policy ... must be Gaussian.”  
**Limitações:** hipóteses do modelo contínuo e ambiente controlado; transposição para execução real exige fricções e restrições adicionais.  
**Repositório:** não localizado. **Baixar:** sim.

### A11 — DeMiguel, Garlappi e Uppal (2009): 1/N como benchmark obrigatório

**Referência:** DeMiguel, V.; Garlappi, L.; Uppal, R. (2009). *Optimal Versus Naive Diversification: How Inefficient Is the 1/N Portfolio Strategy?* The Review of Financial Studies, 22(5), 1915–1953.  
**DOI/publisher:** [10.1093/rfs/hhm075](https://doi.org/10.1093/rfs/hhm075)  
**Descoberta/relação:** S3/S4/S5/S6 → Almahdi e Yang → artigo original; segundo nível.  
**Tema/tipo:** erro de estimação, portfolio optimization; benchmark empírico/metodológico.  
**Dados/amostra:** 14 modelos avaliados em sete conjuntos empíricos, com análise e simulações de erro de estimação.  
**Benchmark/métricas:** 1/N versus extensões da média-variância; Sharpe, retorno equivalente-certo e turnover.  
**Resultado:** nenhum dos 14 modelos supera consistentemente 1/N nas três métricas; os autores estimam janelas extremamente longas para a MV amostral dominar 1/N sob certas calibrações.  
**Afirmação sustentada:** qualquer pipeline ML+otimização deve comparar-se a 1/N e separar ganho preditivo de erro de estimação dos pesos.  
**Localizador/trecho curto:** Abstract: “none is consistently better than the 1/N rule.”  
**Limitações:** conjunto de modelos e dados da época; não invalida métodos posteriores, mas impõe benchmark rigoroso.  
**Repositório:** não localizado. **Baixar:** sim, prioridade máxima.

### A12 — Olorunnimbe e Viktor (2023): revisão focada em backtesting realista

**Referência:** Olorunnimbe, K.; Viktor, H. (2023). *Deep learning in the stock market—a systematic survey of practice, backtesting, and applications*. Artificial Intelligence Review, 56, 2057–2109.  
**DOI/publisher:** [10.1007/s10462-022-10226-0](https://doi.org/10.1007/s10462-022-10226-0)  
**Descoberta/relação:** citado por S2; nó central de segundo nível.  
**Tema/tipo:** revisão sistemática de DL, backtesting, reprodutibilidade e XAI.  
**Corpus/método:** 35 estudos com backtesting, classificados em sete aplicações.  
**Resultado:** trading, previsão de preços e gestão de carteiras dominam; seleção, hedge e risco recebem menos atenção; permanece déficit de explicabilidade e reprodutibilidade.  
**Afirmação sustentada:** métricas de domínio — retorno, volatilidade, drawdown e custos — são necessárias para avaliar utilidade financeira, além de acurácia.  
**Localizador/trecho curto:** Abstract e §3.2.1.3: “substantial work remains ... regarding model explainability.”  
**Limitações:** revisão restrita a DL e a trabalhos que fizeram backtest; qualidade do backtest varia.  
**Repositório:** não localizado. **Baixar:** sim.

### A13 — Arnott, Harvey e Markowitz (2019): protocolo de backtesting para ML

**Referência:** Arnott, R. D.; Harvey, C. R.; Markowitz, H. (2019). *A Backtesting Protocol in the Era of Machine Learning*. The Journal of Financial Data Science, 1(1), 64–74.  
**DOI/publisher:** [10.3905/jfds.2019.1.064](https://doi.org/10.3905/jfds.2019.1.064)  
**Descoberta/relação:** S2 → Olorunnimbe e Viktor → artigo original; segundo nível.  
**Tema/tipo:** protocolo metodológico; overfitting, seleção e escassez de dados.  
**Conteúdo:** discute separação de objetivos, disponibilidade efetiva de dados, seleção de modelos, múltiplos testes, interpretabilidade e limites da inferência em mercados reflexivos.  
**Afirmação sustentada:** ML financeiro exige cautela adicional porque horizontes longos oferecem amostras pequenas e o mercado reage à própria pesquisa.  
**Localizador/trecho curto:** Abstract: “the danger of misapplying these techniques can lead to disappointment.”  
**Limitações:** protocolo conceitual, não benchmark empírico único.  
**Repositório:** não localizado. **Baixar:** sim.

### A14 — Bailey et al. (2016): probabilidade de backtest overfitting

**Referência:** Bailey, D. H.; Borwein, J. M.; López de Prado, M.; Zhu, Q. J. (2016). *The Probability of Backtest Overfitting*. The Journal of Computational Finance, 20(4), 39–69.  
**DOI/publisher:** [10.21314/jcf.2016.322](https://doi.org/10.21314/jcf.2016.322)  
**Descoberta/relação:** expansão metodológica acionada pela cadeia S2 → Olorunnimbe → Arnott; validada diretamente; o próprio artigo cita White (2000).  
**Tema/tipo:** método de validação; multiple testing e overfitting.  
**Método:** define PBO e propõe combinatorially symmetric cross-validation (CSCV), modelo-livre e não paramétrica, para comparar desempenho in-sample e out-of-sample de muitas configurações.  
**Resultado ilustrativo:** no exemplo sazonal sem sinal real, todos os Sharpes IS são positivos, mas cerca de 53% dos OOS são negativos e PBO chega a 55%; no exemplo com efeito real, PBO cai para 13%.  
**Afirmação sustentada:** escolher a melhor entre muitas configurações infla o backtest mesmo quando existe hold-out convencional.  
**Localizador/trecho curto:** PDF pp. 24–28 e conclusão: “CSCV provides reasonable estimates of PBO.”  
**Limitações:** exige conjunto de tentativas/configurações e estrutura temporal adequada; não detecta todo tipo de leakage.  
**Repositório:** não localizado. **Baixar:** sim, prioridade máxima.

### A15 — Bailey e López de Prado (2014): Sharpe deflacionado

**Referência:** Bailey, D. H.; López de Prado, M. (2014). *The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting, and Non-Normality*. The Journal of Portfolio Management, 40(5), 94–107.  
**DOI/publisher:** [10.3905/jpm.2014.40.5.094](https://doi.org/10.3905/jpm.2014.40.5.094)  
**Descoberta/relação:** citado por Bailey et al. (2016); terceiro nível da cadeia de validação.  
**Tema/tipo:** métrica/metodologia de avaliação.  
**Método/resultado:** o DSR corrige inflação do Sharpe por múltiplos testes/seleção e retornos não normais.  
**Afirmação sustentada:** um Sharpe alto não deve ser tratado como evidência suficiente quando muitas estratégias ou hiperparâmetros foram tentados.  
**Localizador/trecho curto:** Abstract: “corrects for two leading sources of performance inflation.”  
**Limitações:** depende de estimar número/independência efetiva das tentativas e momentos da distribuição.  
**Repositório:** não localizado. **Baixar:** sim.

### A16 — White (2000): reality check contra data snooping

**Referência:** White, H. (2000). *A Reality Check for Data Snooping*. Econometrica, 68(5), 1097–1126.  
**DOI/publisher:** [10.1111/1468-0262.00152](https://doi.org/10.1111/1468-0262.00152)  
**Descoberta/relação:** Bailey et al. (2016) → White; terceiro nível.  
**Tema/tipo:** teste estatístico/metodologia.  
**Método:** testa a hipótese de que o melhor modelo encontrado numa busca de especificações não possui superioridade preditiva sobre um benchmark, controlando reuso dos mesmos dados.  
**Afirmação sustentada:** busca repetida de modelos cria resultados aparentemente bons por acaso; a comparação deve incorporar toda a busca.  
**Localizador/trecho curto:** Abstract: “data snooping occurs when ... data is used more than once.”  
**Limitações:** poder do teste pode ser baixo em alguns conjuntos; Hansen e Lunde (2005) mostram esse problema empiricamente.  
**Repositório:** não localizado. **Baixar:** sim.

### A17 — Tetlock (2007): texto de mídia e mercado

**Referência:** Tetlock, P. C. (2007). *Giving Content to Investor Sentiment: The Role of Media in the Stock Market*. The Journal of Finance, 62(3), 1139–1168.  
**DOI/publisher:** [10.1111/j.1540-6261.2007.01232.x](https://doi.org/10.1111/j.1540-6261.2007.01232.x)  
**Descoberta/relação:** S3 → Goodell et al. → artigo original; segundo nível.  
**Tema/tipo:** dados alternativos, NLP/sentimento; estudo empírico seminal.  
**Dados/amostra:** conteúdo diário de coluna do Wall Street Journal e dados de mercado.  
**Método/resultado:** medida quantitativa de pessimismo; pessimismo alto prevê pressão baixista seguida de reversão, e níveis extremos se associam a maior volume.  
**Afirmação sustentada:** informação textual possui relação mensurável com retorno e volume, mas o padrão é compatível com pressão temporária, não simples descoberta de fundamentos.  
**Localizador/trecho curto:** Abstract: “high media pessimism predicts downward pressure.”  
**Limitações:** uma fonte editorial e período histórico; léxico e processo de mídia anteriores à era de redes sociais.  
**Repositório:** não localizado. **Baixar:** sim.

### A18 — Hansen e Lunde (2005): benchmark econométrico para volatilidade

**Referência:** Hansen, P. R.; Lunde, A. (2005). *A forecast comparison of volatility models: does anything beat a GARCH(1,1)?* Journal of Applied Econometrics, 20(7), 873–889.  
**DOI/publisher:** [10.1002/jae.800](https://doi.org/10.1002/jae.800)  
**Descoberta/relação:** expansão da cadeia de volatilidade iniciada em S1/S2; referência clássica usada como benchmark em estudos posteriores.  
**Tema/tipo:** volatilidade; benchmark econométrico fora da amostra.  
**Dados/amostra:** câmbio DM–USD e retornos IBM com variância realizada; 330 modelos ARCH/GARCH.  
**Método/resultado:** SPA e Reality Check. GARCH(1,1) não é superado no câmbio; em IBM é inferior a modelos com efeito de alavancagem. O artigo mostra que o Reality Check pode ter baixo poder.  
**Afirmação sustentada:** comparação ML × econometria deve usar baselines fortes, múltiplas séries e testes de superioridade preditiva; não existe “vencedor universal”.  
**Localizador/trecho curto:** Summary: “no evidence that a GARCH(1,1) is outperformed” no câmbio.  
**Limitações:** não avalia ML moderno; resultados dependem da série, proxy de volatilidade e função de perda.  
**Repositório:** não localizado. **Baixar:** sim.

## 4. Prioridade média — sustentação, comparação e extensão

Nesta faixa estão trabalhos importantes para revisão de literatura, construção de benchmarks e detalhamento de técnicas. Quando o texto integral não foi consultado, a coluna “evidência” limita-se ao que foi confirmado bibliograficamente no resumo ou na página editorial.

| ID | Referência e DOI | Cadeia e tema | Evidência diretamente verificável | Limitação / situação local |
|---|---|---|---|---|
| M1 | Cavalcante, R. C.; Brasileiro, R. C.; Souza, V. L. F.; Nobrega, J. P.; Oliveira, A. L. I. (2016). *Computational Intelligence and Financial Markets: A Survey and Future Directions*. Expert Systems with Applications, 55, 194–211. [10.1016/j.eswa.2016.02.006](https://doi.org/10.1016/j.eswa.2016.02.006) | S1/S2; revisão de previsão e trading. | Organiza técnicas, variáveis, mercados e métricas e aponta lacunas de comparação sistemática. | Revisão anterior ao salto de transformers e DRL; não localizado. |
| M2 | Henrique, B. M.; Sobreiro, V. A.; Kimura, H. (2019). *Literature review: Machine learning techniques applied to financial market prediction*. Expert Systems with Applications, 124, 226–251. [10.1016/j.eswa.2019.01.012](https://doi.org/10.1016/j.eswa.2019.01.012) | S1/S2; revisão sistemática. | Classifica dados, mercados, algoritmos e critérios de avaliação e expõe heterogeneidade metodológica. | Não substitui a leitura dos estudos primários; não localizado. |
| M3 | Goodell, J. W.; Kumar, S.; Lim, W. M.; Pattnaik, D. (2021). *Artificial intelligence and machine learning in finance: Identifying foundations, themes, and research clusters from bibliometric analysis*. Journal of Behavioral and Experimental Finance, 32, 100577. [10.1016/j.jbef.2021.100577](https://doi.org/10.1016/j.jbef.2021.100577) | S3; mapa bibliométrico que levou a Gu, Tetlock e Harvey. | Identifica fundações e clusters de IA/ML em finanças por co-citação e acoplamento bibliográfico. | Bibliometria mede estrutura da literatura, não validade empírica; não localizado. |
| M4 | Nazareth, N.; Reddy, Y. V. (2023). *Financial applications of machine learning: A literature review*. Expert Systems with Applications, 219, 119640. [10.1016/j.eswa.2023.119640](https://doi.org/10.1016/j.eswa.2023.119640) | S2; revisão ampla. | Consolida aplicações em previsão, gestão de risco, fraude e carteiras e discute explicabilidade. | Escopo amplo reduz profundidade por aplicação; não localizado. |
| M5 | Ozbayoglu, A. M.; Gudelek, M. U.; Sezer, O. B. (2020). *Deep learning for financial applications: A survey*. Applied Soft Computing, 93, 106384. [10.1016/j.asoc.2020.106384](https://doi.org/10.1016/j.asoc.2020.106384) | S1/S2; taxonomia de DL. | Reúne arquiteturas e tarefas financeiras, inclusive previsão, trading algorítmico e gestão de carteira. | Resultados dos estudos são pouco comparáveis; não localizado. |
| M6 | Krauss, C.; Do, X. A.; Huck, N. (2017). *Deep neural networks, gradient-boosted trees, random forests: Statistical arbitrage on the S&P 500*. European Journal of Operational Research, 259(2), 689–702. [10.1016/j.ejor.2016.10.031](https://doi.org/10.1016/j.ejor.2016.10.031) | Fischer/Gu; trading e comparação de modelos. | Compara DNN, gradient boosting e random forest em estratégia long-short sobre constituintes do S&P 500. | Rentabilidade histórica depende de custos, universo e protocolo; não localizado. |
| M7 | Long, W.; Lu, Z.; Cui, L. (2019). *Deep learning-based feature engineering for stock price movement prediction*. Knowledge-Based Systems, 164, 163–173. [10.1016/j.knosys.2018.10.034](https://doi.org/10.1016/j.knosys.2018.10.034) | S1/S2/S4; representação de atributos. | Usa autoencoder e modelos profundos para extrair representação antes da classificação do movimento. | Previsão direcional não demonstra, sozinha, valor de carteira; não localizado. |
| M8 | Patel, J.; Shah, S.; Thakkar, P.; Kotecha, K. (2015). *Predicting stock and stock price index movement using Trend Deterministic Data Preparation and machine learning techniques*. Expert Systems with Applications, 42(1), 259–268. [10.1016/j.eswa.2014.07.040](https://doi.org/10.1016/j.eswa.2014.07.040) | S1/S4; preparação de dados e classificação. | Compara ANN, SVM, random forest e naive Bayes com indicadores técnicos transformados. | Mercado/período limitados e sem otimização completa de carteira; não localizado. |
| M9 | Kara, Y.; Boyacioglu, M. A.; Baykan, Ö. K. (2011). *Predicting direction of stock price index movement using artificial neural networks and support vector machines*. Expert Systems with Applications, 38(5), 5311–5319. [10.1016/j.eswa.2010.10.027](https://doi.org/10.1016/j.eswa.2010.10.027) | S1/S4/S6; benchmark ANN × SVM. | Prevê direção do índice ISE National 100 com indicadores técnicos e compara ANN e SVM. | Um mercado, tarefa binária e desenho anterior às boas práticas atuais; não localizado. |
| M10 | Ta, V.-D.; Liu, C.-M.; Tadesse, D. A. (2020). *Portfolio Optimization-Based Stock Prediction Using Long-Short Term Memory Network in Quantitative Trading*. Applied Sciences, 10(2), 437. [10.3390/app10020437](https://doi.org/10.3390/app10020437) | S2/S3/S5; LSTM + otimização. | Integra previsão LSTM e alocação de carteira e compara estratégias quantitativas em backtest. | Artigo aberto, mas resultados dependem da amostra e premissas de negociação; não localizado. |
| M11 | Ma, Y.; Han, R.; Wang, W. (2020). *Prediction-Based Portfolio Optimization Models Using Deep Neural Networks*. IEEE Access, 8, 115393–115405. [10.1109/ACCESS.2020.3003819](https://doi.org/10.1109/ACCESS.2020.3003819) | Forward de S4/S5; predict-then-optimize. | Formula variantes de otimização alimentadas por previsões de redes profundas. | Separar ganho da previsão e ganho do otimizador exige ablação; não localizado. |
| M12 | Du, J. (2022). *Mean–variance portfolio optimization with deep learning based-forecasts for cointegrated stocks*. Expert Systems with Applications, 201, 117005. [10.1016/j.eswa.2022.117005](https://doi.org/10.1016/j.eswa.2022.117005) | Forward de S4; cointegração, DL e carteira. | Combina previsões profundas de ações cointegradas com otimização média-variância. | Caso especializado; sensível à estabilidade da cointegração. **PDF local localizado.** |
| M13 | Ngo, V. M.; Nguyen, H. H.; Nguyen, P. V. (2023). *Does reinforcement learning outperform deep learning and traditional portfolio optimization models in frontier and developed financial markets?* Research in International Business and Finance, 65, 101936. [10.1016/j.ribaf.2023.101936](https://doi.org/10.1016/j.ribaf.2023.101936) | Forward de S4/S5; comparação RL × DL × métodos tradicionais. | Contrasta classes de modelos em mercados desenvolvido e de fronteira. | Acesso ao resultado detalhado foi bibliográfico; não localizado. |
| M14 | Moody, J.; Saffell, M. (2001). *Learning to Trade via Direct Reinforcement*. IEEE Transactions on Neural Networks, 12(4), 875–889. [10.1109/72.935097](https://doi.org/10.1109/72.935097) | Almahdi/S3/S6; origem de RRL financeiro. | Otimiza diretamente uma medida de desempenho de trading, incorporando custos, sem etapa separada de previsão. | Baixa dimensionalidade e mercados/períodos históricos; não localizado. |
| M15 | Bollen, J.; Mao, H.; Zeng, X. (2011). *Twitter mood predicts the stock market*. Journal of Computational Science, 2(1), 1–8. [10.1016/j.jocs.2010.12.007](https://doi.org/10.1016/j.jocs.2010.12.007) | S1/Goodell; sentimento social. | Relaciona dimensões de humor do Twitter à previsão do DJIA com redes neurais. | Resultado famoso, mas sensível a período curto, coleta e replicabilidade; não localizado. |
| M16 | Tetlock, P. C.; Saar-Tsechansky, M.; Macskassy, S. (2008). *More Than Words: Quantifying Language to Measure Firms' Fundamentals*. The Journal of Finance, 63(3), 1437–1467. [10.1111/j.1540-6261.2008.01362.x](https://doi.org/10.1111/j.1540-6261.2008.01362.x) | Goodell → Tetlock; texto e fundamentos. | Notícias negativas específicas das firmas antecipam lucros e retornos, com conteúdo incremental. | Léxico e mídia tradicionais; não é estudo de carteira; não localizado. |
| M17 | Loughran, T.; McDonald, B. (2011). *When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks*. The Journal of Finance, 66(1), 35–65. [10.1111/j.1540-6261.2010.01625.x](https://doi.org/10.1111/j.1540-6261.2010.01625.x) | Goodell; NLP financeiro. | Mostra que dicionários gerais classificam mal termos financeiros e constrói léxico específico para documentos 10-K. | Vocabulário inglês/regulatório e tarefa específica; não localizado. |
| M18 | Xing, F. Z.; Cambria, E.; Zhang, Y. (2019). *Sentiment-aware volatility forecasting*. Knowledge-Based Systems, 176, 68–76. [10.1016/j.knosys.2019.03.029](https://doi.org/10.1016/j.knosys.2019.03.029) | S2/Goodell; sentimento e volatilidade. | Integra sentimento textual a modelos de previsão de volatilidade. | Ganho depende da fonte e da qualidade do sinal textual; não localizado. |
| M19 | Roh, T. H. (2007). *Forecasting the volatility of stock price index*. Expert Systems with Applications, 33(4), 916–922. [10.1016/j.eswa.2006.08.001](https://doi.org/10.1016/j.eswa.2006.08.001) | S1/S2; híbrido NN/econometria. | Compara modelos de volatilidade e combinação de redes com componentes econométricos. | Evidência antiga e restrita a índice; não localizado. |
| M20 | Bergmeir, C.; Hyndman, R. J.; Koo, B. (2018). *A note on the validity of cross-validation for evaluating autoregressive time series prediction*. Computational Statistics & Data Analysis, 120, 70–83. [10.1016/j.csda.2017.11.003](https://doi.org/10.1016/j.csda.2017.11.003) | Arnott/Olorunnimbe; validação temporal. | Demonstra condições em que CV pode ser válida para modelos autorregressivos e distingue dependência temporal de vazamento. | Não autoriza embaralhamento indiscriminado nem cobre todo problema financeiro; não localizado. |
| M21 | Harvey, C. R.; Liu, Y.; Zhu, H. (2016). *... and the Cross-Section of Expected Returns*. The Review of Financial Studies, 29(1), 5–68. [10.1093/rfs/hhv059](https://doi.org/10.1093/rfs/hhv059) | Goodell/Gu; múltiplos testes. | Reavalia significância de centenas de fatores e argumenta que o limiar tradicional é insuficiente sob mineração extensiva. | Hipótese e dependência entre testes afetam o limiar; não localizado. |
| M22 | Brown, S. J.; Goetzmann, W.; Ibbotson, R. G.; Ross, S. A. (1992). *Survivorship Bias in Performance Studies*. The Review of Financial Studies, 5(4), 553–580. [10.1093/rfs/5.4.553](https://doi.org/10.1093/rfs/5.4.553) | Cadeia metodológica; composição do universo. | Mostra como excluir fundos/ativos encerrados cria persistência e desempenho aparentes. | Contexto original de fundos, mas o mecanismo vale para universos históricos de ações; não localizado. |

## 5. Baixa prioridade — complementares e mais distantes da pergunta central

| ID | Referência | Origem/relação e utilidade | Por que não está acima |
|---|---|---|---|
| B1 | Corsi, F. (2009). *A Simple Approximate Long-Memory Model of Realized Volatility*. Journal of Financial Econometrics, 7(2), 174–196. [10.1093/jjfinec/nbp001](https://doi.org/10.1093/jjfinec/nbp001) | S2 → cadeia de volatilidade; segundo nível. HAR-RV é baseline forte e interpretável. | Não usa ML e não trata seleção/alocação; não localizado. |
| B2 | Silva, N. F.; Santos, M.; Gomes, C. F. S.; Andrade, L. P. (2023). *An integrated CRITIC and Grey Relational Analysis approach for investment portfolio selection*. Decision Analytics Journal, 8, 100285. [10.1016/j.dajour.2023.100285](https://doi.org/10.1016/j.dajour.2023.100285) | Forward da linha S5; extensão multicritério da seleção de ativos. | Relação indireta com ML preditivo; validação bibliográfica; não localizado. |
| B3 | Ashrafzadeh, M.; Taheri, H. M.; Gharehgozlou, M.; Zolfani, S. H. (2023). *Clustering-based return prediction model for stock pre-selection in portfolio optimization using PSO-CNN+MVF*. Journal of King Saud University — Computer and Information Sciences, 35(9), 101737. [10.1016/j.jksuci.2023.101737](https://doi.org/10.1016/j.jksuci.2023.101737) | Forward de S4/S5; exemplo recente de pipeline híbrido. | Muitas partes acopladas dificultam atribuir causalmente o ganho; validação bibliográfica; não localizado. |
| B4 | Sharma, M.; Shekhawat, H. S. (2022). *Portfolio optimization and return prediction by integrating modified deep belief network and recurrent neural network*. Knowledge-Based Systems, 250, 109024. [10.1016/j.knosys.2022.109024](https://doi.org/10.1016/j.knosys.2022.109024) | Forward de S4/S5; arquitetura profunda aplicada à previsão e à carteira. | Menor centralidade no grafo e acesso apenas bibliográfico; não localizado. |
| B5 | Abolmakarem, S.; Abdi, F.; Khalili-Damghani, K.; Didehkhani, H. (2023). *Predictive multi-period multi-objective portfolio optimization based on higher order moments: Deep learning approach*. Computers & Industrial Engineering, 183, 109450. [10.1016/j.cie.2023.109450](https://doi.org/10.1016/j.cie.2023.109450) | Forward de S4/S5; DL, multiperíodo e momentos superiores. | Resultado detalhado não validado no texto integral; não localizado. |
| B6 | Silva, N. F.; Andrade, L. P.; Silva, W. S.; Melo, M. K.; Tonelli, A. O. (2024). *Portfolio optimization based on the pre-selection of stocks by the Support Vector Machine model*. Finance Research Letters, 61, 105014. [10.1016/j.frl.2024.105014](https://doi.org/10.1016/j.frl.2024.105014) | Forward de S5; continuidade recente da pré-seleção preditiva. | Artigo curto e acesso apenas bibliográfico na busca; não localizado. |

## 6. Trilha separada: criptoativos

Os trabalhos abaixo são úteis para comparação, mas não devem ser misturados automaticamente aos resultados de ações. Criptoativos têm negociação contínua, microestrutura, regimes, custos e riscos operacionais próprios.

| ID | Referência | Origem/relação; método/dados | Limitação / situação local |
|---|---|---|---|
| C1 | Cui, T.; Ding, S.; Jin, H.; Zhang, Y. (2023). *Portfolio constructions in cryptocurrency market: A CVaR-based deep reinforcement learning approach*. Economic Modelling, 119, 106078. [10.1016/j.econmod.2022.106078](https://doi.org/10.1016/j.econmod.2022.106078) | Forward de S3/S6; alocação dinâmica com CVaR e DRL em criptoativos. | Generalização para ações não é automática. **PDF local localizado.** |
| C2 | Zhou, Z.; Song, Z.; Xiao, H.; Ren, T. (2023). *Multi-source data driven cryptocurrency price movement prediction and portfolio optimization*. Expert Systems with Applications, 219, 119600. [10.1016/j.eswa.2023.119600](https://doi.org/10.1016/j.eswa.2023.119600) | Forward de S4/S5; múltiplas fontes, previsão e otimização de carteira cripto. | Risco de leakage e dependência da disponibilidade das fontes. **PDF local localizado.** |
| C3 | Henriques, I.; Sadorsky, P. (2023). *Forecasting NFT coin prices using machine learning: Insights into feature significance and portfolio strategies*. Global Finance Journal, 58, 100904. [10.1016/j.gfj.2023.100904](https://doi.org/10.1016/j.gfj.2023.100904) | Forward da cadeia S2; previsão por ML e estratégias de carteira de moedas ligadas a NFTs. | Segmento ainda mais específico que cripto em geral; não localizado. |
| C4 | Jiang, Z.; Xu, D.; Liang, J. (2017). *A Deep Reinforcement Learning Framework for the Financial Portfolio Management Problem*. arXiv. [10.48550/arXiv.1706.10059](https://doi.org/10.48550/arXiv.1706.10059) | Referência citada por S6; framework end-to-end de DRL popularizado em carteiras de cripto. | Preprint e forte risco de sobreajuste ao protocolo; não localizado. |
| C5 | Lucarelli, G.; Borrotti, M. (2020). *A Deep Q-Learning Portfolio Management Framework for the Cryptocurrency Market*. Neural Computing and Applications, 32, 17229–17244. [10.1007/s00521-020-05359-8](https://doi.org/10.1007/s00521-020-05359-8) | Segundo nível de S3/S6; agentes locais com deep/double/dueling Q-learning e recompensa global; BTC, LTC, ETH e XRP. | Quatro criptoativos e período específico; não localizado. |

## 7. Referências e classes rejeitadas, com justificativa

| Item | Decisão | Motivo |
|---|---|---|
| Hochreiter e Schmidhuber (1997), artigo original de LSTM | Rejeitado do catálogo principal | Essencial para a arquitetura, mas é fonte geral de computação, não evidência financeira. Deve ser citado apenas se a subseção explicar LSTM. |
| Mnih et al. (2015), *Human-level control through deep reinforcement learning* | Rejeitado do catálogo principal | Fundamento de DQN em jogos; não testa mercados, custos nem carteiras. |
| Sutton e Barto, *Reinforcement Learning: An Introduction* | Rejeitado do catálogo principal | Manual conceitual, útil para definições, mas não evidência empírica financeira. |
| Aplicações de gradient boosting a previsão de energia eólica recuperadas por similaridade | Rejeitadas | Coincidência metodológica sem domínio financeiro. |
| Estudos de previsão de vendas/varejo com LSTM recuperados no forward graph | Rejeitados | Não sustentam inferências sobre retornos, risco ou portfólio. |
| Trabalhos de ciclos de investimento/macroeconomia sem modelo preditivo de ativos | Rejeitados | “Investment” no título gerou correspondência lexical, mas a pergunta de pesquisa é distinta. |
| Otimização fuzzy de carteira sob background risk sem ML | Rebaixada/rejeitada | Pode apoiar otimização robusta, porém não a integração ML-finanças procurada. |
| Particle swarm optimization para carteira sem componente preditivo | Rebaixada/rejeitada | Meta-heurística de otimização não equivale a aprendizado estatístico do mercado. |
| Modelos de financial distress/credit scoring com SMOTE | Rejeitados | São aplicações financeiras de ML, mas a unidade de análise e o desfecho não são retorno/carteira. |
| Previsão de petróleo/commodities sem decisão de portfólio | Rejeitada | Mercado útil como extensão, mas distante do núcleo ações–seleção–alocação. |
| Artigos exclusivamente de detecção de fraude | Rejeitados | Relevantes a fintech, não à hipótese e aos indicadores desta subseção. |
| Citações prospectivas sem metadados confiáveis, DOI resolvível ou fonte editorial | Rejeitadas | Não é possível garantir identidade e rastreabilidade bibliográfica suficientes. |

## 8. Trabalhos faltantes mais importantes no levantamento original

Ranking pelo valor marginal para a subseção, considerando aderência temática, força metodológica e recorrência na cadeia:

1. **DeMiguel, Garlappi e Uppal (2009)** — benchmark 1/N: impede que um otimizador complexo seja avaliado contra uma linha de base fraca.
2. **Fischer e Krauss (2018)** — elo central entre previsão LSTM, ganho econômico e erosão por custos/regime.
3. **Gu, Kelly e Xiu (2020)** — benchmark moderno e amplo de ML para retorno cross-sectional.
4. **Bailey et al. (2016)** — medida explícita de probabilidade de overfitting de backtest.
5. **Harvey, Liu e Zhu (2016)** — controle de múltiplos testes no asset pricing.
6. **White (2000)** — fundamento do problema de data snooping.
7. **Brown et al. (1992)** — viés de sobrevivência na formação do universo histórico.
8. **Olorunnimbe e Viktor (2023)** — avaliação de 35 estudos de backtest em DL financeiro e lacunas de reprodutibilidade.
9. **Arnott, Harvey e Markowitz (2019)** — protocolo específico para backtesting em ML.
10. **Moody e Saffell (2001)** — origem do aprendizado por reforço recorrente aplicado a trading com custos.
11. **Almahdi e Yang (2017)** — referência recorrente em quatro sementes para RL orientado a drawdown.
12. **Paiva et al. (2019)** — caso diretamente aderente de SVM + média-variância no Ibovespa e já disponível localmente.
13. **Ma, Han e Wang (2021)** — previsão, MV/Omega, China e efeito material de turnover; já disponível localmente.
14. **Chen et al. (2021)** — exemplo explícito de previsão XGBoost alimentando média-variância; já disponível localmente.
15. **Loughran e McDonald (2011)** — evita transferir ingenuamente léxicos gerais para texto financeiro.

## 9. Matriz operacional de leitura e download

| Ordem | Trabalho | Ação recomendada | Uso provável no TCC |
|---:|---|---|---|
| 1 | DeMiguel et al. (2009) | Baixar e fichar método/resultados | baseline 1/N e erro de estimação |
| 2 | Fischer e Krauss (2018) | Baixar e fichar tabelas de custo/período | LSTM, trading e não estacionariedade |
| 3 | Gu, Kelly e Xiu (2020) | Baixar suplemento e dados/código se disponíveis | asset pricing por ML |
| 4 | Bailey et al. (2016) | Baixar | overfitting de backtest/CSCV |
| 5 | Harvey, Liu e Zhu (2016) | Baixar | múltiplos testes |
| 6 | White (2000) | Baixar | data snooping |
| 7 | Olorunnimbe e Viktor (2023) | Baixar | revisão crítica de backtests |
| 8 | Arnott et al. (2019) | Baixar | protocolo de pesquisa |
| 9 | Moody e Saffell (2001) | Baixar | fundamento de RL financeiro |
| 10 | Almahdi e Yang (2017) | Baixar | RL com drawdown e custos |
| 11 | Paiva et al. (2019) | **Já existe; fichar PDF local** | evidência brasileira |
| 12 | Ma, Han e Wang (2021) | **Já existe; fichar PDF local** | turnover e otimização |
| 13 | Chen et al. (2021) | **Já existe; fichar PDF local** | XGBoost + MV |
| 14 | Brown et al. (1992) | Baixar | viés de sobrevivência |
| 15 | Loughran e McDonald (2011) | Baixar | NLP financeiro específico |

## 10. Síntese conceitual para orientar a subseção

O grafo revela que “ML aplicado a finanças” contém pelo menos quatro problemas diferentes: **prever** uma variável financeira; **converter** a previsão em posição ou peso; **otimizar** a carteira sob retorno/risco/restrições; e **validar** a estratégia fora da amostra com custos e múltiplas tentativas. Um modelo pode ter boa acurácia e, ainda assim, falhar economicamente porque o sinal é pequeno, instável, concentrado, caro de negociar ou explorado após muitas especificações.

Assim, uma comparação tecnicamente defensável deve separar:

- qualidade preditiva: erro, direção, calibração e estabilidade temporal;
- qualidade econômica: retorno líquido, Sharpe/Sortino, drawdown, turnover, exposição e capacidade;
- desenho de portfólio: benchmark 1/N, média-variância, restrições, regularização e reotimização;
- validade: janela realmente fora da amostra, universo sem survivorship bias, custos, atraso informacional e controle de multiple testing;
- transferibilidade: diferenças entre ações, índices, ETFs e criptoativos.

## 11. Auditoria e conclusão da busca

### Saturação

A segunda expansão, feita a partir de Fischer e Krauss (2018), Henrique et al. (2019), Goodell et al. (2021), Olorunnimbe e Viktor (2023) e Almahdi e Yang (2017), retornou 967 trabalhos únicos antes da união com o primeiro nível. Os novos resultados passaram a repetir os mesmos núcleos — previsão de direção, LSTM, asset pricing, sentimento, RL de carteira e validação — ou a migrar para aplicações laterais. Isso indica **saturação temática operacional**, não exaustividade absoluta.

### Contagens finais

- 51 referências mantidas: 18 altas, 22 médias, 6 baixas e 5 cripto;
- 12 exclusões/classes de exclusão explicitadas;
- 6 referências mantidas com PDF confirmado no repositório local;
- 1.760 nós únicos triados no grafo combinado;
- metadados de 60 candidatos finalistas confrontados com Crossref, além da validação por DOI/página editorial/texto integral conforme disponibilidade.

### Limites do levantamento

1. OpenAlex e Crossref não têm cobertura idêntica a Scopus, Web of Science ou Google Scholar.
2. “Citado por” pode incluir versões preprint e publicadas, gerando duplicatas que exigem normalização por título/DOI.
3. Nem todos os textos integrais estavam abertos; resultados numéricos só foram registrados quando diretamente verificáveis.
4. A presença de um artigo no grafo não valida seu desenho empírico; por isso centralidade e prioridade foram tratadas separadamente.
5. A data de corte é 28/09/2026; trabalhos posteriores não estão cobertos.

### Critério de encerramento

O levantamento foi encerrado porque: (i) as cadeias centrais convergiram; (ii) os trabalhos adicionais já não alteravam os principais eixos conceituais; e (iii) as lacunas relevantes restantes são de **leitura integral/fichamento dos PDFs prioritários**, não de descoberta de novas famílias bibliográficas.
