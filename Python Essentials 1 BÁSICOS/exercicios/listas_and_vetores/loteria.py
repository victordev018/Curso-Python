# verificar quantos acertos fez dos nueros sorteados na loteria

numSorteados = [11, 22, 24, 55, 69]
print("\nLista de numeros sorteados: ", numSorteados)
print("\nInforme os números de seu bulhete:")
numBilhete = []

for i in range(5):
    value = int(input(f"{i+1}° value: "))
    numBilhete.append(value)
print("\nSeu bilhete: ", numBilhete)

acertos = 0
print("\nCalculando acertos:")

for value in numBilhete:
    if value in numSorteados: # se o valor de index i estiver nos numeros sorteados, será incrementado +1
        acertos+=1
print("Quantidade de acertos: ", acertos,"\n")
