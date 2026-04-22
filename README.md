# Fundamentos da Estatística Exploratória

---

## 🗒️ Índice

- [📌 Sobre o Trabalho](#-sobre-o-trabalho)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [💻 Instalação](#-instalação)
- [📦 Bibliotecas Utilizadas](#-bibliotecas-utilizadas)
- [🗂️ Fonte de Dados](#️-fonte-de-dados)
- [📈 Gráficos — Aprofundamento](#-gráficos---aprofundamento)
  - [1. Histograma — Distribuição do PIB Agropecuário](#1--histograma--distribuição-do-pib-agropecuário)
  - [2. Gráfico de Dispersão — Agropecuária × Indústria](#-gráfico-de-dispersão--agropecuária--indústria)
  - [3. Heatmap — Correlação entre Setores](#️-heatmap--correlação-entre-setores)
  - [4. Barras Empilhadas — Top 15 Microrregiões](#-barras-empilhadas--top-15-microrregiões)
- [🧠 Conceitos-chave de Python](#-conceitos-chave-de-python-usados)
- [🎨 Customizações Úteis para ir Além](#-customizações-úteis-para-ir-além)
- [📚 Para Aprender Mais](#-para-aprender-mais)
- [👨‍💻 Autores](#-autor---lucas-oliveira-e-caua-landa)

---

## 📌 Sobre o Trabalho

O presente projeto visa mesclar conceitos de programação em Python com os principais tópicos da Estatística Exploratória ne medida em que construímos uma série de gráficos
usando a Linguagem ```Python``` a partir dos dados de **Contabilidade Social do RS por Microrregião com Valores de PIB Setorial (Adm Pública, Agropecuária, Indústria e demais Serviços)*
a fim de desenvolver e execitar o Pensamento Estatístico dentro das ideias de Snee 

| Nº | Tipo de Gráfico        | Conceito                                                                 | O que mostra no script                                                                 | Exemplo de interpretação                                                                 | Aplicação na análise |
|----|------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|----------------------|
| 1  | Histograma             | Gráfico que mostra a distribuição de frequência de uma variável numérica, agrupando os valores em intervalos (bins). | Distribuição do PIB Agropecuário entre as microrregiões, incluindo linhas indicativas da média e da mediana. | Permite observar se a maioria das microrregiões possui PIB agropecuário baixo, médio ou alto e identificar possíveis assimetrias ou valores extremos. | Análise exploratória da distribuição de dados econômicos. |
| 2  | Gráfico de Dispersão   | Representação gráfica da relação entre duas variáveis quantitativas por meio de pontos em um plano cartesiano. | Relação entre PIB Agropecuário e PIB Industrial, com linha de tendência e pontos coloridos de acordo com o PIB total. | Ajuda a identificar se microrregiões com maior produção agropecuária também tendem a possuir maior atividade industrial. | Identificação de correlações ou padrões entre setores econômicos. |
| 3  | Heatmap (Mapa de Calor)| Visualização de dados matriciais utilizando cores para representar intensidade ou magnitude dos valores. | Matriz de correlação entre os quatro setores econômicos (Agropecuário, Industrial, Serviços e outros). | Cores mais intensas indicam correlação mais forte entre os setores, permitindo identificar relações econômicas relevantes. | Análise de correlação entre variáveis econômicas. |
| 4  | Barras Empilhadas      | Gráfico de barras onde cada barra é subdividida em segmentos que representam diferentes categorias dentro do total. | Top 15 microrregiões por PIB total, mostrando a composição de cada setor econômico dentro do PIB da região. | Permite comparar não apenas o PIB total das regiões, mas também quais setores contribuem mais para a economia local. | Comparação da estrutura econômica entre microrregiões. |

---

## 📁 Estrutura do Projeto

```
📂 projeto/
├── main.py           ← script principal (com comentários didáticos)
├── Planilha_Estatística_Exploratória.xlsx  ← fonte de dados
├── 1_histograma.png ← Png Referenre ao gráfico de Histograma
├── 2_dispersao.png ← Png Referenre ao gráfico de Dispersão
├── 3_heatmap.png ← Png Referenre ao gráfico de Heatmap
├── 4_barras_empilhadas.png ← Png Referenre ao gráfico de Barras Empilhadas
└── README.md
```

---

## 💻 Instalação


Para rodar o Script é preciso instalar 3 bibliotecas. Abra o Terminal e Execute

```bash
pip install pandas matplotlib seaborn
```

Além disso, o **openpyxl** também é necessário para ler arquivos .xlsx com o pandas !!!

```bash
pip install openpyxl
```

---

## 📦 Bibliotecas utilizadas

| Biblioteca | Para que serve no projeto |
|---|---|
| `pandas` | Leitura do Excel, limpeza e manipulação dos dados |
| `matplotlib` | Motor base de renderização dos gráficos |
| `seaborn` | Camada visual de alto nível (gráficos mais bonitos com menos código) |
| `numpy` | Cálculo da linha de tendência (regressão linear simples) |
| `openpyxl` | Engine que o pandas usa internamente para ler arquivos `.xlsx` |

---

## 🗂️ Fonte de Dados

| Campo | Detalhe |
|---|---|
| **Fonte** | DEE-SPGG (Departamento de Economia e Estatística do RS) |
| **Série** | Contabilidade Social — Série 2002 em diante |
| **Indicador** | Valor Adicionado Bruto a Preços Básicos (PIB Setorial) |
| **Ano** | 2021 |
| **Unidade original** | R$ mil |
| **Unidade no script** | R$ milhões (dividido por 1.000) |

---

## 📈 Gráficos - Aprofundamento

### 1. 📊 Histograma — Distribuição do PIB Agropecuário

- **Arquivo:** ```1_histograma.png```

- **O Que é:** Um Histograma agrupa dados em intervalos (chamados **bins**) e mostra a 
frequência de ocorrência em cada intervalo. Aqui visualizamos quantas microrregiões têm um PIB
agropecuário dentro de cada faixa de valor

- **Conceitos Aplicados:**
    * `sns.histplot()` → cria o histograma
    * `ins=10` → número de barras (intervalos)
    * `ax.axvline()` → linha vertical de referência
    * `.mean()` e `.median()` → estatísticas descritivas básicas
    * **Média** vs **Mediana**: quando a média > mediana, os dados têm assimetria positiva (cauda longa à direita — poucos valores muito altos)

> **Porque usar um histograma aqui?** Ele é usado para compreender se a distribuição é uniforme ou concentrada, e identificar se existem microrregiões discrepantes - **outliers**

---

### 🔵 Gráfico de Dispersão — Agropecuária × Indústria

- **Arquivo:** ```2_dispersao.png``` 

- **O Que é:** Um gráfico de dispersão traça um ponto para cada microrregião, no qual o Eixo X é o PIB brasileiro e o Eixo Y é o 
PIB Industrial. Ele é útil para visualizar a correlação entre duas variáveis contínuas

- **Conceitos Aplicados:**
    * `ax.scatter()` → plota os pontos
    * `c=df["Total"], cmap="viridis"` → usa uma terceira variável para colorir os pontos
    * `np.polyfit(x, y, 1)` → calcula os coeficientes `m` (inclinação) e `b` (intercepto)
    da equação da reta `y = mx + b`
    * `ax.annotate()` → adiciona rótulos de texto junto a pontos específicos
    * `zorder` → controla qual elemento fica na frente quando há sobreposição

- **Interpretação**
    * Pontos Próximos da Linha de Tendência -> **Correlação Forte**
    * Pontos Espalhados -> **Correlação Fraca**
    * A cor do Ponto Indica o PIB total da microrregião

---

###  🌡️ Heatmap — Correlação entre Setores

- **Arquivo:** `3_heatmap.png`

- **O Que é:** Trata-se de um mapa de calor que exibe a **Matriz de Correlação de Pearson** entre todos os setores econômicos.
Cada célula indica o grau de relação entre dois setores, indo de **-1** a **+1**

> A **Pearson Correlation Coefficient** (coeficiente de correlação de Pearson) é **uma medida estatística que quantifica o grau de relação linear entre duas variáveis numéricas**.
Quando organizamos os coeficientes de várias variáveis em formato de tabela, chamamos isso de Matriz de Correlação de Pearson.

Assim, têm-se que:

| Valor  | Significado                  |
| ------ | ---------------------------- |
| **1**  | Correlação positiva perfeita |
| **0**  | Nenhuma correlação           |
| **-1** | Correlação negativa perfeita |


- **Conceitos Aplicados:** 
    * `df.corr()` → calcula automaticamente a correlação entre todas as colunas numéricas
    * `sns.heatmap()` → renderiza a matriz como mapa de calor
    * `annot=True` → exibe os valores numéricos nas células
    * `cmap="coolwarm"` → azul = correlação negativa, vermelho = positiva
    * `vmin=-1, vmax=1` → ancora a escala de cores nos extremos matemáticos

- **Tabela de Interpretação**

| Valor de Correlação | Interpretação |
|---|---|
| 0.90 a 1.00 | Correlação muito forte positiva |
| 0.70 a 0.89 | Correlação forte positiva |
| 0.40 a 0.69 | Correlação moderada |
| 0.00 a 0.39 | Correlação fraca |
| Negativo | Relação inversa |

---

### 📊 Barras Empilhadas — Top 15 Microrregiões
 
**Arquivo:** `4_barras_empilhadas.png`
 
**O Que é:** Um gráfico de barras horizontais onde cada barra representa o PIB total de uma microrregião, dividido em segmentos coloridos por setor econômico.
 
**Conceitos aplicados:**
    * `df.nlargest(n, "coluna")` → seleciona os N maiores valores
    * `sort_values("Total")` → ordena para que a maior fique no topo
    * `ax.barh()` → barra horizontal (mais legível com rótulos longos)
    * Acumulador `left` → cada setor começa onde o anterior terminou
    * `zip(lista1, lista2, lista3)` → itera três listas ao mesmo tempo

**Por que Barras Empilhadas?**

> **Permite comparar o total e a composição ao mesmo tempo** — algo que barras lado a lado ou um gráfico de pizza não conseguem fazer tão bem quando há muitas categorias.

---

## 🧠 Conceitos-chave de Python usados
 
### `iloc` vs `loc`
```python
df.iloc[7:]       # seleciona por POSIÇÃO numérica (7ª linha em diante)
df.loc[i, "col"]  # seleciona por RÓTULO (nome do índice e da coluna)
```
 
### List comprehension e `zip()`
```python
# zip() percorre múltiplas listas simultaneamente
for setor, label, cor in zip(setores, labels_s, CORES):
    ...  # a cada iteração, pega um elemento de cada lista
```
 
### Lambda functions nos formatadores
```python
# lambda x, _ : cria uma função anônima de uso único
# x = valor numérico do eixo | _ = posição (ignorada)
mticker.FuncFormatter(lambda x, _: f"R$ {x:,.0f} mi")
```
 
### f-strings com formatação numérica
```python
f"{valor:,.0f}"   # separador de milhar (,) e zero casas decimais (.0f)
f"{valor:.2f}"    # dois decimais
f"R$ {valor:.0f} mi"  # prefixo + sufixo personalizados
```
 
---
 
## 🎨 Customizações úteis para ir além
 
```python
# Mudar o estilo geral do seaborn
sns.set_theme(style="darkgrid")   # grade escura
sns.set_theme(style="ticks")      # minimalista com marcadores
 
# Paletas de cores prontas do seaborn
sns.color_palette("pastel")
sns.color_palette("Set2")
sns.color_palette("rocket")
 
# Salvar em alta resolução para impressão
fig.savefig("grafico.png", dpi=300, bbox_inches="tight")
 
# Salvar em PDF (vetorial, sem perda de qualidade)
fig.savefig("grafico.pdf", bbox_inches="tight")
```
 
---
 
## 📚 Para aprender mais
 
| Recurso | Link |
|---|---|
| Documentação Pandas | https://pandas.pydata.org/docs/ |
| Galeria Seaborn | https://seaborn.pydata.org/examples/ |
| Galeria Matplotlib | https://matplotlib.org/stable/gallery/ |
| Tutorial NumPy | https://numpy.org/learn/ |
 
---
 
## 👨‍💻 Autor - Lucas Oliveira e Caua Landa
 
Projeto desenvolvido como trabalho de **Estatística Exploratória** com
foco em visualização de dados econômicos regionais do Rio Grande do Sul.