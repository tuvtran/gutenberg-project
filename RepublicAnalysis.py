from AbstractGutenberg import AbstractGutenberg


class RepublicAnalysis(AbstractGutenberg):

    def __init__(self, textFile):
        self.textFile = textFile
        self.content = self._loadFileToMemory()
        self.wordFrequencies = {}

    def _loadFileToMemory(self):
        return self.textFile.read()

    def getTotalNumberOfWords(self) -> int:
        return len(self.content.split(" "))

    def getTotalUniqueWords(self) -> int:
        return len(set(self.content.split(" ")))


if __name__ == "__main__":
    novel = open('resources/1497.txt', 'r')

    analysis = RepublicAnalysis(novel)

    print("Analyzing The Republic by Plato")
    print(f"Total number of words is {analysis.getTotalNumberOfWords()}")
    print(f"Total number of unique words is {analysis.getTotalUniqueWords()}")

    novel.close()
