import nltk
import heapq
import pickle
from pathlib import Path
from AbstractGutenberg import AbstractGutenberg
from utils import getTopCommonEnglishWords
from typing import List, Tuple


class BookAnalysis(AbstractGutenberg):

    def __init__(self, textFile):
        self.textFile = textFile
        # contentLines is a list of lines in the novel
        self.contentLines = self._loadFileToMemory()
        # all tokens in a book
        self.allTokens = self._tokenize(self.contentLines)
        self.wordFrequencies = self._setWordFrequencies(self.allTokens)
        self.chapters = self._splitByChapter()
        self.chapterTokens = self._tokenizeChapters()
        self.chapterDictionaries = self._createChapterDictionary()

    def _loadFileToMemory(self) -> List[str]:
        totalLines = []
        for line in self.textFile.readlines():
            totalLines.append(line)
        return totalLines

    def _tokenize(self, bookLines) -> List[str]:
        """
        @param bookLines list of lines in a book
        """
        # convert list of lines to list of list of words
        wordLines = map(
            lambda line: nltk.word_tokenize(line.rstrip('\n')),
            bookLines)
        return [word.lower() for line in wordLines
                for word in line if word.isalpha()]

    def _setWordFrequencies(self, tokens: List[str]):
        """
        Helper method that return a dictionary of word frequencies based on a
        list of tokens

        @param tokens a list of tokens
        """
        frequencies = {}
        for word in tokens:
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1
        return frequencies

    def getTotalNumberOfWords(self) -> int:
        return len(self.allTokens)

    def getTotalUniqueWords(self) -> int:
        return len(set(self.allTokens))

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

    def _splitByChapter(self):
        # initialize a list of index that marks the start of a chapter
        chapters = []
        for i, line in enumerate(self.contentLines):
            # TODO: using a faster string matching algorithm here
            if line.find("Chapter") != -1:
                chapters.append(i)

        return chapters

    def _tokenizeChapters(self):
        """
        Helper method to tokenize a chapter and put it in a list of list of
        words. Since this is really expensive, we will save the list of tokens
        to a Pickle file
        """
        # check if file exists
        file_name = './resources/chapter_tokens_pride.pkl'
        chapterTokensFile = Path(file_name)
        if chapterTokensFile.is_file():
            return pickle.load(open(file_name, 'rb'))

        chapterTokens = []

        # append the length of the book lines into the array
        # so we don't run into array index out of length error
        self.chapters.append(len(self.contentLines))
        for i in range(len(self.chapters) - 1):
            print(f"DEBUG: tokenize chapter {i + 1}")
            chapterTokens.append(self._tokenize(
                self.contentLines[self.chapters[i]:self.chapters[i + 1]]
            ))

        pickle.dump(chapterTokens, open(file_name, 'wb'))

        return chapterTokens

    def _createChapterDictionary(self):
        chapterDictionaries = []
        for chapter in self.chapterTokens:
            chapterDictionaries.append(self._setWordFrequencies(chapter))
        return chapterDictionaries

    def getFrequencyOfWord(self, word: str) -> List[int]:
        result = []
        for chapterDict in self.chapterDictionaries:
            if word not in chapterDict:
                result.append(0)
            else:
                result.append(chapterDict[word])
        return result


if __name__ == "__main__":
    novel = open('resources/1342.txt', 'r')

    analysis = BookAnalysis(novel)

    print("Analyzing Pride and Prejudice by Jane Austen\n")
    print(f"Total number of words is {analysis.getTotalNumberOfWords()}\n")
    print(f"Total number of unique words is {analysis.getTotalUniqueWords()}\n")
    print(f"20 most frequent words are {analysis.get20MostFrequentWords()}\n")
    print("20 most frequent interesting words are " +
          f"{analysis.get20MostInterestingFrequentWords()}\n")
    print(f"20 least frequest words are {analysis.get20LeastFrequentWords()}\n")

    print(analysis.getFrequencyOfWord('elizabeth'))

    novel.close()
