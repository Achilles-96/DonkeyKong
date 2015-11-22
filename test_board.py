__author__ = 'raghuram'

import board
import pygame

class Test_board:
    def test_coins(self):
        board1 = board.Board(None,0)
        coin_count = len(board1.coins)
        assert coin_count == 20
        for coin in board1.coins:
        	posX, posY = coin.getPosition()
        	assert posX >= 0 
        	assert posX <= 1170

    def test_ladders(self):
        board1 = board.Board(None,0)
        ladder_count = len(board1.ladders)
        assert ladder_count == 12