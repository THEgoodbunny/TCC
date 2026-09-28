# Evidências quantitativas — Características do mercado de criptoativos

## 1. Diagnóstico da subseção atual

A subseção já está conceitualmente bem apoiada quanto a quatro pontos: volatilidade elevada, baixa dependência histórica entre criptoativos e classes tradicionais, alteração das relações em crises e possibilidade de previsibilidade explorável por aprendizado de máquina. O principal problema não é falta de temas, mas falta de magnitude, período e condicionantes empíricos.

As afirmações que mais se beneficiariam de números são:

- a comparação de volatilidade entre Bitcoin, Ethereum e ativos tradicionais;
- a alegação de que o Bitcoin seria “dezenas de vezes” mais volátil;
- a diferença entre correlação cripto–ativos tradicionais e correlação dentro do mercado cripto;
- o efeito de crises sobre essas correlações;
- a redução de risco e o desempenho ajustado ao risco obtidos com diversificação;
- a eficácia condicional de stablecoins como hedge ou *safe haven*;
- risco de cauda, CVaR e *maximum drawdown*;
- desempenho efetivo de modelos de ML depois de custos de transação.

Dois cuidados são necessários. Primeiro, os resultados validados não sustentam uma regra universal: as magnitudes mudam com a amostra, frequência e método. Segundo, algumas formulações atuais estão fortes demais. Nas amostras diretamente comparáveis abaixo, a volatilidade do Bitcoin ficou aproximadamente entre 6 e 9 vezes a de índices acionários, enquanto a do Ethereum chegou a cerca de 12,5 vezes a do S&P 500; isso não basta para afirmar genericamente “dezenas de vezes”. Também não foi encontrada, no artigo de Corbet et al. (2020), uma demonstração direta de que criptoativos amplificam o contágio sistêmico.

## 2. Melhores evidências quantitativas

### Q1 — Volatilidade do Bitcoin frente a ações, ouro, câmbio e petróleo

**Classificação:** MUITO FORTE

**Tema:** volatilidade; comparação com ativos tradicionais; risco de cauda.

**Fonte:** Guesmi, Saadi, Abid e Ftiti (2019), *Portfolio diversification with virtual currency: Evidence from bitcoin*.

**BibTeX key:** BIBTEX AUSENTE no arquivo `referencias.bib`.

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/Portfolio diversification with virtual currency Evidence from bitcoin.pdf`

**Página:** PDF 5; página impressa 435.

**Tabela/Figura:** Tabela 1 — “Descriptive statistics of returns series”.

**Amostra/período:** dados diários, 1.561 observações, período impresso como 01/01/2012–05/01/2018.

**Ativos analisados:** Bitcoin, MSCI Emerging Market Index, MSCI Global Market Index, ouro, EUR/USD, WTI, VIX e yuan.

**Métrica:** desvio-padrão dos retornos; mínimos, máximos, assimetria e excesso de curtose.

**Resultado quantitativo:**

- desvio-padrão: Bitcoin 0,0519; MSCI Emerging 0,0086; MSCI Global 0,0067; ouro 0,0096; EUR/USD 0,0053; WTI 0,0205; VIX 0,0713; yuan 0,0014;
- em razões calculadas a partir da própria tabela, o desvio-padrão do Bitcoin foi aproximadamente 6,0 vezes o do MSCI Emerging, 7,7 vezes o do MSCI Global, 5,4 vezes o do ouro, 9,8 vezes o do EUR/USD e 2,5 vezes o do WTI; foi inferior ao do VIX;
- para Bitcoin, retorno mínimo −0,2696, máximo 0,4996 e excesso de curtose 10,474.

Os quocientes acima são cálculos deste relatório; não são razões redigidas pelos autores. O texto metodológico afirma que os log-retornos foram multiplicados por 100, mas a tabela apresenta os valores em notação decimal. Por segurança, os valores são preservados exatamente como impressos e utilizados sobretudo em comparações relativas, sem conversão adicional de unidade.

**Trecho original relevante:** “The return of each series is calculated as the difference of logarithm of two successive prices, multiplied by 100.”

**Interpretação correta:** nessa amostra e frequência, o Bitcoin foi substancialmente mais volátil que ações globais e emergentes, ouro, câmbio e petróleo, além de apresentar caudas pesadas.

**O que NÃO permite afirmar:** não demonstra que o Bitcoin é sempre “dezenas de vezes” mais volátil; não compara títulos de dívida; não autoriza extrapolar a razão para outros períodos ou frequências.

**Onde encaixa na subseção atual:** no primeiro parágrafo, após a comparação entre Bitcoin e classes convencionais.

**Sugestão de uso:** número no texto ou gráfico próprio de barras com os desvios-padrão; a razão é mais clara que a reprodução integral da tabela.

### Q2 — Volatilidade diária de BTC e ETH comparada a S&P 500, ouro e petróleo

**Classificação:** MUITO FORTE

**Tema:** volatilidade; comparação entre classes; extremos e não normalidade.

**Fonte:** Charfeddine, Benlagha e Maouchi (2020), *Investigating the dynamic relationship between cryptocurrencies and conventional assets: Implications for financial investors*.

**BibTeX key:** `charfeddine2020investigating`.

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/Investigating the dynamic relationship between cryptocurrencies and conventional assets Implications for financial investors.pdf`

**Página:** PDF 10; página impressa 207.

**Tabela/Figura:** Tabela 2 — estatísticas descritivas dos retornos diários.

