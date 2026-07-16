# Cati.Jr-Trainee-Dados

Esse é o meu processo para evoluir durante o processo de trainee da Cati.Jr para analista de dados, o conteúdo deve ser atualizado semanalmente mostrando o que aprendi durante cada período. 

# Semana 1 

O foco dessa semana foi revisar alguns conceitos básicos de estatística e estudar as bibliotecas NumPy e Pandas através do curso de Data Analytics da Rocketseat

## Estatística

Foi realizada uma revisão dos conceitos:

- Média 
- Mediana
- Amplitude
- Desvio padrão
- Quartis
- Entre outros

## NumPy

Foram entendidos todos os comandos básicos da biblioteca NumPy. Para consolidar o aprendizado, foi resolvido um exercício da plataforma LeetCode o problema **217 - Contains Duplicate**.

### Problema **217 - Contains Duplicate**

Dado um vetor de números inteiros, determinar se existe algum elemento repetido. O objetivo não era encontrar a solução mais otimizada, mas sim provar que essa biblioteca pode resolver problemas aparentemente complexos em poucas linhas de forma intuitiva.

**Solução**

```python
import numpy as np

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums = np.array(nums)
        tamanho_original = nums.size

        nums = np.unique(nums)
        tamanho_novo = nums.size

        if (tamanho_novo == tamanho_original):
            return False
        else:
            return True
```
## Pandas

Por enquanto só os primeiros vídeos da plataforma foram vistos, o que permitiu de início criar um conceito básico sobre os objetivos e potenciais da biblioteca. Além disso, já foi possível entender a manipulações de arquivos csv e excel. Abaixo há um código em que se importou de um dataset de treinamento de IA com dados de flores, em seguida este arquivo foi salvo dentro do colab.

```python
import pandas as pd

url = 'https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv'

df = pd.read_csv(url)

print(df)

df.to_csv ('iris.csv', index = False)
```

Link do colab: https://colab.research.google.com/drive/15O_bKWJhVRKXv_imxC2LH2QjoQo8iLJO?usp=sharing

# Semana 2

Nessa segunda semana foram estudadas as aulas de Pandas e coleta de dados da Rocketseat

## Aprofundando em Pandas

As aulas foram assistidas por completo na qual foi possível aprender todo o básico sobre a biblioteca, incluindo:

- Head, Shape, Info, Describe
- Loc e Illoc
- Ordenação
- Filtragens Apply e Map
- Concatenação de DataFrames

## Coleta de dados

Foi aprendido a ler dados de APIs e do Google Drive. Além disso, entendi como usar comandos SQL em Python (já tenho o conhecimento de SQL de outros projetos próprios em meu GitHub.)

Segue o link do colab em que foi aplicado todo o aprendizado da semana, os dados vieram de uma planilha de jogos da Indian Premier League (IPL): https://colab.research.google.com/drive/1rIkbhMLLrdvgf5cJltSEd4kc99YjENyt?usp=sharing 

## House Prices Kaggle

Dei uma breve olhada no dataset da atividade e já comecei a refletir em como implementar modelos de IA. Por exemplo, o modelo k-médias prediz a classe de um certo objeto, já que o algoritmo deve devolver um número do preço do imóvel e não só uma classificação ("Preço alto", "Preço baixo", etc), deve-se pensar em uma maneira de adaptar o código ou os dados.

# Semana 3

A semana 3 teve como foco o final da sessão de Data Analytics e o início do aprendizado em machine learning.

## Tratamento de dados

Nessa semana aprendi conceitos muito importantes sobre como identificar e lidar com **duplicatas, valores ausentes e outliers**. Além de outros conceitos como:

- Plotagem de gráficos
- Correlação + Heatmap
- Normalização
- One hot e Label Encoding

## Primeiro teste com machine learning

Segue o link do colab que consiste em uma implementação do modelo linear do scikitlearn em um dataset simples de uma clínica. O objetivo foi tratar os dados e criar um código para prever o custo do seguro de saúde, com base na idade, gênero, IMC, quantidade de filhos, se é fumante e a região.

https://colab.research.google.com/drive/1WuiPqPrTFdTK5WSJgQyhHUEueNQNSs9T?usp=sharing

# Semana 4

Como sugerido, nessa semana começou-se os procedimentos no dataset de House Prices.

Segue o link do colab: https://colab.research.google.com/drive/1XHAeAK-TeyHjPVSqJ6KpH5KKPdGV3_je?usp=sharing

Além disso, também foram aprendidos os seguintes conceitos e como implementá-los em Python:

- K-fold
- Pipeline de pré-processamento
- Teste de normalidade
- Salvamento de modelos e API

# Semana 5

Concluiu-se o tratamento de dados do dataset de House Prices, com destaque para as seguintes decisões:

