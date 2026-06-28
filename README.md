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
| Com K-Fold (média ± desvio padrão) | 0.755 ± 0.132 |

Conclui-se que esse modelo de regressão linear pareceu ter um bom resultado à primeira vista, mas ao se analisar o resultado do 5-Fold percebe-se que essa generalização não é tão boa assim. Logo, outros modelos de Machine Learning devem ser testados.
