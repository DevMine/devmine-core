"""This exception shall be raised in case the data provided to a feature is not
sufficient"""


class DataNotSufficientError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
