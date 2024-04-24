# vamos encontrar a posição de um adado elemento:

lista = [1, 3, 6, 9, 8]
numero = 6
aux = False

for i in range(len(lista)):
    if lista[i] == numero:
        break
print("\nLista:", lista)
print(f"\nPosição do numero {numero} é {i}")