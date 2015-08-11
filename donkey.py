__author__ = 'raghuram'
import person


class Donkey(person.PersonSprite):

    def __init__(self, image_normal, image_hit, position):
        person.PersonSprite.__init__(self, image_normal, image_hit, position)