**Amostra/período:** Amostra I, 18/07/2010–01/10/2018, 2.998 observações; Amostra II, 01/09/2015–01/10/2018, 1.127 observações.

**Ativos analisados:** BTC, ETH, S&P 500, ouro e petróleo bruto.

**Métrica:** desvio-padrão de retornos diários definidos como `100 × log(Pt/Pt−1)`, além de mínimos, máximos, assimetria e curtose.

**Resultado quantitativo:**

- Amostra I: desvio-padrão de BTC 2,503%, S&P 500 0,283%, ouro 0,318% e petróleo 0,666%; BTC equivale a aproximadamente 8,84 vezes o S&P 500, 7,87 vezes o ouro e 3,76 vezes o petróleo;
- Amostra II: BTC 1,723%, ETH 2,983%, S&P 500 0,239%, ouro 0,265% e petróleo 0,744%; ETH equivale a aproximadamente 12,48 vezes o S&P 500 e BTC a 7,21 vezes;
- na Amostra I, BTC teve mínimo diário de −21,347% e máximo de 18,439%; sua curtose foi 14,964;
- os testes Jarque–Bera tiveram `p = 0,000` em todas as séries apresentadas.

As razões são cálculos deste relatório a partir dos desvios-padrão da tabela.

**Trecho original relevante:** “cryptocurrencies experience the highest increases in risk”.

**Interpretação correta:** BTC e ETH exibiram volatilidade diária muito superior à dos ativos tradicionais comparados e distribuições fortemente não normais nessas amostras.

**O que NÃO permite afirmar:** não justifica “dezenas de vezes” como regra geral; não é volatilidade anualizada; o máximo de cerca de 12,5 vezes ocorre para ETH versus S&P 500 em uma amostra específica.

**Onde encaixa na subseção atual:** no primeiro parágrafo, qualificando a frase sobre volatilidade relativa.

**Sugestão de uso:** número no texto ou gráfico próprio de barras, mantendo separadas as duas amostras.

### Q3 — Dependência baixa com ativos tradicionais e maior dependência BTC–ETH

**Classificação:** MUITO FORTE

**Tema:** correlação; diversificação; instabilidade temporal.

**Fonte:** Charfeddine, Benlagha e Maouchi (2020), *Investigating the dynamic relationship between cryptocurrencies and conventional assets: Implications for financial investors*.

**BibTeX key:** `charfeddine2020investigating`.

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/Investigating the dynamic relationship between cryptocurrencies and conventional assets Implications for financial investors.pdf`

**Página:** PDF 12 e 15; páginas impressas 209 e 212.

**Tabela/Figura:** Tabela 4 — medidas estáticas de dependência; Tabela 5 — parâmetro de dependência variável no tempo por cópula t de Student.

**Amostra/período:** mesmos períodos de Q2; pares com ETH usam 01/09/2015–01/10/2018.

**Ativos analisados:** BTC e ETH contra S&P 500, ouro e petróleo; par BTC–ETH.

**Métrica:** Pearson, Spearman, Kendall, DCCA, CCC-GARCH e parâmetro variável no tempo de cópula t.

**Resultado quantitativo:**

- Pearson estático: BTC–S&P 500 = 0,010; BTC–ouro = 0,017; BTC–petróleo = −0,008; ETH–S&P 500 = −0,001; ETH–ouro = −0,049; ETH–petróleo = −0,064;
- BTC–ETH = 0,129 por Pearson, 0,104 por Spearman, 0,070 por Kendall, 0,144 por DCCA e 0,138 por CCC-GARCH; todos com significância de 1%; os pares cripto–tradicional da tabela não receberam marca de significância;
- dependência variável no tempo: média BTC–S&P 500 −0,019, com intervalo observado de −0,085 a 0,130; média BTC–ETH 0,101, com mínimo −0,274 e máximo 0,537.

**Trecho original relevante:** “the level of dependence is very weak”.

**Interpretação correta:** a baixa dependência cripto–tradicional favorece diversificação no período analisado, mas não é constante; a dependência BTC–ETH é maior e varia substancialmente no tempo.

**O que NÃO permite afirmar:** não permite dizer que todas as criptomoedas são sempre altamente correlacionadas; BTC–ETH teve média modesta e chegou a valores negativos; correlação baixa não equivale automaticamente a hedge ou *safe haven*.

**Onde encaixa na subseção atual:** no segundo parágrafo, após a afirmação sobre baixa correlação histórica e antes da discussão de correlação interna.

**Sugestão de uso:** números no texto e, se desejado, heatmap próprio a partir da Tabela 4.

### Q4 — Pesos pequenos de cripto em carteiras mistas e eficácia limitada de hedge

**Classificação:** FORTE

**Tema:** diversificação; alocação; hedge.

**Fonte:** Charfeddine, Benlagha e Maouchi (2020), mesmo artigo de Q2–Q3.

**BibTeX key:** `charfeddine2020investigating`.

**PDF:** mesmo caminho de Q2–Q3.

**Página:** PDF 18; página impressa 215.

**Tabela/Figura:** Tabelas 6 e 7 — pesos médios ótimos, razões de hedge e eficácia de hedge.

**Amostra/período:** mesmos períodos de Q2–Q3.

**Ativos analisados:** BTC ou ETH combinados com S&P 500, ouro e petróleo; também BTC–ETH.

**Métrica:** peso ótimo médio do ativo digital (`Wd`) e *hedging effectiveness* (`HE`) por cópulas e GARCH bivariado.

**Resultado quantitativo:**

- por cópula t de Student, os pesos médios foram 4,9% de BTC com S&P 500, 5,7% com ouro e 17,4% com petróleo; para ETH, 2,5% com S&P 500, 3,6% com ouro e 12,5% com petróleo;
- a eficácia de hedge foi baixa na maior parte dos pares: BTC–S&P 500 9,2%, BTC–ouro 9,4%, ETH–S&P 500 1,9% e ETH–ouro 3,1%; o maior valor da tabela foi 32,2% para BTC–petróleo;
- os modelos BEKK, DCC e ADCC produziram pesos de BTC com S&P 500 entre 5,2% e 5,7% e de ETH com S&P 500 entre 1,4% e 3,2%.

**Trecho original relevante:** “including only a small weight of digital assets”.

**Interpretação correta:** no desenho média-variância do artigo, a diversificação ótima com ativos tradicionais geralmente exigiu pequena participação de BTC ou ETH; a capacidade de hedge foi modesta e dependente do par.

**O que NÃO permite afirmar:** não existe um peso universal; os percentuais dependem do modelo, ativo convencional e amostra; o resultado não prova proteção em crises extremas.

**Onde encaixa na subseção atual:** no segundo parágrafo, concretizando “proporções relativamente pequenas”.

**Sugestão de uso:** números no texto; não é necessário reproduzir as duas tabelas completas.

### Q5 — Diversificação entre criptomoedas e desempenho ajustado ao risco

**Classificação:** MUITO FORTE

**Tema:** correlação interna; diversificação; Sharpe; retorno equivalente de certeza.

**Fonte:** Brauneis e Mestel (2019), *Cryptocurrency-portfolios in a mean-variance framework*.

**BibTeX key:** `brauneis2019cryptocurrency`.

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Cryptocurrency-portfolios in a mean-variance framework.pdf`

