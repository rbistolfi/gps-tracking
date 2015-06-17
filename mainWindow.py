# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Wed Jun 17 11:29:38 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(744, 573)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lblPath = QtGui.QLabel(self.centralwidget)
        self.lblPath.setGeometry(QtCore.QRect(10, 0, 391, 17))
        self.lblPath.setText(_fromUtf8(""))
        self.lblPath.setObjectName(_fromUtf8("lblPath"))
        self.txtFile = QtGui.QPlainTextEdit(self.centralwidget)
        self.txtFile.setGeometry(QtCore.QRect(30, 50, 411, 411))
        self.txtFile.setObjectName(_fromUtf8("txtFile"))
        self.btnConvert = QtGui.QPushButton(self.centralwidget)
        self.btnConvert.setGeometry(QtCore.QRect(550, 20, 85, 27))
        self.btnConvert.setObjectName(_fromUtf8("btnConvert"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOpen = QtGui.QMenu(self.menuFile)
        self.menuOpen.setObjectName(_fromUtf8("menuOpen"))
        self.menuParametres = QtGui.QMenu(self.menubar)
        self.menuParametres.setObjectName(_fromUtf8("menuParametres"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionFile = QtGui.QAction(MainWindow)
        self.actionFile.setObjectName(_fromUtf8("actionFile"))
        self.actionFolder = QtGui.QAction(MainWindow)
        self.actionFolder.setObjectName(_fromUtf8("actionFolder"))
        self.actionDirectoryPath = QtGui.QAction(MainWindow)
        self.actionDirectoryPath.setObjectName(_fromUtf8("actionDirectoryPath"))
        self.actionCategory = QtGui.QAction(MainWindow)
        self.actionCategory.setObjectName(_fromUtf8("actionCategory"))
        self.actionEditZone = QtGui.QAction(MainWindow)
        self.actionEditZone.setObjectName(_fromUtf8("actionEditZone"))
        self.menuOpen.addSeparator()
        self.menuOpen.addAction(self.actionFile)
        self.menuOpen.addAction(self.actionFolder)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addSeparator()
        self.menuParametres.addAction(self.actionDirectoryPath)
        self.menuParametres.addAction(self.actionCategory)
        self.menuParametres.addAction(self.actionEditZone)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuParametres.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Dakar 2015", None))
        self.btnConvert.setText(_translate("MainWindow", "Convert", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuOpen.setTitle(_translate("MainWindow", "Open", None))
        self.menuParametres.setTitle(_translate("MainWindow", "Parametres", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionFile.setText(_translate("MainWindow", "File", None))
        self.actionFolder.setText(_translate("MainWindow", "Folder", None))
        self.actionDirectoryPath.setText(_translate("MainWindow", "Directory Path", None))
        self.actionCategory.setText(_translate("MainWindow", "Category", None))
        self.actionEditZone.setText(_translate("MainWindow", "Edit Zone", None))

