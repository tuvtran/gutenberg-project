from abc import ABCMeta, abstractclassmethod


class AbstractGutenberg:

    __abstract__ = True
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractclassmethod
    def getTotalNumberOfWords() -> int:
        ...

    @abstractclassmethod
    def getTotalUniqueWords() -> int:
        ...

    @abstractclassmethod
    def get20MostFrequentWords():
        ...

    @abstractclassmethod
    def get20MostInterestingFrequentWords():
        ...
