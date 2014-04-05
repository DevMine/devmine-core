#! /usr/bin/env python3.4
# coding utf-8
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



    how_to = ('\nTo write your query, you can mention the feature(s) you are '
              'interested\nin and give them some weight, or importance.\n'
              'It will return the most skilled users combining those skills, '
              'and their scores,\naccording to DevMine\'s crazy algorithm.\n\n'
              'For example, the query: Python 5 Superpower 10\n'
              'will give you:\n\n')
    example = """
        [('Kevin', 11.240153556173475),
         ('Clément', 8.545413290545826),
         ('Laurent', 7.661851902424877),
         ('Frederik', 7.547396298747576),
         ('Robin', 7.060494410357596),
         ('Daniel', 5.780794009967852),
         ('Xuan', 4.955532838858104)]\n"""
    print(how_to, example)

    print('\nHere are the features you can query over:\n')
    for features in data_source.features:
        print(features)
    
    print('\nEnter "quit" to stop your search of amazing developers.\n')

    query = ''
    query = input('Enter your query: \n\n')
    while query != 'quit':
        
        ranking = ranking.Ranking(data_source, composition_functions.dummy)
        ranking.composition_function = composition_functions.weighted_sum

        query = query.split()
        dico = dict()
        for i in range(len(query)):
            if i % 2 == 0:
                dico[query[i]] = int(query[i+1])

        
        pprint(ranking.rank_all(dico))

        query = input('\n\nEnter your query: ')
