__author__ = 'raghuram'
import pygame
from random import randint
import random

import player
import princess
import donkey
import block
import fireball
import coin
import ladder


class Board:
    def __init__(self, screen):
        self.blocks = []
        self.ladders = []
        self.coins = []
        self.fireballs = []
        self.castleblocks = []
        self.levellimits = {}
        self.ladderlimits = {}
        self.donkey = None
        self.princess = None
        self.donkey_group = []
        self.princess_group = []
        # start defining Constamts here
        self.PLAYER_SPEED = 10
        self.PLAYER_CLIMB_SPEED = 5
        self.FULL_LADDER_HEIGHT = 95
        self.LADDER_WIDTH = 30
        self.HALF_LADDER_HEIGHT = 35
        self.PLAYER_HEIGHT = 20
        self.PLAYER_WIDTH = 20
        self.COIN_WIDTH = 20
        self.COIN_HEIGHT = 20
        self.COIN_LEVELS = [470, 390, 310, 230, 150, 70]
        self.FIREBALL_HEIGHT = 25
        self.FIREBALL_WIDTH = 25
        self.FIREBALL_SPEED = 5
        self.JUMP_LIMIT = 30
        self.PLAYER_SPAWN_LEVEL = 480
        self.DONKEY_SPEED = 3
        self.PLAYER_DROP_LEVEL = None
        # End defining constants
        self.block_group = pygame.sprite.RenderPlain(*self.blocks)
        self.ladder_group = pygame.sprite.RenderPlain(*self.ladders)
        self.coin_group = pygame.sprite.RenderPlain(*self.coins)
        self.fireball_group = pygame.sprite.RenderPlain(*self.fireballs)
        self.castle_block_group = pygame.sprite.RenderPlain(*self.blocks)
        self.initlogs(screen)
        self.initladders(screen)
        self.initcoins(screen)
        self.initdonkey(screen)
        self.initprincess(screen)
        self.initcastle(screen)
        self.plr = [player.Player("Images/player2.png", "Images/player.png", "Images/player3.png", "Images/player4.png",
                                  (0, self.PLAYER_SPAWN_LEVEL), self.PLAYER_WIDTH, self.PLAYER_HEIGHT, 0, 2)]
        self.plr_group = pygame.sprite.RenderPlain(*self.plr)
        self.plr_group.draw(screen)
        self.playerparentdict = {}
        self.fireballparentdict = {}
        self.playerparentdict[500] = self.PLAYER_SPAWN_LEVEL
        for i in range(499, 0, -1):  # Player's regular positions in each level
            if i in [480, 400, 320, 240, 160, 80]:
                self.playerparentdict[i] = i
            else:
                self.playerparentdict[i] = self.playerparentdict[i + 1]
        self.fireballparentdict[500] = self.PLAYER_SPAWN_LEVEL
        for i in range(499, 0, -1):  # Fireballs' regular positions in each level
            if i in [480, 400, 320, 240, 160, 80]:
                self.fireballparentdict[i] = i
            else:
                self.fireballparentdict[i] = self.fireballparentdict[i + 1]

    def initlogs(self, screen):  # Initialize all blocks
        self.levellimits = {400: 1, 320: 2, 240: 1, 160: 2, 80: 1, 30: 3}
        self.blocks = [block.Block("Images/log.png", "Images/log.png", (0, 0), 1200, 20),
                       block.Block("Images/log.png", "Images/log.png", (0, 100), 700, 20),
                       block.Block("Images/log.png", "Images/log.png", (200, 180), 1000, 20),
                       block.Block("Images/log.png", "Images/log.png", (0, 260), 1000, 20),
                       block.Block("Images/log.png", "Images/log.png", (200, 340), 1000, 20),
                       block.Block("Images/log.png", "Images/log.png", (0, 420), 1000, 20),
                       block.Block("Images/log.png", "Images/log.png", (0, 500), 1200, 20),
                       ]
        self.block_group = pygame.sprite.RenderPlain(*self.blocks)
        self.block_group.draw(screen)

    def initdonkey(self, screen):  # Initialize donkey
        self.donkey = donkey.Donkey("Images/Donkey2.png", "Images/Donkey.png", (20, 50), 40, 50, 0)
        self.donkey_group = pygame.sprite.RenderPlain(self.donkey)
        self.donkey_group.draw(screen)

    def initprincess(self, screen):  # Initialize princess
        self.princess = princess.Princess("Images/princess2.png", "Images/princess2.png", (120, 20), 20, 30, 0)
        self.princess_group = pygame.sprite.RenderPlain(self.princess)
        self.princess_group.draw(screen)

    def initladders(self, screen):  # Initialize all ladders

        self.ladders = [ladder.Ladder("Images/ladder.png", "Images/ladder.png", (800, 419), self.LADDER_WIDTH,
                                      self.FULL_LADDER_HEIGHT),
                        ladder.Ladder("Images/ladder.png", "Images/ladder.png", (300, 339), self.LADDER_WIDTH,
                                      self.FULL_LADDER_HEIGHT),
                        ladder.Ladder("Images/ladder.png", "Images/ladder.png", (500, 259), self.LADDER_WIDTH,
                                      self.FULL_LADDER_HEIGHT),
                        ladder.Ladder("Images/ladder.png", "Images/ladder.png", (900, 179), self.LADDER_WIDTH,
                                      self.FULL_LADDER_HEIGHT),
                        ladder.Ladder("Images/ladder.png", "Images/ladder.png", (600, 99), self.LADDER_WIDTH,
                                      self.FULL_LADDER_HEIGHT),
                        ladder.Ladder("Images/ladder_broken.png", "Images/ladder_broken.png", (650, 335),
                                      self.LADDER_WIDTH, self.HALF_LADDER_HEIGHT),
                        ladder.Ladder("Images/ladder_broken_down.png", "Images/ladder_broken_down.png", (650, 400),
                                      self.LADDER_WIDTH, self.HALF_LADDER_HEIGHT),
                        ladder.Ladder("Images/ladder_broken.png", "Images/ladder_broken.png", (850, 255),
                                      self.LADDER_WIDTH, self.HALF_LADDER_HEIGHT),
                        ladder.Ladder("Images/ladder_broken_down.png", "Images/ladder_broken_down.png", (850, 320),
                                      self.LADDER_WIDTH, self.HALF_LADDER_HEIGHT),
                        ladder.Ladder("Images/ladder_broken.png", "Images/ladder_broken.png", (300, 95),
                                      self.LADDER_WIDTH, self.HALF_LADDER_HEIGHT),
                        ladder.Ladder("Images/ladder_broken_down.png", "Images/ladder_broken_down.png", (300, 160),
                                      self.LADDER_WIDTH, self.HALF_LADDER_HEIGHT),
                        ladder.Ladder("Images/castleladder.png", "Images/castleladder.png", (220, 45),
                                      self.LADDER_WIDTH, ((self.FULL_LADDER_HEIGHT - 5) * 2) / 3)
                        ]

        for l in self.ladders:
            x, y = l.getPosition()
            w, h = l.getSize()
            if h == self.FULL_LADDER_HEIGHT:
                self.ladderlimits[l.getPosition()] = y + 1 + 60
            else:
                if h == ((self.FULL_LADDER_HEIGHT - 5) * 2) / 3:
                    self.ladderlimits[l.getPosition()] = y + 5 + 30
                elif y % 10 == 0:
                    self.ladderlimits[l.getPosition()] = y
                else:
                    self.ladderlimits[l.getPosition()] = y + 5 + 60
        self.ladder_group = pygame.sprite.RenderPlain(*self.ladders)
        self.ladder_group.draw(screen)

    def initcoins(self, screen):  # Initialize all coins
        self.coins = []
        x = 0
        for i in range(0, 20):
            y = self.COIN_LEVELS[randint(0, 5)]
            if y == 470:
                x = random.randrange(0, 1170, 30)
            elif y in [390, 230]:
                x = random.randrange(0, 1000, 30)
            elif y in [310, 150]:
                x = random.randrange(200, 1170, 30)
            elif y == 70:
                x = random.randrange(350, 700, 30)

            self.coins += [coin.Coin("Images/coin.png", "Images/coin.png", (x, y), self.COIN_WIDTH, self.COIN_HEIGHT)]

        self.coin_group = pygame.sprite.RenderPlain(*self.coins)
        self.coin_group.draw(screen)

    def initcastle(self, screen):
        self.castleblocks = [block.Block("Images/castle.png", "Images/castle.png", (110, 50), 180, 10),
                             block.Block("Images/castlepillar.png", "Images/castlepillar.png", (100, 20), 20, 40),
                             block.Block("Images/castlepillar.png", "Images/castlepillar.png", (280, 20), 20, 40),
                             ]
        self.castle_block_group = pygame.sprite.RenderPlain(*self.castleblocks)
        self.castle_block_group.draw(screen)

    def createfireball(self):  # Creating fireballs
        donkeyx, donkeyy = self.donkey.getPosition()
        self.fireballs += [fireball.Fireball("Images/fireball.png", "Images/fireball.png", (donkeyx + 5, 80),
                                             self.FIREBALL_WIDTH, self.FIREBALL_HEIGHT, randint(1, 2))]
        self.fireball_group = pygame.sprite.RenderPlain(*self.fireballs)

    def key_pressed(self, event):  # Handling a key pressed event
        x, y = self.plr[0].getPosition()
        if event == 1:
            self.plr[0].setState(0)
            x += self.PLAYER_SPEED
        if event == 2:
            self.plr[0].setState(1)
            x -= self.PLAYER_SPEED
        if event == 3:
            y -= self.PLAYER_CLIMB_SPEED
        if event == 4:
            y += self.PLAYER_SPEED
        x = max(x, 0)
        y = max(y, 0)
        x = min(x, 1170)
        y = min(y, self.PLAYER_SPAWN_LEVEL)
        self.plr[0].setPosition((x, y))

    def checkMidAir(self):  # Detecting that player should drop beyond block limits
        x, y = self.plr[0].getPosition()
        if y == 80 and x > 700:
            y += 0.1 * self.PLAYER_SPEED
        if y in self.levellimits and int(self.levellimits[y]) == 1 and x > 1000:
            y += 0.1 * self.PLAYER_SPEED
        if y in self.levellimits and int(self.levellimits[y]) == 2 and x < 170:
            y += 0.1 * self.PLAYER_SPEED
        self.plr[0].setPosition((x, y))

    def update(self, screen):  # Update the board
        self.coin_group.draw(screen)
        self.block_group.draw(screen)
        self.castle_block_group.draw(screen)
        self.ladder_group.draw(screen)
        screen.blit(self.donkey.image, self.donkey.getPosition())
        self.fireball_group.draw(screen)
        self.princess_group.draw(screen)
        self.plr_group.draw(screen)

    def getLadderCollisions(self):  # Check if player is in touch with any ladder

        state = 0
        broken_ladders = [(650, 335), (650, 400), (850, 255), (850, 320), (300, 95), (300, 160)]
        castleladder = (220, 50)
        for s in self.ladder_group.sprites():
            rect1 = self.plr[0].rect
            rect1.topleft = self.plr[0].getPosition()
            playerx, playery = rect1.topleft
            rect1.height = self.PLAYER_HEIGHT
            rect1.width = self.PLAYER_WIDTH
            rect2 = s.rect
            ladderx, laddery = s.rect.topleft
            rect2.height = self.FULL_LADDER_HEIGHT
            rect2.width = self.LADDER_WIDTH
            if rect2.topleft == castleladder:
                rect2.height = ((self.FULL_LADDER_HEIGHT - 5) * 2) / 3
            if rect2.topleft in broken_ladders:
                rect2.height = self.HALF_LADDER_HEIGHT
            if rect1.colliderect(rect2):
                if playery not in self.levellimits and playery != self.PLAYER_SPAWN_LEVEL:
                    self.plr[0].setPosition((ladderx + 5, playery))
                self.plr[0].setState(2)
                state = 1
                break
        if state == 1:
            return 1
        else:
            return 0

    def checkfireballcollision(self):  # Check if player is dead and respawn
        for s in self.fireball_group.sprites():
            rect1 = self.plr[0].rect
            rect1.topleft = self.plr[0].getPosition()
            rect1.height = rect1.width = 20
            rect2 = s.rect
            rect2.height = self.FIREBALL_HEIGHT
            rect2.width = self.FIREBALL_WIDTH
            if rect1.colliderect(rect2):
                if self.plr[0].getLives() == 0:
                    return 0
                else:
                    self.respawnPlayer()
                    self.plr[0].setState(0)
                    self.plr[0].setLives(self.plr[0].getLives() - 1)
                    return 1
        return -1

    def dropplayer(self):  # Drop if player is in middle of air
        x, y = self.plr[0].getPosition()
        levelpos = y
        levelpos = min(self.PLAYER_SPAWN_LEVEL, levelpos)
        levelpos = self.playerparentdict[levelpos]

        if y == levelpos:
            return
        self.plr[0].setPosition((x, min(y + 10, levelpos)))

    def getCoinCollisions(self):  # Checking collisions with any coin
        for c in self.coin_group.sprites():
            rect1 = self.plr[0].rect
            rect1.topleft = self.plr[0].getPosition()
            rect1.height = self.PLAYER_HEIGHT
            rect1.width = self.PLAYER_WIDTH
            rect2 = c.rect
            rect2.height = self.COIN_HEIGHT
            rect2.width = self.COIN_WIDTH
            if rect1.colliderect(rect2):
                c.kill()
                return 1
        return 0

    def playerjump(self, jumpspeed):  # Jumping up function
        x, y = self.plr[0].getPosition()
        levelpos = y
        levelpos = min(self.PLAYER_SPAWN_LEVEL, levelpos)
        levelpos = self.playerparentdict[levelpos]

        if y == levelpos:
            self.PLAYER_DROP_LEVEL = y
        if y <= levelpos - self.JUMP_LIMIT:
            self.plr[0].setPosition((x, levelpos - self.JUMP_LIMIT))
            return 1
        else:
            self.plr[0].setPosition((x, y - jumpspeed))
            return 0

    def playerjumpdown(self, jumpspeed):  # Jumping down function
        x, y = self.plr[0].getPosition()
        levelpos = y
        if self.PLAYER_DROP_LEVEL:
            if min(levelpos, self.PLAYER_DROP_LEVEL) == self.PLAYER_DROP_LEVEL:
                levelpos = min(levelpos, self.PLAYER_DROP_LEVEL)
                self.PLAYER_DROP_LEVEL = None
        levelpos = self.playerparentdict[levelpos]

        if y >= levelpos:
            self.plr[0].setPosition((x, levelpos))
            return 1
        else:
            self.plr[0].setPosition((x, y + jumpspeed))
            return 0

    def checkplayerlevel(self):  # checks that player should not fall down beyond ladder through a block
        x, y = self.plr[0].getPosition()
        for s in self.ladder_group.sprites():
            rect1 = self.plr[0].rect
            rect1.topleft = self.plr[0].getPosition()
            rect1.height = self.PLAYER_HEIGHT
            rect1.width = self.PLAYER_WIDTH
            rect2 = s.rect
            if rect1.colliderect(rect2):
                y = min(y, self.ladderlimits[rect2.topleft])
                self.plr[0].setPosition((x, y))
                break

    def updatefireballs(self):  # Update fireball positions and directions
        i = 0
        for s in self.fireball_group.sprites():
            x, y = s.getPosition()
            if x <= 0 and y == self.PLAYER_SPAWN_LEVEL:
                pass
            else:
                state = s.getState()
                if x <= 0:
                    state = 1
                if x >= 1180:
                    state = 2
                if state != 3:
                    if state == 1:
                        x += self.FIREBALL_SPEED
                    else:
                        x -= self.FIREBALL_SPEED
                    collisions = pygame.sprite.spritecollide(s, self.ladder_group, False)
                    if collisions:
                        ly = self.ladderlimits[collisions[0].rect.topleft]
                        ladderx, laddery = collisions[0].rect.topleft
                        if y != ly:
                            val = randint(1, 10)
                            if val == 5:
                                y += 2 * self.FIREBALL_SPEED
                                x = ladderx
                                state = 3
                    if y == 80 and x > 700:
                        y += 2 * self.FIREBALL_SPEED
                        state = 3
                    if y in self.levellimits and int(self.levellimits[y]) == 1 and x > 1000:
                        y += 2 * self.FIREBALL_SPEED
                        state = 3
                    if y in self.levellimits and int(self.levellimits[y]) == 2 and x < 170:
                        y += 2 * self.FIREBALL_SPEED
                        state = 3
                else:
                    y = min(self.fireballparentdict[y], y + 2 * self.FIREBALL_SPEED)
                    if self.fireballparentdict[y] == y:
                        state = randint(0, 1)
                self.fireballs[i] = fireball.Fireball("Images/fireball.png", "Images/fireball.png", (x, y),
                                                      self.FIREBALL_WIDTH, self.FIREBALL_HEIGHT, state)
                i += 1
        del self.fireballs[i:]
        self.fireball_group = pygame.sprite.RenderPlain(*self.fireballs)

    def updatedonkey(self, flipdonkey):  #Update donkey position and direction
        self.donkey.setState(self.donkey.getState() ^ flipdonkey)
        direction = self.donkey.getdirection()
        x, y = self.donkey.getPosition()
        if x >= 180:
            direction = 1
        if x <= 0:
            direction = 0
        if direction == 0:
            x += self.DONKEY_SPEED
        else:
            x -= self.DONKEY_SPEED
        self.donkey.setdirection(direction)
        self.donkey.setPosition((x, y))
        self.donkey_group = pygame.sprite.RenderPlain(self.donkey)

    def getPlayerScore(self):
        return self.plr[0].getScore()

    def setPlayerScore(self, newscore):
        self.plr[0].setScore(newscore)

    def getPlayerLives(self):
        return self.plr[0].getLives()

    def checkwin(self):   # check if player reached destination
        x, y = self.plr[0].getPosition()
        if y <= 35:
            for b in self.castle_block_group.sprites():
                rect1 = self.plr[0].rect
                rect1.topleft = self.plr[0].getPosition()
                rect1.height = self.PLAYER_HEIGHT
                rect1.width = self.PLAYER_WIDTH
                rect2 = b.rect
                if rect1.colliderect(rect2):
                    return 1
        return 0

    def setPlayerstraight(self): # Set player straight when not moving
        self.plr[0].setState(3)

    def respawnPlayer(self): # Respawn player at left bottom
        self.killfireballs()
        self.plr[0].setPosition((0, self.PLAYER_SPAWN_LEVEL))

    def setplayerlives(self):
        self.plr[0].setLives(2)

    def killfireballs(self):  # Kill all fireballs
        self.fireballs = []
        self.fireball_group = pygame.sprite.RenderPlain(*self.fireballs)

    def upgradeplayerlevel(self):
        self.plr[0].upgradelevel()

    def getplayerlevel(self):
        return self.plr[0].getlevel()

    def boostfireball(self): # Increase speed of fireball
        self.FIREBALL_SPEED += 2
