# Citações acadêmicas sobre o Índice de Sharpe

## Escopo e critério de validação

Foram examinados recursivamente **61 PDFs** em `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA`. A busca foi feita no texto extraído diretamente dos PDFs com `pdftotext -layout`, preservando as quebras de página, e cada trecho abaixo foi conferido na página indicada do próprio PDF. Foram identificados 43 PDFs candidatos por termos diretos ou correlatos; somente trechos no corpo/abstract/metodologia dos artigos foram aproveitados. Não foi usada nenhuma obra de Assaf Neto.

Convenção: “página do PDF” é a página física do arquivo (contagem iniciada em 1); “página impressa” é a numeração exibida pelo periódico quando presente.

## Melhores citações

As seis ideias solicitadas podem ser sustentadas, prioritariamente, pelas entradas M1–M9 abaixo:

1. **Retorno excedente, taxa livre de risco e risco:** M1, M2, M3 e M4 apresentam a fórmula e identificam seus componentes.
2. **Denominador como risco/volatilidade:** M1, M2, M3 e M4 explicitam que o denominador é o desvio-padrão/volatilidade.
3. **Maior Sharpe = melhor relação retorno-risco:** M1 afirma isso expressamente; M5 o descreve como maior retorno por unidade de risco.
4. **Sharpe como objetivo de seleção/otimização:** M5, M6 e M7.
5. **Máximo Sharpe e pesos/carteira ótima:** M6, M7 e M8.
6. **Máximo Sharpe e carteira de tangência:** M9 é a fonte direta localizada.

### M1 — DIRETA

- **Título:** Online risk-based portfolio allocation on subsets of crypto assets applying a prototype-based clustering algorithm
- **Autores / ano:** Luis Lorenzo; Javier Arroyo (2023)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Online risk-based portfolio allocation on subsets of crypto assets applying a prototype-based clustering algorithm.pdf`
- **Página do PDF / impressa:** 20 / Page 20 of 40
- **BibTeX:** `lorenzo2023online`
- **Citação literal:** 
-“The Sharpe ratio is the average excess risk-free return by volatility unit or total risk. The ratio determines the risk of the investment concerning the return of an investment with zero risk: \(SR_c = (r_P-r_f)/\sigma_P\), where \(r_P\) in Eq. 4 is the portfolio return, \(r_f\) is the risk-free rate and \(\sigma_P\) is the portfolio risk (standard deviation or the volatility of the portfolio). … The greater the value of the Sharpe ratio, the more attractive the risk-adjusted return of the portfolio.”
- 
- **Tradução/síntese:** Define o índice como retorno excedente sobre ativo livre de risco por unidade de volatilidade/risco total; identifica cada termo da fórmula e afirma que valor maior é mais atrativo.
- **Afirmação do TCC que sustenta:** definição, numerador excedente a \(r_f\), denominador de risco/volatilidade e interpretação de valores maiores.
- **Contexto:** subseção metodológica “Strategy 1: Sharpe ratio”; não é referência bibliográfica nem resultado de tabela.

### M2 — DIRETA

- **Título:** Portfolio Optimization Methods for the Digital Asset Market: A Comprehensive Survey
- **Autores / ano:** Giorgos Demosthenous; Chrysis Georgiou (2026)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Portfolio Optimization Methods for the Digital Asset Market - A Comprehensive Survey.pdf`
- **Página do PDF / impressa:** 15 / 342:15
- **BibTeX:** `demosthenous2026portfolio`
- **Citação literal:** “One of the most important metrics for evaluating portfolio performance is the Sharpe ratio [75], defined as: \(S = (\mathbb{E}[R_p]-R_f)/\sigma_p\), where \(\mathbb{E}[R_p]\) is the expected portfolio return, \(R_f\) is the risk-free rate, and \(\sigma_p\) is the standard deviation of portfolio returns.”
- **Tradução/síntese:** A fórmula é retorno esperado da carteira menos taxa livre de risco, dividido pelo desvio-padrão dos retornos da carteira.
- **Afirmação do TCC que sustenta:** formulação formal do Índice de Sharpe e interpretação do denominador como volatilidade.
- **Contexto:** definição apresentada pela revisão em seção de métricas de desempenho de portfólios.

