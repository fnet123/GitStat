# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\myproject\gitstat\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem

class Ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(780, 500)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 261, 531))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.projectsTreeWidget = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        self.projectsTreeWidget.setObjectName("projectsTreeWidget")
        self.projectsTreeWidget.headerItem().setText(0, "Project")
        self.projectsTreeWidget.headerItem().setText(1, "Path")
        self.horizontalLayout.addWidget(self.projectsTreeWidget)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 0, 651, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        tableHeader = ["Author", "Add", "Delete", "Total", "Commits"]
        self.tableWidget.setColumnCount(len(tableHeader))
        self.tableWidget.setHorizontalHeaderLabels(tableHeader)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectColumns)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralWidget)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 911, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuProject = QtWidgets.QMenu(self.menuBar)
        self.menuProject.setObjectName("menuProject")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.actionAddAuthor = QtWidgets.QAction(self.toolBar)
        self.actionAddAuthor.setObjectName("actionAddAuthor")
        self.toolBar.addAction(self.actionAddAuthor)

        self.actionDelAuthor = QtWidgets.QAction(self.toolBar)
        self.actionDelAuthor.setObjectName("actionDelAuthor")
        self.toolBar.addAction(self.actionDelAuthor)

        self.actionRun = QtWidgets.QAction(self.toolBar)
        self.actionRun.setObjectName("actionRun")
        self.toolBar.addAction(self.actionRun)

        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionRemove = QtWidgets.QAction(MainWindow)
        self.actionRemove.setObjectName("actionRemove")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGitVersion = QtWidgets.QAction(MainWindow)
        self.actionGitVersion.setObjectName("actionGitVersion")
        self.menuProject.addAction(self.actionAdd)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionRemove)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionSave)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionGitVersion)
        self.menuBar.addAction(self.menuProject.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GitStat"))
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionRemove.setText(_translate("MainWindow", "Remove"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionGitVersion.setText(_translate("MainWindow", "Git Version"))

        self.actionAddAuthor.setText("+")
        self.actionDelAuthor.setText("-")
        self.actionRun.setText(">")