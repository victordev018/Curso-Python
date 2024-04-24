'''
Crie um programa com um loop for e uma declaração break . O programa deve iterar sobre os caracteres 
de um endereço de e-mail, sair do loop quando chegar ao símbolo @ , e imprimir a parte antes de @ 
numa linha. Use o esqueleto abaixo:
'''

email = input("Digite um endereço de email: ")

for letra in email:
    if letra == "@":
        break
    print(f"{letra}", end="")