**Página:** PDF 2, 4 e 5; páginas impressas 260, 262 e 263.

**Tabela/Figura:** texto metodológico; Tabela 2; Tabela 3.

**Amostra/período:** dados diários de 01/01/2015–31/12/2017 para as 500 criptomoedas de maior capitalização; estratégias fora da amostra usam os ativos mais líquidos, janela-base de 183 dias, 59 criptoativos que entraram ao menos uma vez e custo de transação de 25 pontos-base.

**Ativos analisados:** carteiras somente de criptoativos; benchmark 1/N; CRIX; carteiras média-variância; ativos individuais.

**Métrica:** correlação de retornos; retorno médio diário; desvio-padrão; Sharpe; *certainty equivalent return*.

**Resultado quantitativo:**

- quase 98% das correlações pareadas entre 500 criptoativos ficaram entre −0,10 e 0,20;
- Sharpe médio: carteiras 1/N = 0,1865; 144 carteiras otimizadas = 0,1301; 226 observações de criptoativos constituintes = 0,0928; CRIX = 0,1596;
- o menor Sharpe entre as 24 parametrizações 1/N, 0,1549, superou o terceiro quartil das carteiras otimizadas, 0,1534;
- retorno equivalente de certeza médio: 1/N = 0,0073; otimizadas = 0,0047; constituintes = −0,0336;
- na parametrização-base, o portfólio de mínima variância com rebalanceamento diário teve desvio-padrão diário de 3,48%, contra 12,83% do ativo de máximo retorno selecionado; o CRIX apresentou 3,60%.

**Trecho original relevante:** “almost 98% of all pairwise correlations [...] fall within the range from −0.10 to 0.20”.

**Interpretação correta:** a baixa correlação cruzada cria diversificação interna relevante; no estudo, a estratégia ingênua 1/N superou, em média, otimizações média-variância e ativos isolados em Sharpe e CEQ.

**O que NÃO permite afirmar:** não prova que 1/N sempre vence Markowitz; os autores testaram um período de forte expansão e escolhas específicas de liquidez, janela, restrição *long-only* e custos.

**Onde encaixa na subseção atual:** no final do segundo parágrafo, substituindo a afirmação genérica por magnitude e ressalva metodológica.

**Sugestão de uso:** números no texto ou gráfico próprio com Sharpe/CEQ médios; a Figura 2 do artigo é visualmente útil, mas não foi extraída por ausência de dados tabulares de todos os pontos e por licença não identificada como aberta.

### Q6 — Aumento de correlações do Bitcoin no início da COVID-19

**Classificação:** MUITO FORTE

**Tema:** crise; correlação; perda de diversificação; volatilidade.

**Fonte:** Corbet, Larkin e Lucey (2020), *The contagion effects of the COVID-19 pandemic: Evidence from gold and cryptocurrencies*.

