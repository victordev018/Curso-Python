# contador para saber quantas vezes as funções foram invocadas:
# counter = 0

# uso da variável __name__ para verificar o ambiente de execução
# if __name__ == "__main__":
#     print("estamos no nosso modulo...")
# else:
#     print("estamos na nossa main...")

# convenção: quando não queremos que uma entidade não seja modificada,
# denominanos seu nome com esse padrão: "__nameEntidade__", esta é uma
# convenção, não necessariamente será respeitada pelos utilizadores.

#!/usr/bin/env python3 

"""este módulo faz operações com valores de lista"""

__counter = 0

# método para calcular valores de uma lista.
def sumL(lista):
    global __counter
    __counter += 1
    soma = 0
    for element in lista:
        soma += element
    return soma

def prodL(lista):
    global __counter
    __counter += 1
    prod = 1
    for element in lista:
        prod *= element
    return prod

# verificar se as funções estão funcionando coretamente
if __name__ == "__main__":
    print("estamos no nosso módulo...")
    listinha = [element+1 for element in range(5)]
    print(sumL(listinha) == 15) # se estiver ok, print True
    print(prodL(listinha) == 120) # se estiver ok, print True

