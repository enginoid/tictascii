from ticlib.players import HumanPlayer, ComputerPlayer
from ticlib.base import Tournament, Board


def get_participating_players(raw_input=raw_input):
    """
   Allows the user to select number of human players.
   Validates input and returns a matching tuple of players.
   """
    no_players = 0
    while no_players != 1 and no_players != 2:
        inp = raw_input("Single player or multiplayer? (1/2): ")
        try:
            no_players = int(inp)
        except ValueError:
            print "Invalid input - please try again"
            pass

    if no_players is 1:
        return (HumanPlayer('X'), ComputerPlayer('O'))
    else:
        return (HumanPlayer('X'), HumanPlayer('O'))


if __name__ == "__main__":
    main()