**BibTeX key:** `corbet2020contagion`.

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/The contagion effects of the COVID-19 pandemic Evidence from gold and cryptocurrencies.pdf`

**Página:** PDF 3, 5 e 6; páginas impressas 3, 5 e 6.

**Tabela/Figura:** Tabela 2; Tabela 3; Figura 2.

**Amostra/período:** retornos horários de 11/03/2019–10/03/2020, 5.701 observações; 4.580 antes e 1.122 depois de 31/12/2019.

**Ativos analisados:** Bitcoin, Shanghai, Shenzhen, DJIA, WTI e ouro.

**Métrica:** correlação de retornos e correlação condicional dinâmica; desvio-padrão horário.

**Resultado quantitativo:**

- correlação do Bitcoin antes/depois do marco de 31/12/2019: Shanghai 0,0188 → 0,3436; Shenzhen 0,0209 → 0,3857; DJIA 0,0361 → 0,4299; WTI −0,0071 → 0,2792; ouro 0,0392 → 0,4688;
- o desvio-padrão horário do Bitcoin foi 0,0097 antes e 0,0067 depois; portanto, nesse recorte, o resultado central é aumento de correlação, não aumento da volatilidade do Bitcoin;
- no GARCH da Tabela 4, o coeficiente de Bitcoin sobre as bolsas chinesas não foi estatisticamente significativo.

**Trecho original relevante:** “There is evidence of sharp elevations in dynamic correlations between these markets.”

**Interpretação correta:** no início da COVID-19, o Bitcoin passou de correlações quase nulas para correlações positivas moderadas com bolsas, ouro e WTI, reduzindo seu benefício de diversificação naquele episódio.

**O que NÃO permite afirmar:** não demonstra por si só que o Bitcoin causou ou amplificou contágio sistêmico; correlação não implica causalidade; a separação “pós-COVID” começa em 31/12/2019 e termina antes da fase global mais intensa de março de 2020.

**Onde encaixa na subseção atual:** no terceiro parágrafo, ao discutir crises e perda temporária de diversificação.

**Sugestão de uso:** tabela compacta ou gráfico próprio tipo *slope chart*; a Figura 2 pode ser reproduzida/adaptada com atribuição, pois o artigo declara licença CC BY 4.0.

### Q7 — Correlações na pandemia: cripto convencional versus Tether

**Classificação:** MUITO FORTE

**Tema:** crise; correlação; diversificação; stablecoin; *safe haven*.

**Fonte:** Goodell e Goutte (2021), *Diversifying equity with cryptocurrencies during COVID-19*.

**BibTeX key:** `goodell2021diversifying`.

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/1 parte intro - decisoes de investimentos e tomada de decisao/Diversifying equity with cryptocurrencies during COVID-19.pdf`

**Página:** PDF 4 e 5; páginas impressas 4 e 5.

**Tabela/Figura:** Figura 2 — heatmap do período completo; Figura 3 — heatmap do período de pandemia.

**Amostra/período:** 28/02/2019–09/02/2021, 471 observações; subperíodo de pandemia de março de 2020 a fevereiro de 2021.

**Ativos analisados:** BTC, ETH, LTC, Tether; Swiss, IBEX 35, DAX, CAC 40, FTSE 100, EURO STOXX 50, S&P 500 e VIX.

**Métrica:** coeficientes de correlação dos retornos.

**Resultado quantitativo:**

- correlação BTC–S&P 500: 0,163 no período completo e 0,209 na pandemia; LTC–S&P 500: 0,133 → 0,213; ETH–S&P 500: 0,165 → 0,192;
- correlações internas: BTC–LTC 0,730 → 0,835; LTC–ETH 0,699 → 0,834; BTC–ETH 0,745 → 0,747;
- Tether–S&P 500: −0,016 → −0,230; Tether–IBEX: −0,005 → −0,186; Tether–DAX: −0,002 → −0,156; Tether–CAC 40: −0,001 → −0,153;
- contudo, Tether teve correlação positiva na pandemia com Swiss (0,073), FTSE 100 (0,163) e EURO STOXX 50 (0,133); com o VIX, passou de 0,028 para 0,216.

**Trecho original relevante:** “co-movements between cryptocurrencies and equity indices gradually increased as COVID-19 progressed.”

**Interpretação correta:** as criptomoedas convencionais apresentaram correlações positivas maiores com ações e entre si durante a pandemia; o Tether mostrou relação negativa relevante com alguns, mas não todos, os índices acionários.

**O que NÃO permite afirmar:** não é correto escrever que Tether teve correlação negativa com “as ações” de forma universal; três dos sete índices exibiram correlação positiva no subperíodo. As Figuras 2 e 3 comparam período completo e pandemia, não uma divisão perfeitamente simétrica pré/pós.

**Onde encaixa na subseção atual:** no terceiro parágrafo, qualificando a afirmação sobre Tether como *safe haven*.

**Sugestão de uso:** adaptar as duas matrizes em um painel comparativo ou citar somente os pares mais informativos; não reproduzir sem verificar permissão, pois o PDF declara “All rights reserved”.

### Q8 — Redução de VaR e ES com stablecoins em mercados extremos

**Classificação:** MUITO FORTE

**Tema:** risco extremo; stablecoins; *safe haven*; diversificação.

**Fonte:** Wang, Ma e Wu (2020), *Are stablecoins truly diversifiers, hedges, or safe havens against traditional cryptocurrencies as their name suggests?*

