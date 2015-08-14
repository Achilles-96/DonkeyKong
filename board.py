__author__ = 'raghuram'
import pygame, math, sys
import player
import princess
import donkey
import block, fireball, coin, ladder
from random import randint
import random
from pygame.locals import *


class Board():
    def __init__(self, screen):
        self.blocks = []
        self.ladders = []
        self.coins = []
        self.fireballs = []
        self.levellimits = {}
        self.ladderlimits = {}
        self.block_group = pygame.sprite.RenderPlain(*self.blocks)
        self.ladder_group = pygame.sprite.RenderPlain(*self.ladders)
        self.coin_group = pygame.sprite.RenderPlain(*self.coins)
        self.fireball_group = pygame.sprite.RenderPlain(*self.fireballs)
        self.initlogs(screen)
        self.initladders(screen)
        self.initcoins(screen)
        self.plr = [player.Player("coin.png", "coin.png", (0, 450), 20, 20,0)]
        self.plr_group = pygame.sprite.RenderPlain(*self.plr)
        self.plr_group.draw(screen)
        self.playerparentdict ={}
        self.fireballparentdict={}
        self.playerparentdict[500]=460
        for i in range (499,0,-1):
            if(i in [460, 380, 300, 220, 140, 60]):
                self.playerparentdict[i]=i
            else:
                self.playerparentdict[i]=self.playerparentdict[i+1]
        self.fireballparentdict[500]=460
        for i in range (499,0,-1):
            if(i in [460, 380, 300, 220, 140, 60]):
                self.fireballparentdict[i]=i
            else:
                self.fireballparentdict[i]=self.fireballparentdict[i+1]
        '''
        self.princess1 = princess.Princess("log.py","log.py",(0,0))
        self.dnky = donkey.Donkey()
        '''

    def initlogs(self, screen):  # Intialize all blocks
        self.levellimits = {380: 1, 300: 2, 220: 1, 140: 2, 60: 1}
        self.blocks = [block.Block("log.png", "log.png", (0, 0), 1200, 20),
                       block.Block("log.png", "log.png", (0, 80), 1000, 20),
                       block.Block("log.png", "log.png", (200, 160), 1000, 20),
                       block.Block("log.png", "log.png", (0, 240), 1000, 20),
                       block.Block("log.png", "log.png", (200, 320), 1000, 20),
                       block.Block("log.png", "log.png", (0, 400), 1000, 20),
                       block.Block("log.png", "log.png", (0, 480), 1200, 20), ]
        self.block_group = pygame.sprite.RenderPlain(*self.blocks)
        self.block_group.draw(screen)
        self.donkey = donkey.Donkey("Donkey.png","Donkey.png",(20,30),40,50,0)
        self.donkey_group = pygame.sprite.RenderPlain(self.donkey)


    def initladders(self, screen):  # Intialize all ladders

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
        self.ladderlimits = {(800, 399): 460, (300, 319): 380, (500, 239): 300, (900, 159): 220, (600, 79): 140,
                             (650, 380): 380, (850, 300): 300, (300, 140): 140, (650, 315): 380, (850, 235): 300,
                             (300, 75): 140}
        self.ladder_group = pygame.sprite.RenderPlain(*self.ladders)
        self.ladder_group.draw(screen)

    def initcoins(self, screen):  # Intialize all coins
        xlis = [450, 370, 290, 210, 130, 50]
        ''',430,350,270,190,110,30'''
        self.coins = []
        x=0
        for i in range(0, 20):
            y =  xlis[randint(0, 5)]
            if y == 450 or y == 430:
                x= random.randrange(0,1170,1)
            elif y in [370,210,50,350,190,30]:
                x=random.randrange(0,1000,1)
            elif y in [290,130,270,110]:  x=random.randrange(200,1170,1)

            self.coins += [coin.Coin("coin.png", "coin.png", (x, y), 20, 20)]

        self.coin_group = pygame.sprite.RenderPlain(*self.coins)
        self.coin_group.draw(screen)

    def createfireball(self):  # Creating fireballs
        self.fireballs += [fireball.Fireball("coin.png", "coin.png", (30, 60), 20, 20, randint(1, 2))]
        self.fireball_group = pygame.sprite.RenderPlain(*self.fireballs)

    def key_pressed(self, event):  # Handling a key pressed event
        x, y = self.plr[0].getPosition()
        state =0
        if event == 1:
            state =0
            x += 10
        if event == 2:
            state =1
            x -= 10
        if event == 3:
            y -= 5
        if event == 4:
            y += 10
        x = max(x, 0)
        y = max(y, 0)
        x = min(x, 1170)
        y = min(y, 460)
        if (y in self.levellimits and int(self.levellimits[y]) == 1 and x > 1000):
            y += 1
        if (y in self.levellimits and int(self.levellimits[y]) == 2 and x < 170):
            y += 1
        self.plr[0] = player.Player("player2.png", "player.png", (x, y), 20, 20,state)
        self.plr_group = pygame.sprite.RenderPlain(*self.plr)

    def update(self, screen):  # Update the board
        self.coin_group.draw(screen)
        self.block_group.draw(screen)
        self.ladder_group.draw(screen)
        self.plr_group.draw(screen)
        self.fireball_group.draw(screen)
        self.donkey_group.draw(screen)

    def getLadderCollisions(self):  # Check if player is in touch with any ladder

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
                state = 1
                break
        if state == 1:
            return 1
        else:
            return 0

    def checkfireballcollision(self):
        state = 0
        for s in self.fireball_group.sprites():
            rect1 = self.plr[0].rect
            rect1.topleft = self.plr[0].getPosition()
            rect1.height = rect1.width = 20
            rect2 = s.rect
            rect2.height = 25
            rect2.width = 25
            if rect1.colliderect(rect2):
                state = 1
                break

    def dropplayer(self):  # Drop if player is in middle of air
        x, y = self.plr[0].getPosition()
        state = self.plr[0].getState()
        levelpos = y
        levelpos = self.playerparentdict[levelpos]
        if y == levelpos:
            return
        self.plr[0] = player.Player("player2.png", "player.png", (x, min(y + 10, levelpos)), 20, 20,state)
        self.plr_group = pygame.sprite.RenderPlain(*self.plr)

    def getCoinCollisions(self):  # Checking collisions with any coin
        for c in self.coin_group.sprites():
            rect1 = self.plr[0].rect
            rect1.topleft = self.plr[0].getPosition()
            rect1.height = rect1.width = 20
            rect2 = c.rect
            rect2.height = rect2.width = 30
            if rect1.colliderect(rect2):
                c.kill()
                self.plr[0].collectCoin()

    def playerjump(self):  # Jumping up function
        x, y = self.plr[0].getPosition()
        state = self.plr[0].getState()
        levelpos = y
        levelpos = self.playerparentdict[levelpos]
        if y <= levelpos - 30:
            self.plr[0] = player.Player("player2.png", "player.png", (x, levelpos - 30), 20, 20,state )
            self.plr_group = pygame.sprite.RenderPlain(*self.plr)
            return 1
        else:
            self.plr[0] = player.Player("player2.png", "player.png", (x, y - 5), 20, 20,state)
            self.plr_group = pygame.sprite.RenderPlain(*self.plr)
            return 0

    def playerjumpdown(self):  # Jumping down function
        x, y = self.plr[0].getPosition()
        state = self.plr[0].getState()
        levelpos = y
        levelpos=self.playerparentdict[levelpos]
        if y >= levelpos:
            self.plr[0] = player.Player("player2.png", "player.png", (x, levelpos), 20, 20,state )
            self.plr_group = pygame.sprite.RenderPlain(*self.plr)
            return 1
        else:
            self.plr[0] = player.Player("player2.png", "player.png", (x, y + 5), 20, 20,state)
            self.plr_group = pygame.sprite.RenderPlain(*self.plr)
            return 0

    def checkplayerlevel(self):  # chaecks that player should not fall down beyond ladder through a block
        x, y = self.plr[0].getPosition()
        state = self.plr[0].getState()
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
                y = min(y, self.ladderlimits[rect2.topleft])
                self.plr[0] = player.Player("player2.png", "player.png", (x, y), 20, 20,state)
                self.plr_group = pygame.sprite.RenderPlain(*self.plr)
                break

    def updatefireballs(self,flipdonkey):
        i=0
        for s in self.fireball_group.sprites():
            x, y = s.getPosition()
            if x<=0 and y == 460:
                pass
            else:
                state = s.getState()
                if x <= 0: state = 1
                if x >= 1200: state = 2
                if state == 1:
                    x += 5
                else:
                    x -= 5
                collisions = pygame.sprite.spritecollide(s,self.ladder_group,False)
                if collisions:
                    ly =self.ladderlimits[collisions[0].rect.topleft]
                    if y != ly:
                        val = randint(1,5)
                        if val == 5:
                            y+=1
                            state = randint(0,1)
                        y = self.fireballparentdict[y]
                if (y  in self.levellimits and int(self.levellimits[y]) == 1 and x > 1000):
                    y += 1
                    y = self.fireballparentdict[y]
                    state = randint(1, 2)
                if (y  in self.levellimits and int(self.levellimits[y]) == 2 and x < 170):
                    y += 1
                    y = self.fireballparentdict[y]
                    state = randint(1, 2)
                self.fireballs[i] = fireball.Fireball("fireball.png", "fireball.png", (x, y), 20, 20, state)
                i += 1
        del self.fireballs[i:]
        self.fireball_group = pygame.sprite.RenderPlain(*self.fireballs)
        self.donkey = donkey.Donkey("Donkey.png","Donkey2.png",(20,30),40,50,flipdonkey^(self.donkey.getState()))
        self.donkey_group = pygame.sprite.RenderPlain(self.donkey)
