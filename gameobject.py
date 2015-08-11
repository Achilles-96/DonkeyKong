__author__ = 'raghuram'
import pygame, math, sys


class GameObject(pygame.sprite.Sprite):
    def __init__(self, image_normal, image_hit, position, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.normal = pygame.image.load(image_normal)
        self.hit = pygame.image.load(image_hit)
        self.rect = pygame.Rect(self.normal.get_rect())
        self.rect.topleft = position
        self.position = position
        # self.image = pygame.transform.scale(self.normal,(width*scale,height*scale))
        self.image = self.normal
        self.image = pygame.transform.scale(self.image, (width, height))

    def hit(self):
        self.image = self.hit
