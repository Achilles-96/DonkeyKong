__author__ = 'raghuram'

import board

class Test_donkey:
    def test_movement(self):
        board1 = board.Board(None,0)
        prevX, prevY = board1.donkey.getPosition()
        for i in range(30):
            board1.updatedonkey(0)
        updatedX, updatedY = board1.donkey.getPosition()
        assert updatedY == prevY
        assert updatedX > prevX

    def test_donkey_range(self):
        board1 = board.Board(None,0)
        for i in range(300):
            board1.updatedonkey(0)
            curX, curY = board1.donkey.getPosition()
            assert curX >= 0
            assert curX <= 180
