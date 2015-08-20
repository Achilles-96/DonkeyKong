__author__ = 'raghuram'
import pygame


class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self, image, text, screen, life_image):
        font = pygame.font.SysFont("comicsansms", 70)
        text = font.render(str(text), True, (102, 51, 0))
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.life_image = pygame.image.load(life_image)
        self.image = pygame.transform.scale(self.image, (200, 80))
        screen.blit(self.image, (500, 530))
        screen.blit(text, (500 + 75 - (text.get_width() / 2), 530 + 55 - (text.get_height() / 2)))

    def update(self, text, screen):
        font = pygame.font.SysFont("comicsansms", 70)
        text = font.render(str(text), True, (102, 51, 0))
        screen.blit(self.image, (500, 530))
        screen.blit(text, (500 + 50 - (text.get_width() / 2), 530 + 40 - (text.get_height() / 2)))

    def update_lives(self, screen, lives):
        for i in range(lives):
            self.life_image = pygame.transform.scale(self.life_image, (25, 50))
            screen.blit(self.life_image, (620 + i * 35, 545))

    def update_level(self, level, screen):
        font = pygame.font.SysFont("comicsansms", 70)
        text = font.render(str(level), True, (218, 165, 32))
        text = pygame.transform.scale(text, (20, 30))
        screen.blit(text, (500 + 100 - (text.get_width() / 2), 530 + 20 - (text.get_height() / 2)))
