import nltk
import heapq
from AbstractGutenberg import AbstractGutenberg
from utils import getTopCommonEnglishWords
from typing import List, Tuple


class RepublicAnalysis(AbstractGutenberg):

    def __init__(self, textFile):
        self.textFile = textFile
        # contentLines is a list of lines in the novel
        self.contentLines = self._loadFileToMemory()
        self.tokens = self._tokenize()
        self.wordFrequencies = self._setWordFrequencies()

    def _loadFileToMemory(self):
        totalLines = []
        for line in self.textFile.readlines():
            totalLines.append(line)
        return totalLines

    def _tokenize(self):
        # convert list of lines to list of list of words
        wordLines = map(
            lambda line: nltk.word_tokenize(line.rstrip('\n')),
            self.contentLines)
        return [word.lower() for line in wordLines
                for word in line if word.isalpha()]

    def _setWordFrequencies(self):
        frequencies = {}
        for word in self.tokens:
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1
        return frequencies

    def getTotalNumberOfWords(self) -> int:
        return len(self.tokens)

    def getTotalUniqueWords(self) -> int:
        return len(set(self.tokens))

    def get20MostFrequentWords(self) -> Tuple[str, int]:
        return heapq.nlargest(
            n=20, iterable=self.wordFrequencies.items(),
            key=lambda pair: pair[1]
        )

    def get20MostInterestingFrequentWords(self) -> List[Tuple[str, int]]:
        mostCommonWords = getTopCommonEnglishWords()
        filteredFrequencies = {
            k: self.wordFrequencies[k] for k in self.wordFrequencies
            if k not in mostCommonWords
        }
        return heapq.nlargest(
            n=20, iterable=filteredFrequencies.items(),
            key=lambda pair: pair[1]
        )

    def get20LeastFrequentWords(self) -> List[Tuple[str, int]]:
        return heapq.nsmallest(
            n=20, iterable=self.wordFrequencies.items(),
            key=lambda pair: pair[1]
        )


if __name__ == "__main__":
    novel = open('resources/1497.txt', 'r')

    analysis = RepublicAnalysis(novel)

    print("Analyzing The Republic by Plato\n")
    print(f"Total number of words is {analysis.getTotalNumberOfWords()}\n")
    print(f"Total number of unique words is {analysis.getTotalUniqueWords()}\n")
    print(f"20 most frequent words are {analysis.get20MostFrequentWords()}\n")
    print("20 most frequent interesting words are " +
          f"{analysis.get20MostInterestingFrequentWords()}\n")
    print(f"20 least frequest words are {analysis.get20LeastFrequentWords()}\n")

    novel.close()
