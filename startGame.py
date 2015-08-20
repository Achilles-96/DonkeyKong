__author__ = 'raghuram'
import pygame
from pygame.locals import *
from random import randint

import board
import scoreboard


class Game:
    def __init__(self, background, quitimage, yes_image, no_image, restart_image):
        pygame.font.init()
        self.screen = pygame.display.set_mode((1200, 620), DOUBLEBUF)
        self.screen.set_alpha(None)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(background)
        self.quitimage = pygame.image.load(quitimage)
        self.yesimage = pygame.image.load(yes_image)
        self.noimage = pygame.image.load(no_image)
        self.restart = pygame.image.load(restart_image)
        self.background = pygame.transform.scale(self.background, (1200, 620))
        self.quitimage = pygame.transform.scale(self.quitimage, (400, 60))
        self.yesimage = pygame.transform.scale(self.yesimage, (50, 50))
        self.noimage = pygame.transform.scale(self.noimage, (50, 50))
        self.restart = pygame.transform.scale(self.restart, (400, 60))
        self.screen.blit(self.background, self.background.get_rect())
        pygame.mixer.init()
        pygame.mixer.music.load("GameMusic.mp3")
        pygame.mixer.music.play()
        pygame.display.flip()

    def run(self):  # The function which runs the game
        board1 = board.Board(self.screen)
        stateright = 0
        stateleft = 0
        stateup = 0
        statedown = 0
        jumpstate = 0
        timer = 0
        jumpspeed = 0
        donkeytimer = 0
        fireballfrequency = (60, 80)
        lim = randint(fireballfrequency[0], fireballfrequency[1])
        scoreboard1 = scoreboard.ScoreBoard("images/scoreboard.png", board1.getPlayerScore(), self.screen,
                                            "images/liveplayer.png")
        while 1:
            quitstate = 0
            fireballhitme = 0
            self.screen.set_alpha(None)
            if timer == lim:
                board1.createfireball()
                timer = 0
                lim = randint(fireballfrequency[0], fireballfrequency[1])
            timer += 1
            prevScore = board1.getPlayerScore()
            ladderstate = board1.getLadderCollisions()
            collectCoin = board1.getCoinCollisions()
            self.clock.tick(30)
            pygame.key.set_repeat()
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    quitstate = 1
                if not hasattr(ev, 'key'):
                    continue
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
                if ev.key == K_ESCAPE:
                    quitstate = 1

            if quitstate == 1:
                if self.confirmquit() == 1:
                    return -1

            board1.updatefireballs()
            donkeytimer += 1
            if donkeytimer == 10:
                donkeytimer = 0
                board1.updatedonkey(1)
            else:
                board1.updatedonkey(0)
            if stateup == 1 and ladderstate == 1:
                board1.key_pressed(3)
                dead = board1.checkfireballcollision()
                if dead == 0:
                    if self.askforrestart(board1) == 1:
                        return -1
                    else:
                        return 0
                elif dead == 1:
                    fireballhitme = 1
                    jumpstate = 0

            if statedown == 1 and ladderstate == 1:
                board1.key_pressed(4)
                dead = board1.checkfireballcollision()
                if dead == 0:
                    if self.askforrestart(board1) == 1:
                        return -1
                    else:
                        return 0
                elif dead == 1:
                    fireballhitme = 1
                    jumpstate = 0

            if ladderstate == 1:
                board1.checkplayerlevel()
                dead = board1.checkfireballcollision()
                if dead == 0:
                    if self.askforrestart(board1) == 1:
                        return -1
                    else:
                        return 0
                elif dead == 1:
                    fireballhitme = 1
                    jumpstate = 0

            if stateright == 1:
                board1.key_pressed(1)
                dead = board1.checkfireballcollision()
                if dead == 0:
                    if self.askforrestart(board1) == 1:
                        return -1
                    else:
                        return 0
                elif dead == 1:
                    fireballhitme = 1
                    jumpstate = 0

            if stateleft == 1:
                board1.key_pressed(2)
                dead = board1.checkfireballcollision()
                if dead == 0:
                    if self.askforrestart(board1) == 1:
                        return -1
                    else:
                        return 0
                elif dead == 1:
                    fireballhitme = 1
                    jumpstate = 0

            if stateright == 0 and stateleft == 0 and ladderstate == 0:
                board1.setPlayerstraight()

            if ladderstate == 1 and jumpstate == 1:
                jumpstate = 0
            if jumpstate == 1:
                if board1.playerjump(jumpspeed) == 1:
                    jumpstate = 2
                    jumpspeed = 0
                else:
                    jumpspeed -= 2

                dead = board1.checkfireballcollision()
                if dead == 0:
                    if self.askforrestart(board1) == 1:
                        return -1
                    else:
                        return 0
                elif dead == 1:
                    fireballhitme = 1
                    jumpstate = 0

            if jumpstate == 2:
                if board1.playerjumpdown(jumpspeed) == 1:
                    jumpstate = 0
                    jumpspeed = 10
                else:
                    jumpspeed += 2

                dead = board1.checkfireballcollision()
                if dead == 0:
                    if self.askforrestart(board1) == 1:
                        return -1
                    else:
                        return 0
                elif dead == 1:
                    fireballhitme = 1
                    jumpstate = 0

            if ladderstate == 0 and jumpstate == 0:
                board1.dropplayer()
                dead = board1.checkfireballcollision()
                if dead == 0:
                    if self.askforrestart(board1) == 1:
                        return -1
                    else:
                        return 0
                elif dead == 1:
                    fireballhitme = 1
                    jumpstate = 0

            board1.checkMidAir()

            if board1.checkwin() == 1:
                board1.respawnPlayer()
                board1.initcoins(self.screen)
                board1.setplayerlives()
                board1.setplayerlives()
                collectCoin = 10
                lower, upper = fireballfrequency
                fireballfrequency = (lower - 20, upper - 20)
                board1.boostfireball()
                board1.killfireballs()
                board1.upgradeplayerlevel()

            self.screen.blit(self.background, self.background.get_rect())
            board1.update(self.screen)
            board1.setPlayerScore(max(0, prevScore + collectCoin * 5 - fireballhitme * 25))
            scoreboard1.update(board1.getPlayerScore(), self.screen)
            scoreboard1.update_lives(self.screen, board1.getPlayerLives())
            scoreboard1.update_level(board1.getplayerlevel(), self.screen)
            pygame.display.flip()

    def confirmquit(self):  # Ask if player really wants to quit
        while 1:
            self.screen.blit(self.quitimage, (400, 200))
            yes = self.screen.blit(self.yesimage, (500, 300))
            no = self.screen.blit(self.noimage, (650, 300))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if yes.collidepoint(pos):
                        return 1
                    elif no.collidepoint(pos):
                        return 0
            pygame.display.flip()

    def askforrestart(self,board1):  # Ask if player wants to restart
        self.screen.blit(self.background, self.background.get_rect())
        board1.update(self.screen)
        pygame.display.flip()
        while 1:
            self.screen.blit(self.restart, (400, 200))
            yes = self.screen.blit(self.yesimage, (500, 300))
            no = self.screen.blit(self.noimage, (650, 300))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if yes.collidepoint(pos):
                        return 0
                    elif no.collidepoint(pos):
                        return 1
            pygame.display.flip()


if __name__ == '__main__':
    while 1:
        game = Game('images/background.jpg', 'images/areyousure.png', 'images/yes.png', 'images/no.png',
                    'images/restart.png')
        status = game.run() # Launch a new game
        if status == -1:
            break
