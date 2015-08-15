__author__ = 'raghuram'
import person
import pygame

class Donkey(person.PersonSprite):

    def __init__(self, image_normal, image_hit, position,width, height,state):
        person.PersonSprite.__init__(self, image_normal, image_hit, position,width, height,state)

    def getState(self):
        return self.state

    def setState(self,state):
        self.state=state
        if state == 0:
            self.image =self.left
        else:
            self.image =self.right

    def setPosition(self,position):
        self.position = position
        pygame.Rect(self.image.get_rect()).topleft = position