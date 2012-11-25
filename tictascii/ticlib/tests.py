import unittest
import random

from tictascii.ticlib.base import Board
from tictascii.ticlib.players import Player, HumanPlayer


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def testInitialMatrix(self):
        self.assertEquals(self.board._get_none_matrix(3), [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ])


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def testInitialPlayer(self):
        self.assertEquals(self.player.get_wins(), 0)

    def testIncrementWins(self):
        self.player = Player()
        self.player.increment_wins()
        self.assertEquals(self.player.get_wins(), 1)

    def testGamesWon(self):
        self.player = Player()
        self.assertEquals(self.player.get_wins(), 0)


def raw_input_mock():
    return random.randint(1, 9)


class HumanPlayerTest(unittest.TestCase):

    raw_input = raw_input_mock

    def setUp(self):
        self.player = HumanPlayer()
