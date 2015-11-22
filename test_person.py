__author__ = 'raghuram'
import board

class Test_person:

    def test_movement(self):
        board1 = board.Board(None,0)
        prevX, prevY = board1.plr[0].getPosition()
        board1.key_pressed(1)
        curX, curY = board1.plr[0].getPosition()
        assert curY == prevY
        assert curX == prevX + board1.PLAYER_SPEED


    def test_right_collision(self):
        board1 = board.Board(None,0)
        for i in range(300):
            board1.key_pressed(1)
        curX, curY = board1.plr[0].getPosition()
        assert curX <= 1700

    def test_left_collision(self):
        board1 = board.Board(None,0)
        for i in range(300):
            board1.key_pressed(1)
        for i in range(300):
            board1.key_pressed(2)
        curX, curY = board1.plr[0].getPosition()
        assert curX >= 0

    def test_ladder_climb(self):
        board1 = board.Board(None,0)
        curX, curY = board1.plr[0].getPosition()
        board1.plr[0].setPosition((800, curY))
        board1.key_pressed(3)
        newX, newY = board1.plr[0].getPosition()
        assert newY < curY

    def test_jump(self):
        board1 = board.Board(None, 0)
        curX, curY = board1.plr[0].getPosition()
        jumpstate = 1
        jumpspeed = 10
        for i in range(100):
            if jumpstate == 1:
                if board1.playerjump(jumpspeed) == 1:
                    jumpstate = 2
                    jumpspeed = 0
                else:
                    jumpspeed -= 2

            if jumpstate == 2:
                if board1.playerjumpdown(jumpspeed) == 1:
                    jumpstate = 0
                    jumpspeed = 10
                else:
                    jumpspeed += 2
            
            newX, newY = board1.plr[0].getPosition()

            assert newY <= curY and newY >= curY - board1.JUMP_LIMIT


    def test_coin_collect(self):
        board1 = board.Board(None, 0)
        curScore = board1.plr[0].getScore()
        coin_posX, coin_posY = board1.coins[0].getPosition()
        board1.plr[0].setPosition((coin_posX,coin_posY))
        collectCoin = board1.getCoinCollisions()
        assert collectCoin == 1

    def test_midair_fall(self):
        board1 = board.Board(None, 0)
        curX, curY = (750, 75) #mid air random getPosition
        board1.plr[0].setPosition((curX,curY))
        board1.checkMidAir()
        newX, newY = board1.plr[0].getPosition()
        assert newY <= curY