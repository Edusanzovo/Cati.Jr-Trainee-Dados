# Cati.Jr-Trainee-Dados

Esse é o meu processo para evoluir durante o processo de trainee da Cati.Jr para analista de dados, o conteúdo deve ser atualizado semanalmente mostrando o que aprendi durante cada período. Não será usado auxílio de inteligências artificiais desde a escrita do README até os códigos, para que essa experiência seja a mais orgânica possível. Caso seja necessário o uso em algum momento, **estará explicitamente dito**.

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

Nessa semana aprendi conceitos muito importantes para tratamento de dados, sobre como identificar e lidar com **duplicatas, valores ausentes e outliers**. Além de outros conceitos como:

- Plotagem de gráficos
- Correlação + Heatmap
- Normalização
- One hot e Label Encoding

Segue o link do colab que consiste em uma implementação do modelo linear do scikitlearn em um dataset simples de uma clínica. O objetivo foi tratar os dados e criar um código para prever o custo do seguro de saúde, com base na idade, gênero, IMC, quantidade de filhos, se é fumante e a região.

https://colab.research.google.com/drive/1WuiPqPrTFdTK5WSJgQyhHUEueNQNSs9T?usp=sharing
