__author__ = 'raghuram'
import gameobject


class Fireball(gameobject.GameObject):

    def __init__(self, image_normal, image_hit, position):
        gameobject.GameObject.__init__(self, image_normal, image_hit, position)
