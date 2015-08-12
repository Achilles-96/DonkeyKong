__author__ = 'raghuram'
import gameobject


class Fireball(gameobject.GameObject):
    def __init__(self, image_normal, image_hit, position, width, height, state):
        gameobject.GameObject.__init__(self, image_normal, image_hit, position, width, height)
        self.state = state

    def getPosition(self):
        return self.position

    def getState(self):
        return self.state
