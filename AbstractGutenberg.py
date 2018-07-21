from abc import ABCMeta, abstractclassmethod


class AbstractGutenberg:

    __abstract__ = True
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractclassmethod
    def getTotalNumberOfWords(self) -> int:
        ...

    @abstractclassmethod
    def getTotalUniqueWords(self) -> int:
        ...

    @abstractclassmethod
    def get20MostFrequentWords(self):
        ...

    @abstractclassmethod
    def get20MostInterestingFrequentWords(self):
        ...

    @abstractclassmethod
    def get20LeastFrequentWords(self):
        ...
