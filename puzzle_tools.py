"""
Some functions for working with puzzles
"""
from puzzle import Puzzle
from collections import deque
from word_ladder_puzzle import * # Should we be importing indiviual puzzle classes?
from sudoku_puzzle import *
# set higher recursion limit
# which is needed in PuzzleNode.__str__
# you may uncomment the next lines on a unix system such as CDF
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
import sys
sys.setrecursionlimit(10**6)


# TODO
# implement depth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
def depth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode | None
    """
    children = puzzle.extensions()
    p = PuzzleNode(puzzle, children, None)  # Create the first puzzle node
    initial = dfs_helper(p)  # Pass the root puzzle node to the helper function
    if initial:
        p1 = PuzzleNode(initial[-1].puzzle, [initial[-2]], p)
        for i in range(2, len(initial)):
            p2 = PuzzleNode(initial[-1 * (i)], [initial[ -1 * (i + 1)]],
                            initial[-1 * (i - 1)])
                # Iterate over the list and link the puzzle nodes together
                # Return the root puzzle node linked through to the solution
        return p
    return None # Return None if no solution is possible

def dfs_helper(puzzle_node):
    """
    A helper function to do the recursion for depth first solve.
    @type puzzle: Puzzle
    @rtype: list[PuzzleNode]
    """
    seen_set = set()

    if puzzle_node.puzzle.is_solved():
        return [puzzle_node]
    child_list = []
    temp_list = puzzle_node.puzzle.extensions()
    # Create a list of puzzle extensions based on the current configuration
    for node in temp_list:
        if str(node) not in seen_set:
            child_list.extend([PuzzleNode(node, node.extensions(), puzzle_node)])
            seen_set.add(str(node))
        # Convert the puzzle extensions into puzzle nodes and add them to a list
    for item in child_list:
        if dfs_helper(item):
            return dfs_helper(item) + [item]
    return False




# TODO
# implement breadth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
# Hint: you may find a queue useful, that's why
# we imported deque
def breadth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child PuzzleNode containing an extension
    of the puzzle in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """


# Class PuzzleNode helps build trees of PuzzleNodes that have
# an arbitrary number of children, and a parent.
class PuzzleNode:
    """
    A Puzzle configuration that refers to other configurations that it
    can be extended to.
    """

    def __init__(self, puzzle=None, children=None, parent=None):
        """
        Create a new puzzle node self with configuration puzzle.

        @type self: PuzzleNode
        @type puzzle: Puzzle | None
        @type children: list[PuzzleNode]
        @type parent: PuzzleNode | None
        @rtype: None
        """
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]

    def __eq__(self, other):
        """
        Return whether Puzzle self is equivalent to other

        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self):
        """
        Return a human-readable string representing PuzzleNode self.

        # doctest not feasible.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))


if __name__ == '__main__':
    #import doctest
    #doctest.testmod()    
    file = open('words.txt', 'r', encoding = 'utf-8')
    word_set = set(file.read().split())
    w = WordLadderPuzzle('cove', 'cost', word_set)
    x = depth_first_solve(w)
    print(x)
    grid = ["*", "B", "C", "*"]
    grid += ["C", "*", "A", "B"]
    grid += ["B", "A", "D", "C"]
    grid += ["D", "C", "B", "*"]
    s = SudokuPuzzle(4, grid, {"A", "B", "C", "D"})
    x = depth_first_solve(s)
    for i in x:
        print(i)

    
