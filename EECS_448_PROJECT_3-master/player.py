import pygame
import sys
import os



class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.shark()
    def shark(self):
        shark = 'image/fugu.png'
        img = pygame.image.load(shark).convert()
        self.images.append(img)
        self.images = self.images[0]
        self.rect = self.images.get_rect()