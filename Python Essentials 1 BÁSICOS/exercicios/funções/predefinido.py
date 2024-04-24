# usando função com o valor de um de seus parãmetros já pré-definidos.

def showName(namePrimary, nameSecundary = "Victor"):
    print("\nYour name: ", namePrimary,nameSecundary)

name = input("primeiro nome: ")
showName(name)