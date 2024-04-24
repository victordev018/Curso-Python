lista = [1,1,2,4,5,5]

auxiliar = []

for i in lista:
    if i in auxiliar:
        continue
    auxiliar.append(i)

print(auxiliar)