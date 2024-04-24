# usando o loop for para inserir valores para uma lista vazia:
lista = []
for i in range(5): #adicionando 5 elementos, lembrando que começa no 0 e 5 não é incluso.
    value = int(input(f"{i+1}° value: "))
    lista.insert(i, value)

print("\nLista: ", lista, "Length: ", len(lista))

print("\nSoma valores da lista:")
soma = 0
for i in lista:
    soma += i
print("\nSoma: ", soma, "\n")

# trocando de posição alguns elementos da lista:
print("\nTrocando de posição os elementos:")
lista[0], lista [4] = lista[4], lista[0]
print("\nLista atualizada: ", lista)