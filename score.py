class Score:
    """ Simple class to represent a score in a game """

    def __init__(self, name, score):
        """ Initializes private attributes

        Args:
            name (str): name of the player (cannot be empty)
            score (int): score of the player (cannot be negative)
        
        Raises:
            ValueError: name is empty or not string, score is not integer or negative
        """

        if type(name) is not str or not name:
            raise ValueError("Invalid name.")
        if type(score) is not int or score < 0:
            raise ValueError("Invalid score.")

        self._name = name
        self._score = score
        
    @property
    def name(self):
        return self._name
        
    @property
    def score(self):
        return self._score

    @property
    def __dict__(self):
        """Returns a dictionary representation of this object"""
        return {'name': self._name, 'score': self._score}

    def __str__(self):
        return f'Score: {self._name} ({self._score})'

    def __gt__(self, other):
        if type(other) is not type(self):
            raise TypeError("Unspported type")
        return self._score > other._score


if __name__ == "__main__":
    good = Score("Good", 999)
    print(good.__dict__)

