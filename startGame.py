__author__ = 'raghuram'
import pygame, math, sys
import board
from pygame.locals import *
from random import randint


class Game:
    def __init__(self, background):
        self.screen = pygame.display.set_mode((1200, 500))
        self.clock = pygame.time.Clock()
        # pygame.draw.rect(self.screen,(0,0,0),(300,315,30,90))
        self.background = pygame.image.load(background)
        self.background = pygame.transform.scale(self.background, (1200, 500))
        self.screen.blit(self.background, self.background.get_rect())
        pygame.display.flip()

    def run(self):
        board1 = board.Board(self.screen)
        stateright = 0
        stateleft = 0
        stateup = 0
        statedown = 0
        ladderstate = 0
        jumpstate = 0
        timer = 0
        lim =randint(100,120)
        while 1:
            # print timer
            if timer == lim:
                board1.createfireball()
                timer = 0
                lim = randint(180,200)
            timer += 1
            ladderstate = board1.getLadderCollisions()
            board1.getCoinCollisions()
            self.clock.tick(30)
            pygame.key.set_repeat()
            for ev in pygame.event.get():
                if not hasattr(ev, 'key'): continue
                if ev.type == KEYDOWN and ev.key == K_RIGHT:
                    stateright = 1
                if ev.type == KEYUP and ev.key == K_RIGHT:
                    stateright = 0
                if ev.type == KEYDOWN and ev.key == K_LEFT:
                    stateleft = 1
                if ev.type == KEYUP and ev.key == K_LEFT:
                    stateleft = 0
                if ev.type == KEYDOWN and ev.key == K_UP:
                    stateup = 1
                if ev.type == KEYUP and ev.key == K_UP:
                    stateup = 0
                if ev.type == KEYDOWN and ev.key == K_DOWN:
                    statedown = 1
                if ev.type == KEYUP and ev.key == K_DOWN:
                    statedown = 0
                if ev.type == KEYDOWN and ev.key == K_SPACE:
                    jumpstate = 1
            board1.updatefireballs()
            if stateup == 1 and ladderstate == 1:
                board1.key_pressed(3)
                board1.checkfireballcollision()

            if statedown == 1 and ladderstate == 1:
                board1.key_pressed(4)
                board1.checkfireballcollision()
            if ladderstate == 1:
                #print board1.plr[0].getPosition()
                board1.checkplayerlevel()
                board1.checkfireballcollision()
            if stateright == 1:
                board1.key_pressed(1)
                board1.checkfireballcollision()
            if stateleft == 1:
                board1.key_pressed(2)
                board1.checkfireballcollision()

            if ladderstate == 1 and jumpstate == 1: jumpstate = 0
            if jumpstate == 1:
                if board1.playerjump() == 1:
                    jumpstate = 2
                board1.checkfireballcollision()

            if jumpstate == 2:
                if board1.playerjumpdown() == 1:
                    jumpstate = 0
                board1.checkfireballcollision()

            if ladderstate == 0 and jumpstate == 0:
                board1.dropplayer()
                board1.checkfireballcollision()

            self.screen.blit(self.background, self.background.get_rect())
            board1.update(self.screen)
            pygame.display.flip()


if __name__ == '__main__':
    game = Game('background.png')
    game.run()
