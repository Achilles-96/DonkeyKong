__author__ = 'raghuram'
import pygame
import person


class Player(person.PersonSprite):

    def __init__(self, image_normal, image_hit, position, width, height,state,lives):
        person.PersonSprite.__init__(self, image_normal, image_hit, position, width, height,state)
        self.score = 0
        self.lives = lives


    def getPosition(self):
        return self.position

    def setPosition(self,position):
        self.position = position
        pygame.Rect(self.image.get_rect()).topleft = position

    def setState(self,state):
        self.state=state
        if state == 0:
            self.image =self.left
        else:
            self.image =self.right

    def setLives(self,lives):
        self.lives =lives

    def setScore(self,newScore):
        self.score = newScore

    def getState(self):
        return self.state

    def getLives(self):
        return self.lives

    def getScore(self):
        return self.score