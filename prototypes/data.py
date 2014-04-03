"""This file provides abstraction over the source of data used in the server"""

import random


class DataSource:
    """This class abstracts the underlying system that stores the computed
    features about the developers"""
    def __init__(self):
        pass


class RandomData(DataSource):
    def __init__(self, seed=None):
        r = random.Random(seed)
        print(r.random())

        self.scores = {}
        self.features = ["Python", "Cookies", "Chocolate",
                         "Superpowers", "Doge"]
        self.developers = ["Robin", "Kevin", "Laurent", "Xuan",
                           "Frederik", "Daniel", "Clément"]

        for developer in self.developers:
            scores = {}
            for feature in self.features:
                scores[feature] = r.random()
            self.scores[developer] = scores
