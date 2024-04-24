listaNumeros = []
print("Lista vazia: ", listaNumeros)

qtd_val = int(input("qtd values: "))

for elements in range(qtd_val):
    valor = int(input("> value: "))
    listaNumeros.append(valor)

print(f"Lista com valores: {listaNumeros}")

del listaNumeros[0]
print(listaNumeros)