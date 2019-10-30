import pygame
import sys
import os
from player import Player

worldx =960
worldy =720
fps = 40
ani=4
clock = pygame.time.Clock()
main = True
pygame.init()
BLUE  = (255,255,255)

world = pygame.display.set_mode([worldx,worldy])
player = Player()   # 生成玩家
player.rect.x = 0  # 移动 x 坐标
player.rect.y = 0   # 移动 y 坐标
player_list = pygame.sprite.Group()
player_list.add(player)


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
    world.blit(backdrop, backdropbox)
    player_list.draw(screen)
    pygame.display.flip()
    clock.tick(fps)

