# encontrar o numero da vida pela data do aniverário:
data_nasc = input("Informe sua data de nascimento: (AAAAMMDD): ")
vetor_data_nasc = data_nasc.split()
print(vetor_data_nasc)


def somarLista(vetor):
    soma = 0
    for elements in vetor:
        soma += elements
    return soma

# faça jota