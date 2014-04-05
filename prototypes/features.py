"""This file provides abstraction over the set of features"""

from abc import ABCMeta, abstractmethod

class AbstractFeature(metaclass=ABCMeta):

    def __init__(self, data_source):
        self.data_source = data_source
	__verify_sufficient_data__(data_source)


    @abstractmethod

    def compute_score(self, id):

	"""Compute the score for this feature for the given id"""

	pass


    @abstractmethod

    def __verify_sufficient_data__(self, data_source):

	""" Make sure the data source supports everything this feature needs
	If that is not the case, this method should raise a
	DataNotSufficientError """

	pass


    @abstractmethod

    def __str__(self):
        
	pass
    

class DataNotSufficientError(Exception):

    def __init__(self, value):
  	self.value = value

    def __str__(self):
        return repr(self.value)
