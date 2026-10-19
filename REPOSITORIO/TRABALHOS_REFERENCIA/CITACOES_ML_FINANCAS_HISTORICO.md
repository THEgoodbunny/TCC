# Machine Learning em finanças — levantamento histórico e bibliográfico

## Parte I — Panorama e linha do tempo

Os intervalos abaixo seguem referências identificáveis no acervo. São pontos de apoio documentais, não uma periodização universal nem uma evolução linear em que cada técnica substitui a anterior.

| Período/marco                   | Evolução técnica e problema financeiro                                                    | Aplicação/mudança metodológica                                                              | Evidência disponível e localização                                                           | Lacuna/alcance                                                                                                                       |
| -------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| 1966, 1968 e 1980                | Indicadores contábeis, análise discriminante e Logit para antecipar dificuldades/falência | Formalizar alertas a partir de características observadas das empresas                         | **F1, Sun et al. (2020)**, PDF 1–2 e referências 1–3, PDF 16: Beaver, Altman e Ohlson   | Antecedentes estatísticos, não origem do ML; originais ausentes                                                                    |
| 1985 e 1990                      | Particionamento recursivo/árvores e redes neurais na classificação de empresas            | Aprender relações entre atributos financeiros e situação de dificuldade                     | **F1**, PDF 2, referências 4–5, PDF 16: Frydman, Altman e Kao; Odom e Sharda             | Aplicações antigas documentadas secundariamente; não afirmar pioneirismo absoluto nem repetir taxas de acerto não verificadas    |
| 1996 e 1998                      | Redes probabilísticas para movimentos de preços/níveis de retorno                         | Formular previsão como classificação ligada a comprar, manter ou vender                      | **F3, Ferreira et al. (2021)**, PDF 10, referências 72 e 45, PDF 19                       | Originais de Schierholt–Dagli e Kim–Chun ausentes; datas são dos estudos, não da invenção das redes                            |
| 1998 e 2001                      | RL recorrente aplicado a sistemas de negociação e portfólios                              | Relacionar aprendizado diretamente ao desempenho de decisões sequenciais                       | **F6, Jiang et al. (2024)**, PDF 2–3 e referências, PDF 14: Moody et al.; Moody–Saffell | Fontes primárias ainda não localizadas; não datar o nascimento de RL financeiro em 2024                                           |
| 2004, 2005 e 2007                | Mineração de notícias; SVM direcional; redes combinadas a modelos de volatilidade         | Ampliar fontes de informação, alvos e combinações com econometria                           | **F3**, PDF 10 e 12–13; referências 55, 36 e 38, PDF 19: Mittermayer, Huang et al., Roh  | Evidência secundária; não usar resultados numéricos desses originais como verificados                                            |
| 2008; 2010–2019                 | SVM para condição financeira; ensembles, reamostragem e atualização temporal             | Tratar não linearidade, classes raras e mudança da relação entre indicadores e dificuldades | **F1**, PDF 2–3 e referências 6, 8–19 e 23, PDF 16                                      | Trabalhos citados de crédito e falência não equivalem todos à concessão de crédito a pessoas físicas                          |
| 2011–2015                       | Sentimento em redes sociais e modelos que combinam texto e preços                           | Transformar manifestações textuais em atributos para previsão de movimentos                  | **F3**, PDF 14, referências 9 e 60, PDF 18–19: Bollen et al.; Nguyen et al.              | Medidas de sentimento/associação não comprovam causalidade nem lucro realizável                                                  |
| 2020                             | Ensemble dinâmico AdaBoost–SVM e SMOTE; LSTM com pré-seleção de ações                 | Problemas coexistentes: alerta empresarial e seleção antes da alocação                      | **F1** (Sun) e **F2** (Wang), originais lidos                                        | Sun usa situações de 2002–2016; Wang, séries de 1994–2019. Ambos disponíveis online em 2019, publicados em volumes de 2020     |
| 2021                             | RF/SVR/DL versus ARIMA; AdaBoost sobre LSTM/GRU                                              | Prever retornos para carteiras e preços de uma commodity; confrontar métricas e custos        | **F4** (Ma) e **F5** (Busari–Lim), originais lidos                                  | ARIMA supera alguns modelos de ML em Ma; vantagem do híbrido em petróleo não demonstra vantagem universal nem financeira líquida |
| 2020–2024, sintetizados em 2025 | Redes recorrentes, híbridos CNN–LSTM e múltiplas fontes de dados                          | Previsão de ações, índices, câmbio, commodities, títulos, cripto e volatilidade           | **F7, Giantsidi–Tarantola (2025)**, PDF 1–3, 29–30 e 37–38                             | Revisão de 187 estudos, não experimento único nem levantamento de adoção operacional                                            |
| 2024                             | DRL/TD3 com recompensa que incorpora risco e custos                                          | Aprender ações de compra/manutenção/venda que alteram a carteira                            | **F6**, método PDF 3–6, teste PDF 7–13                                                  | Backtest em ações; melhor Sharpe no cenário apresentado convive com maior volatilidade que os benchmarks tradicionais             |

**Leitura histórica recomendada:** começar pela necessidade de classificar risco e prever variáveis financeiras; mostrar as tentativas de aprendizado supervisionado e a diversidade de alvos; apresentar a ampliação das fontes, ensembles e memória temporal; encerrar distinguindo previsão, seleção, otimização e políticas. RL possui antecedentes antigos e se desenvolve em paralelo: não é simplesmente a etapa que “veio depois” de todas as redes profundas.

### Seleção e prioridade

Escala qualitativa: alta/média/baixa; qualidade é a adequação da evidência à afirmação proposta, não um ranking de periódicos.

| ID | Estudo                       | Relevância histórica                          | Didática / abrangência                                | Qualidade da evidência para este uso                                       | Redundância com outras seções                             | Prioridade                             |
| -- | ---------------------------- | ----------------------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------ | -------------------------------------- |
| F1 | Sun et al. (2020)            | Alta, retrospectiva desde 1966                  | Alta; risco empresarial, desbalanceamento e adaptação | Primária para o experimento de 2020; secundária para os antecedentes      | Baixa                                                        | Essencial para a abertura              |
| F2 | Wang et al. (2020)           | Média; exemplo contemporâneo, não pioneiro   | Alta; prever → selecionar → alocar                    | Primária, com dados/método/resultados e ressalvas                         | Alta, já usado na Seção 3                                 | Ponte final, com brevidade             |
| F3 | Ferreira et al. (2021)       | Alta; mapeamento 1995–2019 e referências      | Alta; previsão, sentimento e carteiras                 | Primária bibliométrica; secundária para resultados dos artigos revisados | Média                                                       | Essencial para a evolução            |
| F4 | Ma et al. (2021)             | Média; coexistência de métodos               | Alta; parâmetros, custos e resultados negativos        | Primária, incluindo tabelas e conclusão                                   | Alta                                                         | Essencial como contraponto e ponte     |
| F5 | Busari e Lim (2021)          | Média; exemplo de ensemble recorrente          | Alta; amplia o domínio além de ações/cripto         | Primária para previsão; sem teste de investimento                         | Baixa para aplicações; média para fundamentos de AdaBoost | Complementar recomendado               |
| F6 | Jiang et al. (2024)          | Média; antecedentes de RL são secundários    | Alta; política versus previsão                        | Primária para TD3 e backtest; secundária para Moody                       | Média/alta                                                  | Ponte final e distinção conceitual   |
| F7 | Giantsidi e Tarantola (2025) | Alta para o recorte recente, baixa para origens | Alta; diversos ativos, volatilidade e limites           | Primária para a revisão; secundária para estudos nela citados            | Média                                                       | Essencial para síntese contemporânea |

## Parte II — Fichamento individual dos estudos

### F1 — Sun et al. (2020): do diagnóstico estatístico ao aprendizado dinâmico de dificuldades financeiras

**Identificação**

- **Título:** *Class-imbalanced dynamic financial distress prediction based on Adaboost-SVM ensemble combined with SMOTE and time weighting*.
- **Autores:** Jie Sun; Hui Li; Hamido Fujita; Binbin Fu; Wenguo Ai.
- **Publicação:** *Information Fusion*, 54 (2020), 128–144. Disponível online em 23/07/2019; manter **2020** como ano do volume.
- **DOI:** `10.1016/j.inffus.2019.07.006`, verificado no PDF 1.
- **PDF:** `TRABALHOS_REFERENCIA/3 parte intro - machine learning/Class-imbalanced dynamic financial distress prediction based on Adaboost-SVM ensemble combined with SMOTE and time weighting.pdf`.
- **BibTeX:** nenhuma entrada correspondente no único `.bib` disponível; não foi criada chave.

**Caracterização e leitura**

