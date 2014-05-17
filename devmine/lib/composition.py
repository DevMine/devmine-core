"""This file provides abstraction over the tasks of computing the ranking"""
import numpy as np
import time
import scipy.sparse as sparse

from devmine.app.models.feature import Feature
from devmine.app.models.score import Score


__scores_matrix = None
__users_list = None


def __construct_weight_vector(db, query):
    """
    Construct a weight vector, taking default weight from features from the
    database and adapt weights according to the query, which is in the form
    {'python': 5, 'java': 3}.
    Return the weight vector as a dictionnary of feature names and their
    weight.
    """

    features = db.query(Feature).order_by(Feature.name).all()

    weight_vector = []
    for f in features:
        if f.name in query:
            weight_vector.append(query[f.name])
        else:
            weight_vector.append(f.default_weight)

    return weight_vector


def __compute_ranks(A, b, u):
    """
    Compute the ranks vector using a weighted sum.

    Parameter
    ---------
    A:  m x n matrix that contains m users and their n corresponding
        features. The values of each feature must be normalized between
        0 and 1.
    b:  Weights vector of size n
    u:  List of dictionnaries of size n that contains the ulogin and the
        did (developer ID). It must match the rows of the vector b.

    Return
    ------
    retval:  Dictionnary of the form {'username1': rank1, ...}
    """

    ranks = A.dot(b)

    retval = []
    it = np.nditer(ranks, flags=['f_index'])
    while not it.finished:
        retval.append({
            'ulogin': u[it.index]['ulogin'],
            'rank': it[0].tolist(),
            'did': u[it.index]['did']
        })
        it.iternext()

    return retval


def get_scores_matrix(db):
    """
    Returns the scores matrix and the list of associated users.
    Data is computed/accessed once and is cached in memory for later calls.
    """
    global __scores_matrix
    global __users_list

    if __scores_matrix is None:
        scores = db.query(Score).order_by(Score.fname).values(Score.ulogin,
                                                              Score.fname,
                                                              Score.score,
                                                              Score.did)

        features = [f.name for f in
                    db.query(Feature.name).order_by(Feature.name).all()]
        users_login = [f.ulogin for f in
                       db.query(Score.ulogin).group_by(Score.ulogin).all()]
        users = dict(zip(users_login, range(len(users_login))))
        users_did = dict(zip(users_login, range(len(users_login))))

        nfeatures = len(features)
        nusers = len(users)
        __scores_matrix = np.zeros((nusers, nfeatures), dtype=np.float32)

        for (ulogin, fname, score, did) in scores:
            users_did[ulogin] = did
            __scores_matrix[users[ulogin], features.index(fname)] = score

        # Normalize
        maxs = __scores_matrix.max(axis=0)

        # Ensure that we don't divide by 0
        at_least_1 = lambda x: x if x != 0 else 1
        vfunc = np.vectorize(at_least_1)

        __scores_matrix = __scores_matrix / vfunc(maxs)
        __scores_matrix = sparse.csc_matrix(__scores_matrix)

        __users_list = [{'ulogin': k, 'did': v} for (k,v) in users_did.items()]

    return __scores_matrix, __users_list


def rank(db, query):
    """
    Compute the ranking for the developers.
    The weight vector is determined from the user query.
    """
    start_time = time.time()

    w = __construct_weight_vector(db, query)

    A, u = get_scores_matrix(db)
    b = np.matrix(w).transpose()

    ranks = __compute_ranks(A, b, u)
    end_time = time.time()
    elapsed_time = (end_time-start_time)

    return ranks, elapsed_time
