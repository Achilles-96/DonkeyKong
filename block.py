__author__ = 'raghuram'
import gameobject


class Block(gameobject.GameObject):
    def __init__(self, image_normal, image_hit, position, width, height):
        gameobject.GameObject.__init__(self, image_normal, image_hit, position, width, height)
        self.size = (width, height)

    def getSize(self):
        return self.size
