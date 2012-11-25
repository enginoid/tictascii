
import random
from tictascii.ticlib.exceptions import MarkerOutOfRange, MarkerExists


class Player(object):

    def __init__(self, marker):
        self.marker = marker
        self.games_won = 0

    def increment_wins(self):
        self.games_won += 1

    def get_wins(self):
        return self.games_won

    def make_a_move(self):
        raise NotImplementedError()


class HumanPlayer(Player):

    def make_a_move(self, board):
        while True:
            try:
                x = int(raw_input("X: "))
                y = int(raw_input("Y: "))
            except MarkerOutOfRange:
                print "The provided marker isn't within the board range."
            except MarkerExists:
                print "A marker has already been placed at this location."
            else:
                board.set_marker(self.marker, x, y)
                return


class ComputerPlayer(Player):

    def make_a_move(self, board):
        while True:
            try:
                x = random.randint(0, 3)
                y = random.randint(0, 3)
            except MarkerExists:
                pass  # just retry if there's already a marker here
            else:
                board.set_marker(self.marker, x, y)
                return
