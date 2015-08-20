__author__ = 'raghuram'
import gameobject
import pygame


class Fireball(gameobject.GameObject):
    def __init__(self, image_normal, image_hit, position, width, height, state):
        gameobject.GameObject.__init__(self, image_normal, image_hit, position, width, height)
        self.state = state

    def getState(self):
        return self.state

    def setState(self,state):
        self.state = state
