import unittest

from tictascii.ticlib.base import Board


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def testInitialMatrix(self):
        self.assertEquals(self.board._get_none_matrix(3), [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ])

    def testHorizontalWinningMarker(self):
        self.assertEquals('X', self.board._get_winning_marker([
            ['X', 'X', 'X'],
            [None, None, None],
            [None, None, None],
        ]))

    def testVerticalWinningMarker(self):
        self.assertEquals('O', self.board._get_winning_marker([
            ['O', None, None],
            ['O', None, None],
            ['O', None, None],
        ]))

    def testDownRightDiagonalWinningMarker(self):
        self.assertEquals('O', self.board._get_winning_marker([
            ['O', None, None],
            [None, 'O', None],
            [None, None, 'O'],
        ]))

    def testDownLeftDiagonalWinningMarker(self):
        self.assertEquals('X', self.board._get_winning_marker([
            [None, None, 'X'],
            [None, 'X', None],
            ['X', None, None],
        ]))

    def testNoWinningMarker(self):
        self.assertEquals(None, self.board._get_winning_marker([
            ['O', 'O', 'X'],
            ['X', None, 'X'],
            ['X', 'X', 'O'],
        ]))
