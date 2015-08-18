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
        self.castleblocks = []
        self.levellimits = {}
        self.ladderlimits = {}
        self.block_group = pygame.sprite.RenderPlain(*self.blocks)
        self.ladder_group = pygame.sprite.RenderPlain(*self.ladders)
        self.coin_group = pygame.sprite.RenderPlain(*self.coins)
        self.fireball_group = pygame.sprite.RenderPlain(*self.fireballs)
        self.castle_block_group = pygame.sprite.RenderPlain(*self.blocks)
        self.initlogs(screen)
        self.initladders(screen)
        self.initcoins(screen)
        self.initcastle(screen)
        self.plr = [player.Player("player2.png", "player.png","player3.png","player4.png", (0, 480), 20, 20,0,2)]
        self.plr_group = pygame.sprite.RenderPlain(*self.plr)
        self.plr_group.draw(screen)
        self.playerparentdict ={}
        self.fireballparentdict={}
        self.playerparentdict[500]=480
        for i in range (499,0,-1):
            if(i in [480, 400, 320, 240, 160, 80]):
                self.playerparentdict[i]=i
            else:
                self.playerparentdict[i]=self.playerparentdict[i+1]
        self.fireballparentdict[500]=480
        for i in range (499,0,-1):
            if(i in [480, 400, 320, 240, 160, 80]):
                self.fireballparentdict[i]=i
            else:
                self.fireballparentdict[i]=self.fireballparentdict[i+1]

    def initlogs(self, screen):  # Intialize all blocks
        self.levellimits = {400: 1, 320: 2, 240: 1, 160: 2, 80: 1,30:3}
        self.blocks = [block.Block("log.png", "log.png", (0, 0), 1200, 20),
                       block.Block("log.png", "log.png", (0, 100), 700, 20),
                       block.Block("log.png", "log.png", (200, 180), 1000, 20),
                       block.Block("log.png", "log.png", (0, 260), 1000, 20),
                       block.Block("log.png", "log.png", (200, 340), 1000, 20),
                       block.Block("log.png", "log.png", (0, 420), 1000, 20),
                       block.Block("log.png", "log.png", (0, 500), 1200, 20),
                       ]
        self.block_group = pygame.sprite.RenderPlain(*self.blocks)
        self.block_group.draw(screen)
        self.donkey = donkey.Donkey("Donkey2.png","Donkey.png",(20,50),40,50,0)
        self.donkey_group = pygame.sprite.RenderPlain(self.donkey)
        self.princess = princess.Princess("princess2.png","princess2.png",(120,20),20,30,0)
        self.princess_group = pygame.sprite.RenderPlain(self.princess)


    def initladders(self, screen):  # Intialize all ladders

        self.ladders = [ladder.Ladder("ladder.png", "ladder.png", (800, 419), 30, 95),
                        ladder.Ladder("ladder.png", "ladder.png", (300, 339), 30, 95),
                        ladder.Ladder("ladder.png", "ladder.png", (500, 259), 30, 95),
                        ladder.Ladder("ladder.png", "ladder.png", (900, 179), 30, 95),
                        ladder.Ladder("ladder.png", "ladder.png", (600, 99), 30, 95),
                        ladder.Ladder("ladder_broken.png", "ladder_broken.png", (650, 335), 30, 35),
                        ladder.Ladder("ladder_broken_down.png", "ladder_broken_down.png", (650, 400), 30, 35),
                        ladder.Ladder("ladder_broken.png", "ladder_broken.png", (850, 255), 30, 35),
                        ladder.Ladder("ladder_broken_down.png", "ladder_broken_down.png", (850, 320), 30, 35),
                        ladder.Ladder("ladder_broken.png", "ladder_broken.png", (300, 95), 30, 35),
                        ladder.Ladder("ladder_broken_down.png", "ladder_broken_down.png", (300, 160), 30, 35),
                        ladder.Ladder("castleladder.png", "castleladder.png", (220, 45), 30, 60)
                        ]

        for l in self.ladders:
            x,y = l.getPosition()
            w,h = l.getSize()
            if h == 95:
                self.ladderlimits[l.getPosition()] = y + 1 +60
            else:
                if h == 60:
                    self.ladderlimits[l.getPosition()]= y+ 5+30
                elif y % 10 == 0:
                    self.ladderlimits[l.getPosition()]  = y
                else:
                    self.ladderlimits[l.getPosition()] = y+5+60
        self.ladder_group = pygame.sprite.RenderPlain(*self.ladders)
        self.ladder_group.draw(screen)

    def initcoins(self, screen):  # Intialize all coins
        levellis = [470, 390, 310, 230, 150, 70]
        self.coins = []
        x=0
        for i in range(0, 20):
            y =  levellis[randint(0, 5)]
            if y == 470:
                x= random.randrange(0,1170,30)
            elif y in [390,230]:
                x=random.randrange(0,1000,30)
            elif y in [310,150]:  x=random.randrange(200,1170,30)
            elif y == 70: x=random.randrange(350,700,30)

            self.coins += [coin.Coin("coin.png", "coin.png", (x, y), 20, 20)]

        self.coin_group = pygame.sprite.RenderPlain(*self.coins)
        self.coin_group.draw(screen)

    def initcastle(self,screen):
        self.castleblocks = [block.Block("castle.png", "castle.png", (110,50), 180,10),
                             block.Block("castlepillar.png", "castlepillar.png", (100,20), 20,40),
                             block.Block("castlepillar.png", "castlepillar.png", (280,20), 20,40),
                             ]
        self.castle_block_group=pygame.sprite.RenderPlain(*self.castleblocks)
        self.castle_block_group.draw(screen)

    def createfireball(self):  # Creating fireballs
        self.fireballs += [fireball.Fireball("fireball.png", "fireball.png", (30, 80), 20, 20, randint(1, 2))]
        self.fireball_group = pygame.sprite.RenderPlain(*self.fireballs)

    def key_pressed(self, event):  # Handling a key pressed event
        x, y = self.plr[0].getPosition()
        if event == 1:
            self.plr[0].setState(0)
            x += 10
        if event == 2:
            self.plr[0].setState(1)
            x -= 10
        if event == 3:
            y -= 5
        if event == 4:
            y += 10
        x = max(x, 0)
        y = max(y, 0)
        x = min(x, 1170)
        y = min(y, 480)
        if y == 80 and x>700 :
            y+=1
        if (y in self.levellimits and int(self.levellimits[y]) == 1 and x > 1000):
            y += 1
        if (y in self.levellimits and int(self.levellimits[y]) == 2 and x < 170):
            y += 1
        self.plr[0].setPosition((x,y))


    def update(self, screen):  # Update the board
        self.coin_group.draw(screen)
        self.block_group.draw(screen)
        self.ladder_group.draw(screen)
        self.fireball_group.draw(screen)
        self.donkey_group.draw(screen)
        self.castle_block_group.draw(screen)
        self.princess_group.draw(screen)
        self.ladder_group.draw(screen)
        self.plr_group.draw(screen)


    def getLadderCollisions(self):  # Check if player is in touch with any ladder

        state = 0
        broken_ladders = [(650, 335), (650, 400), (850, 255), (850, 320), (300, 95), (300, 160)]
        castleladder = (220, 50)
        for s in self.ladder_group.sprites():
            rect1 = self.plr[0].rect
            rect1.topleft = self.plr[0].getPosition()
            playerx,playery = rect1.topleft
            rect1.height = rect1.width = 20
            rect2 = s.rect
            ladderx,laddery = s.rect.topleft
            rect2.height = 95
            rect2.width = 30
            if rect2.topleft == castleladder:
                rect2.height = 60
            if rect2.topleft in broken_ladders:
                rect2.height = 35
            if rect1.colliderect(rect2):
                if playery not in self.levellimits and playery!=480:
                    self.plr[0].setPosition((ladderx+5,playery))
                self.plr[0].setState(2)
                state = 1
                break
        if state == 1:
            return 1
        else:
            return 0

    def checkfireballcollision(self,de=0):  #Check if player is dead and respawn
        for s in self.fireball_group.sprites():
            rect1 = self.plr[0].rect
            rect1.topleft = self.plr[0].getPosition()
            rect1.height = rect1.width = 20
            rect2 = s.rect
            rect2.height = 25
            rect2.width = 25
            if rect1.colliderect(rect2):
                self.fireballs = []
                self.fireball_group = pygame.sprite.RenderPlain(*self.fireballs)
                if self.plr[0].getLives() == 0:
                    return 0
                else:
                    self.plr[0].setPosition((0,480))
                    self.plr[0].setState(0)
                    self.plr[0].setLives(self.plr[0].getLives()-1)
                    return 1
        return -1

    def dropplayer(self):  # Drop if player is in middle of air
        x, y = self.plr[0].getPosition()
        levelpos = y
        levelpos = min(480,levelpos)
        levelpos = self.playerparentdict[levelpos]

        if y == levelpos:
            return
        self.plr[0].setPosition((x,min(y+10,levelpos)))

    def getCoinCollisions(self):  # Checking collisions with any coin
        for c in self.coin_group.sprites():
            rect1 = self.plr[0].rect
            rect1.topleft = self.plr[0].getPosition()
            rect1.height = rect1.width = 20
            rect2 = c.rect
            rect2.height = rect2.width = 30
            if rect1.colliderect(rect2):
                c.kill()
                return 1
        return 0

    def playerjump(self,jumpspeed):  # Jumping up function
        x, y = self.plr[0].getPosition()
        levelpos = y
        levelpos = min(480,levelpos)
        levelpos = self.playerparentdict[levelpos]

        if y <= levelpos - 30:
            self.plr[0].setPosition((x,levelpos-30))
            return 1
        else:
            self.plr[0].setPosition((x,y-jumpspeed))
            return 0

    def playerjumpdown(self,jumpspeed):  # Jumping down function
        x, y = self.plr[0].getPosition()
        levelpos = y
        levelpos = min(480,levelpos)
        levelpos=self.playerparentdict[levelpos]

        if y >= levelpos:
            self.plr[0].setPosition((x,levelpos))
            return 1
        else:
            self.plr[0].setPosition((x,y+jumpspeed))
            return 0

    def checkplayerlevel(self):  # chaecks that player should not fall down beyond ladder through a block
        x, y = self.plr[0].getPosition()
        for s in self.ladder_group.sprites():
            rect1 = self.plr[0].rect
            rect1.topleft = self.plr[0].getPosition()
            rect1.height = rect1.width = 20
            rect2 = s.rect
            if rect1.colliderect(rect2):
                y = min(y, self.ladderlimits[rect2.topleft])
                self.plr[0].setPosition((x,y))
                break

    def updatefireballs(self,flipdonkey):  #Update fireball positions
        i=0
        for s in self.fireball_group.sprites():
            x, y = s.getPosition()
            if x<=0 and y == 480:
                pass
            else:
                state = s.getState()
                if x <= 0: state = 1
                if x >= 1180: state = 2
                if state != 3:
                    if state == 1:
                        x += 5
                    else:
                        x -= 5
                    collisions = pygame.sprite.spritecollide(s,self.ladder_group,False)
                    if collisions:
                        ly =self.ladderlimits[collisions[0].rect.topleft]
                        ladderx,laddery = collisions[0].rect.topleft
                        if y != ly:
                            val = randint(1,10)
                            if val == 5:
                                y+=10
                                x=ladderx
                                state = 3
                    if y == 80 and x>700 :
                        y+=10
                        state = 3
                    if (y  in self.levellimits and int(self.levellimits[y]) == 1 and x > 1000):
                        y += 10
                        state = 3
                    if (y  in self.levellimits and int(self.levellimits[y]) == 2 and x < 170):
                        y += 10
                        state = 3
                else:
                    y=min(self.fireballparentdict[y],y+10)
                    if self.fireballparentdict[y] == y:
                        state=randint(0,1)
                self.fireballs[i] = fireball.Fireball("fireball.png", "fireball.png", (x, y), 20, 20, state)
                i += 1
        del self.fireballs[i:]
        self.fireball_group = pygame.sprite.RenderPlain(*self.fireballs)
        self.donkey.setPosition((20,50))
        self.donkey.setState(self.donkey.getState()^flipdonkey)

    def getPlayerScore(self):
        return self.plr[0].getScore()

    def setPlayerScore(self,newscore):
        self.plr[0].setScore(newscore)

    def getPlayerLives(self):
        return self.plr[0].getLives()

    def checkwin(self):
        x, y =self.plr[0].getPosition()
        if y<= 35:
            for b in self.castle_block_group.sprites():
                rect1 = self.plr[0].rect
                rect1.topleft = self.plr[0].getPosition()
                rect1.height = rect1.width = 20
                rect2 = b.rect
                if rect1.colliderect(rect2):
                    return 1
        return 0

    def setPlayerstraight(self):
        self.plr[0].setState(3)