- **Contexto e problema:** antecipar deterioração empresarial para apoiar gestão de risco. A introdução retoma modelos estáticos de Beaver, Altman e Ohlson, depois árvores, redes e SVM. A contribuição própria procura enfrentar simultaneamente mudança de conceito e menor frequência das empresas em dificuldade, em vez de apenas trocar o classificador.
- **Referências tradicionais:** análise univariada, discriminante multivariada e Logit são antecedentes da revisão, não comparadores experimentais de todos os resultados de 2020. A comparação principal do experimento é entre ADASVM-TW, integração simples de SMOTE e integração de SMOTE nas iterações do ensemble.
- **ML:** SVMs combinadas por AdaBoost; ponderação por recência/erro; SMOTE para sintetizar exemplos da classe minoritária. A integração proposta diferencia exemplos novos/antigos e difíceis/fáceis.
- **Dados:** companhias de Shanghai e Shenzhen; anos de referência 2002–2016; 438 empresas em dificuldade e 2.190 normais, em pareamento 1:5; 2.628 empresas iniciais. Indicadores CSMAR do exercício T−2. De 55 indicadores contábeis iniciais, 19 são selecionados, abrangendo rentabilidade, solvência, estrutura, crescimento e outras dimensões. Dados e definição do desfecho: PDF 9, impressa 136.
- **Alvo:** dificuldade definida por dois anos consecutivos de lucro líquido negativo ou patrimônio líquido inferior ao capital registrado. Não é uma amostra de transações fraudulentas nem necessariamente um evento de inadimplência contratual.
- **Decisão:** classificação para alerta financeiro e revisão de controles. A utilidade gerencial é motivação do artigo; não há experimento mostrando redução causal de falências ou de perdas de um banco.
- **Resultados próprios:** 50 repetições; as integrações SMOTE melhoram identificação da classe minoritária. A integração embutida tem melhor combinação de medidas que a simples. O ganho exige sacrificar parte da identificação das empresas normais e da acurácia global, PDF 15, impressa 142. Não escrever apenas “melhorou a acurácia”.
- **Ressalvas dos autores:** mudança da distribuição torna modelos passados inadequados; desbalanceamento pode afetar especialmente os classificadores de IA; a integração simples pode gerar exemplos ruidosos sob mudança de conceito. A conclusão propõe aplicações futuras a outros problemas, não as considera já demonstradas.
- **Cautela adicional desta leitura:** amostra pareada e desfecho específico limitam extrapolação a carteiras reais de crédito. O pareamento usa situação de empresas normais em anos anteriores e posteriores ao ano de referência; seleção/preprocessamento devem ser auditados antes de reutilizar o protocolo prospectivamente. Esta ressalva é nossa, não uma autocrítica explicitamente formulada pelos autores.

**Relevância para o TCC**

É a melhor abertura histórica localizada: mostra que ML financeiro não surgiu apenas para prever cotações. Permite explicar classificação supervisionada e o custo assimétrico dos erros. A afirmação adequada é que a literatura passou a investigar modelos capazes de aprender relações não lineares e de lidar com classes raras/mudança temporal; não que estatística tradicional se tornou inútil. Prioridade alta, sem redundância substancial com as seções de cripto/MV.

**Citações diretas verificadas**

**F1.1 — PDF 2; página impressa 129.**

> In the early stage of FDP research, Beaver [1] proposes the single variable discriminant model, Altman [2] puts forward the multivariate discriminant analysis (MDA) model, and Ohlson [3] applies the logistic regression (Logit) model. These are the representative statistical FDP models and they are still widely applied today.

- **Contexto:** Seção 2.1, revisão da literatura.
- **O que comprova / ressalva:** Identifica modelos estatísticos antecedentes. As datas de 1966/1968/1980 vêm das referências 1–3, PDF 16; não são aplicações de ML.

**F1.2 — PDF 2; página impressa 129.**

> Then, with the development of artificial intelligence methods, Frydman et al. [4] construct a decision tree FDP model, and Odom and Sharda [5] construct an NNs FDP model, and they are early attempts of applying artificial intelligence methods to FDP.

- **Contexto:** Seção 2.1, sequência dos antecedentes.
- **O que comprova / ressalva:** Relata árvores e redes como tentativas antigas. A referência 4 é de 1985 e a 5 de 1990, PDF 16. Evidência secundária: não comprova o desempenho dos originais nem prioridade absoluta.

**F1.3 — PDF 15; página impressa 142.**

> In summary, compared with the ADASVM-TW model, the S-SMOTEADASVM-TW model significantly improves TPrate and G value at the expense of significantly sacrificing Acc, TNrate and F value, and the E-SMOTE-ADASVM-TW model significantly improves TPrate, F value and G value at the expense of significantly sacrificing Acc and TNrate.

- **Contexto:** Discussão dos resultados, após comparação das medidas.
- **O que comprova / ressalva:** O ganho de identificação da classe minoritária e de medidas agregadas envolve redução de acurácia global e de reconhecimento da classe normal; não houve melhora simultânea em tudo.

### F2 — Wang et al. (2020): previsão e pré-seleção antes da alocação

**Identificação**

- **Título:** *Portfolio formation with preselection using deep learning from long-term financial data*.
- **Autores:** Wuyu Wang; Weizi Li; Ning Zhang; Kecheng Liu.
- **Publicação:** *Expert Systems with Applications*, 143 (2020), artigo 113042; online em 17/10/2019.
- **DOI:** `10.1016/j.eswa.2019.113042`, PDF 1. **Diverge do DOI terminado em `112467` registrado no fichamento canônico; o original local sustenta `113042`.** O canônico foi preservado.
- **PDF:** `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Portfolio formation with preselection using deep learning from long-term financial data.pdf`.
- **BibTeX:** entrada ausente no `.bib` disponível. `wang2020portfolio` aparece nos fichamentos anteriores, mas não teve existência confirmada em arquivo bibliográfico.

**Caracterização e leitura**

- **Problema e motivação:** escolher ativos antes de calcular seus pesos, explorando dependências temporais dos retornos. O desenho preserva MV como etapa decisória; a rede não é descrita como substituta automática de toda a teoria de portfólio.
- **Comparadores:** SVM, random forest, DNN e ARIMA na previsão; LSTM/SVM/seleção aleatória combinados com MV ou 1/N na formação de carteiras. ARIMA é o comparador estatístico, 1/N uma regra de alocação.
- **Dados:** março de 1994 a março de 2019. O corpo metodológico informa **21 ações escolhidas do FTSE 100**, não 100 ações efetivamente usadas. Séries diárias de abertura, fechamento, máxima, mínima e volume; cinco indicadores técnicos e quinze observações defasadas de retorno selecionados como entradas, PDF 4–5. São descritos 22 conjuntos de treino/teste sobrepostos, PDF 15.
- **Saída e decisão:** previsão de retorno do período seguinte; ordenação decrescente; pré-seleção dos ativos; solução MV para determinar alocação. A data inicial dos dados não é evidência de aplicação de LSTM em 1994.
- **Resultados:** os autores reportam vantagem do LSTM+MV em várias avaliações. A análise de Sharpe por triênios é mais informativa que uma frase universal: supera os comparadores em seis de oito triênios sem custos, cinco com o custo rotulado de 0,05 bps e quatro com 0,1 bps, PDF 14. Conservar a unidade que o artigo imprime; não converter silenciosamente bps em porcentagem.
- **Limitações dos autores:** uso de variáveis técnicas/defasadas, ausência de fatores externos como política e juros, um único país; não garantem adequação a outros mercados, PDF 16. O desempenho depende do período e das hipóteses de custo/capital.
- **Cautela desta leitura:** universo retrospectivo e subconjunto de ações exigem atenção à seleção/sobrevivência; não apresentar 25 anos de dados como garantia automática de validação sem viés.

**Relevância para o TCC**

Usar apenas no encerramento para separar “quais ativos” de “quanto investir”. É também uma evidência de que a evolução das aplicações inclui integrar novos preditores a métodos financeiros existentes. A ficha é detalhada para consulta; a futura subseção pode aproveitar somente uma ou duas afirmações, pois o estudo já pertence à revisão específica de ML–MV.

**Citações diretas verificadas**

**F2.1 — PDF 3; página impressa 3.**

> Actually, the high accuracy of prediction does not represent the optimal investment strategy.

- **Contexto:** Discussão que antecede a metodologia.
- **O que comprova / ressalva:** Os próprios autores distinguem precisão de previsão e decisão ótima; a frase não quantifica o descolamento em todos os mercados.

**F2.2 — PDF 4; página impressa 4.**

> Hence, this paper randomly chooses twenty-one stocks from FTSE 100 as sample data, which is sufficiently large for the asset preselection before forming the portfolio for individual investors.

- **Contexto:** Seção 3.1, dados.
- **O que comprova / ressalva:** Confirma o subconjunto de 21 ações; FTSE 100 é o universo de referência, não o tamanho efetivo da amostra.

**F2.3 — PDF 5; página impressa 5.**

> In the first stage, LSTM method is applied to predict the return of the sample stocks in the next period. All the predicted results will be sorted in descending order and the top stocks will enter into the next phase.

- **Contexto:** Seção 3.4, arquitetura do método.
- **O que comprova / ressalva:** Distingue previsão, ranking e pré-seleção. A fase seguinte de MV, descrita no mesmo contexto, define a alocação.

**F2.4 — PDF 16; página impressa 16.**

> In addition, the study uses the asset data in only one country of the UK. Due to the different political environment and economic backgrounds, we cannot ensure whether the proposed method is suitable for the stock markets from other countries.

- **Contexto:** Seção 5.4, limitações.
- **O que comprova / ressalva:** Os autores limitam explicitamente a generalização geográfica. Não extrapolar os resultados a criptoativos.

### F3 — Ferreira, Gandomi e Cardoso (2021): mapa retrospectivo do mercado acionário

**Identificação**

- **Título:** *Artificial Intelligence Applied to Stock Market Trading: A Review*.
- **Autores, conforme assinatura do PDF:** Fernando G. D. C. Ferreira; Amir H. Gandomi; Rodrigo T. N. Cardoso.
- **Publicação:** *IEEE Access*, 9 (2021), 30898–30917.
- **DOI:** `10.1109/ACCESS.2021.3058133`, PDF 1.
- **PDF:** `TRABALHOS_REFERENCIA/Artificial_Intelligence_Applied_to_Stock_Market_Trading_A_Review.pdf`.
- **BibTeX:** entrada ausente no `.bib` disponível; `ferreira2021artificial` está mencionada em fichamento prévio, sem confirmação bibliográfica local.

**Caracterização e leitura**

