class Board(object):
    DIMENSIONS = 3

    def __init__(self):
        self.player_moves = self._get_none_matrix(self.DIMENSIONS)

    def _get_none_matrix(self, dimensions):
        """
        Returns an NxN list of lists with values initialized to `None`,
        where N is the provided `dimensions`.
        """
        get_none_row = lambda length: [None for _ in range(length)]
        return [get_none_row(dimensions) for _ in range(dimensions)]