**BibTeX key:** `wang2020stablecoins`.

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/Are stablecoins truly diversifiers, hedges, or safe havens against traditional cryptocurrencies as their name suggests.pdf`

**Página:** PDF 14–16; páginas impressas 14–16.

**Tabela/Figura:** Tabelas 7, 8 e 9 — avaliação de risco de cauda para carteiras contra BTC, LTC e XRP.

**Amostra/período:** stablecoins atreladas ao dólar, 06/03/2015–20/03/2019, 1.438 observações; atreladas ao ouro, 13/10/2017–20/03/2019, 524 observações; dados diários.

**Ativos analisados:** BTC, LTC, XRP; Tether, BitUSD, NuBits, DGD, HGT e XAUR; USD e ouro como bases de comparação.

**Métrica:** redução de Value-at-Risk e Expected Shortfall nos níveis de 95%, 99% e 99,9%, calculadas como diferença entre o risco do criptoativo e o risco da carteira cripto–stablecoin. A Carteira 1 usa peso otimizado; a Carteira 2 usa pesos iguais.

**Resultado quantitativo:**

- Carteira 1 com Tether, nível de 99,9%: para BTC, redução de VaR 0,139 e de ES 0,149; para LTC, 0,257 e 0,355; para XRP, 0,295 e 0,404;
- para XRP–Tether, no nível de 99%, as reduções foram 0,138 (VaR) e 0,205 (ES);
- vários portfólios com stablecoins atreladas ao ouro apresentaram reduções negativas; por exemplo, BTC–DGD teve −0,035 em VaR e −0,045 em ES no nível de 99,9%;
- a estratégia otimizada produziu reduções geralmente maiores que a carteira de pesos iguais.

As tabelas expressam as diferenças na mesma escala de retorno usada pelo artigo e não imprimem símbolo de porcentagem; por isso os valores não são reconvertidos aqui para pontos percentuais.

**Trecho original relevante:** “the safe haven property of stablecoins changes across market conditions.”

**Interpretação correta:** stablecoins atreladas ao dólar, sobretudo Tether, reduziram perdas extremas em várias combinações, mas o efeito depende da stablecoin, do criptoativo, do quantil e da regra de pesos.

**O que NÃO permite afirmar:** não autoriza chamar toda stablecoin de *safe haven*; resultados negativos para vários pares mostram que algumas combinações aumentaram o risco medido.

**Onde encaixa na subseção atual:** no terceiro parágrafo, após a ressalva de que a função de proteção ocorre apenas em condições específicas.

**Sugestão de uso:** números no texto ou gráfico próprio com VaR/ES nos três criptoativos; não reproduzir as tabelas integrais sem permissão, pois o PDF não declara licença aberta.

### Q9 — ML: desempenho econômico, custos, CVaR e drawdown

**Classificação:** MUITO FORTE

**Tema:** ML; previsão; retorno de estratégia; risco extremo; custos de transação.

**Fonte:** Sebastião e Godinho (2021), *Forecasting and trading cryptocurrencies with machine learning under changing market conditions*.

**BibTeX key:** `sebastiao2021forecasting`.

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/s40854-020-00217-x (1).pdf`

**Página:** PDF 23, 25–27; páginas impressas 23, 25–27.

**Tabela/Figura:** Tabela 6 — previsão; Tabela 7 — desempenho das estratégias.

**Amostra/período:** 15/08/2015–03/03/2019; teste iniciado em 13/04/2018, com 325 dias; previsão de retorno um dia à frente por janela móvel de 648 dias.

**Ativos analisados:** Bitcoin, Ethereum e Litecoin.

**Métrica:** taxa de acerto, MAE, RMSE, retorno anual, retorno após custo *round-trip* de 0,5%, Sharpe anualizado, CVaR diário a 1% e *maximum drawdown*.

**Resultado quantitativo:**

- no teste, taxa de acerto de classificação: RF para ETH 60,00%; SVM para ETH 56,92%; SVM para LTC 55,69%; modelo linear para BTC 46,15%;
- Ensemble 5: retorno anual após custos de 9,622% para ETH e 5,730% para LTC; Sharpe anualizado de 80,17% e 91,35%, respectivamente;
- para ETH, Ensemble 5 teve CVaR a 1% de 12,63% e drawdown máximo de 28,92%, contra 17,81% e 89,67% no *buy-and-hold*;
- para LTC, Ensemble 5 teve CVaR de 6,921% e drawdown de 23,46%, contra 14,45% e 86,80% no *buy-and-hold*;
- mesmo a melhor família de estratégias manteve risco de cauda relevante; considerando as estratégias de ensemble, o artigo resume CVaR entre 3,88% e 13,40% e drawdown entre 11,15% e 48,06%.

**Trecho original relevante:** “the forecasting accuracy is quite different across models and cryptocurrencies”.

**Interpretação correta:** os ensembles geraram resultados economicamente positivos para ETH e LTC depois de custos em uma amostra de baixa, mas acurácia isolada não foi uniformemente alta e o risco de cauda permaneceu material.

**O que NÃO permite afirmar:** não prova superioridade geral de ML; o melhor modelo depende do ativo e da métrica; Sharpe e retorno não eliminam drawdowns; não se deve comparar diretamente esses números com outro artigo sem harmonizar amostra e estratégia.

**Onde encaixa na subseção atual:** nos parágrafos sobre previsibilidade e desempenho de ML, acrescentando custos e risco ao lado da acurácia.

**Sugestão de uso:** tabela compacta ou números no texto; a Tabela 7 pode ser adaptada sob CC BY 4.0, mas uma versão reduzida é mais legível.

### Q10 — Heterogeneidade de volatilidade e caudas entre 16 criptomoedas

**Classificação:** COMPLEMENTAR

**Tema:** volatilidade interna; não normalidade; risco de cauda.

**Fonte:** Fakhfekh e Jeribi (2020), *Volatility dynamics of crypto-currencies’ returns: Evidence from asymmetric and long memory GARCH models*.

**BibTeX key:** `fakhfekh2020volatility`.