- **Tipo:** revisão e análise bibliométrica, não backtest próprio. Busca Scopus em 27/05/2020: 2.326 documentos de 1995–2019; a discussão incorpora também exemplos recentes. Não confundir o intervalo do levantamento com a totalidade das datas presentes nas referências.
- **Abrangência:** otimização de portfólios, previsão acionária, sentimento financeiro e combinações. A evolução de métodos computacionais de otimização inclui heurísticas que não devem ser contabilizadas automaticamente como ML.
- **Motivação:** reconhecer padrões, processar informação e apoiar decisões de investimento; a apresentação da relação com popularização dos computadores é interpretação histórica dos revisores, não demonstração causal nem data universal de início das finanças computacionais.
- **Entradas e alvos:** preços, retornos, volume, indicadores técnicos/fundamentalistas; notícias e mensagens. Saídas incluem preços, retornos, classes de tendência, volatilidade e regras de negociação. O fluxograma distingue preparação, treino, validação e teste, PDF 9; tabelas de entradas/saídas, PDF 12.
- **Evolução documentada secundariamente:** redes probabilísticas em 1996/1998; SVM para direção em 2005; híbridos NN–EWMA/GARCH/EGARCH em 2007; notícias em 2004/2009 e Twitter em 2011; DL em trabalhos posteriores. Datas conferidas nas referências, não inferidas do período das séries.
- **Resultados próprios da revisão:** crescimento de publicações no recorte e organização dos problemas/fontes de dados. Resultados de retorno e acurácia dos artigos resumidos são secundários e não são reproduzidos como testes verificados.
- **Limitações dos autores:** dificuldade de construir consulta abrangente, grande volume de documentos e foco nos mais citados; carência de comparações entre otimização complexa e modelos básicos; avaliação insuficiente da contribuição de cada atributo, PDF 17–18. Contagem bibliométrica não mede implantação industrial.
- **Leitura crítica:** a formulação simplificada da hipótese dos mercados eficientes no PDF 9 não deve ser copiada como definição completa. Tampouco usar uma previsão com erro menor para declarar refutação geral da eficiência de mercado.

**Relevância para o TCC**

É a principal espinha dorsal dos casos de mercado de capitais e da ampliação de preços para texto. Sustenta uma narrativa de diversificação de tarefas e fontes de informação, não uma competição em que toda novidade vence. Prioridade alta; citar como revisão quando recorrer aos episódios antigos.

**Citações diretas verificadas**

**F3.1 — PDF 2; página impressa 30899.**

> The query, performed on May 27, 2020, returned a total of 2326 documents, including journal and conference papers published between 1995 and 2019.

- **Contexto:** Seção II, descrição da coleta Scopus.
- **O que comprova / ressalva:** Confirma tamanho e janela do corpus, não data de surgimento de ML financeiro nem adoção por instituições.

**F3.2 — PDF 10; página impressa 30907.**

> Reference [72] proposed a Probabilistic Neural Network to predict financial prices movement trends using historical assets price series. Three different classes of trends were considered, each one indicating a different action: buying, keeping, and selling a given asset.

- **Contexto:** Seção IV, relato do estudo de Schierholt e Dagli (1996), ref. 72 no PDF 19.
- **O que comprova / ressalva:** Documenta secundariamente redes para classificar tendências ligadas a ações de negociação. Não comprova rentabilidade líquida nem que tenha sido o primeiro estudo.

**F3.3 — PDF 10; página impressa 30907.**

> Reference [38] presented three hybrid Artificial Neural Network time series models: NN-EWMA, NN-GARCH, and NN-EGARCH, which uses EWMA, GARCH, and EGARCH to determine input variables before applying the ANN to predict financial assets volatility.

- **Contexto:** Seção IV, relato de Roh (2007), ref. 38 no PDF 19.
- **O que comprova / ressalva:** Evidencia combinação de redes e econometria para outro alvo: volatilidade. Não atribuir o resultado empírico a Ferreira nem afirmar substituição de GARCH por ML.

**F3.4 — PDF 18; página impressa 30915.**

> The first works on sentiments analysis applied to financial investment employed the news as the object of study. Due to the popularization of social networks, a large number of comments about financial assets and their companies are available on the Internet, which is becoming the most used source of information in this type of analysis.

- **Contexto:** Seção VII.A, síntese sobre fontes textuais.
- **O que comprova / ressalva:** A revisão descreve a ampliação de notícias para redes sociais; a expressão first works é dos revisores e limitada à sua reconstrução, não prova prioridade histórica absoluta.

### F4 — Ma, Han e Wang (2021): previsão como parâmetro e avaliação após custos

**Identificação**

- **Título:** *Portfolio optimization with return prediction using deep learning and machine learning*.
- **Autores:** Yilin Ma; Ruizhu Han; Weizhong Wang.
- **Publicação:** *Expert Systems with Applications*, 165 (2021), artigo 113973; online em 05/09/2020.
- **DOI:** `10.1016/j.eswa.2020.113973`, PDF 1.
- **PDF:** `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Portfolio optimization with return prediction using deep learning and machine learning.pdf`.
- **BibTeX confirmado:** `ma2021portfolio`, em `TRABALHOS_REFERENCIA/ML_FINANCAS_EXPANSAO/referencias_ml_financas_expansao.bib`.

**Caracterização e leitura**

- **Problema:** combinar previsão/pré-seleção e otimização MV e Omega. A motivação contrapõe estimativas baseadas em médias históricas a informações preditivas. Isso não prova que substituir médias históricas por ML sempre melhora carteiras.
- **Métodos:** RF e SVR; LSTM, DMLP e CNN; ARIMA como benchmark preditivo. Previsões participam da pré-seleção e das formulações de carteira; não se verificou aqui previsão ML da matriz de covariâncias.
- **Dados:** constituintes do China Securities 100; após excluir ações sem histórico suficiente/suspensas por longo tempo, **49 ações**, PDF 6. Dados de 04/01/2007–31/12/2015; quatro anos de treino, um de validação e o seguinte de teste em janelas; avaliação de 05/01/2012–31/12/2015, 970 dias, PDF 12. Entradas são retornos históricos simples; não atribuir notícias ou fundamentos ao experimento.
- **Saída e decisão:** retornos previstos, seleção e parâmetros para modelos MVF/OF que produzem pesos. A decisão final depende da previsão e da regra de alocação; não é política RL.
- **Resultados:** RF tem os menores MAE/MSE, seguido por LSTM e DMLP na comparação reportada. **ARIMA supera CNN e SVR** na análise de erros, PDF 6. RF+MVF permanece a melhor variante MVF no protocolo; entre Omega, o efeito dos custos altera a preferência para SVR+OF. O turnover consome aproximadamente metade dos retornos totais, especialmente em RF+MVF/RF+OF, PDF 12.
- **Métricas não equivalentes:** Tabela 7 registra para RF MAE de 0,0185 e hit rate global de 48,69%; menor erro de regressão não equivale a alta taxa de acerto direcional. As comparações econômicas usam outras métricas e não decorrem automaticamente desses valores.
- **Limitações dos autores:** apenas retornos históricos como entradas e alto turnover; outras fontes são propostas para pesquisas futuras, PDF 13. O estudo é restrito ao mercado/período analisado.
- **Cautela desta leitura:** exclusão de ações sem histórico e suspensas limita generalização; as frases promocionais do resumo sobre superioridade de ML devem ser lidas à luz dos resultados que favorecem ARIMA contra algumas redes/modelos.

**Relevância para o TCC**

É o contraponto empírico principal à narrativa de progresso linear: maior complexidade não determina o vencedor e custos alteram conclusões. Serve à transição para Markowitz distinguindo previsão, parâmetros e pesos; detalhes extensos de carteiras devem permanecer na seção específica. Não repetir sua alegação de “primeira combinação” como pioneirismo independente.

**Citações diretas verificadas**

**F4.1 — PDF 6; página impressa 6.**

> Besides, the traditional time series model ARIMA performs better than CNN and SVR, and CNN’s predictive error is the highest among these models.

- **Contexto:** Seção 5.1, comparação de previsão.
- **O que comprova / ressalva:** É resultado próprio contrário a uma superioridade universal do ML: ARIMA supera CNN e SVR na comparação de erro do estudo.

**F4.2 — PDF 12; página impressa 12.**

> Experimental results show that RF+MVF still outperforms the other MVF models, but RF+OF is surpassed by SVR+OF since it owns higher turnover rate. And, the RF+MVF model performs better than SVR+OF. In addition, turnover erodes nearly half of their total returns especially for RF+MVF and RF+OF.

- **Contexto:** Seção 6.1, síntese dos resultados após custos.
- **O que comprova / ressalva:** Custos alteram o ranking de Omega e corroem retornos; a vantagem reportada permanece condicionada às carteiras/período testados.

**F4.3 — PDF 13; página impressa 13.**

> This study also has limitations because we only apply simple historical returns as input features in order to compare with the benchmark model.

- **Contexto:** Seção 6.3, limitações.
- **O que comprova / ressalva:** Confirma que o experimento não usou notícias, câmbio ou indicadores macroeconômicos como entradas.

### F5 — Busari e Lim (2021): ensembles recorrentes em previsão de commodity

**Identificação**

- **Título:** *Crude oil price prediction: A comparison between AdaBoost-LSTM and AdaBoost-GRU for improving forecasting performance*.
- **Autores:** Ganiyu Adewale Busari; Dong Hoon Lim.
- **Publicação:** *Computers and Chemical Engineering*, 155 (2021), artigo 107513.
- **DOI:** `10.1016/j.compchemeng.2021.107513`, PDF 1.
- **PDF:** `TRABALHOS_REFERENCIA/3 parte intro - machine learning/Crude oil price prediction A comparison between AdaBoost-LSTM and AdaBoost-GRU for improving forecasting performance.pdf`.
- **BibTeX:** entrada correspondente não encontrada no `.bib` disponível.

