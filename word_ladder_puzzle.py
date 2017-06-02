from puzzle import Puzzle


class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word, to_word, ws):
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

        # TODO
        # implement __eq__ and __str__
        # __repr__ is up to you
    def __eq__(self, other):
        """
        Return whether WordLadderPuzzle self is equivalent to other.
        
        @type self: WordLadderPuzzle
        @type other: WordLadderPuzzle
        @rtype: Bool
        
        >>> w1 = WordLadderPuzzle("soul", "cost", {'case', 'cave' 'same'})
        >>> w2 = WordLadderPuzzle("soul", "cost", {'case', 'cave' 'same'})
        >>> repr(w1) == repr(w2)
        True 
        """
        return type(self), self._from_word, self._to_word, self._word_set == \
               type(other), other._from_word, other._to_word, other._word_set
    
    def __str__(self):
        """
        Return a string representtion of WordLadderPuzzle self.
        
        @type self: WordLadderPuzzle
        @rtype: str
        
        >>> w = WordLadderPuzzle("hot", "hat", {'hit', 'hat', 'hot'})
        >>> str(w)
        'From word: hot, To word: hat'
        """
        return 'From word: {}, To word: {}'.format(self._from_word, 
                                                   self._to_word)
    
    def __repr__(self):
        """
        Representation of WordLadderPuzzle self.
        
        @type self: WordLadderPuzzle
        @rtype: str
        
        Examples are the same as for str method.
        """
        return str(self)

    # TODO
    # override extensions
    # legal extensions are WordLadderPuzzles that have a from_word that can
    # be reached from this one by changing a single letter to one of those
    # in self._chars
    def extensions(self):
        """
        Return a list of extensions of WordLadderPuzzle self.
        
        @type self: WordLadderPuzzle
        @rtype: list[Puzzle]
        """
        
        word = list(self._from_word)
        original = word[:]
        index = 0
        possible_words= []
        for i in range(len(self._from_word)):            
            for char in self._chars:
                word[i] = char
                if ''.join(word) in self._word_set:
                    possible_words.append(''.join(word))
                word = original[:]
        
        puzzle_list = []
        for word in possible_words:
            if word != self._from_word:
                puzzle_list.append(WordLadderPuzzle(word, self._to_word, 
                                                    self._word_set))
        return puzzle_list      
        

    # TODO
    # override is_solved
    # this WordLadderPuzzle is solved when _from_word is the same as
    # _to_word
    def is_solved(self):
        """
        Return True if this WordLadderPuzzle is solved i.e when _from_word =
        _to_word.
        
        @type self: WordLadderPuzzle
        @rtype: Bool
        
        >>> w = WordLadderPuzzle("hot", "hat", {'hit', 'hat', 'hot'})
        >>> w.is_solved()
        False
        """
        return self._from_word == self._to_word
    
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words.txt", "r", encoding = 'utf-8') as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("same", "cost", word_set)
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
