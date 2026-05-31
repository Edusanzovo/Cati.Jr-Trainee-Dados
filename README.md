# Cati.Jr-Trainee-Dados

# Semana 1 

O foco dessa semana foi revisar alguns conceitos básicos de estatística e estudar as bibliotecas NumPy e Pandas através do curso de Data Analytics da Rocketseat

## Estatística Descritiva

Foi realizada uma revisão dos conceitos:

- Média 
- Mediana
- Amplitude
- Desvio padrão
- Quartis
- Entre outros

## NumPy

Foram entendidos todos os comandos básicos da biblioteca NumPy. Para consolidar o aprendizado, foi resolvido um exercício da plataforma LeetCode o problema **217 - Contains Duplicate** da plataforma LeetCode.

### Problema **217 - Contains Duplicate**

Dado um vetor de números inteiros, determinar se existe algum elemento repetido.

**Solução**

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

## Pandas

Por enquanto só os 2 primeiros vídeos da plataforma foram vistos, o que permitiu criar um conceito básico sobre os objetivos e potenciais da biblioteca.