**Caracterização e leitura**

- **Problema:** previsão diária do preço do petróleo de exportação; motivação macroeconômica e de planejamento. É um exemplo de previsão de commodity, não uma estratégia validada de negociação de futuros ou de portfólio.
- **Antecedentes discutidos:** ARIMA, passeio aleatório, GARCH, VAR e ECM; ANN/SVM em pesquisas anteriores. **O experimento próprio compara LSTM, GRU, AdaBoost–LSTM e AdaBoost–GRU**, não executa todos aqueles benchmarks econométricos.
- **Dados:** preços diários do boletim estatístico do Banco Central da Nigéria; 2.660 observações, das quais 2.655 sequências supervisionadas após janela de cinco pontos; cinco preços anteriores para prever o sexto. Divisão em 1.991 exemplos de treino e 664 de teste, PDF 4–5; o texto informa `shuffle=false`.
- **Período com inconsistência interna:** resumo e seção de dados indicam 23/10/2009–23/06/2021; conclusão indica término em 23/07/2021. Adota-se a seção de dados para caracterização, conservando a divergência, sem corrigi-la por suposição.
- **Motivação técnica:** combinar redes com memória temporal e boosting para reduzir erros. Data de aplicação em 2021 não é data de criação de GRU/LSTM/AdaBoost.
- **Resultados próprios:** Tabela 4, PDF 7: MAE 3,2925/3,0372/1,6374/1,4164 e RMSE 5,5120/5,2622/3,0161/2,4602, respectivamente para LSTM, GRU, AdaBoost–LSTM e AdaBoost–GRU. Neste experimento, os ensembles reduzem os erros e AdaBoost–GRU apresenta os menores valores.
- **Decisão financeira:** previsão poderia subsidiar planejamento e análise de exposição; o artigo não testa uma regra de compra/venda, custos de transação, Sharpe ou alocação. Não converter redução de MAE em lucro ou redução demonstrada de risco de carteira.
- **Ressalvas presentes no texto:** condições econômicas mudam e treinamento com informação antiga pode prejudicar generalização, PDF 4. A conclusão não apresenta seção dedicada de limitações; não atribuir aos autores ressalvas que eles não fizeram.
- **Cautelas desta leitura:** uma série, uma divisão de dados e ausência de avaliação financeira; divergência de datas; a Tabela 4 imprime SI de 0,722 para LSTM, desproporcional aos demais, de modo que não se usa esse indicador para inferências adicionais. Essas observações não anulam os valores de MAE/RMSE, mas restringem o alcance do exemplo.

**Relevância para o TCC**

Amplia a narrativa para commodities e mostra, didaticamente, que ensembles podem combinar redes recorrentes, sem entrar nas equações já tratadas em fundamentos. Prioridade complementar: basta um exemplo de previsão, explicitamente separado de rentabilidade e otimização.

**Citações diretas verificadas**

**F5.1 — PDF 4; página impressa 4.**

> Because the economic conditions change over time, training the network with old information could result in a poor model generalization that might not be relevant to the present economic situation (Elshendy et al., 2018).

- **Contexto:** Seção 3.1, justificativa da coleta.
- **O que comprova / ressalva:** Os autores reconhecem risco de generalização ao treinar com informação antiga; é argumento com referência a terceiros, não teste próprio de regimes.

**F5.2 — PDF 4; página impressa 4.**

> Using a forward-moving window of size 5, we used the first 5 data points as input (predictor, that is, x1 to x5) to predict the sixth data point (target, that is, y1) […]

- **Contexto:** Seção 3.2, construção do problema supervisionado.
- **O que comprova / ressalva:** Define entradas e alvo concretos da previsão. A sequência prevê preço, não ordens ou pesos.

**F5.3 — PDF 9; página impressa 9.**

> We measure forecasting performance in terms of five evaluation metrics. These metrics include both scale-dependence (e.g., MAE and RMSE) and scale-independence (e.g., MAPE and WMAPE) metrics.

- **Contexto:** Conclusão.
- **O que comprova / ressalva:** Confirma avaliação por erros de previsão. Não demonstra lucro, controle de risco ou vantagem de carteira.

### F6 — Jiang, Olmo e Atwi (2024): aprender políticas de negociação e alocação

**Identificação**

- **Título:** *Deep reinforcement learning for portfolio selection*.
- **Autores:** Yifu Jiang; Jose Olmo; Majed Atwi.
- **Publicação:** *Global Finance Journal*, 62 (2024), artigo 101016.
- **DOI:** `10.1016/j.gfj.2024.101016`, PDF 1.
- **PDF:** `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Deep reinforcement learning for portfolio selection.pdf`.
- **BibTeX:** entrada ausente no `.bib` disponível; `jiang2024deep` é apenas chave mencionada em fichamento anterior nesta cópia.

**Caracterização e leitura**

- **Problema:** decisões sequenciais em carteiras de muitas ações, com custos e aversão ao risco. A revisão menciona RL recorrente financeiro em Moody et al. (1998) e Moody–Saffell (2001), PDF 2–3; seus originais permanecem não localizados.
- **Método próprio:** DRL com TD3; redes para representar política/valor e variantes CNN/LSTM. Recompensa incorpora valor da carteira, penalidade de risco e custo de negociar; denominação média-variância estendida dos autores. Não é apenas previsão pontual de retorno alimentando um programa quadrático separado.
- **Entradas, saídas e decisão:** o estado inclui preços e posições anteriores, PDF 4. A ação representa quantidades de ativos a comprar, manter ou vender; o espaço é normalizado para uso com RL de ação contínua. A sequência altera a composição da carteira. Evitar resumir a saída como previsão de preço ou afirmar que o modelo só devolve pesos diretamente.
- **Dados:** Yahoo Finance, 30 constituintes DJIA e 100 S&P100; fechamento diário de 01/04/2010–09/03/2023. Treino até 02/01/2020, validação 03/01/2020–29/04/2021 e teste 30/04/2021–09/03/2023, PDF 7.
- **Benchmarks:** Max-Sharpe, **minimum variance**, e variantes DRL. Na tabela do artigo, `MV` designa mínima variância; não confundir a sigla desse benchmark com qualquer formulação geral de média-variância.
- **Resultados:** cenário DJIA, β=0,005 e custo ξ=0,05%, Tabela 2, PDF 9: RTC-CNN-TD3 tem retorno anual de 26,91%, Sharpe 1,19, volatilidade anual 22,01% e drawdown 19,11%; mínima variância, respectivamente 3,25%, 0,31, 13,42% e 16,01%. Maior retorno/Sharpe convive com maior volatilidade e drawdown que mínima variância.
- **Ressalvas dos autores:** escolha dos dados afeta aprendizado e estratégia; estabilidade/convergência são relevantes; custos e aversão ao risco precisam ser considerados, PDF 2. O artigo reconhece maior volatilidade frente aos dois benchmarks tradicionais, PDF 9. Assume taxa de custo constante entre ativos, PDF 3.
- **Cautelas desta leitura:** resultados de backtest sob parâmetros determinados; não provam execução real, robustez em todos os regimes ou transferibilidade a cripto. A combinação de risco e custos na recompensa não dispensa análise das hipóteses e restrições do ambiente.

**Relevância para o TCC**

É a principal distinção entre aprender uma previsão e aprender uma política. O relato de antecedentes mostra que RL financeiro não nasceu com TD3. No encerramento, apresentar duas alternativas coexistentes: ML fornece informações à otimização, ou aprendizado orienta diretamente decisões sequenciais. Usar poucas linhas para não transformar a subseção em revisão de RL–MV.

**Citações diretas verificadas**

**F6.1 — PDF 2; página impressa 2.**

> Moody et al. (1998, 2001) designed a recurrent RL asset allocation method that used market data from the S&P500 index and US Treasury bill data.

- **Contexto:** Revisão da literatura, seção 2.
- **O que comprova / ressalva:** Registra antecedentes de RL recorrente em alocação. Originais de 1998/2001 não localizados; não transportar seus resultados como verificados.

**F6.2 — PDF 4; página impressa 4.**

> Specifically, the objective of the agent is to learn an optimal trading policy π (st , at ) that selects an action to maximize the reward function.

- **Contexto:** Seção 3.2, formulação do processo decisório.
- **O que comprova / ressalva:** O aprendizado visa uma política que seleciona ações por recompensa, não apenas minimizar erro de previsão.

**F6.3 — PDF 9; página impressa 9.**

> On the downside, this strategy exhibits higher annual volatility than the two benchmark methods.

- **Contexto:** Resultados DJIA, comentário da Tabela 2.
- **O que comprova / ressalva:** A melhoria de retorno/Sharpe não representa redução de todas as medidas de risco; há maior volatilidade frente aos benchmarks tradicionais.

### F7 — Giantsidi e Tarantola (2025): diversidade contemporânea e limites de generalização

**Identificação**

- **Título:** *Deep learning for financial forecasting: A review of recent trends*.
- **Autoras:** Sofia Giantsidi; Claudia Tarantola.
- **Publicação:** *International Review of Economics and Finance*, 104 (2025), artigo 104719; disponível online em 05/11/2025.
- **DOI:** `10.1016/j.iref.2025.104719`, PDF 1.
- **PDF:** `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Deep learning for financial forecasting A review of recent trends.pdf`.
- **BibTeX:** entrada ausente no `.bib` disponível; `giantsidi2025deep` aparece em fichamento anterior, sem confirmação em arquivo bibliográfico.

**Caracterização e leitura**

