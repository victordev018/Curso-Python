# criando lista beatles vazia:
beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("\nCompoentes da banda the beatles: ", beatles)

#adicionando mais dois integrantes na lista da banda
print("\nAdicione mais dois integrantes na banda: ")
for i in range(2):
    integrante = input(f"{i+1}° integrante: ")
    beatles.append(integrante)
print("\nCompoentes da banda the beatles: ", beatles)

#Deletando os dois ultimos integrantes recem adicionados na lista
print("\nDeletando os dois ultimos adicionados na banda:")
del beatles[-2]  # deleta o último elemento
del beatles[-1]  # deleta o penútimo elemento
print("\nCompoentes da banda the beatles: ", beatles)

# adicionando um novo integrande na lista, desta vez na posição (index) 1.
print("\nAdicionando mais um na 1° posição:")
integrante = input("integrante: ")
beatles.insert(0, integrante)
print("\nCompoentes da banda the beatles: ", beatles)