### M3 — DIRETA

- **Título:** Deep reinforcement learning for portfolio selection
- **Autores / ano:** Yifu Jiang; José Olmo; Majed Atwi (2024)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Deep reinforcement learning for portfolio selection.pdf`
- **Página do PDF / impressa:** 8 / 8
- **BibTeX:** `jiang2024deep`
- **Citação literal:** “A complementary performance measure widely used in the literature is the Sharpe ratio, which measures the portfolio return per risk unit. The Sharpe ratio is defined as: \(SR=(E[\rho_t]-\rho_f)/\sigma_{\rho_t}\), where \(\rho_t\) denotes the portfolio return, … \(\rho_f\) is the risk-free return, and \(\sigma_{\rho_t}\) is the unconditional volatility of \(\rho_t\), defined as \(\sigma_{\rho_t}=\sqrt{Var(\rho_t)}\).”
- **Tradução/síntese:** Trata o Sharpe como retorno da carteira por unidade de risco e define a volatilidade como raiz da variância do retorno.
- **Afirmação do TCC que sustenta:** retorno por unidade de risco e uso do desvio-padrão/volatilidade como risco total.
- **Contexto:** seção de medidas de desempenho, imediatamente antes da comparação dos métodos de carteira.

### M4 — DIRETA

- **Título:** Mean-variance portfolio optimization with deep learning based-forecasts for cointegrated stocks
- **Autores / ano:** Juan Du (2022)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Mean–variance portfolio optimization with deep learning based-forecasts for cointegrated stocks.pdf`
- **Página do PDF / impressa:** 6 / 6
- **BibTeX:** `du2022mean`
- **Citação literal:** “The SAR and the SOR are measures of the risk-adjusted return, which are utilized to analyze not only how high the risk premium is but also how small the variation in the return rate is. … Sharpe ratio = \(\frac{E[r_{i,t}]-r_f}{std(r_{i,t})}\). … where \(E[r_{i,t}]-r_f\) is the annualized monthly excess return. \(std(r_{i,t})\) is the standard deviation of the monthly log return. \(r_f\) is the monthly risk-free interest rate.”
- **Tradução/síntese:** Explicita retorno excedente anualizado no numerador, taxa livre de risco e desvio-padrão dos retornos mensais no denominador.
- **Afirmação do TCC que sustenta:** relação matemática entre prêmio de risco, taxa livre de risco e volatilidade; desempenho ajustado ao risco.
- **Contexto:** metodologia de avaliação de desempenho; a notação \(i\) é a adotada pelo artigo para o retorno avaliado.

### M5 — MUITO FORTE

- **Título:** Portfolio Optimization Methods for the Digital Asset Market: A Comprehensive Survey
- **Autores / ano:** Giorgos Demosthenous; Chrysis Georgiou (2026)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Portfolio Optimization Methods for the Digital Asset Market - A Comprehensive Survey.pdf`
- **Página do PDF / impressa:** 15 / 342:15
- **BibTeX:** `demosthenous2026portfolio`
- **Citação literal:** “SRO methods aim to maximize this quantity, effectively seeking the highest attainable return per unit of risk.”
- **Tradução/síntese:** Métodos de otimização do Sharpe buscam o maior retorno atingível por unidade de risco.
- **Afirmação do TCC que sustenta:** uso do Sharpe como função objetivo de otimização de carteira.
- **Contexto:** frase imediatamente posterior à definição/formula do Sharpe na mesma página; “this quantity” refere-se explicitamente a \(S=(\mathbb{E}[R_p]-R_f)/\sigma_p\).

### M6 — MUITO FORTE

- **Título:** Cryptocurrency Portfolio Optimisation Based on LSTM Time Series Forecasting
- **Autores / ano:** Zhihan Xu; Xinyue Zhang; Zili Zhou (2025)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Cryptocurrency Portfolio Optimisation Based on LSTM Time Series Forecasting.pdf`
- **Página do PDF / impressa:** 4 / não identificada
- **BibTeX:** `xu2025cryptocurrency`
- **Citação literal:** “The objective is to optimize the portfolio’s risk-adjusted returns by maximizing the Sharpe Ratio.”
- **Tradução/síntese:** O objetivo de otimização declarado é maximizar retornos ajustados ao risco via Sharpe.
- **Afirmação do TCC que sustenta:** maximização do Sharpe como objetivo de otimização de carteiras.
- **Contexto:** corpo da introdução/metodologia do artigo, ao apresentar o modelo Markowitz estendido; não é apenas o título de um trabalho citado.

