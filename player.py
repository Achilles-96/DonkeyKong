__author__ = 'raghuram'
import pygame
import person


class Player(person.PersonSprite):

    def __init__(self, image_left, image_right, image_straight,image_climb,position, width, height,state,lives):
        person.PersonSprite.__init__(self, image_left, image_right, position, width, height,state)
        self.score = 0
        self.lives = lives
        self.image_straight = pygame.image.load(image_straight)
        self.image_straight =pygame.transform.scale(self.image_straight, (width, height))
        self.image_climb = pygame.image.load(image_climb)
        self.image_climb =pygame.transform.scale(self.image_climb, (width, height))


    def getPosition(self):
        return self.position

    def setPosition(self,position):
        self.position = position
        pygame.Rect(self.image.get_rect()).topleft = position

    def setState(self,state):
        self.state=state
        if state == 0:
            self.image =self.left
        elif state==1:
            self.image =self.right
        elif state == 3:
            self.image=self.image_straight
        elif state == 2:
            self.image=self.image_climb


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