- **Tipo e dados da revisão:** 187 estudos Scopus de 2020–2024; seleção inicial de 211, com filtros de idioma, tipo de publicação, técnicas e tarefas, PDF 2–3. O período do corpus não é uma única janela de preços, tampouco o ano de origem do DL financeiro.
- **Problemas:** prever ações, índices, câmbio, commodities, títulos, cripto e volatilidade. A Tabela 7 registra 75, 83, 11, 8, 2, 23 e 10 estudos nessas categorias, com sobreposição; não somar como artigos únicos nem interpretar como distribuição do mercado financeiro real.
- **Métodos:** DMLP, redes recorrentes/LSTM/GRU, CNN, autoencoders, híbridos e pré-processamento; dados técnicos, fundamentais e sentimento. Motivação: relações não lineares e temporais, informação heterogênea, ruído e não estacionariedade.
- **Tradicionais e híbridos:** GARCH aparece em previsão de volatilidade, inclusive combinado com redes. O tratamento de volatilidade no PDF 29 é relato de estudos de terceiros, não experimento próprio das revisoras.
- **Resultado próprio:** taxonomia, distribuição e diagnóstico metodológico. Predomínio de LSTM e crescimento de combinações não equivalem à superioridade universal; PDF 30 declara explicitamente a dependência do problema, ativos e dados.
- **Decisão:** previsões podem apoiar estratégias e risco, mas a revisão distingue aplicações além da previsão. Não transformar a discussão de robo-advisors em demonstração de adoção institucional ou resultado econômico do corpus inteiro.
- **Limitações das autoras:** filtros podem omitir achados; excluem conferências, literatura cinzenta e preprints; foco e palavras-chave restringem o universo, PDF 3. Lacunas em testes de estresse, protocolos comparáveis, validação financeira das explicações, custo computacional e capacidade de generalização sob mudanças de regime, PDF 37.
- **Contraponto secundário útil:** PDF 3 relata replicação de Buczyński et al. (2023) em que previsões ingênuas podem rivalizar com DL. Como o original não foi localizado, usar apenas como avaliação relatada pela revisão, sem apresentar resultados específicos como reproduzidos ou verificados diretamente.

**Relevância para o TCC**

Fecha a evolução técnica sem converter novidade em progresso inevitável. Permite mostrar que modelos híbridos e mais dados respondem a problemas reais, mas introduzem exigências de avaliação e implantação. Cripto deve aparecer somente como um dos domínios, preparando a passagem para as seções específicas.

**Citações diretas verificadas**

**F7.1 — PDF 2; página impressa 2.**

> Financial markets generate massive streams of complex, non-stationary data, creating both challenges and opportunities for predictive modeling.

- **Contexto:** Introdução.
- **O que comprova / ressalva:** Motiva a modelagem com dados complexos e não estacionários; não comprova que DL resolva automaticamente esses desafios.

**F7.2 — PDF 30; página impressa 30.**

> The literature suggests that no single model is universally best, with optimal performance depending on task specificity, asset volatility, data characteristics, and the incorporation of domain knowledge.

- **Contexto:** Seção 7, síntese da revisão.
- **O que comprova / ressalva:** Rejeita superioridade universal; resultados dependem da tarefa, dos dados e do conhecimento financeiro.

**F7.3 — PDF 37; página impressa 37.**

> DL models face significant challenges when applied to financial time series, primarily due to non-stationarity, volatility, chaotic behavior, and noise. These issues are further exacerbated by regime shifts and structural breaks, which hinder model generalization.

- **Contexto:** Seção 8.12, resposta sobre desafios dos modelos.
- **O que comprova / ressalva:** Não estacionariedade, ruído, mudanças de regime e quebras estruturais continuam limitando DL. Não confundir flexibilidade funcional com imunidade a mudança de distribuição.

## Parte III — Casos de uso de ML em finanças

**P** = evidência do experimento original lido; **S** = relato secundário verificado em revisão/seção de literatura. Usos sugeridos não devem ser confundidos com intervenções efetivamente implantadas.

| Aplicação                                 | Problema financeiro                                                                  | Entrada do modelo                                                                      | Saída do modelo                                       | Utilização prática                                                                                   | Referências                                          |
| ------------------------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Alerta de dificuldades financeiras          | Antecipar deterioração de empresas, com classe minoritária e mudança de conceito | Indicadores contábeis, rótulos históricos, recência                                | Classe dificuldade/normal                              | Apoiar alerta e controles; redução de perdas não foi testada causalmente                             | F1,**P**, PDF 9 e 15–16                        |
| Credit scoring                              | Avaliar risco de solicitantes/empresas                                               | Dados de crédito/atributos nos trabalhos citados; sem base empírica própria fichada | Classe/escore de risco                                 | Apoiar análise de crédito; detalhes de concessão não verificados nos originais                      | F1,**S**, PDF 2–3 e referências 8–19, PDF 16 |
| Previsão de preço                         | Antecipar preço de commodity                                                        | Cinco preços diários anteriores                                                      | Preço do próximo ponto                               | Subsídio à análise/planejamento; sem regra de trading validada                                       | F5,**P**, PDF 4–7                              |
| Previsão de retorno                        | Estimar retorno de ações                                                           | Retornos defasados; no caso de Wang também indicadores técnicos                      | Retorno futuro estimado                                | Ordenar ativos e/ou fornecer estimativas ao processo de alocação                                      | F2 e F4,**P**, PDF 5 e 6, respectivamente       |
| Classificação de movimento/sinais         | Identificar direção ou classes de tendência                                       | Preços, indicadores técnicos/fundamentais                                            | Subida/queda ou categorias de tendência               | Associar a comprar/manter/vender; a regra de execução é uma etapa adicional                          | F3,**S**, PDF 10–12                            |
| Sentimento financeiro                       | Extrair informação de notícias e mensagens                                        | Texto, termos, mensagens e eventualmente preços                                       | Polaridade/escores; posteriormente direção ou preço | Usar texto como atributo para decisão; sentimento positivo não equivale diretamente a ordem de compra | F3,**S**, PDF 12–14 e 18                       |
| Previsão de volatilidade                   | Estimar variabilidade futura                                                         | Séries financeiras e componentes econométricos nos estudos revisados                 | Volatilidade prevista                                  | Subsidiar controle de exposição; não define sozinha pesos nem covariância multiativo                | F3,**S**, PDF 10; F7, **S**, PDF 29–30   |
| Pré-seleção de ativos                    | Reduzir universo elegível antes de alocar                                           | Retornos previstos/ranking                                                             | Subconjunto de ações                                 | Encaminhar ativos selecionados ao MV ou a uma regra 1/N                                                 | F2,**P**, PDF 5                                 |
| Produção de parâmetros para otimização | Incorporar estimativas prospectivas à carteira                                      | Retornos previstos e dados financeiros usados pelo otimizador                          | Estimativas; depois pesos pela otimização            | Separar o componente preditivo da solução MV/Omega                                                    | F4,**P**, método e PDF 6, 12–13               |
| Política de negociação multiativo        | Escolher decisões sequenciais com custos e risco                                    | Preços e posições anteriores; recompensas                                           | Quantidades de compra/manutenção/venda por ativo     | Alterar exposição/carteira via política aprendida                                                    | F6,**P**, PDF 3–4 e 7–9                       |

**Fraudes/transações anômalas:** não foi selecionado estudo original adequado para reconstruir método, dados, resultados e evolução histórica. Menções genéricas em surveys do acervo não bastam para preencher artificialmente uma linha empírica. A lacuna permanece na Parte V.

### Distinções necessárias para a transição ao TCC

- **Prever preço ou retorno** produz uma estimativa de variável; seu erro é avaliado por métricas preditivas. F5 e F4 mostram que isso não é o mesmo que simular uma carteira.
- **Gerar sinal de compra/venda** demanda transformar a estimativa em ação, por limiar ou regra; F3 documenta classes de tendência associadas a ações. O limiar, o horizonte e o custo afetam a utilidade.
- **Estimar risco** tem outro alvo, como volatilidade; a precisão do retorno não comprova qualidade da previsão de risco. F3/F7 documentam essa tarefa separadamente. Não presumir que previsão univariada de volatilidade fornece toda a matriz de covariância.
- **Selecionar ativos** produz um conjunto ou ranking; **otimizar** produz uma alocação sob objetivo e restrições. Em F2, LSTM faz previsão/pré-seleção e MV determina a composição.
- **Produzir parâmetros** significa usar a previsão dentro da formulação de carteira, como em F4; o otimizador não se transforma em ML por consumir essas estimativas.
- **Aprender uma política** liga estados a ações avaliadas por recompensas, como em F6. A política pode modificar a carteira sem uma etapa independente de previsão pontual de retorno. Sua avaliação precisa considerar a trajetória, risco e custos.

## Parte IV — Proposta de encadeamento narrativo

Não se recomenda começar pela definição histórica geral de IA, pelo perceptron ou pela data de invenção de LSTM. O fio condutor deve ser o problema financeiro e o que muda na decisão quando se aprende com dados.

