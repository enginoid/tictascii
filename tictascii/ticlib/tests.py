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
