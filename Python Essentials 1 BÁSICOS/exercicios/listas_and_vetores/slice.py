# copiar valor(es) de uma lista para outra:
# usamos o slice, lista2 = lista1[start, end]
# start é o index do primeiro elemento incluido no slice; end, index do  primeiro elemento não incluido no slice.

lista1 = [1, 2, 3, 4, 5]
print("\nLista 1: ", lista1)
lista2 =lista1[2:4]
print("Lista 2: ", lista2, "\n")

# omitindo o start, endende-se que o start é index 0:
print("\nOmitindo o start:")
lista2 = lista1[:3]
print("Lista: ", lista2)

# omitindo o end entendes-se que que o end é o comprimeto da lista: len(lista2).
print("\nOmitindo o end:")
lista2 = lista1[3:]
print("Lsita: ", lista2)

# omitindo ambos, fará uma cópia de toda a lista:
print("\nOmitindo start e end:")
lista2 = lista1[:]
print("LIsta: ",lista2 )

# usando a funcção del junto com slice para apagar elementos específicos ou até mesmo todos de uma lista.
# deletando elementos de index 0 até o index 1
print("\nApagando 2 elemnetos da lista:")
del lista1[0:2]
print("Lista: ", lista1)

# deletando toda o conteudo da lista:
print("\nDeletando todos os elemntos:")
del lista1[:]
print("Lista: ", lista1)

# del lista1, apagará a lista, não seus elementos