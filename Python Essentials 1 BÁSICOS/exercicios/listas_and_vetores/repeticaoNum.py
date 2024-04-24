# remova os numeros repetidos de uma lista

lista = []
# adicionando valores a uma lista vazia:
for i in range(5):
    value = int(input(f"{i+1}° value: "))
    lista.append(value)

listaTemporaria = []

print("\nLista: ", lista)

for element in lista:
    if element not in listaTemporaria:
        listaTemporaria.append(element)
print("\nLista sem repetiçôes: ", listaTemporaria, "\n")


    