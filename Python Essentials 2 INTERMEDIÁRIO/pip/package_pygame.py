

import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False

# explicação linha a linha:

# linha 1: importar o pygame e deixá-lo servir-nos;
# linha 3: o programa será executado enquanto a variável run for True;
# linhas 4 e 5: determinar o tamanho da janela;
# linha 6: inicializar o ambiente do pygame;
# linha 7: preparar a janela de aplicação e definir o seu tamanho;
# linha 8: fazer um objeto representando a fonte padrão de tamanho 48 pontos;
# linha 9: fazer um objeto representando um determinado texto - o texto será anti-aliased (True) e branco (255,255,255)
# linha 10: inserir o texto no buffer do ecrã (atualmente invisível);
# linha 11: virar os buffers do ecrã para tornar o texto visível;
# linha 12: o loop principal do pygame começa aqui;
# linha 13: obter uma lista de todos os eventos de pygame pendentes;
# linhas 14 a 16: verificar se o utilizador fechou a janela ou clicou em algum lugar dentro dela ou pressionou qualquer tecla;
# linha 15: se sim, parar de executar o código.