| Bloco                                                 | Estudos/evidências recomendados                                                                         | Objetivo didático e afirmação defensável                                                                            | Ligação com o seguinte / limites                                                                                                                  |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Problemas anteriores ao ML                         | F1, introdução/revisão, PDF 1–2; antecedentes de 1966/1968/1980                                      | Empresas e analistas já buscavam antecipar deterioração por indicadores e modelos estatísticos                      | Introduzir aprendizado como outra forma de modelar relações; não classificar os antecedentes como ML                                             |
| 2. Tentativas iniciais de aprendizado financeiro      | F1, árvores de 1985/redes de 1990; F3, redes probabilísticas de 1996/1998                              | Mostrar a passagem documentada a classificadores aprendidos em risco empresarial e movimentos de mercado                | Sinalizar acesso indireto. Sistemas especialistas antigos permanecem lacuna; não inserir uma etapa obrigatória sem fonte                          |
| 3. Expansão dos alvos e decisões                    | F3, PDF 10–14; F1, revisão de crédito                                                                 | Diferenciar dificuldade financeira, direção de preços, volatilidade e sentimento; explicar entradas → saída → uso | A variedade de tarefas motiva diversidade de modelos e dados, não um único algoritmo vencedor                                                     |
| 4. Fontes mais diversas e modelos combinados          | F3 para notícias/redes sociais; F5 para AdaBoost–GRU/LSTM; F1 para SMOTE/recência; F7 para 2020–2024 | Mostrar problemas que justificam combinações: memória, ruído, classe rara, mudança de conceito e texto             | Evitar dizer que o campo evoluiu só aumentando profundidade. Texto pode ser tratado por léxico ou por modelo aprendido                            |
| 5. Resultados, comparação e limites contemporâneos | F4, ARIMA versus CNN/SVR e custos; F7, PDF 30 e 37; F1, trade-off entre classes                          | Explicar por que desempenho deve ser definido por tarefa e validado temporalmente; preservar resultados adversos        | Preparar pergunta final: mesmo havendo previsão útil, como transformá-la em decisão de investimento?                                            |
| 6. Decisões de investimento e ponte para portfólios | F2, previsão/pré-seleção → MV; F4, previsões → parâmetros; F6, política → ações              | Separar regressão, classificação, seleção, otimização e RL; mostrar convivência com métodos financeiros        | Encerrar com o problema do TCC: investigar essas interfaces em portfólios de criptoativos sob MV, sem antecipar resultados da revisão específica |

**Ordem temporal a preservar:** o bloco de políticas contemporâneas deve remeter explicitamente aos antecedentes RL de 1998/2001 relatados por Jiang. A ordenação didática dos blocos não significa que RL surgiu após LSTM+MV de 2020.

**Proporção sugerida:** dedicar a maior parte da subseção aos blocos 1–5; reservar um fechamento curto ao bloco 6. Wang/Ma/Jiang explicam funções diferentes do ML, sem repetir tabelas de resultados da Seção 3. Cripto aparece como destino da pergunta de pesquisa, não como prova da história de todo o setor financeiro.

**Afirmações a evitar na redação:** “ML começou em finanças em 1990”; “sistemas especialistas são ML”; “redes profundas substituíram a econometria”; “mais acurácia implica mais lucro”; “o modelo não exige cuidados com não estacionariedade”; “o primeiro trabalho de RL financeiro é de 2024”; “há prova de adoção generalizada porque a literatura cresceu”. O acervo não sustenta essas formulações.

## Parte V — Lacunas bibliográficas e fontes primárias pendentes

### Lacunas por problema histórico

| Lacuna                                               | O que falta demonstrar                                                                         | Fonte necessária e consequência para a redação                                                                                                             |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Origem anterior aos anos 1980                        | Quando e em quais instituições o aprendizado foi efetivamente testado em tarefas financeiras | Estudos contemporâneos aos episódios e histórias documentais com referências primárias; não declarar uma data única de origem                           |
| Sistemas especialistas financeiros iniciais          | Sistemas baseados em regras, tarefas, dados, validação e eventual componente aprendido       | Artigos técnicos originais e relatos institucionais datados; separar IA simbólica de ML. Wang menciona sistema de 2013, mas isso não prova os primórdios   |
| Árvores e primeiras redes em dificuldades/falência | Dados, comparadores e resultados dos estudos de 1985/1990                                      | Originais de Frydman et al. e Odom–Sharda; até lá, manter atribuição a Sun                                                                                |
| Crédito de varejo, concessão e inadimplência      | Evolução do scoring e seus resultados fora da amostra                                        | Estudos originais com definição de default, horizonte, calibração, custo de erro e base de tomadores; Sun não substitui essa documentação               |
| Fraude e anomalias transacionais                     | Datas de aplicações, transações, classes raras, falsos alarmes e atualização             | Artigos originais com dados de transações e avaliação operacional; menção em survey é insuficiente                                                      |
| Redes e SVM em mercados nos anos 1980–2000          | Comparadores, séries, custos, validação e prioridade histórica                             | Originais de previsão/classificação e revisões históricas mais abrangentes; o recorte 1995–2019 de Ferreira não prova ausência de trabalhos anteriores |
| RL financeiro inicial                                | Objetivo econômico direto, custos e dados dos estudos de 1998/2001                            | Moody et al. e Moody–Saffell integrais; entrada BibTeX existente não confirma leitura                                                                        |
| Texto e sentimento iniciais                          | Diferença entre léxico fixo, classificação aprendida e previsão/negociação              | Originais de mineração de notícias e redes sociais, com horários de informação e disponibilidade real; não tratar associação como causalidade         |
| Volatilidade e risco                                 | Testes originais dos híbridos econometria–ML e cobertura de risco                            | Roh (2007), Xing et al. (2019) e estudos de volatilidade da revisão recente; conferir alvo, benchmark e perda apropriada                                      |
| Adoção pelo setor                                  | Uso real, escala, custos operacionais, governança e persistência                             | Estudos institucionais/documentais ou empíricos de implantação. Experimentos acadêmicos não comprovam difusão comercial                                  |
| Replicação e resultados negativos antigos          | Frequência de fracassos, estabilidade e comparações históricas justas                      | Trabalhos de replicação e séries comparáveis, além de estudos individuais; não inferir a taxa de sucesso da seleção positiva da literatura             |
| Bibliografia e redação do TCC                      | Chaves reais e posição exata da subseção na versão atual                                  | Arquivos`.tex` e `.bib` principais ausentes nesta cópia; DOCX é apenas contexto complementar                                                             |

### Referências históricas identificadas no corpo/bibliografia dos PDFs lidos

**Todas as linhas seguintes são fontes primárias ainda não localizadas como texto integral nesta investigação.** Metadados são os transcritos das referências locais, sujeitos à confirmação no original; não se inventaram DOIs ou chaves. Os resultados desses trabalhos não foram fichados como evidência primária.

| Referência identificada                                                                                                                                                                                               | Onde foi conferida                 | Utilidade e estado                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| W. Beaver (1966),*Financial ratios as predictors of failure*, Journal of Accounting Research, 4, suplemento, S71–111                                                                                                | F1, PDF 16, ref. 1                 | Antecedente estatístico; DOI/chave não confirmados                                                                                                                                                                    |
| E. I. Altman (1968),*Financial ratios discriminant analysis and the prediction of corporate bankruptcy*, Journal of Finance, 23(4), 589–609                                                                         | F1, PDF 16, ref. 2                 | Antecedente discriminante; grafia do título conforme lista secundária                                                                                                                                                 |
| J. Ohlson (1980),*Financial ratio and the probabilistic prediction of bankruptcy*, Journal of Accounting Research, 18, 109–131                                                                                      | F1, PDF 16, ref. 3                 | Antecedente Logit; conferir título formal no original                                                                                                                                                                  |
| H. Frydman; E. I. Altman; D. Kao (1985),*Introducing recursive partitioning for financial classification: the case of financial distress*, Journal of Finance, 40, 269–291                                          | F1, PDF 2 e 16, ref. 4             | Particionamento recursivo aplicado a dificuldade financeira; alta prioridade                                                                                                                                            |
| M. Odom; R. Sharda (1990),*Neural networks model for bankruptcy prediction*, Proceedings of the IEEE International Conference on Neural Network, 2, 163–168                                                         | F1, PDF 2 e 16, ref. 5             | Redes para falência; conferir título formal e dados no original; alta prioridade                                                                                                                                      |
| K. Schierholt; C. H. Dagli (1996),*Stock market prediction using different neural network classification architectures*, IEEE/IAFE Conference on Computational Intelligence for Financial Engineering, 72–78        | F3, PDF 10 e 19, ref. 72           | Redes e classes de ação em mercado acionário                                                                                                                                                                         |
| S. H. Kim; S. H. Chun (1998),*Graded forecasting using an array of bipolar predictions: Application of probabilistic neural networks to a stock market index*, International Journal of Forecasting, 14(3), 323–337 | F3, PDF 10 e 19, ref. 45           | Redes probabilísticas e níveis de retorno                                                                                                                                                                             |
| J. Moody; L. Wu; Y. Liao; M. Saffell (1998),*Performance functions and reinforcement learning for trading systems and portfolios*, Journal of Forecasting, 17, 441–470                                              | F6, PDF 2 e 14                     | Antecedente de aprendizado orientado ao desempenho econômico                                                                                                                                                           |
| J. Moody; M. Saffell (2001),*Learning to trade via direct reinforcement*, IEEE Transactions on Neural Networks, 12(4), 875–889                                                                                      | F6, PDF 2–3 e 14;`.bib` local   | Chave**confirmada** `moody2001learning`, DOI bibliográfico `10.1109/72.935097`; PDF ausente. A lista de Jiang usa o nome posterior do periódico, divergindo do `.bib`; não resolver isso silenciosamente |
| M. A. Mittermayer (2004),*Forecasting intraday stock price trends with text mining techniques*, Annual Hawaii International Conference on System Sciences, 37, 1029–1038                                            | F3, PDF 12 e 19, ref. 55           | Mineração de notícias e previsão intradiária                                                                                                                                                                       |
| W. Huang; Y. Nakamori; S.-Y. Wang (2005),*Forecasting stock market movement direction with support vector machine*, Computers & Operations Research, 32(10), 2513–2522                                              | F3, PDF 10 e 19, ref. 36           | SVM e classificação direcional                                                                                                                                                                                        |
| T. H. Roh (2007),*Forecasting the volatility of stock price index*, Expert Systems with Applications, 33(4), 916–922                                                                                                | F3, PDF 10 e 19, ref. 38           | Híbridos rede–modelos econométricos de volatilidade                                                                                                                                                                  |
| Y. Ding; X. Song; Y. Zen (2008),*Forecasting financial condition of Chinese listed companies based on support vector machine*, Expert Systems with Applications, 34, 3081–3089                                      | F1, PDF 3 e 16, ref. 6             | SVM em condição financeira; nomes conforme referência secundária                                                                                                                                                    |
| R. P. Schumaker; H. Chen (2009),*Textual analysis of stock market prediction using breaking financial news: The AZFin text system*, ACM Transactions on Information Systems, 27(2), 1–19                            | F3, PDF 13 e 19, ref. 74           | Combinação de notícia e informação de mercado                                                                                                                                                                      |
| J. Bollen; H. Mao; X. Zeng (2011),*Twitter mood predicts the stock market*, Journal of Computational Science, 2(1), 1–8                                                                                             | F3, PDF 14 e 18, ref. 9            | Sentimento social; não atribuir causalidade a associação preditiva                                                                                                                                                   |
| T. H. Nguyen; K. Shirai; J. Velcin (2015),*Sentiment analysis on social media for stock movement prediction*, Expert Systems with Applications, 42(24), 9603–9611                                                   | F3, PDF 14 e 19, ref. 60           | Mensagens e movimentos de ações                                                                                                                                                                                       |
| F. Barboza; H. Kimura; E. I. Altman (2017),*Machine learning models and bankruptcy prediction*, Expert Systems with Applications, 83, 405–417                                                                       | F1, PDF 3 e 16, ref. 23            | Comparação de ensembles e métodos tradicionais; não reproduzir como verificado o ganho numérico citado por Sun                                                                                                     |
| F. Z. Xing; E. Cambria; Y. Zhang (2019),*Sentiment-aware volatility forecasting*, Knowledge-Based Systems, 176, 68–76                                                                                               | F3, PDF 19, ref. 70;`.bib` local | Chave`xing2019sentiment`, DOI bibliográfico `10.1016/j.knosys.2019.03.029`; PDF ausente                                                                                                                            |

