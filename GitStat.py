#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import time
import sys
import platform
import os

import json

from Ui import Ui
from Utils import getPipOutput
from GitTool import GitTool
from Project import Project

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTreeWidgetItemIterator
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox

from MsgDialog import *

class RootWindow(QMainWindow, Ui):
    def __init__(self, parent=None):
        super(RootWindow, self).__init__(parent)

        if "Windows" == platform.system():
            ErrorDialog("Not support Windows now", "")
            exit(-1)

        self.projectMap = {}
        self.gitTool = GitTool()
        self.setupUi(self)
        self.currentShowProject = 0

        self.configFilePath = os.getcwd() + "/GitStat.conf"

        self.loadconfig(self.configFilePath)

    def loadconfig(self, path):
        fd = 0
        if os.path.exists(path):
            if (0 == os.path.getsize(path)):
                return
            fd = open(path, 'r+')
            config = json.loads(fd.read())
            for obj in config:
                newProject = self.addProject(obj["project"],obj["dir"])
                for authorName in obj["authors"]:
                    newProject.saveAuthor(authorName)
        else:
            fd = open(path, 'w')
        fd.close()

    def isHadSameProject(self, name='', dir=''):
        for key, project in self.projectMap.items():
            if name == key and dir == project.getDir():
                return True
        return False

    def isHadSameTreeTtem(self, tree, col, itemname):
        itemIter = QtWidgets.QTreeWidgetItemIterator(tree, QTreeWidgetItemIterator.All)
        while itemIter.value():
            if itemname == itemIter.value().text(col):
                return True
            itemIter += 1
        return False

    def addProject(self, name, projectDir):
        newProject = Project()
        newProject.setName(name)
        newProject.setDir(projectDir)

        topItem = QtWidgets.QTreeWidgetItem(self.projectsTreeWidget);
        topItem.setText(0, newProject.getName())
        topItem.setText(1, newProject.getDir())
        newProject.setQtTopItem(topItem)

        self.projectMap[name] = newProject
        return self.projectMap[name]

    def getProjectByItemSelected(self):
        itemIter = QtWidgets.QTreeWidgetItemIterator(self.projectsTreeWidget, QTreeWidgetItemIterator.Selected)
        if not itemIter.value() or itemIter.value().parent():
            ErrorDialog("Haven't select any project", "You must select one");
            return 0
        projectName = itemIter.value().text(0)
        return self.projectMap[projectName]

    @pyqtSlot()
    def on_actionAddAuthor_hovered(self):
        self.actionAddAuthor.setToolTip("Add author into git project")

    @pyqtSlot()
    def on_actionAddAuthor_triggered(self):
        if 0 == self.projectsTreeWidget.topLevelItemCount():
            ErrorDialog("Haven't any git project", "You must add before");
            return

        project = self.getProjectByItemSelected()
        if 0 == project:
            return;

        authorName, ok = QInputDialog.getText(self, "input", "Enter git author name:")
        if not ok or len(authorName)==0:
            return

        if project.isHadSameAuthor(authorName):
            ErrorDialog("Add duplicated git author", "You had been added yet");
            return

        project.saveAuthor(authorName)

    @pyqtSlot()
    def on_actionDelAuthor_hovered(self):
        self.actionDelAuthor.setToolTip("Delete author")

    @pyqtSlot()
    def on_actionDelAuthor_triggered(self):
        itemIter = QtWidgets.QTreeWidgetItemIterator(self.projectsTreeWidget, QTreeWidgetItemIterator.Selected)
        if not itemIter.value() or not itemIter.value().parent():
            ErrorDialog("Haven't select any author", "You must select one");
            return
        author = itemIter.value().text(0)
        project = self.projectMap[itemIter.value().parent().text(0)]
        project.deleteAuthor(author)

    def clearTableWidget(self, project = 0):
        if self.currentShowProject != project and 0 != project:
            return

        row = self.tableWidget.rowCount()
        while (0 <= row):
            self.tableWidget.removeRow(row)
            row -= 1

    def showProject(self, project):
        self.clearTableWidget()

        row = 0
        for author in project.getAuthors():
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(author.getName()))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(author.add))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(author.delete))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(author.total))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(author.commitCount))
            print("%s Add:%s Delete:%s Total:%s CommitCount:%s"%
                (author.getName(),author.add,author.delete,author.total,author.commitCount))
            row += 1

        self.currentShowProject = project

    @pyqtSlot()
    def on_actionRun_triggered(self):
        project = self.getProjectByItemSelected()
        if 0 == project:
            return

        project.collect(self.gitTool)
        self.showProject(project)

    @pyqtSlot()
    def on_actionRun_hovered(self):
        self.actionRun.setToolTip("Run")

    #Add new project
    @pyqtSlot()
    def on_actionAdd_triggered(self):
        projectDir = QFileDialog.getExistingDirectory(self.centralWidget, "Select project directory", "/")
        name = projectDir[projectDir.rfind('/') + 1:]

        gitDir = projectDir + "/.git"
        if True != os.path.isdir(gitDir):
            ErrorDialog(gitDir, "isn't exsit directory");
            return

        if self.isHadSameProject(name, projectDir):
            ErrorDialog("Add a duplicated project", "You had been added yet");
            return

        newProject = self.addProject(name, projectDir);
        # self.projectsTreeWidget.addTopLevelItem(newProject.getQtTopItem())

    #Remove project
    @pyqtSlot()
    def on_actionRemove_triggered(self):
        project = self.getProjectByItemSelected()
        self.clearTableWidget(project)
        if 0 == project:
            return
        self.projectsTreeWidget.takeTopLevelItem(self.projectsTreeWidget.indexOfTopLevelItem(project.getQtTopItem()))
        del self.projectMap[project.getName()]

    def closeEvent(self, event):
        choice = QMessageBox.question(self, 'Quit', 'You sure to quit?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.Yes:
            self.on_actionSave_triggered()
            event.accept()
            # self.close()
        else:
            event.ignore()

    @pyqtSlot()
    def on_actionSave_triggered(self):
        data = []
        for name, project in self.projectMap.items():
            jsonObj = {}
            jsonObj["project"] = name
            jsonObj["dir"] = project.getDir()
            arrary = []
            for author in project.authors:
                arrary.append(author.getName())
            jsonObj["authors"] = arrary
            data.append(jsonObj)

        fd = open(self.configFilePath, 'w+')
        fd.write(json.dumps(data))
        fd.close()

    @pyqtSlot()
    def on_actionAbout_triggered(self):
        MsgDialog("About", "copyright © 2017-2099 QiuWang")

    @pyqtSlot()
    def on_actionGitVersion_triggered(self):
        MsgDialog("Git Version", self.gitTool.getGitVersion())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RootWindow()
    win.show()
    sys.exit(app.exec_())
