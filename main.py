import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# trecho dedicado a janela do jogo

largura_janela = 400
altura_janela = 400

tela_jogo = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Poupy")
relogio_jogo = pygame.time.Clock()

while True:

    relogio_jogo.tick(30)  # 30 fps
    tela_jogo.fill((0, 0, 0))  # cor da tela preta

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()