### Auditoria de divergências e decisões de seleção

| Item                                                                                                      | Evidência desta investigação                           | Decisão                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Wang: DOI e universo                                                                                      | PDF 1:`113042`; PDF 4: 21 ações do FTSE 100           | Registrar correção aqui; preservar os outros fichamentos                                                                                     |
| Ma: universo                                                                                              | PDF 6: 49 ações após filtros                           | Distinguir universo de referência CSI 100 da amostra efetiva                                                                                  |
| Busari: fim da série                                                                                     | Junho em resumo/dados; julho na conclusão                | Conservar a divergência; não harmonizar por suposição                                                                                      |
| Paiva                                                                                                     | Duas cópias presentes, texto extraído corrompido        | Não afirmar verificação literal nova; candidato pendente de leitura visual/OCR                                                              |
| PDFs declarados disponíveis no catálogo de expansão                                                    | Não localizados nesta cópia                             | Diferenciar catálogo, entrada`.bib` e disponibilidade real                                                                                  |
| `fintech-05-00091.pdf`                                                                                  | Arquivo local existe; canônico dizia PDF não localizado | Inventariado, mas fora do núcleo histórico por foco cripto/GNN e redundância; não reproduzir a ausência antiga                            |
| Arquivos com títulos variantes de*Empirical evidence on deep learning-enhanced portfolio optimization* | Cópias idênticas por hash                               | Um único documento físico duplicado; excluído do núcleo. A capa não basta para validar status editorial nem resolver alertas do canônico |
| Estatística clássica, algoritmos genéticos e GARCH–cópulas                                           | Presentes em finanças/portfólios no acervo              | Não contar como evidência de ML sem componente aprendido pertinente                                                                          |
| Artigos de alfabetização financeira, comportamento e regulação                                        | Triagem de identidade/tema                                | Contexto financeiro, mas sem contribuição central à história de ML nesta seleção                                                         |
| Muitos estudos ML–cripto–MV de 2023–2026                                                               | Inventariados                                             | Reservados às seções próprias. A exclusão não significa falta de relevância acadêmica nem ausência de resultados negativos            |

## Anexo — Inventário físico e duplicatas

O inventário a seguir cobre todos os PDFs, não apenas a pasta de ML. **Inventariado/triado não significa lido integralmente.** As sete fichas da Parte II são o conjunto de leitura aprofundada desta investigação. Livros, outros trabalhos e fichamentos foram usados apenas para contexto/triagem quando indicado; não fundamentam resultados específicos sem ficha e página.

### Distribuição física

