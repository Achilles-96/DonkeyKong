__author__ = 'raghuram'
import pygame,math,sys
from pygame.locals import *


class PersonSprite(pygame.sprite.Sprite):

    def __init__(self, image_left, image_right, position, width, height,state):
        pygame.sprite.Sprite.__init__(self)
        self.left = pygame.image.load(image_left)
        self.right = pygame.image.load(image_right)


        self.position = position
        self.state =state
        if state == 0:
            self.image =self.left
        else:
            self.image=self.right
        self.left =pygame.transform.scale(self.left, (width, height))
        self.right =pygame.transform.scale(self.right, (width, height))
        self.image=self.left
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = position

    def personhit(self):
        self.image = self.hit