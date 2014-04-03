"""This file runs the prototype"""

import data
import ranking
import composition_functions


if __name__ == "__main__":
    import sys
    from pprint import pprint

    seed = None
    if len(sys.argv) > 1:
        seed = sys.argv[1]

    data_source = data.RandomData(seed)
    pprint(data_source.scores)

    ranking = ranking.Ranking(data_source, composition_functions.dummy)
    pprint(ranking.rank_all({}))

    ranking.composition_function = composition_functions.sum_scores
    pprint(ranking.rank_all({"Cookies": 10}))

    ranking.composition_function = composition_functions.weighted_sum
    pprint(ranking.rank_all({"Cookies": 10}))
