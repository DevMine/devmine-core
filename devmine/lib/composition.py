import numpy as np


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
