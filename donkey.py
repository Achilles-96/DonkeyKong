__author__ = 'raghuram'
import person


class Donkey(person.PersonSprite):

    def __init__(self, image_normal, image_hit, position,width, height,state):
        person.PersonSprite.__init__(self, image_normal, image_hit, position,width, height,state)

    def getState(self):
        return self.state