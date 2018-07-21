from abc import ABCMeta, abstractclassmethod
from typing import List, Tuple


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
    def get20MostFrequentWords(self) -> List[Tuple[str, int]]:
        ...

    @abstractclassmethod
    def get20MostInterestingFrequentWords(self) -> List[Tuple[str, int]]:
        ...

    @abstractclassmethod
    def get20LeastFrequentWords(self) -> List[Tuple[str, int]]:
        ...

    @abstractclassmethod
    def getFrequencyOfWord(self) -> List[int]:
        ...