**PDF:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/2 parte intro - Cripto/Volatility dynamics of crypto-currencies’ returns.pdf`

**Página:** PDF 5–6; páginas impressas 5–6.

**Tabela/Figura:** Tabela 1 — estatísticas descritivas; Figura 1 — evolução dos retornos.

**Amostra/período:** 07/08/2017–12/12/2018, frequência diária, 366 observações.

**Ativos analisados:** Bitcoin e 15 altcoins, incluindo Ethereum, Ripple, IOTA, NEO, QTUM, Stellar e outras.

**Métrica:** desvio-padrão, assimetria, curtose, Jarque–Bera e testes de memória longa.

**Resultado quantitativo:**

- desvio-padrão diário em escala decimal: Bitcoin 0,0551; Ethereum 0,0695; Ripple 0,0913; IOTA 0,1027; NEO 0,1053; Stellar 0,1070; QTUM 0,1183;
- curtose: Bitcoin 5,406; Ripple 12,46; QTUM 17,96; todos os 16 ativos apresentaram curtose acima de 3;
- Jarque–Bera foi significativo a 1% para todas as séries da tabela.

**Trecho original relevante:** “The kurtosis high associated values indicate [...] extreme values on the tails.”

**Interpretação correta:** a volatilidade é elevada, mas heterogênea entre criptoativos, e a amostra mostra caudas pesadas generalizadas.

**O que NÃO permite afirmar:** não compara criptoativos a classes tradicionais; não mede correlação entre moedas; a amostra é curta e coincide com um episódio específico do mercado.

**Onde encaixa na subseção atual:** no primeiro ou no último bloco de ressalvas, para mostrar que “cripto” não é uma classe homogênea.

**Sugestão de uso:** nota complementar ou gráfico próprio de barras para um subconjunto de ativos; evitar reproduzir a tabela inteira.

## 3. Figuras, tabelas e visual aids candidatas

### V1 — Heatmap de correlações no período completo

**Fonte:** Goodell e Goutte (2021), *Diversifying equity with cryptocurrencies during COVID-19*.

**Página:** PDF/impressa 4.

**Figura/Tabela:** Figura 2.

**Caption original:** “Heatmap of the return series for the full period.”

**O que mostra:** matriz numérica de correlações entre BTC, LTC, ETH, Tether, sete índices acionários e VIX.

**Período:** 28/02/2019–09/02/2021.

**Ativos:** quatro criptomoedas, sete índices acionários e VIX.

**Por que agrega ao TCC:** torna simultaneamente visíveis a forte correlação interna BTC–LTC–ETH, a correlação positiva mais baixa com ações e a posição distinta do Tether.

**Qual argumento sustenta:** correlação interna do mercado cripto e diversificação imperfeita em relação a mercados tradicionais.

**Forma recomendada de uso:** adaptar ou recriar; idealmente usar em painel com V2. A reprodução direta exigiria verificar permissão, pois não há licença aberta explícita.

**Licença explícita no artigo:** não identificado; o PDF informa “All rights reserved”.

**Arquivo extraído:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/FIGURAS_CANDIDATAS_CRIPTO/goodell2021_fig2_heatmap_periodo_completo.png`

### V2 — Heatmap de correlações durante a pandemia

**Fonte:** Goodell e Goutte (2021), mesmo artigo de V1.

**Página:** PDF/impressa 5.

**Figura/Tabela:** Figura 3.

**Caption original:** “Heatmap of the return series for pandemic period.”

**O que mostra:** matriz numérica para o subperíodo da COVID-19, permitindo comparar as correlações de BTC/LTC/ETH e o comportamento heterogêneo do Tether.

**Período:** março de 2020–fevereiro de 2021.

**Ativos:** mesmos de V1.

**Por que agrega ao TCC:** fornece contraste visual direto com V1 e evita a afirmação excessiva de que o Tether foi negativamente correlacionado com todos os mercados acionários.

**Qual argumento sustenta:** correlações de criptoativos mudam em crises; o papel de *safe haven* depende do índice observado.

**Forma recomendada de uso:** adaptar ou recriar em conjunto com V1; não reproduzir automaticamente.

**Licença explícita no artigo:** não identificado; o PDF informa “All rights reserved”.

**Arquivo extraído:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/FIGURAS_CANDIDATAS_CRIPTO/goodell2021_fig3_heatmap_covid.png`

### V3 — Correlações dinâmicas de ouro e Bitcoin com bolsas chinesas

**Fonte:** Corbet, Larkin e Lucey (2020), *The contagion effects of the COVID-19 pandemic: Evidence from gold and cryptocurrencies*.

**Página:** PDF/impressa 6.

**Figura/Tabela:** Figura 2.

**Caption original:** “Dynamic correlations between denoted company and the Shanghai & Shenzhen Stock Exchanges”.

**O que mostra:** dois painéis com correlações condicionais dinâmicas de Shanghai/Shenzhen com ouro e Bitcoin, destacando o período posterior a 31/12/2019.

**Período:** gráfico concentrado aproximadamente entre outubro de 2019 e março de 2020; estimação usa a amostra de 11/03/2019–10/03/2020.

**Ativos:** Bitcoin, ouro, Shanghai e Shenzhen.

**Por que agrega ao TCC:** visualiza a mudança de regime que a Tabela 3 quantifica, sem depender de valores estimados visualmente.

**Qual argumento sustenta:** elevação temporária da correlação em crise e erosão do benefício de diversificação.

**Forma recomendada de uso:** reproduzir ou adaptar com atribuição e indicação de que a área sombreada começa em 31/12/2019.

**Licença explícita no artigo:** sim — CC BY 4.0.

**Arquivo extraído:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/FIGURAS_CANDIDATAS_CRIPTO/corbet2020_fig2_correlacoes_dinamicas_covid.jpg`

