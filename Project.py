from Author import Author
from GitTool import GitTool
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItemIterator

class Project():
    def __init__(self):
        self.name = ''
        self.dir = ''
        self.authors = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setDir(self, dir):
        self.dir = dir

    def getDir(self):
        return self.dir

    def setQtTopItem(self, widget):
        self.qtTopItem = widget

    def getQtTopItem(self):
        return self.qtTopItem

    def saveAuthor(self, authorName):
        author = Author(authorName)
        item = QtWidgets.QTreeWidgetItem(self.getQtTopItem())
        item.setText(0, authorName)
        # item.setCheckState(0, False)
        author.setQtItem(item)
        self.authors.append(author)

        self.getQtTopItem().addChild(item)
        self.getQtTopItem().setExpanded(True)

    def deleteAuthor(self, authorName):
        for author in self.authors:
            if author.getName() == authorName:
                self.getQtTopItem().removeChild(author.getQtItem())
                self.authors.remove(author)

    def getAuthors(self):
        return self.authors

    def isHadSameAuthor(self, authorName):
        for author in self.authors:
            if author.getName() == authorName:
                return True
        return False

    def collect(self, gitTool):
        curDir = os.getcwd()
        os.chdir(self.getDir())
        for author in self.getAuthors():
            commitInfo  = gitTool.getCommitInfo(author.getName())
            commitCount = gitTool.getCommitCount(author.getName())
            author.saveCommitInfo(commitInfo, commitCount)
        os.chdir(curDir)
