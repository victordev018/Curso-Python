# random(), produz um número float x vindo do intervalo (0.0, 1.0)

# gerando 5 valores aleatórios:
from random import random

print("\nSeed padrão: ")
for elements in range(5):
    print(random())

from random import seed

print("\nSeed 0: ")
# seed(0)

for elements in range(5):
    print(random())

# gerando valores aleatórios com randint(left, right)
from random import randint
print("\nvalores inteiros aleatório entre 5 e 10: ")

for elements  in range(5):
    print(randint(5,10))

# choice() escolhe um elemento aleatório a partir de uma sequência
lista = [1, 2, 3, 4, 5, 6 , 7 , 8, 9]
from random import choice
print("\nchoice: ", choice(lista))

# sample(), constroi uma lista acom elementos "aleatórios" de uma sequência:
from random import sample
print("\nSample(lista, 9): ", sample(lista, 9))