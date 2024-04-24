# neste código iremos ordenar uma lista

lista = [1, 4, 3, 8, 5]

print("\nLIsta: ", lista)

passagem = True
while passagem:
    passagem =  False  # caso os elementos ja estejam ordenados ele não entrará no loop
    for i in range(len(lista ) - 1):
        if lista[i] > lista[i +1 ]: # compardando se o primeiro elemento do par é maior que o segundo
            passagem = True
            lista[i], lista[i+1] = lista[i+1], lista[i] # se for true, será trocado de posição os valores

print("\nLista atualizada: ", lista)

# Ordenando nova lista com interação do usuário:
print("\nInsira os valores da nova lista:")
lista2 = []

# adicionando 5 elementos em uma lista vazia
for i in range(5):
    value = int(input(f"{i+1}° Value: "))
    lista2.append(value)
print("\nLista 2: ", lista2)

# ordenando os elementos da minha lista:
passagem = True
while passagem:
    passagem = False
    for i in range(len(lista2) - 1):
        if lista2[i] > lista2[i+1]:
            passagem = True
            lista2[i], lista2[i+1] = lista2[i+1], lista2[i]
print("\nLista 2 ordenada: ", lista2, "\n")

# segunda maneira de ordenar uma lista
listinha = [1, 9, 8, 7, 3]
print("\nLista 3: ", listinha)
listinha.sort() # método sort(), oedena a lista em de maneira crescente
print("\nLista ordenada: ", listinha)

# invertendo os valores de uma lista:
listinha.reverse()
print("\nLista invertida: ", listinha)