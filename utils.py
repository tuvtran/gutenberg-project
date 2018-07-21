def getTopCommonEnglishWords(file='resources/most_common_1000.txt'):
    """
    This function takes a file of most common English words
    and return a set that contains those words up to k
    """
    result = set()
    with open(file, 'r') as wordFile:
        for line in wordFile.readlines():
            result.add(line.rstrip('\n'))
    return result
