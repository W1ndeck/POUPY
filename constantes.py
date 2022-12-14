import pygame
from pygame.locals import *
import os
import pickle
# from classe_bixinho import Poupy

pygame.init()



def salvar_progresso(fome, limpeza):  # func guardar prog em arquivo
    bixinho = (fome, limpeza)
    arquivo = open('save_bixinho.dat', 'wb')
    pickle.dump(bixinho, arquivo)
    arquivo.close()


def recuperar_progresso(fome, limpeza): # func ler prog em arquivo
    try:
        arquivo = open("save_bixinho.dat", "rb")
        bixinho = pickle.load(arquivo)
        arquivo.close() 
    except:

        arquivo = open("save_bixinho.dat", "wb")
        arquivo.close()
        bixinho = (fome, limpeza)
    
    return bixinho

def ler_imagens(primeiro_numero, segundo_numero, sprite, xsprite, ysprite):
    lista_imagens = []
    for i in range(primeiro_numero, segundo_numero):
        img = sprite.subsurface((i * xsprite, 0), (xsprite, ysprite))
        lista_imagens.append(img)

    return lista_imagens

def add_sprites_grupo(*sprites):
    spritegroup = pygame.sprite.Group() 
    for sprite in sprites:
        spritegroup.add(sprite)

    return spritegroup



DIRETORIO_PRINCIPAL = os.path.dirname(__file__)
DIRETORIO_IMAGENS = os.path.join(DIRETORIO_PRINCIPAL, 'sprites')
DIRETORIO_SONS = os.path.join(DIRETORIO_PRINCIPAL, 'trilha sonora')
SPRITE_SHEET = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, 'link_sprites.png'))
SPRITE_COMIDA = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, 'apple.png'))
SPRITE_BUT_COMIDA = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, 'apple_button.png'))
SPRITE_BUT_SABAO = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, 'botao_sabao.png'))
SPRITE_SABAO = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, 'sabao_sprites.png'))
SPRITE_MOUSE = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, 'mouse_sprites.png'))
SPRITE_AFAGADO = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, 'link_sprites_afago.png'))
SPRITE_COMENDO = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, 'link_sprites_comendo.png'))
SPRITES_BARRAS = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, 'barra_vida.png'))
TELA_FUNDO = pygame.image.load(os.path.join(DIRETORIO_IMAGENS, 'telafundo.png'))


LARGURA_JANELA = 640
ALTURA_JANELA = 480
POSICAO_RELOGIO = (500, 10)
RELOGIO_JOGO = pygame.time.Clock()

#core

PRETO = (0, 0, 0)

#Fontes

FONTE_CS = pygame.font.SysFont("comicsansms", 40, True, True)