__author__ = 'raghuram'
import pygame

class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self,image,text,screen):
       font = pygame.font.SysFont("comicsansms", 70)
       text = font.render(str(text), True, (102, 51, 0))
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(image)

       self.image = pygame.transform.scale(self.image, (150,100))
       screen.blit(self.image,(1050,400))
       screen.blit(text,(1050+75 -(text.get_width()/2),400+45-(text.get_height()/2)))