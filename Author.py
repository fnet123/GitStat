class Author(object):
    def __init__(self, name):
        self.name = name
        self.commitCount = 0
        self.add    = 0
        self.delete = 0
        self.total  = 0

    def getName(self):
        return self.name

    def saveCommitInfo(self, commitInfo, commitCount = 0):
        self.commitCount = commitCount

        if (0 != len(commitInfo[0])):
            self.add    = commitInfo[0]
        if (0 != len(commitInfo[1])):
            self.delete = commitInfo[1]
        if (0 != len(commitInfo[2])):
            self.total  = commitInfo[2]

    def setQtItem(self, item):
        self.item = item

    def getQtItem(self):
        return self.item