- Os valores nulos da coluna LotFrontage foram subsituídos a partir de um modelo de regressão linear usando outras duas colunas: LotArea e LotConfig. Como queria-se aproximadamente a medida da casa que tinha contato com a rua, não é difícl perceber que esse valor é proporcional à raiz quadrada da área e linearmente proporcional a configuração do lote. Assim, esses valores ausentes foram aproximados pela fórmula: c2 * ​LotConfig + c1 * sqrt(LotArea) + c0. Nos quais c2, c1 e c0 são constantes.
- Ao se calcular o número de outliers o resultado foi superior a 10% dos dados. Com isso, ao invés de retirar todos eles, somente os valores de SalePrice (coluna alvo) maiores que 500000 foram excluídos. O que totalizou menos de 1% da amostra, garantindo que informações cruciais não fossem perdidas.
- Colunas não numéricas com mais 10 elementos únicos foram tratadas com target-encoding ao invés de one-hot-encoding, para evitar sobrecarga de colunas e garantir melhor generalização. Vale destacar que **essa técnica alternativa foi aprendida durante esta semana enquanto pesquisava em como tratar casos do gênero**.

Foram feitos dois treinamentos do modelo de regressão linear, um sem K-Fold e outro com (5-Fold). Seguem os resultados medidos com a métrica de R² score:

| Método | Resultado |
|--------|----------:|
| Sem K-Fold | 0.860 |
| Com K-Fold (média ± desvio padrão) | 0.765 ± 0.126 |

Conclui-se que esse modelo de regressão linear pareceu ter um bom resultado à primeira vista, mas ao se analisar o resultado do 5-Fold percebe-se que essa generalização não é tão boa assim. Logo, outros modelos de Machine Learning devem ser testados.

# Semana 6

Nesta semana foram testados os algoritmos K-Means, KNN e MPLRegressor. Além do mais, foi implementado o streamlit, permitindo aos usuários preverm o valor de uma casa ao fornecerem algumas informações.

## K-Means

O pré-processamento foi praticamente idêntico ao do algoritmo de regressão linear, a única diferença é que usou-se o ordinal encoding em colunas não numéricas de mais de 10 elementos únicos. Essa decisão foi tomada porque não é possível usar target encoding em algoritmos não supervisionados, que é o caso do k-means.

Analisando o gráfico do cotovelo, o valor ideal para K (número de agrupamentos) foi 4 e o erro foi de 40000 unidades.

## KNN

Após o pré-processamento do algoritmo da regressão linear, os números da coluna "SalePrice" foram transformadas em strings. Foi testado o algoritmo com K = 4 e K =3, respectivamente foram usadas essas fórmulas para adaptar os dados da coluna alvo.

Foi feito uma iteração para descobrir qual o melhor k (vizinhos) para esse problema.

```python
# 4 classes
def categoria(preco):
    if preco <= 129900:
        return "Low"
    elif preco <= 162500:
        return "Low-Average"
    elif preco <= 213000:
        return "High-Average"
    else:
        return "High"

# 3 classes
def categoria(preco):
    if preco <= 129900:
        return "Low"
    elif preco <= 213000:
        return "Average"
    else:
        return "High"
```
Os dados foram separados com base nas informações da tabela df.describe().

## MPLRegressor

Modelo de rede neural adaptado para devolver valores numéricos ao invés de atribuir grupos. Esse algoritmo foi o pior até o momento, possivelmente por ser muito complexo para um problema com relativamente "poucos dados".

## Resultados Obtidos

| Algoritmo | Métrica | Melhor Configuração | Resultado |
|-----------|----------|--------------------|-----------|
| K-Means | Método do Cotovelo | K = 4 | Erro: **40.000** |
| KNN (3 classes) | Acurácia | k = 3 | **0,81** |
| KNN (4 classes) | Acurácia | k = 13 | **0,78** |
| MLPRegressor | R² Médio | default | **0,509 ± 0,048** |

## Streamlit

Como a tabela possuí muitas colunas seria inviável ao usuário ter que digitar todas elas. Por isso, usando um gráfico de correlação, viu-se que os 3 atributos com maior impacto no "SalePrice" eram: área de vivência, quantidade de carros que cabem na garagem e qualidade geral.

Assim, treinou-se um modelo só com esses 3 atributos.

# Semana 7

Testes e resultados finais.

## Comparação dos Modelos

| Tratamento dos Outliers | Linear Regression (R² ± DP) | Random Forest (R² ± DP) | Gradient Boosting (R² ± DP) |
|-------------------------|----------------------------:|------------------------:|----------------------------:|
| Sem remoção | **0.715 ± 0.171** | **0.917 ± 0.011** | **0.931 ± 0.007** |
| Remoção > 700000 | **0.809 ± 0.113** | **0.910 ± 0.020** | **0.919 ± 0.017** |
| Remoção > 500000 | **0.765 ± 0.125** | **0.868 ± 0.024** | **0.877 ± 0.040** |
| Remoção de todos os outliers | **0.785 ± 0.121** | **0.924 ± 0.005** | **0.926 ± 0.008** |

## Resultados do Ensemble

| Tratamento dos Outliers | R² | MSE | RMSE | Kaggle Esperado (Log-RMSE) |
|-------------------------|---:|------------:|---------:|---------------------------:|
| Sem remoção | **0.939** | 404.397.464 | 20.110 | **0.01012** |
| Remoção > 700000 | **0.932** | 358.910.102 | 18.945 | **0.01056** |
| Remoção > 500000 | **0.903** | 468.213.205 | 21.638 | **0.01800** |
| Remoção de todos os outliers | **0.924** | 269.250.694 | 16.409 | **0.01143** |
