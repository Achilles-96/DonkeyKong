__author__ = 'raghuram'
import pygame, math, sys
import player
import princess
import donkey
import block, fireball, coin, ladder
from random import randint
from pygame.locals import *


class Board():
    def __init__(self, screen):
        self.blocks = []
        self.ladders = []
        self.coins = []
        self.levellimits = {}
        self.ladderlimits = {}
        self.block_group = pygame.sprite.RenderPlain(*(self.blocks))
        self.ladder_group = pygame.sprite.RenderPlain(*(self.ladders))
        self.coin_group = pygame.sprite.RenderPlain(*self.coins)
        self.initlogs(screen)
        self.initladders(screen)
        self.initcoins(screen)
        self.plr = [player.Player("coin.png", "coin.png", (0, 450), 20, 20)]
        #print self.plr[0].getPosition()
        self.plr_group = pygame.sprite.RenderPlain(*self.plr)
        self.plr_group.draw(screen)
        '''
        self.princess1 = princess.Princess("log.py","log.py",(0,0))
        self.dnky = donkey.Donkey()
        '''

    def initlogs(self, screen):
        self.levellimits={380:1,300:2,220:1,140:2,60:1}
        self.blocks = [block.Block("log.png", "log.png", (0, 0), 1200, 20),
                       block.Block("log.png", "log.png", (0, 80), 1000, 20),
                       block.Block("log.png", "log.png", (200, 160), 1000, 20),
                       block.Block("log.png", "log.png", (0, 240), 1000, 20),
                       block.Block("log.png", "log.png", (200, 320), 1000, 20),
                       block.Block("log.png", "log.png", (0, 400), 1000, 20),
                       block.Block("log.png", "log.png", (0, 480), 1200, 20), ]
        self.block_group = pygame.sprite.RenderPlain(*self.blocks)
        self.block_group.draw(screen)

    def initladders(self, screen):

        self.ladders = [ladder.Ladder("ladder.png", "ladder.png", (800, 399), 30, 95),
                        ladder.Ladder("ladder.png", "ladder.png", (300, 319), 30, 95),
                        ladder.Ladder("ladder.png", "ladder.png", (500, 239), 30, 95),
                        ladder.Ladder("ladder.png", "ladder.png", (900, 159), 30, 95),
                        ladder.Ladder("ladder.png", "ladder.png", (600, 79), 30, 95),
                        ladder.Ladder("ladder_broken.png", "ladder_broken.png", (650, 315), 30, 35),
                        ladder.Ladder("ladder_broken_down.png", "ladder_broken_down.png", (650, 380), 30, 35),
                        ladder.Ladder("ladder_broken.png", "ladder_broken.png", (850, 235), 30, 35),
                        ladder.Ladder("ladder_broken_down.png", "ladder_broken_down.png", (850, 300), 30, 35),
                        ladder.Ladder("ladder_broken.png", "ladder_broken.png", (300, 75), 30, 35),
                        ladder.Ladder("ladder_broken_down.png", "ladder_broken_down.png", (300, 140), 30, 35),
                        ]
        self.ladderlimits = {(800,399):460,(300,319):380,(500,239):300,(900,159):220,(600,79):140,
                             (650,380):380,(850,300):300,(300,140):140,(650,315):380,(850,235):300,(300,75):140}
        self.ladder_group = pygame.sprite.RenderPlain(*self.ladders)
        self.ladder_group.draw(screen)

    def initcoins(self, screen):
        xlis = [450, 370, 290, 210, 130, 50]
        for i in range(0, 20):
            x, y = randint(170, 1000), xlis[randint(0, 5)]
            self.coins += [coin.Coin("coin.png", "coin.png", (x, y), 30, 30)]
        self.coin_group = pygame.sprite.RenderPlain(*self.coins)
        self.coin_group.draw(screen)

    def key_pressed(self, event):
        x, y = self.plr[0].getPosition()
        if event == 1:
            x += 10
        if event == 2:

            x -= 10
            print x
        if event == 3:
            y -= 5
        if event == 4:
            y += 10
            print y

        x = max(x, 0)
        y = max(y, 0)
        x = min(x, 1170)
        y = min(y, 460)
        if(y in self.levellimits and int(self.levellimits[y])==1 and x>1000):
            y+=1
        if(y in self.levellimits and int(self.levellimits[y])==2 and x<170):
            y+=1
        # print x, y
        self.plr[0] = player.Player("coin.png", "coin.png", (x, y), 20, 20)
        self.plr_group = pygame.sprite.RenderPlain(*self.plr)

    def update(self, screen):
        self.coin_group.draw(screen)
        self.block_group.draw(screen)
        self.ladder_group.draw(screen)
        self.plr_group.draw(screen)

    def getLadderCollisions(self):

        # collisions = pygame.sprite.spritecollide(self.plr[0], self.ladder_group,False)
        state = 0
        for s in self.ladder_group.sprites():
            rect1 = self.plr[0].rect
            rect1.topleft = self.plr[0].getPosition()
            rect1.height = rect1.width = 20
            rect2 = s.rect
            rect2.height = 95
            rect2.width = 30
            if rect2.topleft in [(650, 315), (650, 380), (850, 235), (850, 300), (300, 75), (300, 140)]:
                rect2.height = 35
            if rect1.colliderect(rect2):
                # print rect1, s.rect
                state = 1
                break
        if state == 1:
            return 1
        else:
            return 0

    def dropplayer(self):
        x, y = self.plr[0].getPosition()
        levelpos = y
        while (levelpos not in [460, 380, 300, 220, 140, 60]):
            levelpos += 1
        if y== levelpos:
            return
        self.plr[0] = player.Player("coin.png", "coin.png", (x, min(y+10,levelpos)), 20, 20)
        self.plr_group = pygame.sprite.RenderPlain(*self.plr)

    def getCoinCollisions(self):
        for c in self.coin_group.sprites():
            rect1 = self.plr[0].rect
            rect1.topleft = self.plr[0].getPosition()
            rect1.height = rect1.width = 20
            rect2 = c.rect
            rect2.height = rect2.width = 30
            if rect1.colliderect(rect2):
                c.kill()
                self.plr[0].collectCoin()

    def playerjump(self):
        x, y = self.plr[0].getPosition()
        levelpos = y
        while levelpos not in [460, 380, 300, 220, 140, 60]:
            levelpos+=1
        #print levelpos,y
        if y <= levelpos - 25:
            self.plr[0] = player.Player("coin.png", "coin.png", (x, levelpos-25), 20, 20)
            self.plr_group = pygame.sprite.RenderPlain(*self.plr)
            return 1
        else:
           # print "hi"
            self.plr[0] = player.Player("coin.png", "coin.png", (x, y-5), 20, 20)
            self.plr_group = pygame.sprite.RenderPlain(*self.plr)
            return 0

    def playerjumpdown(self):
        x, y = self.plr[0].getPosition()
        levelpos = y
        while levelpos not in [460, 380, 300, 220, 140, 60]:
            levelpos+=1
        #print levelpos,y
        if y>= levelpos:
            self.plr[0] = player.Player("coin.png", "coin.png", (x, levelpos), 20, 20)
            self.plr_group = pygame.sprite.RenderPlain(*self.plr)
            return 1
        else:
            self.plr[0] = player.Player("coin.png", "coin.png", (x, y+5), 20, 20)
            self.plr_group = pygame.sprite.RenderPlain(*self.plr)
            return 0

    def checkplayerlevel(self):
        state = 0
        x, y = self.plr[0].getPosition()
        for s in self.ladder_group.sprites():
            rect1 = self.plr[0].rect
            rect1.topleft = self.plr[0].getPosition()
            rect1.height = rect1.width = 20
            rect2 = s.rect
            rect2.height = 95
            rect2.width = 30
            if rect2.topleft in [(650, 315), (650, 380), (850, 235), (850, 300), (300, 75), (300, 140)]:
                rect2.height = 35
            if rect1.colliderect(rect2):
                y=min(y,self.ladderlimits[rect2.topleft])
                self.plr[0] = player.Player("coin.png", "coin.png", (x, y), 20, 20)
                self.plr_group = pygame.sprite.RenderPlain(*self.plr)
                break




