import pygame




class Player():

    def __init__(self,master,x,y,img_path):
        self._master = master
        self. image = pygame.image.load(img_path)
        self.x = x
        self.y = y
    def move (self,x,y):
        self.x +=x
        self.y +=y
    def draw(self):
        self._master.blit(self.image,(self.x,self.y))