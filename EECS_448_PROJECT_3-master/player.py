import pygame
import sys
import os



class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.shark()
    def shark(self):
        img = pygame.image.load(os.path.join('image', 'icon.png')).convert()
        self.images.append(img)
        self.images = self.images[0]
        self.rect = self.images.get_rect()