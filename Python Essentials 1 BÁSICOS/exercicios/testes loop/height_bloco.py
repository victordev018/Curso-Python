'''
A sua tarefa é escrever um programa que leia o número de blocos que os construtores têm,
e que produza a altura da pirâmide que pode ser construída utilizando estes blocos.
Nota: a altura é medida pelo número de camadas completamente preenchidas - se os 
construtores não tiverem um número suficiente de blocos e não conseguirem completar a camada seguinte, 
terminam o seu trabalho imediatamente.
'''

num_blocos = int(input("Numeros de blocos: "))

linha_atual = 0
blocos_empilhados = 0
while num_blocos > 0:
    blocos_empilhados += 1
    if blocos_empilhados % (linha_atual+1) == 0:
        blocos_empilhados = 0
        linha_atual += 1
    num_blocos -= 1

print(f"altura: {linha_atual}")

# valeu patrocinio