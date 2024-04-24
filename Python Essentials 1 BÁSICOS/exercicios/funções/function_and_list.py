
# função para somar valores de uma lista
def sumValueList(lista):
    s = 0 # soma
    for element in lista:
        s += element
    return s # retorna soma

# adicionando valores em uma lista vazia:
numList = []
qtd_elements = int(input("\nQuantos valores deseja colocar na lista? "))
for i in range(qtd_elements):
    value = int(input(f"{i+1}° value: "))
    numList.append(value)
print("\nLista: ", numList)

# invocando função para calcular a soma dos elementos dessa lista:
somaElements = sumValueList(numList)
print("\nSoma: ", somaElements, "\n")