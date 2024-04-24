'''
Houve uma vez um chapéu. O chapéu não continha nenhum coelho, mas uma lista de cinco números: 1, 2, 3, 4, e 5.

A sua tarefa é:

escrever uma linha de código que peça ao utilizador para substituir o número médio na lista por um número inteiro 
introduzido pelo utilizador (Passo 1)
escrever uma linha de código que remova o último elemento da lista (Passo 2)
escrever uma linha de código que imprima o comprimento da lista existente (Passo 3).

'''

chapeu_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# alterando o numero medio da lista, no caso o 5, de index 4.
chapeu_list[4] = int(input("new value: "))

# removendo o último elemento da lista
del chapeu_list[-1]

# imprimindo o comprimento da lista:
print("\nLength list: ", len(chapeu_list))
print(chapeu_list, "\n")