### M7 — FORTE

- **Título:** Bitcoin and Portfolio Diversification: A Portfolio Optimization Approach
- **Autores / ano:** Walid Bakry; Audil Rashid; Somar Al-Mohamad; Nasser El-Kanj (2021)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/4 parte intro - Teoria de Portifólio/Bitcoin and Portfolio Diversification A Portfolio Optimization Approach.pdf`
- **Página do PDF / impressa:** 1 / 1
- **BibTeX:** `bakry2021bitcoin`
- **Citação literal:** “The study employs different constraining optimization frameworks that seek to maximize risk-adjusted returns (Sharpe ratio) of the portfolio by optimizing allocations to each asset class (asset allocation).”
- **Tradução/síntese:** O artigo associa maximizar retorno ajustado ao risco (Sharpe) ao ajuste das alocações por classe de ativo.
- **Afirmação do TCC que sustenta:** relação entre maximização do Sharpe e pesos/alocações da carteira.
- **Contexto:** abstract do próprio artigo. Ele explica a finalidade dos frameworks usados, sem depender de uma fonte secundária.

### M8 — FORTE

- **Título:** Integrating Choquet portfolios and machine learning interpretability for robust cryptocurrency investment strategies
- **Autores / ano:** João Pedro M. Franco; Márcio P. Laurini (2025)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Integrating Choquet portfolios and machine learning interpretability for robust cryptocurrency investment strategies.pdf`
- **Página do PDF / impressa:** 8 / 8
- **BibTeX:** `franco2025integrating`
- **Citação literal:** “The set of hyperparameters that resulted in the portfolio with the highest Modified Sharpe Ratio is selected from the portfolios produced in the prior step. The portfolio weights that achieve the maximum Modified Sharpe Ratio in the validation sample are then applied to the test sample.”
- **Tradução/síntese:** Os pesos associados ao maior Sharpe Modificado na validação são escolhidos e usados no teste.
- **Afirmação do TCC que sustenta:** seleção de pesos de carteira a partir da maximização de uma medida do tipo Sharpe.
- **Contexto:** refere-se ao **Modified Sharpe Ratio**, não ao Sharpe tradicional; é evidência complementar para o mecanismo “maximizar razão risco-retorno → escolher pesos”, com essa ressalva explícita.

### M9 — FORTE

