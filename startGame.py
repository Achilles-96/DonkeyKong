__author__ = 'raghuram'
import pygame, math, sys
import board
from pygame.locals import *
from random import randint
import scoreboard



class Game:
    def __init__(self, background):
        pygame.font.init()
        self.screen = pygame.display.set_mode((1200, 500),DOUBLEBUF)
        self.screen.set_alpha(None)
        self.clock = pygame.time.Clock()
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
        jumpspeed = 0
        donkeytimer = 0
        lim =randint(50,70)
        while 1:
            self.screen.set_alpha(None)
            if timer == lim:
                board1.createfireball()
                timer = 0
                lim = randint(50,70)
            timer += 1
            prevScore = board1.getPlayerScore()
            ladderstate = board1.getLadderCollisions()
            collectCoin = board1.getCoinCollisions()
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
                if ev.type == KEYDOWN and ev.key == K_SPACE and jumpstate == 0:
                    jumpstate = 1
                    jumpspeed = 10

            donkeytimer += 1
            if donkeytimer == 10:
                donkeytimer = 0
                board1.updatefireballs(1)
            else:
                board1.updatefireballs(0)
            if stateup == 1 and ladderstate == 1:
                board1.key_pressed(3)
                if board1.checkfireballcollision() == 0:
                    break

            if statedown == 1 and ladderstate == 1:
                board1.key_pressed(4)
                if board1.checkfireballcollision() == 0:
                    break
            if ladderstate == 1:
                board1.checkplayerlevel()
                if board1.checkfireballcollision() == 0:
                    break
            if stateright == 1:
                board1.key_pressed(1)
                if board1.checkfireballcollision() == 0:
                    break
            if stateleft == 1:
                board1.key_pressed(2)
                if board1.checkfireballcollision() == 0:
                    break

            if ladderstate == 1 and jumpstate == 1: jumpstate = 0
            if jumpstate == 1:
                if board1.playerjump(jumpspeed) == 1:
                    jumpstate = 2
                    jumpspeed = 0
                else:
                    jumpspeed -= 2
                if board1.checkfireballcollision() == 0:
                    break
                elif board1.checkfireballcollision() == 1:
                    jumpstate = 0

            if jumpstate == 2:
                if board1.playerjumpdown(jumpspeed) == 1:
                    jumpstate = 0
                    jumpspeed = 10
                else:
                    jumpspeed += 2
                if board1.checkfireballcollision() == 0:
                    break
                elif board1.checkfireballcollision() == 1:
                    jumpstate = 0

            if ladderstate == 0 and jumpstate == 0:
                board1.dropplayer()
                if board1.checkfireballcollision() == 0:
                    break

            self.screen.blit(self.background, self.background.get_rect())
            board1.update(self.screen)
            board1.setPlayerScore(prevScore+collectCoin*5)
            scoreboard.ScoreBoard("scoreboard.png",board1.getPlayerScore(),self.screen)
            pygame.display.flip()


if __name__ == '__main__':
    while 1:
        game = Game('background.jpg')
        game.run()
