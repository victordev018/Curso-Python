# dicionários, não é uma lista, é um tipo de dado que tem uma chave e um valor (key-value).

# agenda telefonica com seus identificadores
agendaTelefonica = {"mamae" : 8242342642, "papai": 1983782432}

# chaves de identificadores que será procurada
chaves = ["mamae", "papai", "vovo"]

# exibindo todo o dicionário
print("\nAgenda: ", agendaTelefonica)

# exibindo um elemento específico
print("\nNumber mamae: ", agendaTelefonica["mamae"])
print("Number papai: ", agendaTelefonica["papai"])

# varrendo dicionáro verificando se possue ou não um elemento com as chaves listadas
for word in chaves:
    if word in agendaTelefonica:
        print("\n", word, "-> ", agendaTelefonica[word])
    else:
        print("\n",word, "not is in Agenda Telefonica\n")

# dicionário e for usando o método keys():
for key in agendaTelefonica.keys(): # metodo keys(), permite que o dicionário seja iterável
    print(key, "--> ", agendaTelefonica[key])

# utilizando o método items()
print("\nMetodo item():")
for parent, number in agendaTelefonica.items(): # cada tuple recebe um key_value(cahve-valor)
    print(parent, "--> ", number)

# usando o método values():
print("\nMétodo values(): ")
for values in agendaTelefonica.values(): # este recebe somente os valores do dicionário.
    print(values)

# alterando o valor de uma chave:
print("\nAlterando telefone de mamae")
agendaTelefonica["mamae"] = 111111111
for parent, number in agendaTelefonica.items():
    print(parent, "-> ", number)

# adicionando novo valor key-value:
print("\nAdicionando novo par key-value:")
agendaTelefonica["vovo"] = 999999922 # chave previamente inexistente
for parent, number in agendaTelefonica.items():
    print(parent, "-> ", number)
# pode adicionar usando o método update({key:value})

# removendo um par de dados(key-value) de um dicionário:
print("\nRemovendo um elemento do dicionário: ")
del agendaTelefonica["papai"]
for parent, number in agendaTelefonica.items():
    print(parent, "-> ", number)

# pode copiar o dicionário utilizando o método copy()
print("\nCopiando um dicionário")
animals = {
    1 : "cats",
    2 : "dogs", 
    3 : "coelho"
}

animais2 = animals.copy()
for parent, number in animais2.items():
    print(parent, "-> ", number)