- **Título:** Portfolio Optimization Methods for the Digital Asset Market: A Comprehensive Survey
- **Autores / ano:** Giorgos Demosthenous; Chrysis Georgiou (2026)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Portfolio Optimization Methods for the Digital Asset Market - A Comprehensive Survey.pdf`
- **Página do PDF / impressa:** 4 / 342:4
- **BibTeX:** `demosthenous2026portfolio`
- **Citação literal:** “By varying \(\mu_p\), one obtains the efficient frontier, which represents the asset portfolios offering the highest expected return for each corresponding level of risk (see Figure 1). The tangency point between this frontier and the capital allocation line (CAL) based on a risk-free rate, corresponds to the optimal portfolio combining maximum return per unit of risk.”
- **Tradução/síntese:** O ponto de tangência entre fronteira eficiente e CAL baseada na taxa livre de risco corresponde à carteira ótima de máximo retorno por unidade de risco.
- **Afirmação do TCC que sustenta:** conexão entre fronteira eficiente, CAL, carteira de tangência e máximo Sharpe.
- **Contexto:** descrição teórica da MVO; embora não use o nome “Sharpe” nesta frase, “maximum return per unit of risk” é precisamente a interpretação pertinente e está no contexto de carteira ótima.

## Citações adicionais

### A1 — MUITO FORTE

- **Título:** Forecasting and trading cryptocurrencies with machine learning under changing market conditions
- **Autores / ano:** H. Sebastião; P. Godinho (2021)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/3 parte intro - machine learning/Forecasting and trading cryptocurrencies.pdf`
- **Página do PDF / impressa:** 21 / Page 21 of 30
- **BibTeX:** `sebastiao2021forecasting`
- **Citação literal:** “The annualized Sharpe ratio is the ratio between the daily return and the standard deviation of daily returns, considering all days in the test sample, multiplied by \(\sqrt{365}\).”
- **Tradução/síntese:** Para anualizar, o artigo divide o retorno diário pelo desvio-padrão dos retornos diários e multiplica por \(\sqrt{365}\).
- **Afirmação do TCC que sustenta:** volatilidade/desvio-padrão como denominador e cuidado com a periodicidade/anualização do indicador.
- **Contexto:** definição operacional da métrica empregada no backtest. O trecho não explicita taxa livre de risco; portanto, não deve ser usado sozinho para definir o Sharpe completo.

### A2 — FORTE

- **Título:** Artificial Intelligence Applied to Stock Market Trading: A Review
- **Autores / ano:** Fernando G. D. C. Ferreira; Amir H. Gandomi; Rodrigo T. N. Cardoso (2021)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/Artificial_Intelligence_Applied_to_Stock_Market_Trading_A_Review.pdf`
- **Página do PDF / impressa:** 6 / 30903
- **BibTeX:** `ferreira2021artificial`
- **Citação literal:** “Note that although the first risk measure proposed by Markowitz is variance, some of the first studies on portfolio optimization attempted to use other measures, such as Absolute Deviation or Semi-absolute Deviation. Constraints were also considered in order to bring the model closer to reality. … [96] performed Particle Swarm Optimization (PSO) … for three different monobjective optimization models: Mean-Variance model with minimum return constraint, Mean-Variance utility function model using weight factors, and Sharpe-ratio maximization portfolio optimization model.”
- **Tradução/síntese:** A revisão registra explicitamente modelos de otimização de carteira cuja função objetivo é maximizar o Sharpe.
- **Afirmação do TCC que sustenta:** existência e uso de modelos de otimização por maximização do Sharpe.
- **Contexto:** revisão de literatura; o trecho descreve modelos estudados, não propõe uma fórmula própria.

### A3 — COMPLEMENTAR

- **Título:** Portfolio Optimization Methods for the Digital Asset Market: A Comprehensive Survey
- **Autores / ano:** Giorgos Demosthenous; Chrysis Georgiou (2026)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Portfolio Optimization Methods for the Digital Asset Market - A Comprehensive Survey.pdf`
- **Página do PDF / impressa:** 10 / 342:10
- **BibTeX:** `demosthenous2026portfolio`
- **Citação literal:** “Unlike the Sharpe ratio, which penalizes all volatility equally, the Sortino ratio considers only downside volatility, while the Calmar ratio evaluates return relative to MDD, allowing them to capture nuances of portfolio performance that the Sharpe ratio may overlook in highly volatile markets.”
- **Tradução/síntese:** O Sharpe trata toda volatilidade igualmente; Sortino e Calmar podem captar dimensões não capturadas por ele em mercados muito voláteis.
- **Afirmação do TCC que sustenta:** limitação/cuidado interpretativo: o Sharpe não distingue volatilidade favorável de desfavorável.
- **Contexto:** discussão de métricas de avaliação para criptoativos; é uma ressalva específica a mercados com alta volatilidade e drawdowns.

### A4 — COMPLEMENTAR

