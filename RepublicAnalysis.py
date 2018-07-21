from AbstractGutenberg import AbstractGutenberg


class RepublicAnalysis(AbstractGutenberg):

    def __init__(self, textFile):
        self.textFile = textFile
        self.content = self._loadFileToMemory()

    def _loadFileToMemory(self):
        return self.textFile.read()

    def getTotalNumberOfWords(self) -> int:
        return len(self.content.split(" "))


if __name__ == "__main__":
    novel = open('resources/1497.txt', 'r')

    analysis = RepublicAnalysis(novel)

    print("Analyzing The Republic by Plato")
    print(f"Total number of words is {analysis.getTotalNumberOfWords()}")

    novel.close()
