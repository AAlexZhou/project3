import pygame
import sys
import os
from player import Player

worldx =960
worldy =720
fps = 40
clock = pygame.time.Clock()
main = True

pygame.init()

back ='image/backbord.jpg'
shark = 'image/icon.png'

screen = pygame.display.set_mode((worldx,worldy))
background = pygame.image.load(back).convert()
background = pygame.transform.scale(background,(worldx,worldy),screen)
player =Player(background,200,200,shark)
mx =0
my =0

while main == True:
    background = pygame.image.load(back).convert()
    background = pygame.transform.scale(background, (worldx, worldy), screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            main = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                mx =-1
            if event.key == ord('w'):
                my = -1
            if event.key == ord('d'):
                mx =1
            if event.key == ord('s'):
                my = 1
        if event.type == pygame.KEYUP:
            if event.key == ord('a'):
                if mx ==-1:
                    my =0
            if event.key == ord('w'):
                if my == -1:
                    mx = 0
            if event.key == ord('d'):
                if mx == 1:
                    my = 0
            if event.key == ord('s'):
                if my ==1:
                    mx =0
    player.move(mx,my)
    player.draw()
    clock.tick(fps)
    pygame.display.flip()