- **Título:** Integrating Choquet portfolios and machine learning interpretability for robust cryptocurrency investment strategies
- **Autores / ano:** João Pedro M. Franco; Márcio P. Laurini (2025)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Integrating Choquet portfolios and machine learning interpretability for robust cryptocurrency investment strategies.pdf`
- **Página do PDF / impressa:** 8 / 8
- **BibTeX:** `franco2025integrating`
- **Citação literal:** “The MSR (Gregoriou and Gueyie, 2003) extends the traditional Sharpe Ratio by addressing its limitations in capturing the risks associated with non-normal return distributions. In the computation of MSR, the standard deviation is supplanted as the risk measure in the Sharpe Ratio by the (negative) VaR(5 %) as the risk measure.”
- **Tradução/síntese:** Em distribuições não normais, o artigo apresenta o Sharpe Modificado, que troca o desvio-padrão por VaR negativo como medida de risco.
- **Afirmação do TCC que sustenta:** limitação do Sharpe tradicional diante de retornos não normais e alternativa baseada em risco de cauda.
- **Contexto:** trata-se expressamente do **Modified Sharpe Ratio**; usar como discussão de limitação, não como definição do índice convencional.

### A5 — COMPLEMENTAR

- **Título:** Cryptocurrency-portfolios in a mean-variance framework
- **Autores / ano:** Alexander Brauneis; Roland Mestel (2019)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Cryptocurrency-portfolios in a mean-variance framework.pdf`
- **Página do PDF / impressa:** 1 / 259
- **BibTeX:** `brauneis2019cryptocurrency`
- **Citação literal:** “In terms of the Sharpe ratio and certainty equivalent returns, the 1/N-portfolio outperforms single cryptocurrencies and more than 75% of mean-variance optimal portfolios.”
- **Tradução/síntese:** No estudo empírico, a carteira igualmente ponderada supera criptomoedas isoladas e mais de 75% das carteiras média-variância segundo Sharpe e retorno equivalente certo.
- **Afirmação do TCC que sustenta:** uso do Sharpe para comparar o desempenho ajustado ao risco de carteiras concorrentes.
- **Contexto:** resultado do abstract para a amostra analisada; não deve ser generalizado como superioridade universal de 1/N.

### A6 — COMPLEMENTAR

- **Título:** Portfolio formation with preselection using deep learning from long-term financial data
- **Autores / ano:** Wuyu Wang et al. (2020)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Portfolio formation with preselection using deep learning from long-term financial data.pdf`
- **Página do PDF / impressa:** 12 / 12
- **BibTeX:** `wang2020portfolio`
- **Citação literal:** “The Sharpe ratio measures excess return using standard deviation and can be explained as the return per unit of risk. We find that the LSTM+MV achieves the highest level of 0.5845, with the SVM+MV coming in second with 0.4569.”
- **Tradução/síntese:** Além de definir a medida, o artigo a usa para comparar estratégias: a maior razão foi a LSTM+MV.
- **Afirmação do TCC que sustenta:** Sharpe como medida comparativa de retorno excedente por unidade de risco.
- **Contexto:** seção de resultados de estratégias específicas e custos de transação; os números não são definição de um limiar universal de qualidade.

### A7 — DIRETA

- **Título:** Empirical evidence on deep learning-enhanced portfolio optimization: integrating CNN-LSTM forecasts with mean-variance theory in cryptocurrency markets
- **Autores / ano:** Dipo Dunsin; Aashish Acharya; Mohamed Chahine Ghanem; Salma Bellalouna; Hamza Kheddar (2025)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/Empirical evidence on deep learning-enhanced portfolio optimization - integrating CNN-LSTM forecasts with mean-variance theory in cryptocurrency markets.pdf`
- **Página do PDF / impressa:** 9 / 9
- **BibTeX:** `dunsin2025empirical` (entrada `@Misc`, identificada como preprint SSRN no próprio `.bib`)
- **Citação literal:** “The Sharpe ratio measures the risk-adjusted returns by comparing excess portfolio returns to their volatility. Sharpe Ratio = (Rp – Rf) / σp. Where: Rp = Return of portfolio; Rf = Risk-Free rate; σp = standard deviation of the portfolio’s excess return. The Sharpe ratio provides a standardised measure of return per risk.”
- **Tradução/síntese:** Define diretamente o Sharpe como retorno excedente da carteira menos taxa livre de risco, dividido pelo desvio-padrão, e como retorno padronizado por risco.
- **Afirmação do TCC que sustenta:** definição completa, taxa livre de risco, volatilidade e retorno por unidade de risco.
- **Contexto:** seção “Rolling Sharpe Ratio Analysis”. O arquivo declara na própria página ser preprint não revisado por pares; por isso é útil como confirmação local, mas não deve substituir as fontes publicadas M1–M4.

