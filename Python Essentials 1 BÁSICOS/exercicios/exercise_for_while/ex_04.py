'''
Crie um programa com um loop for e uma declaração continue . O programa deve iterar sobre 
uma string de dígitos, substituir cada 0 com xe imprimir a string modificada no ecrã. Use 
o esqueleto abaixo:
'''

string = input("string: ")

for caractere in string:
    if caractere == "0":
        print("x", end="")
        continue
    print(f"{caractere}", end="")