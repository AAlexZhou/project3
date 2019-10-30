import pygame
import sys
import os

worldx =960
worldy =720
fps = 40
ani=4
clock = pygame.time.Clock()
main = True
pygame.init()
BLUE  = (25,25,200)

world = pygame.display.set_mode([worldx,worldy])


while main == True:
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
    world.fill(BLUE)
    pygame.display.flip()
    clock.tick(fps)

