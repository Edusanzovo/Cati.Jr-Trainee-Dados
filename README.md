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

Foram entendidos todos os comandos básicos da biblioteca NumPy. Para consolidar o aprendizado, foi resolvido um exercício da plataforma LeetCode o problema **217 - Contains Duplicate** da plataforma LeetCode.

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

Por enquanto só os 2 primeiros vídeos da plataforma foram vistos, o que permitiu de início criar um conceito básico sobre os objetivos e potenciais da biblioteca.
