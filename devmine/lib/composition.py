"""This file provides abstraction over the tasks of computing the ranking"""
import numpy as np

from devmine.app.models.feature import Feature


def construct_weight_vector(db, query):
    """
    Construct a weight vector, taking default weight from features from the
    database and adapt weights according to the query, which is in the form
    {'python': 5, 'java': 3}.
    Return the weight vector as a dictionnary of feature names and their weight.
    """

    features = db.query(Feature).order_by(Feature.name).all()
    weight_vector = {f.name: f.default_weight for f in features}

    for k in query:
        weight_vector[k] = query[k]

    return weight_vector


def compute_scores(A, b, u):
    """
    Compute the scores vector using a weighted sum.

    Parameter
    ---------
    A:  m x n matrix that contains m users and their n corresponding
        features. The values of each feature must be normalized between
        0 and 1.
    b:  Weights vector of size n
    u:  Vector of size n that contains the user names. They must match
        the rows of the vector b.

    Return
    ------
    retval:  Dictionnary of the form {'username1': score1, ...}
    """

    scores = np.dot(A, b)

    retval = {}
    it = np.nditer(scores, flags=['f_index'])
    while not it.finished:
        retval[u[it.index]] = it[0].tolist()
        it.iternext()

    return retval


def rank(db):
    """
    Compute the ranking for the developers.
    The weight vector is determined from the user query.
    """
    pass
