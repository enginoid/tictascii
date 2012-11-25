
import random


class Player(object):

    def __init__(self):
        self.games_won = 0

    def increment_wins(self):
        self.games_won += 1

    def get_wins(self):
        return self.games_won


class HumanPlayer(Player):

    def make_a_move(self, board):
        move = 0
        while not board.validate_input(move):
            move = raw_input("Make yo' move: ")
            if not board.validate_input(move):
                move = raw_input("Illegal input - try again: ")
        board.set_mark(move)


class ComputerPlayer(Player):

    def make_a_move(self, board):
        move = random.randint(1, 9)
        while not board.validate_input(move):
            move = random.randint(1, 9)
        board.set_mark(move)
