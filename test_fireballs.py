__author__ = 'raghuram'
import board

class Test_fireballs:
    def test_creation(self):
        board1 = board.Board(None,0)
        prevFireballCount = len(board1.fireballs)
        board1.createfireball()
        updatedFireballcount = len(board1.fireballs)
        assert updatedFireballcount == prevFireballCount + 1

    def test_movement(self):
        board1 = board.Board(None,0)
        board1.createfireball()
        prevX, prevY = board1.fireballs[0].getPosition()
        for i in range(30):
            board1.updatefireballs()
        curX, curY = board1.fireballs[0].getPosition()
        assert curX > prevX

    def test_drop(self):
        board1 = board.Board(None,0)
        board1.createfireball()
        prevX, prevY = board1.fireballs[0].getPosition()
        for i in range(200):
            board1.updatefireballs()
        curX, curY = board1.fireballs[0].getPosition()
        assert curY > prevY
