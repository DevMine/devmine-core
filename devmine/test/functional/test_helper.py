import sys

sys.path = ['../../..'] + sys.path

import devmine


def get_app():
    return devmine.Devmine().app