### V4 — Desempenho e risco das estratégias de ML

**Fonte:** Sebastião e Godinho (2021), *Forecasting and trading cryptocurrencies with machine learning under changing market conditions*.

**Página:** PDF/impressa 25.

**Figura/Tabela:** Tabela 7.

**Caption original:** “Performance of the trading strategies on the test sample, based on model assembling”.

**O que mostra:** retorno, retorno após custos, Sharpe, CVaR e drawdown de *buy-and-hold* e Ensembles 4, 5 e 6 para BTC, ETH e LTC.

**Período:** teste com 325 dias, iniciado em 13/04/2018 e contido na amostra encerrada em 03/03/2019.

**Ativos:** BTC, ETH e LTC.

**Por que agrega ao TCC:** reúne desempenho e risco na mesma evidência e impede que acurácia preditiva seja confundida com rentabilidade ou segurança.

**Qual argumento sustenta:** ML pode produzir ganho após custos em alguns ativos, mas ainda envolve CVaR e drawdowns relevantes.

**Forma recomendada de uso:** adaptar para uma tabela menor com somente retorno após custos, Sharpe, CVaR e drawdown; a reprodução integral é densa demais para a subseção.

**Licença explícita no artigo:** sim — CC BY 4.0.

**Arquivo extraído:** `/mnt/SSD_SEC/GIT/TCC/REPOSITORIO/TRABALHOS_REFERENCIA/FIGURAS_CANDIDATAS_CRIPTO/sebastiao2021_table7_desempenho_ml.png`

## 4. Melhor conjunto para realmente inserir no TCC

O conjunto mais equilibrado contém sete evidências e três recursos visuais:

1. **Q1 ou Q2, não ambas em detalhe:** usar uma comparação direta de volatilidade. Q1 cobre mais classes; Q2 tem unidade percentual mais clara e inclui ETH. Q2 é preferível se a prioridade for precisão de unidade; Q1 é preferível se a prioridade for amplitude de classes.
2. **Q3:** acrescenta coeficientes claros de dependência baixa com ativos tradicionais e maior dependência BTC–ETH.
3. **Q5:** quantifica o benefício de diversificação dentro do mercado cripto e traz Sharpe/CEQ fora da amostra com custos.
4. **Q6:** mostra que a diversificação pode se deteriorar em crises, com correlações do Bitcoin saltando de valores próximos de zero para 0,28–0,47.
5. **Q7:** refina a narrativa sobre Tether; apresenta evidência favorável para alguns índices, mas impede uma generalização incorreta.
6. **Q8:** fornece uma medida concreta de perdas extremas e demonstra que a proteção de stablecoins é condicional.
7. **Q9:** oferece evidência de ML economicamente interpretável depois de custos, acompanhada de CVaR e drawdown.

Os três recursos visuais prioritários são:

- **V1 + V2 como um único painel comparativo:** a mudança das matrizes de correlação é mais informativa que uma lista extensa de coeficientes; recomenda-se recriar/adaptar, não reproduzir automaticamente.
- **V3:** melhor figura pronta para a discussão de crise, com licença CC BY 4.0 e forte ligação com Q6.
- **V4 em versão reduzida:** melhor recurso para ML porque equilibra retorno, custo e risco; a tabela completa é excessiva para a subseção.

