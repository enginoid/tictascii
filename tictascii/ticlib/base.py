from tictascii.ticlib.exceptions import MarkerExists, MarkerOutOfRange


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

    def _get_winning_marker(self, matrix):
        """
        Returns the winning marker for a given board matrix if a winner
        exists for the matrix, otherwise `None`.  A winner is defined is
        someone who has a marker across the entire board matrix.
        """
        matrix_indices = range(self.DIMENSIONS)
        get_row = lambda n: matrix[n]
        get_column = lambda n: (matrix[i][n] for i in matrix_indices)

        # Create a list of marker 3-sequences
        sequences = []
        sequences.extend(get_row(i) for i in matrix_indices)
        sequences.extend(get_column(i) for i in matrix_indices)

        # Diagonal li from top-left to bottom-right.
        sequences.append((matrix[i][i] for i in matrix_indices))

        # Diagonal line from bottom-left to top-right.
        sequences.append((matrix[i][(self.DIMENSIONS - 1) - i]
                          for i in matrix_indices))

        # Check whether there's any winning sequence by going through all
        # possible sequences and determining whether they only consist of
        # a single marker.
        for sequence in sequences:
            try:
                [winning_marker] = set(sequence)  # set removes duplicates
            except ValueError:  # unpacking error if not exactly 1 marker
                pass  # just move on to the next sequence
            else:
                # don't consider `None` sequences as winners
                if winning_marker:
                    return winning_marker

    def set_marker(self, marker, x, y):
        """
        Set the position (x, y) to `marker` and check for errors.

        Raises:
            MarkerOutOfRange -- if the `x` and `y` given are invalid
            MarkerExists -- if there's already a marker at this location
        """
        try:
            current_mark = self.player_moves[x][y]
        except IndexError:
            raise MarkerOutOfRange("This marker doesn't fit on the board.")
        else:
            if current_mark:
                raise MarkerExists("This marker already exists.")
            self.player_moves[x][y] = marker
