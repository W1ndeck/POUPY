import pygame
from pygame.locals import *
import os
# from random import randint


pygame.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'sprites')
diretorio_sons = os.path.join(diretorio_principal, 'trilha sonora')
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'link_sprites.png'))
sprite_comida = pygame.image.load(os.path.join(diretorio_imagens, 'apple.png'))

# criando a classe do bichinho virtual


class Poupy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # setando os sprites de cada direção
        self.img_stoped = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 120, 0), (120, 130))
            self.img_stoped.append(img)

        self.img_down = []
        for j in range(3, 13):
            img = sprite_sheet.subsurface((j * 120, 0), (120, 130))
            self.img_down.append(img)

        self.img_left = []
        for k in range(13, 23):
            img = sprite_sheet.subsurface((k * 120, 0), (120, 130))
            self.img_left.append(img)

        self.img_up = []
        for l in range(23, 33):
            img = sprite_sheet.subsurface((l * 120, 0), (120, 130))
            self.img_up.append(img)

        self.img_right = []
        for m in range(33, 43):
            img = sprite_sheet.subsurface((m * 120, 0), (120, 130))
            self.img_right.append(img)

        self.action = 0  # 0: stoped 1:down 2:left 3:up 4:right
        self.index_frame = 0
        self.image = self.img_stoped[self.index_frame]
        self.image = pygame.transform.scale(self.image, (120, 130))

        self.rect = self.image.get_rect()

        self.timer_andar = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_andar, 5000)
        self.newx = 300
        self.newy = 300
        self.x = 300
        self.y = 300
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y


    def update(self):

        if self.newx != self.rect.x:
            if self.newx > self.rect.x:
                self.update_action(4)
                if (self.rect.x + 2) > self.newx:
                    self.newx = self.rect.x 
                if self.newx == self.rect.x and self.newy != self.rect.y:
                    if self.newy > self.rect.y:
                        self.update_action(1)
                    elif self.newy < self.rect.y:
                        self.update_action(3)

            if self.newx < self.rect.x:
                self.update_action(2)
                if (self.rect.x - 2) < self.newx:
                    self.newx = self.rect.x 
                if self.newx == self.rect.x and self.newy != self.rect.y:
                    if self.newy > self.rect.y:
                        self.update_action(1)
                    elif self.newy < self.rect.y:
                        self.update_action(3)

            if self.newy < self.rect.y and self.newx < self.rect.x + 240 and self.newx > self.rect.x - 120 :
                self.update_action(3)
                if (self.rect.y - 2) < self.newy:
                    self.newy = self.rect.y 
                if self.newy == self.rect.y and self.newx != self.rect.x:
                    if self.newx > self.rect.x:
                        self.update_action(4)
                    elif self.newx < self.rect.x:
                        self.update_action(2)

            if self.newy > self.rect.y and self.newx < self.rect.x + 240 and self.newx > self.rect.x - 120:
                self.update_action(1)
                if (self.rect.y + 2) < self.newy:
                    self.newy = self.rect.y 
                if self.newy == self.rect.y and self.newx != self.rect.x:
                    if self.newx > self.rect.x:
                        self.update_action(4)
                    elif self.newx < self.rect.x:
                        self.update_action(2)

        if self.newx == self.rect.x and self.newy == self.rect.y:
            self.update_action(0)

        if self.action == 0:
            self.image = self.img_stoped[int(self.index_frame)]
            self.index_frame += 0.05
            if self.index_frame >= len(self.img_stoped):
                self.index_frame = 0

        elif self.action == 1:
            self.image = self.img_down[int(self.index_frame)]
            self.index_frame += 0.2
            self.rect.y += 2
            if self.index_frame >= len(self.img_down):
                self.index_frame = 0
                self.update_action(0)

        elif self.action == 2:
            self.image = self.img_left[int(self.index_frame)]
            self.index_frame += 0.2
            self.rect.x -= 2
            if self.newy < self.rect.y:
                self.rect.y -= 2
            if self.newy > self.rect.y:
                self.rect.y += 2
            if self.index_frame >= len(self.img_left):
                self.index_frame = 0
                self.update_action(0)

        elif self.action == 3:
            self.image = self.img_up[int(self.index_frame)]
            self.index_frame += 0.2
            self.rect.y -= 2
            if self.index_frame >= len(self.img_up):
                self.index_frame = 0
                self.update_action(0)

        elif self.action == 4:
            self.image = self.img_right[int(self.index_frame)]
            self.index_frame += 0.2
            self.rect.x += 2
            if self.newy < self.rect.y:
                self.rect.y -= 2
            if self.newy > self.rect.y:
                self.rect.y += 2
            if self.index_frame >= len(self.img_right):
                self.index_frame = 0
                self.update_action(0)

        self.image = pygame.transform.scale(self.image, (120, 130))

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.index_frame = 0

class Alimento(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.comida_parada = sprite_comida.subsurface((0, 0), (32, 32))
        self.sendo_comida = []
        for i in range(0,5):
            img = sprite_comida.subsurface((i * 32 , 0), (32, 32))
            self.sendo_comida.append(img)
        self.index_frame_maca = 0
        self.image = self.comida_parada
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.start_comer = False

        #eles tem q receber as coordenadas do mouse na tela
        self.x = 300
        self.y = 300
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

    def sendo_comido(self):
        self.start_comer = True
        
    def update(self):
        if self.start_comer == True:
            self.image = self.sendo_comida[int(self.index_frame_maca)]
            self.index_frame_maca += 0.05
            if self.index_frame_maca >= len(self.sendo_comida):
                self.index_frame_maca = 5
                
        self.image = pygame.transform.scale(self.image, (32, 32))
