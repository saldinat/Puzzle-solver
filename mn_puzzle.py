from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    # TODO
    # implement __eq__ and __str__
    # __repr__ is up to you
    def __eq__(self, other):
        """
        Return whether MNPuzzle self is equivalent to other.

        @param MNpuzzle self: this MNPuzzle
        @param MNPuzzle other: other MNPuzzle
        #rtype: Bool

        >>> p1 = MNPuzzle((("1", "2", "3"), ("4", "*", "5")), (("1", "2", "3"), ("4", "5", "")))
        >>> p2 = MNPuzzle((("1", "2", "3"), ("4", "*", "5")), (("1", "2", "3"), ("4", "5", "")))
        >>> repr(p1) == repr(p2)
        True
        """
        return (type(self), self.from_grid, self.to_grid == type(other),
                other.from_grid, self.to_grid)

    def __str__(self):
        """
        String representation of MNPuzzle self.

        @param MNPuzzle self: this MNPUzzle self
        @rtype: str

        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> p = MNPuzzle(start_grid, target_grid)
        >>> str(p)
        "From grid:\\n('*', '2', '3')\\n('1', '4', '5')\\nTo grid:\\n('1', '2', '3')\\n('4', '5', '*')\\n"
        """
        from_ = ''
        to_ = ''
        for i in range(len(self.from_grid)):
            from_ += str(self.from_grid[i]) + '\n'
            to_ += str(self.to_grid[i]) + '\n'
        return 'From grid:\n{}To grid:\n{}'.format(from_, to_)

    def __repr__(self):
        """
        Representation of MNPUzzle self.

        @type self: MNPuzzle
        @rtype: str

        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> p = MNPuzzle(start_grid, target_grid)
        >>> str(p)
        "From grid:\\n('*', '2', '3')\\n('1', '4', '5')\\nTo grid:\\n('1', '2', '3')\\n('4', '5', '*')\\n"
        """
        return 'From grid: {}, To grid: {}'.format(self.from_grid, self.to_grid)

    # TODO
    # override extensions
    # legal extensions are configurations that can be reached by swapping one
    # symbol to the left, right, above, or below "*" with "*"
    def extensions(self):
        """
        Return list of extensions of MNPuzzle self.

        @type self: MNPuzzle
        @rtype: list[MNPuzzle]

        EXAMPLES
        """
        # finding the index of the empty position(row, column)
        row = 0
        column = 0
        for i in range(len(self.from_grid)):
            if '*' in self.from_grid[i]:
                row = i
                column = self.from_grid[i].index('*')

        puzzle_list = []
        from_l = []
        # swap on the right
        if column + 1 < len(self.from_grid[row]):
            from_l = [list(x) for x in self.from_grid]
            from_l[row][column], from_l[row][column + 1] = \
                from_l[row][column + 1], from_l[row][column]
            for i in range(len(from_l)):
                from_l[i] = tuple(from_l[i])
            puzzle_list.append(MNPuzzle(tuple(from_l), self.to_grid))

        # swap on the left
        if column - 1 > 0:
            from_l = [list(x) for x in self.from_grid]
            from_l[row][column], from_l[row][column - 1] = \
                from_l[row][column - 1], from_l[row][column]
            for i in range(len(from_l)):
                from_l[i] = tuple(from_l[i])
            puzzle_list.append(MNPuzzle(tuple(from_l), self.to_grid))

        # swap on the bottom
        if row + 1 < len(self.from_grid):
            from_l = [list(x) for x in self.from_grid]
            from_l[row][column], from_l[row + 1][column] = \
                from_l[row + 1][column], from_l[row][column]
            for i in range(len(from_l)):
                from_l[i] = tuple(from_l[i])
            puzzle_list.append(MNPuzzle(tuple(from_l), self.to_grid))

        # swap on the top
        if row - 1 >= 0:
            from_l = [list(x) for x in self.from_grid]
            from_l[row][column], from_l[row - 1][column] = \
                from_l[row - 1][column], from_l[row][column]
            for i in range(len(from_l)):
                from_l[i] = tuple(from_l[i])
            puzzle_list.append(MNPuzzle(tuple(from_l), self.to_grid))

        return puzzle_list

    # TODO
    # override is_solved
    # a configuration is solved when from_grid is the same as to_grid

    def is_solved(self):
        """
        Return whether MNPuzzle self is solved.

        @type self: MNPuzzle
        @rtype: bool

        >>> from_grid = (("1", "2", "*"), ("4", "5", "6"))
        >>> to_grid = (("1", "2", "*"), ("4", "5", "6"))
        >>> mn = MNPuzzle(from_grid, to_grid)
        >>> mn.is_solved()
        True
        """
        return self.from_grid == self.to_grid


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("1", "2", "3"), ("5", "*", "5"))
    #from puzzle_tools import breadth_first_solve, depth_first_solve
    #from time import time
    #start = time()
    #solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    #end = time()
    #print("BFS solved: \n\n{} \n\nin {} seconds".format(
        #solution, end - start))
    #start = time()
    #solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    #end = time()
    #print("DFS solved: \n\n{} \n\nin {} seconds".format(
        #solution, end - start))


    p = MNPuzzle(start_grid, target_grid)
    print(str(p))
    p2 = MNPuzzle(start_grid, target_grid)
    [print(x) for x in p2.extensions()]
