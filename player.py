__author__ = 'raghuram'
import pygame
import person


class Player(person.PersonSprite):

    def __init__(self, image_normal, image_hit, position, width, height,state):
        person.PersonSprite.__init__(self, image_normal, image_hit, position, width, height,state)
        self.score = 0
        self.lives = 3


    def getPosition(self):
        return self.position

    def setPosition(self,position):
        pygame.Rect(self.image.get_rect()).topleft = position

    def collectCoin(self):
        self.score += 5

    def getState(self):
        return self.state