# importando o módulo math:
import math

# qualificando pi e sin, com seu módulo de origem:
math.pi
math.sin

# valor de seno de pi sobre dois:
print(math.sin(math.pi / 2))  # output: 1.0

# provando que não há conflito quando definimos nosso proprio pi e sin:

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print("nossa função: ",sin(pi/2) )
print("modulo math: ",math.sin(math.pi / 2) )

# indica precisamente qual a entidade (ou entidades) do módulo que é aceitável no código:

#Do modulo math,  import o método pow
from math import pow

# não necessariamente precisa da qualificação do modulo math:
print("4 expoente 2: ", pow(4, 2))

# importando todos os métodos de um módulo:
from math import *

# aliasing: mudando o nome de um determinado módulo:
import math as matematica
print("Matematica pow: ",matematica.pow(2, 2))

# para mudar o nome de um método de um módulo:
from math import pow as exponeciacao
print("exponeciação 3, 2: ",exponeciacao(3, 2))

# dir() é capaz de revelar todos os nomes fornecidos através de um determinado módulo
# import math

# for name in dir(math):
#     print(name, end="\t")

