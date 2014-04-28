"""
Exceptions that shall be raised during features computation shall be defined in
this file.
"""


class DataNotSufficientError(Exception):
    """
    This exception shall be raised in case the data provided to a feature is
    not sufficient.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