### A8 — DIRETA

- **Título:** Portfolio Optimization Based on MPT-LSTM Neural Networks: A case study of Cryptocurrency Markets
- **Autores / ano:** Habib Zouaoui; Meryem-Nadjat Naas (2025)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Portfolio Optimization Based on MPT-LSTM Neural Networks A case study of Cryptocurrency Markets.pdf`
- **Página do PDF / impressa:** 7 / 88
- **BibTeX:** **não encontrada** em `/mnt/SSD_SEC/GIT/TCC/latex-cefetmg - TCC/referencias.bib`.
- **Citação literal:** “Sharpe Ratio = \(\frac{\mathbb{E}[R_P]-R_f}{\sigma_P}\)”; “Purpose in Optimization: Maximize risk-adjusted return relative to a risk-free rate”; “Interpretation: Higher values indicate better risk-adjusted performance.”
- **Tradução/síntese:** A tabela do artigo traz fórmula, finalidade de maximizar retorno ajustado ao risco relativo à taxa livre de risco e interpretação de que valores maiores são melhores.
- **Afirmação do TCC que sustenta:** fórmula, otimização e comparação por valores maiores do Sharpe.
- **Contexto:** tabela analítica “Key risk-adjusted performance metrics in portfolio optimization”, não uma referência bibliográfica. A informação está em tabela de conteúdo do artigo, e não em tabela de referências.

### A9 — FORTE

- **Título:** When Richer Information Does Not Improve Allocation: Machine Learning and Portfolio Optimisation in NFT-Ecosystem Tokens
- **Autores / ano:** David Toscano; Juan C. Roca; Francisco Jareño (2026)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/NOVOS SEC 3/When Richer Information Does Not Improve Allocation - Machine Learning and Portfolio Optimisation in NFT-Ecosystem Tokens.pdf`
- **Página do PDF / impressa:** 14 / 13
- **BibTeX:** `toscano2026richer`
- **Citação literal:** “For the MMV and MV strategies, portfolio optimization is implemented via Monte Carlo simulation, generating 50,000 candidate portfolios per rolling window; optimal weights are selected by maximizing the Sharpe ratio, providing a robust computational approximation of the efficient frontier in contexts where estimation risk often penalizes traditional analytical solutions.”
- **Tradução/síntese:** O artigo seleciona os pesos ótimos maximizando o Sharpe e relaciona esse procedimento a uma aproximação computacional da fronteira eficiente.
- **Afirmação do TCC que sustenta:** maximização do Sharpe para determinação de pesos e sua relação operacional com a fronteira eficiente.
- **Contexto:** metodologia própria do artigo; é uma implementação por simulação Monte Carlo, não uma identidade teórica geral.

### A10 — FORTE

