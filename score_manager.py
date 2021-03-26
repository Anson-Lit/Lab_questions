from models.score import Score
# from score import Score


class ScoreManager:
    """
    Represents a score manager
    """
    def __init__(self):
        self._scores = {}

    @property
    def scores(self):
        scores_list = []
        for value in self._scores.values():
            scores_list.append(value)
        return scores_list

    def add_score(self, values):
        self._scores[values.name] = values

    def remove_score(self, score_name):
        if score_name in self._scores:
            del self._scores[score_name]

    def __len__(self):
        return len(self.scores)
    
    def get_scores(self):
        scores_to_return = []
        for item in self._scores.values():
            scores_to_return.append(item.__dict__)
        return scores_to_return


if __name__ == "__main__":
    sm = ScoreManager()
    good = Score("Good", 999)
    bad = Score("bad", 222)
    sm.add_score(bad)
    sm.add_score(good)
    print(sm.get_scores())

    