| Diretório                                                                             | PDFs |
| -------------------------------------------------------------------------------------- | ---: |
| `.`                                                                                  |    4 |
| `TRABALHOS_REFERENCIA`                                                               |    4 |
| `TRABALHOS_REFERENCIA/1 parte intro - decisoes de investimentos e tomada de decisao` |    7 |
| `TRABALHOS_REFERENCIA/2 parte intro - Cripto`                                        |   13 |
| `TRABALHOS_REFERENCIA/3 parte intro - machine learning`                              |    8 |
| `TRABALHOS_REFERENCIA/4 parte intro - Teoria de Portifólio`                         |    3 |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados`                          |   16 |
| `TRABALHOS_REFERENCIA/NOVOS SEC 3`                                                   |   13 |

### Arquivos e destino na investigação

| Arquivo relativo à raiz                                                                                                                                                                           | Destino                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `DIOGO M.R. TEIXEIRA - Previsão de Preços de Ações  Machine ⏎ Learning.pdf`                                                                                                                 | Triagem; dissertação contemporânea de previsão, preterida pelos artigos/revisões selecionados        |
| `Finanças Corporativas E Valor (Alexandre Assaf Neto).pdf`                                                                                                                                      | Inventário; livro de finanças, fora do núcleo de história de ML                                       |
| `Maria Rocha - Regulação Prudencial e Risco Bancário No Brasil.pdf`                                                                                                                           | Triagem temática; finanças/regulação/comportamento, sem contribuição histórica central selecionada |
| `Ross - Fundamentals of Corporate Finance.pdf`                                                                                                                                                   | Inventário; livro de finanças, fora do núcleo de história de ML                                       |
| `TRABALHOS_REFERENCIA/1 parte intro - decisoes de investimentos e tomada de decisao/Behavioral finance factors and investment decisions.pdf`                                                     | Triagem temática; finanças/regulação/comportamento, sem contribuição histórica central selecionada |
| `TRABALHOS_REFERENCIA/1 parte intro - decisoes de investimentos e tomada de decisao/Bitcoin A safe haven asset and a winner amid political and economic.pdf`                                     | Triagem temática; finanças/regulação/comportamento, sem contribuição histórica central selecionada |
| `TRABALHOS_REFERENCIA/1 parte intro - decisoes de investimentos e tomada de decisao/Diversifying equity with cryptocurrencies during COVID-19.pdf`                                               | Triagem temática; finanças/regulação/comportamento, sem contribuição histórica central selecionada |
| `TRABALHOS_REFERENCIA/1 parte intro - decisoes de investimentos e tomada de decisao/How financial literacy moderate.pdf`                                                                         | Triagem temática; finanças/regulação/comportamento, sem contribuição histórica central selecionada |
| `TRABALHOS_REFERENCIA/1 parte intro - decisoes de investimentos e tomada de decisao/Investigating the dynamic relationship between cryptocurrencies and.pdf`                                     | Triagem temática; finanças/regulação/comportamento, sem contribuição histórica central selecionada |
| `TRABALHOS_REFERENCIA/1 parte intro - decisoes de investimentos e tomada de decisao/Is there a risk-return trade-off in cryptocurrency markets.pdf`                                              | Triagem temática; finanças/regulação/comportamento, sem contribuição histórica central selecionada |
| `TRABALHOS_REFERENCIA/1 parte intro - decisoes de investimentos e tomada de decisao/Portfolio optimization with robust stochastic dominance testing.pdf`                                         | Triagem temática; finanças/regulação/comportamento, sem contribuição histórica central selecionada |
| `TRABALHOS_REFERENCIA/2 parte intro - Cripto/A crypto safe haven against Bitcoin.pdf`                                                                                                            | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/2 parte intro - Cripto/Are stablecoins truly diversifiers, hedges, or safe havens against traditional cryptocurrencies as their name suggests.pdf`                         | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/2 parte intro - Cripto/Cryptocurrency trading a comprehensive survey.pdf`                                                                                                  | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/2 parte intro - Cripto/Explainable artificial intelligence for crypto asset allocation.pdf`                                                                                | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/2 parte intro - Cripto/Intelligent cryptocurrency trading system using integrated.pdf`                                                                                     | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/2 parte intro - Cripto/Investigating the dynamic relationship between cryptocurrencies and conventional assets Implications for financial investors.pdf`                   | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/2 parte intro - Cripto/Portfolio diversification with virtual currency Evidence from bitcoin.pdf`                                                                          | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/2 parte intro - Cripto/Testing for herding in the cryptocurrency market.pdf`                                                                                               | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/2 parte intro - Cripto/The contagion effects of the COVID-19 pandemic Evidence from gold and cryptocurrencies.pdf`                                                         | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/2 parte intro - Cripto/Volatility dynamics of crypto-currencies’ returns.pdf`                                                                                             | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/2 parte intro - Cripto/forecasting-03-00024-v2.pdf`                                                                                                                        | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/2 parte intro - Cripto/mathematics-13-01623.pdf`                                                                                                                           | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/2 parte intro - Cripto/s40854-020-00217-x (1).pdf`                                                                                                                         | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/3 parte intro - machine learning/A Novel Cryptocurrency Price Prediction Model Using GRU, LSTM and bi-LSTM Machine Learning Algorithms.pdf`                                | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/3 parte intro - machine learning/Class-imbalanced dynamic financial distress prediction based on Adaboost-SVM ensemble combined with SMOTE and time weighting.pdf`         | Ficha F1; leitura aprofundada                                                                             |
| `TRABALHOS_REFERENCIA/3 parte intro - machine learning/Comparative Performance of Machine Learning Ensemble Algorithms for.pdf`                                                                  | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/3 parte intro - machine learning/Crude oil price prediction A comparison between AdaBoost-LSTM and AdaBoost-GRU for improving forecasting performance.pdf`                 | Ficha F5; leitura aprofundada                                                                             |
| `TRABALHOS_REFERENCIA/3 parte intro - machine learning/Ensemble Deep Learning Models for Forecasting.pdf`                                                                                        | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/3 parte intro - machine learning/Explainable artificial intelligence for crypto asset allocation.pdf`                                                                      | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/3 parte intro - machine learning/Forecasting and trading cryptocurrencies.pdf`                                                                                             | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/3 parte intro - machine learning/Intelligent cryptocurrency trading system using integrated.pdf`                                                                           | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/4 parte intro - Teoria de Portifólio/Bitcoin and Portfolio Diversification A Portfolio Optimization Approach.pdf`                                                         | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/4 parte intro - Teoria de Portifólio/J Corp Accounting Finance - 2024 - Jeleskovic - Cryptocurrency portfolio optimization  Utilizing a GARCH‐copula model.pdf`          | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/4 parte intro - Teoria de Portifólio/Markowitz Mean-Variance Portfolio Optimization with.pdf`                                                                             | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Computational Intelligence and Neuroscience - 2022 - Padhi - An Intelligent Fusion Model with Portfolio Selection and.pdf`            | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Cryptocurrency-portfolios in a mean-variance framework.pdf`                                                                           | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Deep learning for financial forecasting A review of recent trends.pdf`                                                                | Ficha F7; leitura aprofundada                                                                             |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Deep reinforcement learning for portfolio selection.pdf`                                                                              | Ficha F6; leitura aprofundada                                                                             |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Deep reinforcement learning for stock portfolio optimization by connecting.pdf`                                                       | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Enhancing Markowitz_s portfolio selection paradigm with machine learning.pdf`                                                         | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Enhancing portfolio.pdf`                                                                                                              | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Markowitz Mean-Variance Portfolio Optimization with Predictive Stock Selection Using Machine Learning.pdf`                            | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Mean–variance portfolio optimization using machine learning-based stock price prediction.pdf`                                        | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Mean–variance portfolio optimization with deep learning based-forecasts for cointegrated stocks.pdf`                                 | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Optimal Markowitz portfolio using returns.pdf`                                                                                        | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Optimization of portfolios with cryptocurrencies.pdf`                                                                                 | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Paiva2019.pdf`                                                                                                                        | Candidato pendente: extração textual corrompida; cópia duplicada                                       |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Portfolio Optimization Based on MPT-LSTM Neural Networks A case study of Cryptocurrency Markets.pdf`                                  | Triagem; exemplo contemporâneo ou sobreposição com fundamentos/estudos relacionados                    |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Portfolio formation with preselection using deep learning from long-term financial data.pdf`                                          | Ficha F2; leitura aprofundada                                                                             |
| `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Portfolio optimization with return prediction using deep learning and machine learning.pdf`                                           | Ficha F4; leitura aprofundada                                                                             |
| `TRABALHOS_REFERENCIA/Artificial_Intelligence_Applied_to_Stock_Market_Trading_A_Review.pdf`                                                                                                      | Ficha F3; leitura aprofundada                                                                             |
| `TRABALHOS_REFERENCIA/NOVOS SEC 3/A machine learning framework for multi-market portfolio optimization - Evidence from U.S. stocks and cryptocurrencies.pdf`                                     | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/NOVOS SEC 3/Cryptocurrency Portfolio Optimisation Based on LSTM Time Series Forecasting.pdf`                                                                               | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/NOVOS SEC 3/Empirical evidence on deep learning-enhanced portfolio optimization - integrating CNN-LSTM forecasts with mean-variance theory in cryptocurrency markets.pdf`  | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/NOVOS SEC 3/Empirical evidence on deep learning-enhanced portfolio woptimization - theory in cryptocurrency integrating CNN-LSTM markets forecasts with mean-variance.pdf` | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/NOVOS SEC 3/Integrating Choquet portfolios and machine learning interpretability for robust cryptocurrency investment strategies.pdf`                                      | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/NOVOS SEC 3/Multi-source data driven cryptocurrency price movement prediction and portfolio optimization.pdf`                                                              | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/NOVOS SEC 3/Online risk-based portfolio allocation on subsets of crypto assets applying a prototype-based clustering algorithm.pdf`                                        | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/NOVOS SEC 3/Portfolio Optimization Methods for the Digital Asset Market - A Comprehensive Survey.pdf`                                                                      | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/NOVOS SEC 3/Portfolio constructions in cryptocurrency market - A CVaR-based deep reinforcement learning approach.pdf`                                                      | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/NOVOS SEC 3/QFE-09-03-023.pdf`                                                                                                                                             | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/NOVOS SEC 3/The diversification benefits of cryptocurrency factor portfolios - Are they there.pdf`                                                                         | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/NOVOS SEC 3/When Richer Information Does Not Improve Allocation - Machine Learning and Portfolio Optimisation in NFT-Ecosystem Tokens.pdf`                                 | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/NOVOS SEC 3/fintech-05-00091.pdf`                                                                                                                                          | Triagem; reservado ao recorte específico de cripto/portfólios                                           |
| `TRABALHOS_REFERENCIA/Paiva2019.pdf`                                                                                                                                                             | Candidato pendente: extração textual corrompida; cópia duplicada                                       |
| `TRABALHOS_REFERENCIA/s41264-023-00249-1.pdf`                                                                                                                                                    | Triagem temática; finanças/regulação/comportamento, sem contribuição histórica central selecionada |
| `TRABALHOS_REFERENCIA/sustainability-15-09358.pdf`                                                                                                                                               | Triagem temática; finanças/regulação/comportamento, sem contribuição histórica central selecionada |

### Duplicatas

Cinco pares com SHA-256 idêntico (68 arquivos, 63 conteúdos binários distintos):

- `TRABALHOS_REFERENCIA/2 parte intro - Cripto/Explainable artificial intelligence for crypto asset allocation.pdf`; `TRABALHOS_REFERENCIA/3 parte intro - machine learning/Explainable artificial intelligence for crypto asset allocation.pdf`.
- `TRABALHOS_REFERENCIA/2 parte intro - Cripto/s40854-020-00217-x (1).pdf`; `TRABALHOS_REFERENCIA/3 parte intro - machine learning/Forecasting and trading cryptocurrencies.pdf`.
- `TRABALHOS_REFERENCIA/4 parte intro - Teoria de Portifólio/Markowitz Mean-Variance Portfolio Optimization with.pdf`; `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Markowitz Mean-Variance Portfolio Optimization with Predictive Stock Selection Using Machine Learning.pdf`.
- `TRABALHOS_REFERENCIA/5 parte intro - estudos relacionados/Paiva2019.pdf`; `TRABALHOS_REFERENCIA/Paiva2019.pdf`.
- `TRABALHOS_REFERENCIA/NOVOS SEC 3/Empirical evidence on deep learning-enhanced portfolio optimization - integrating CNN-LSTM forecasts with mean-variance theory in cryptocurrency markets.pdf`; `TRABALHOS_REFERENCIA/NOVOS SEC 3/Empirical evidence on deep learning-enhanced portfolio woptimization - theory in cryptocurrency integrating CNN-LSTM markets forecasts with mean-variance.pdf`.

Há ainda dois pares com a mesma primeira página textual e mesma identidade de artigo, embora hashes diferentes: Park–Yang (*Intelligent cryptocurrency trading system using integrated*, pastas 2 e 3) e Charfeddine et al. (*Investigating the dynamic relationship…*, pastas 1 e 2). Foram tratados como cópias da mesma obra na triagem, sem contagem adicional de estudos. Não foi realizada comparação integral de versões desses dois pares.

Os títulos de arquivos foram mantidos como encontrados; não constituem, por si, validação bibliográfica. O símbolo `⏎` na entrada de Teixeira representa uma quebra de linha real no nome do arquivo.

### Outros materiais consultados

- `CITACOES_SEC3_POR_SUBSECAO.md`: estrutura canônica e mapa de redundâncias; preservado.
- `CITACOES_ML_FINANCAS.md`, `CITACOES_ML_FINANCAS_EXPANDIDO.md` e `ML_FINANCAS_EXPANSAO/CITACOES_ML_FINANCAS_EXPANSAO_DISPONIVEL.md`: índices prévios e alegações de disponibilidade confrontadas com o inventário.
- `ML_FINANCAS_EXPANSAO/referencias_ml_financas_expansao.bib`: conferência de entradas e chaves.
- `meu-trabalho.docx`: contexto textual do TCC; preservado.
- Outros fichamentos de Sharpe, curva de indiferença e resultados quantitativos de cripto foram inventariados, sem necessidade de incorporá-los à base histórica.

### Conferência final de alcance

Este documento sustenta uma história parcial, com fontes secundárias explícitas para os antecedentes e evidências primárias recentes para ilustrar problemas e escolhas. A prioridade de complementação bibliográfica é recuperar os originais históricos, sobretudo classificação financeira e RL, antes de reforçar afirmações de origem ou pioneirismo. A transição para criptoativos e Markowitz é conceitual: a utilidade de previsões, sinais, estimativas de risco ou políticas para uma carteira precisa ser avaliada no problema de alocação específico, não presumida a partir da história dos algoritmos.