- **Título:** Optimal Markowitz portfolio using returns forecasted with time series and machine learning models
- **Autores / ano:** Damian Ślusarczyk; Robert Ślepaczuk (2025)
- **PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Optimal Markowitz portfolio using returns.pdf`
- **Página do PDF / impressa:** 12 / Page 12 of 40
- **BibTeX:** `slusarczyk2025optimal`
- **Citação literal:** “The goal is to find a vector of weights w which optimizes the objective function. Two portfolio optimization problems are considered, a global maximum information ratio portfolio and a global minimum variance portfolio. Global maximum information ratio portfolio (GMIR) The information ratio is a measure of the trade-off between returns and risk. A GMIR portfolio is equivalent to the global maximum Sharpe ratio portfolio with a risk-free rate equal to 0.”
- **Tradução/síntese:** O vetor de pesos é otimizado; com taxa livre de risco zero, a carteira de máximo information ratio equivale à carteira de máximo Sharpe.
- **Afirmação do TCC que sustenta:** determinação de pesos por objetivo risco-retorno e caso especial de máximo Sharpe quando \(r_f=0\).
- **Contexto:** desenvolvimento do framework média-variância. A equivalência declarada é condicionada explicitamente a taxa livre de risco igual a zero.

## Termos pesquisados

- Busca literal, sem depender de nomes de arquivo, em texto extraído página a página: `Sharpe ratio`, `Sharpe index`, `Sharpe measure`, `Sharpe`, `risk-adjusted return`, `risk adjusted performance`, `excess return`, `excess return per unit of risk`, `return per unit of risk`, `risk-free rate`, `risk free rate`, `portfolio volatility`, `standard deviation`, `maximum Sharpe`, `maximize Sharpe`, `maximizing Sharpe`, `Sharpe maximization`, `optimal Sharpe`, `tangency portfolio`, `tangency point`, `efficient frontier`, `capital allocation line`, `reward-to-variability`.
- Variações em português: `índice de Sharpe`, `retorno ajustado ao risco`, `retorno excedente`, `taxa livre de risco`, `volatilidade da carteira`, `carteira de tangência`, `maximização do Sharpe`.
- Termos de descoberta correlatos: `SRO`, `risk premium`, `standard deviation of portfolio returns`, `Modified Sharpe Ratio`, `CAL`, `mean-variance`, `portfolio weights`, `asset allocation`, `risk-adjusted performance`.
- Estratégia de controle: busca com contexto, separação por quebra de página do PDF, leitura do trecho completo e conferência de cabeçalhos/numeração impressa. A chave BibTeX foi procurada por título no arquivo `/mnt/SSD_SEC/GIT/TCC/latex-cefetmg - TCC/referencias.bib`.

## Resultados descartados

- `Is there a risk-return trade-off in cryptocurrency markets.pdf`, `Bitcoin A safe haven asset and a winner amid political and economic.pdf` e `s41264-023-00249-1.pdf`: ocorrências de “Sharpe” eram autor em referência (p.ex., Sharpe, 1964) ou nome de pessoa, sem explicação do índice no corpo do artigo.
- Diversos PDFs de previsão/trading, inclusive cópias duplicadas de `Intelligent cryptocurrency trading system using integrated.pdf`: traziam apenas tabelas, gráficos, valores de Sharpe ou testes estatísticos, sem definição/interpretação suficiente para uma citação teórica independente.
- `Portfolio Optimization Methods for the Digital Asset Market - A Comprehensive Survey.pdf`: referências à entrada bibliográfica “William F. Sharpe. 1966 …” foram ignoradas; somente os trechos analíticos do corpo foram usados.
- `Bitcoin and Portfolio Diversification A Portfolio Optimization Approach.pdf`: a região de fórmula de máximo Sharpe extraída em layout estava tipograficamente corrompida/fragmentada; ela não foi transcrita como citação. Foi aproveitado apenas o abstract legível e validado.
- Menções apenas a “maximum Sharpe ratio” em listas de métodos, tabelas, legendas ou títulos de trabalhos citados foram excluídas quando não explicavam a medida, sua interpretação, seleção de pesos ou otimização.

## Resumo quantitativo

- PDFs pesquisados: **61**.
- PDFs candidatos por busca textual: **43**.
- Artigos/trabalhos acadêmicos com resultados válidos registrados: **15** (inclui um preprint SSRN, explicitamente marcado em A7).
- Citações por classificação: **DIRETA 7; MUITO FORTE 3; FORTE 6; COMPLEMENTAR 3**.