Esse conjunto cobre volatilidade, correlação/diversificação, crise, risco de cauda/*safe haven* e ML sem transformar a subseção em catálogo estatístico. Q4 e Q10 podem permanecer como reserva para nota ou discussão adicional.

## 5. Possíveis gráficos próprios

### G1 — Volatilidade diária: cripto versus ativos tradicionais

**Fonte dos dados:** Charfeddine et al. (2020), Tabela 2, Amostra II.

**Valores:** BTC 1,723%; ETH 2,983%; S&P 500 0,239%; ouro 0,265%; petróleo 0,744%.

**Unidades:** desvio-padrão percentual de retornos logarítmicos diários.

**Período:** 01/09/2015–01/10/2018.

**Formato recomendado:** barras horizontais.

**Título sugerido:** “Volatilidade diária de criptoativos e ativos tradicionais, 2015–2018”.

**Observação sobre comparabilidade:** todos os valores vêm da mesma amostra e metodologia; não anualizar apenas alguns ativos.

### G2 — Dependência estática entre criptoativos e ativos tradicionais

**Fonte dos dados:** Charfeddine et al. (2020), Tabela 4.

**Valores:** Pearson: BTC–S&P 0,010; BTC–ouro 0,017; BTC–petróleo −0,008; BTC–ETH 0,129; ETH–S&P −0,001; ETH–ouro −0,049; ETH–petróleo −0,064.

**Unidades:** coeficiente de correlação de Pearson.

**Período:** pares de BTC desde 18/07/2010; pares com ETH desde 01/09/2015; fim em 01/10/2018.

**Formato recomendado:** heatmap simples com indicação de significância apenas no par BTC–ETH.

**Título sugerido:** “Dependência estática entre criptomoedas e ativos convencionais”.

**Observação sobre comparabilidade:** deixar visível que os pares com ETH têm amostra mais curta.

### G3 — Correlações do Bitcoin antes e depois do início da COVID-19

**Fonte dos dados:** Corbet et al. (2020), Tabela 3.

**Valores:** Shanghai 0,0188 → 0,3436; Shenzhen 0,0209 → 0,3857; DJIA 0,0361 → 0,4299; WTI −0,0071 → 0,2792; ouro 0,0392 → 0,4688.

**Unidades:** coeficiente de correlação.

**Período:** 11/03/2019–10/03/2020; corte em 31/12/2019.

**Formato recomendado:** *slope chart* ou barras agrupadas antes/depois.

**Título sugerido:** “Mudança das correlações do Bitcoin no início da COVID-19”.

**Observação sobre comparabilidade:** o “depois” contém somente 1.122 observações horárias e não cobre toda a pandemia.

### G4 — Desempenho ajustado ao risco de carteiras somente de criptoativos

**Fonte dos dados:** Brauneis e Mestel (2019), Tabela 3.

**Valores:** Sharpe médio 1/N 0,1865; otimizado 0,1301; ativos constituintes 0,0928; CRIX 0,1596. CEQ médio 0,0073; 0,0047; −0,0336, respectivamente.

**Unidades:** Sharpe adimensional; CEQ na escala de retorno do artigo.

**Período:** 2015–2017.

**Formato recomendado:** dois painéis de barras, um para Sharpe e outro para CEQ.

**Título sugerido:** “Diversificação ingênua, otimização e ativos isolados no mercado cripto”.

**Observação sobre comparabilidade:** `M` difere entre grupos; as barras são médias de conjuntos de estratégias/ativos, não uma única carteira por categoria.

### G5 — Redução de risco extremo proporcionada pelo Tether

**Fonte dos dados:** Wang et al. (2020), Tabelas 7–9, Carteira 1.

**Valores no nível de 99,9%:** BTC: VaR 0,139, ES 0,149; LTC: 0,257, 0,355; XRP: 0,295, 0,404.

**Unidades:** diferença de VaR/ES na escala de retorno do artigo.

**Período:** 06/03/2015–20/03/2019.

**Formato recomendado:** barras agrupadas VaR versus ES para BTC, LTC e XRP.

**Título sugerido:** “Redução de risco extremo em carteiras cripto–Tether”.

**Observação sobre comparabilidade:** usar apenas a Carteira 1 e o mesmo nível de confiança; não misturar com stablecoins atreladas ao ouro, que usam amostra mais curta.

## 6. Evidências rejeitadas ou problemáticas

- **Baur e Hoang (2021), afirmação de que o Bitcoin seria oito vezes mais volátil que ações:** a frase da introdução atribui o número a Harvey; é evidência de segunda mão, não resultado estimado pelo artigo. O próprio estudo foi aproveitável para stablecoins, mas esse número não deve ser citado como achado dos autores.
- **“Bitcoin é dezenas de vezes mais volátil que ativos tradicionais”:** nenhuma tabela diretamente validada nesta execução sustenta essa formulação como regra. As comparações dentro de uma mesma amostra ficaram aproximadamente entre 6 e 9 vezes para Bitcoin versus índices acionários e chegaram a 12,48 vezes para ETH versus S&P 500. A frase precisa ser qualificada ou substituída por uma amostra concreta.
- **Corbet et al. (2020) como evidência de “amplificação do contágio sistêmico”:** o artigo mostra aumento de correlação dinâmica, mas o coeficiente de Bitcoin nos modelos GARCH das bolsas chinesas não foi significativo. A formulação causal/sistêmica excede a evidência validada.
- **Goodell e Goutte (2021), Tether negativamente correlacionado com ações em geral:** a Figura 3 mostra correlação negativa com IBEX, DAX, CAC e S&P 500, mas positiva com Swiss, FTSE 100 e EURO STOXX 50. Deve-se nomear os índices ou escrever que o efeito foi heterogêneo.
- **Goodell e Goutte, Tabelas 4 e 5:** são matrizes de pesos de uma rede neural, não matrizes de correlação. Não devem ser apresentadas como coeficientes de correlação; para isso, usar as Figuras 2 e 3.
- **Park e Yang (2023), desvios-padrão de preços:** tabelas em nível de preço não são comparáveis entre ativos e não devem ser usadas como medida de volatilidade relativa. Os resultados de acurácia e negociação são válidos, mas foram deixados fora do conjunto principal porque Q9 já oferece retorno após custos, CVaR e drawdown em um desenho mais completo.
- **Fakhfekh e Jeribi (2020) para comparação com ações ou títulos:** a Tabela 1 contém apenas criptomoedas. O artigo menciona ativos convencionais na revisão, mas isso não é resultado empírico próprio; por isso Q10 foi classificada apenas como complementar.
- **Umar et al. (2021) e comportamento cíclico de *safe haven*:** o material inspecionado é baseado em causalidade por wavelets e transições de regime, mas não foi selecionado um coeficiente simples com período e interpretação inequívoca. Mantém-se como suporte qualitativo, não como número pronto.
- **Fang et al. (2022) e atrasos de vários dias por escalabilidade:** a passagem localizada no texto é contextual e depende de episódio/fonte externa; não foi validado um dado operacional primário com amostra e método. Não usar como evidência quantitativa.
- **Figuras puramente ilustrativas de preços ou capitalização:** não foram selecionadas quando não forneciam métrica comparável, período claramente delimitado ou relação direta com as afirmações da subseção.
- **Preprints e duplicatas de versões não publicadas:** não foram usados no conjunto final. Quando havia artigo publicado no repositório, foi priorizada a versão publicada.

