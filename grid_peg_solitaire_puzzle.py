from puzzle import Puzzle


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    # TODO
    # implement __eq__, __str__ methods
    # __repr__ is up to you
    def __eq__(self, other):
        """
        Return whether GridPegSolitairePuzzle self is equivalent to other.

        @type self: GridPegSolitairePuzzle
        @type other: GridPegSolitairePuzzle
        @rtype: Bool

        >>> grid = [["*", "*", ".", "*"], ["*", "*", "*", "*"]]
        >>> grid += [["*", "*", "*", "*"], ["*", "*", "*", "*"]]
        >>> gpsp1 = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> gpsp2 = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> repr(gpsp1) == repr(gpsp2)
        True
        """
        return type(self), self._marker, self._marker_set == type(other), \
               other._marker, other._marker_set

    def __str__(self):
        """
        Return a string representation of GridPegSolitairePuzzle self.

        @type self: GridPegSolitairePuzzle
        @rtype: str

        Due to the fact that sets are not ordered, the output is different every
         time and the test fails. That's why we are omitting the example.
        """
        gr = ''
        for i in range(len(self._marker)):
            gr += str(self._marker[i]) + '\n'
        return "Grid:\n{}\nMarker set: {}".format(gr, self._marker_set)

    def __repr__(self):
        """
        Representation of GridPegSolitairePuzzle self.

        @type self: GridPegSolitairePuzzle
        @rtype: str

        Same as with str method, ue to the fact that sets are not ordered, the
        output is different every time and the test fails. That's why we are
        omitting the example.
        """
        gr = ''
        for i in range(len(self._marker)):
            gr += str(self._marker[i]) + '\n'
        return "Grid:\n{}\nMarker set: {}".format(gr, self._marker_set)

    # TODO
    # override extensions
    # legal extensions consist of all configurations that can be reached by
    # making a single jump from this configuration

    def extensions(self):
        """
        Return list of legal extensions of GridPegSolitairePuzzle self.

        @type self: GridPegSolitairePuzzle
        @rtype: list[GridPegSolitairePuzzle]

        >>> grid = [['*', '.', '*', '*'], ['*', '*', '*', '*']]
        >>> grid += [['*', '*', '*', '*'], ['*', '*', '*', '*']]
        >>> gpsp1 = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> gpsp2 = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> gpsp1.extensions() == gpsp2.extensions()
        True
        """
        # finding empty positions
        empty = []
        extensions = []
        for i in range(len(self._marker)):
            for j in range(len(self._marker[i])):
                if self._marker[i][j] == '.':
                    row = i
                    column = j
                    empty.append((row, column))
        for dot in empty:
            row = dot[0]
            column = dot[1]
            # for top
            if row - 2 >= 0 and self._marker[row - 2][column] == '*' and \
               self._marker[row - 1][column] == '*':
                # hard copy
                new = [x.copy() for x in self._marker]
                new[row - 1][column], new[row][column], new[row - 2][column] = \
                    '.', '*', '.'
                extensions.append(GridPegSolitairePuzzle(new, self._marker_set))
            # for bottom
            if row + 2 < len(self._marker) and self._marker[row + 2][column] \
                    == '*' and self._marker[row + 1][column] == '*':
                new = [x.copy() for x in self._marker]
                new[row + 1][column], new[row][column], new[row + 2][column] = \
                    '.', '*', '.'
                extensions.append(GridPegSolitairePuzzle(new, self._marker_set))
            # for left
            if column - 2 >= 0 and self._marker[row][column - 2] == '*' and \
               self._marker[row][column - 2] == '*':
                new = [x.copy() for x in self._marker]
                new[row][column], new[row][column - 1], new[row][column - 2] = \
                    '*', '.', '.'
                extensions.append(GridPegSolitairePuzzle(new, self._marker_set))
            # for right
            if column + 2 < len(self._marker[0]) and \
               self._marker[row][column + 2] == '*' and \
               self._marker[row][column + 1] == '*':
                new = [x.copy() for x in self._marker]
                new[row][column], new[row][column + 1], new[row][column + 2] = \
                    '*', '.', '.'
        return extensions

    # TODO
    # override is_solved
    # A configuration is solved when there is exactly one "*" left

    def is_solved(self):
        """
        Return whether GridPegSolitairePuzzle self is solved.

        @type self: GridPegSolitairePuzzle
        @rtype: bool

        >>> grid = [[".", "*", ".", "."], [".", ".", ".", "."]]
        >>> grid += [[".", ".", ".", "."], [".", ".", ".", "."]]
        >>> gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
        >>> gpsp.is_solved()
        True
        """
        c = 0
        for i in range(len(self._marker)):
            c += self._marker[i].count('*')
        return c == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))
