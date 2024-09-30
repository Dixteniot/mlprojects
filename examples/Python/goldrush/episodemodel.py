class AbstractEpisodeModel():
    def __init__(self, episode):
        self.name = episode.name
        self.number = episode.number
        self.fileName = episode.fileName
        self.wordList = []
        self.characterList = []
        self.knowledgeBase = []
        self.wordStats = []
        self.wordListStats = []
        self.characterListStats = []

    def readEpisode(self, episode):
        pass

    def wordStatsAnalysis(self, listx):
        pass

    def wordStatistics(self, listx):
        pass

    def average(self, sumx, n):
        pass

    def standardDeviation(self, listx, mean):
        pass

    def decode(self, data):
        pass

    def encode(self, data):
        pass

    def cleanData(self, data):
        pass

    def sortList(self, listx):
        pass

    def printStats(self, listx):
        pass
