# exibir o maior numero de uma lista>

listaNum = [1, 6, 8, 98, 77, 56]

maior = listaNum[0]

for i in listaNum[1:]:
    if i > maior:
        maior = i
print("\nMaior numero: ", maior)