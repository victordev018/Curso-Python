# construir um jogo da velha

#função para verificar se há um ganhador
def verificarGanhador():
    houveVencedor = False

    # Checa linhas horizontais
    houveVencedor = checarLinhasHorizontais()
    if houveVencedor: return True

    # Checar linhas verticais
    houveVencedor = checarLinhasVerticais()
    if houveVencedor: return True

    # Checar diagonal principal
    houveVencedor = checarDiagonalPrincipal()
    if houveVencedor: return True

    return houveVencedor

def checarLinhasHorizontais():
    campeao = ""
    # Percorrer todas as linhas
    for y in range(len(tabuleiro)):
        campeao = checarCampeaoDaLinha(tabuleiro[y])
        
        # Ignorar proximas linhas caso já tenhamos um campeão
        if campeao != "":
            break
    
    return True if campeao != "" else False

def checarLinhasVerticais():
    campeao = ""

    # Checando uma coluna de cada vez:
    numeroDeColunas = len(tabuleiro[0])
    for x in range(numeroDeColunas):
        novaLinha = []
        # Em cada linha, adicionar o elemento da coluna especifica
        for y in range(len(tabuleiro)):
            linha = tabuleiro[y]
            elementoDessaColuna = linha[x]
            novaLinha.append(elementoDessaColuna)

        # Com a linha pronta, checar se houve campeão
        campeao = checarCampeaoDaLinha(novaLinha)

        if campeao != "": 
            break
    
    return True if campeao != "" else False

def checarDiagonalPrincipal():
    campeao = ""
    
    novaLinha = []
    # percorrendo linhas:
    for x in range(len(tabuleiro)):
        linha = tabuleiro[x]
        elemento = linha[x]
        novaLinha.append(elemento)

    # Com a linha pronta, checar se hoyve campeão
    campeao = checarCampeaoDaLinha(novaLinha)
    return campeao != ""
        

# Avalia se todos os elementos sao iguais, e retorna-o
def checarCampeaoDaLinha(linha):
    campeao = ""
    piloto = linha[0]
    if piloto == '| |':
        return campeao
    # Percorrer todos os elementos da linha
    for x in range(len(linha)):
        elemento = linha[x]
        if elemento != piloto: 
            break
        # Estou no ultimo elemento
        if x == len(linha) - 1:
            campeao = elemento
            print(f"Temos um campeão: {campeao}")

    return campeao

        
    

# função para atribuir x ou o no tabuleiro:
def atribuirElementoNoTab(jogada, val):
    if jogada == 'A1':
        tabuleiro[0][0] = f'|{val}|'
    elif jogada == 'B1':
        tabuleiro[0][1] = f'|{val}|'
    elif jogada == 'C1':
        tabuleiro[0][2] = f'|{val}|'
    elif jogada == 'A2':
        tabuleiro[1][0] = f'|{val}|'
    elif jogada == 'B2':
        tabuleiro[1][1] = f'|{val}|'
    elif jogada == 'C2':
        tabuleiro[1][2] = f'|{val}|'
    elif jogada == 'A3':
        tabuleiro[2][0] = f'|{val}|'
    elif jogada == 'B3':
        tabuleiro[2][1] = f'|{val}|'
    else:
        tabuleiro[2][2] = f'|{val}|'

# função de jogadas:
def novaJogada(jogagdor):
    if jogagdor == 'x':
        print("\nSua jogada deve indicar por linha e coluna.")
        jogada = input(f"em qual posição deseja jogar X ?")
        atribuirElementoNoTab(jogada, 'X')
    else:
        print("\nSua jogada deve indicar por linha e coluna.")
        jogada = input(f"em qual posição deseja jogar O ?")
        atribuirElementoNoTab(jogada, 'O')


# função de exibir tabuleiro
def exibirTbauleiro():
    print("\n")
    print("> JOGO DA VELHA <\n")
    print("   A   B   C")
    c = 0
    for linha in tabuleiro:
        c += 1
        print(c, end=" ")
        for element in linha:
            print(element, end=" ") 
        print("\n")

alguemVenceu = False
# criando o tabuleiro com um arrey bidimensional
tabuleiro = [[ '| |' for element in range(3)] for line in range(3)]
c = 2
while not alguemVenceu:
    exibirTbauleiro()
    if c % 2 == 0:
        novaJogada('x')
    else:
        novaJogada('O')
    exibirTbauleiro()
    alguemVenceu = verificarGanhador()
    c += 1
    
    
print("\npartida finalizada!!\n")
