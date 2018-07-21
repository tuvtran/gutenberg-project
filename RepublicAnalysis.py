import nltk
from AbstractGutenberg import AbstractGutenberg
from typing import Tuple


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
        return sorted(
            self.wordFrequencies.items(),
            reverse=True, key=lambda pair: pair[1])[:20]


if __name__ == "__main__":
    novel = open('resources/1497.txt', 'r')

    analysis = RepublicAnalysis(novel)

    print("Analyzing The Republic by Plato")
    print(f"Total number of words is {analysis.getTotalNumberOfWords()}")
    print(f"Total number of unique words is {analysis.getTotalUniqueWords()}")
    print(analysis.get20MostFrequentWords())

    novel.close()
