# criamos uma matriz 8x8
tabuleiro = []
empity = " - "

# for i in range(8):
#     row = [0 for j in range(8)] # criando linhas com oito elemnetos 
#     tabuleiro.append(row)
# print(tabuleiro, "\n")

# podemos fazer da seguinte forma:
tabuleiro = [[empity for i in range(8)] for j in range(8)]

# adicionando valores a campos específicos da matriz, localizando 
# pelo 1° index que corresponde a linha e o 2° a coluna
tabuleiro[0] [0] = "rock"
tabuleiro[0] [7] = "rock"
tabuleiro[7] [0] = "rock"
tabuleiro[7] [7] = "rock"
print(tabuleiro)