# alterando o valor de uma das posições de uma lista de números.

numbers = [10, 23, 67, 89, 99]

print("\nLista inicialde valores: ")
print("\nLista: ", numbers)

print("\nLista de valores alterando o valor de index 2")
numbers[2] = 200 # atribuindo um outro valor a elemneto de posição 2 da lista
print("\nLista: ", numbers)

# copiando o valor do 5° elemento para o 1° elemneto
print("\nLista de valores copiando o elemneto de index 5 para o de posição 1")
numbers[0] =  numbers[4]
print("\nLista: ", numbers)

# conseguindo o tamanho (length) da lista
print("\nApresentando o tamanho da lista")
tamannho = len(numbers)
print("\nLength List: ", tamannho)

# funciona tambem da seguinte maneira:
# print("\nLength List: ", len(numbers))

# removendo um item da lista:
print("\nRemovendo o 5° item da lista:")
del numbers[4]
print("Length List: ", len(numbers), " elements: ", numbers, )

# index negativo:
print("\nIndex negativo")
print(numbers[-1]) #apresentará o último valor da lisa
print(numbers[-2]) #apresentará o penúltimo valor da lista

#adicionando novos valores na lista usando os seguintes métodos:

#append(value): aidiciona o novo valor passado como argumento para o final da lista
print("\nAcicionando novos valores na lista: ")
print("\nAppend:")
numbers.append(24)
print("\nLenght list: ", len(numbers), "\nElements: ", numbers)

#insert(location, value): adiciona um novo valor em um index(posição) específica passada como argumeto
print("\nInsert:")
numbers.insert(2, 25)
print("\nLenght list: ", len(numbers), "\nElements: ", numbers)