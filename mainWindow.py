# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Thu Jun 18 13:22:07 2015
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
        MainWindow.resize(1036, 648)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lblPath = QtGui.QLabel(self.centralwidget)
        self.lblPath.setGeometry(QtCore.QRect(0, 540, 751, 21))
        self.lblPath.setFrameShape(QtGui.QFrame.Panel)
        self.lblPath.setFrameShadow(QtGui.QFrame.Raised)
        self.lblPath.setText(_fromUtf8(""))
        self.lblPath.setObjectName(_fromUtf8("lblPath"))
        self.btnConvert = QtGui.QPushButton(self.centralwidget)
        self.btnConvert.setGeometry(QtCore.QRect(580, 10, 85, 27))
        self.btnConvert.setObjectName(_fromUtf8("btnConvert"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 681, 161))
        self.groupBox.setStyleSheet(_fromUtf8("background-color: rgb(122, 155, 216)"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 40, 581, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KacstOne"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.splitter = QtGui.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(270, 100, 301, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.lblMoto = QtGui.QLabel(self.splitter)
        self.lblMoto.setStyleSheet(_fromUtf8("background-color: white"))
        self.lblMoto.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblMoto.setFrameShadow(QtGui.QFrame.Raised)
        self.lblMoto.setObjectName(_fromUtf8("lblMoto"))
        self.lnCountMoto = QtGui.QLineEdit(self.splitter)
        self.lnCountMoto.setStyleSheet(_fromUtf8("background-color: rgb(250, 250, 250)"))
        self.lnCountMoto.setObjectName(_fromUtf8("lnCountMoto"))
        self.lblQuad = QtGui.QLabel(self.splitter)
        self.lblQuad.setStyleSheet(_fromUtf8("background-color: white"))
        self.lblQuad.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblQuad.setFrameShadow(QtGui.QFrame.Raised)
        self.lblQuad.setObjectName(_fromUtf8("lblQuad"))
        self.lnCountQuad = QtGui.QLineEdit(self.splitter)
        self.lnCountQuad.setStyleSheet(_fromUtf8("background-color: rgb(250, 250, 250)"))
        self.lnCountQuad.setObjectName(_fromUtf8("lnCountQuad"))
        self.lblAuto = QtGui.QLabel(self.splitter)
        self.lblAuto.setStyleSheet(_fromUtf8("background-color: white"))
        self.lblAuto.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblAuto.setFrameShadow(QtGui.QFrame.Raised)
        self.lblAuto.setObjectName(_fromUtf8("lblAuto"))
        self.lnCountAuto = QtGui.QLineEdit(self.splitter)
        self.lnCountAuto.setStyleSheet(_fromUtf8("background-color: rgb(250, 250, 250)"))
        self.lnCountAuto.setObjectName(_fromUtf8("lnCountAuto"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(-20, 240, 871, 271))
        self.tableWidget.setMinimumSize(QtCore.QSize(871, 271))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 271))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1036, 27))
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
        self.label.setText(_translate("MainWindow", "DESAFIO RUTA 40 - 2015                     ETAPA    1", None))
        self.lblMoto.setText(_translate("MainWindow", "Motos", None))
        self.lblQuad.setText(_translate("MainWindow", "Quad", None))
        self.lblAuto.setText(_translate("MainWindow", "Autos", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Competidor N°", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "N° Orden", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Categoría", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "WPT", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "DZ", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Disc", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Cod", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Version", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "GPS N°", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Observaciones", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuOpen.setTitle(_translate("MainWindow", "Open", None))
        self.menuParametres.setTitle(_translate("MainWindow", "Parametres", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionFile.setText(_translate("MainWindow", "File", None))
        self.actionFolder.setText(_translate("MainWindow", "Folder", None))
        self.actionDirectoryPath.setText(_translate("MainWindow", "Directory Path", None))
        self.actionCategory.setText(_translate("MainWindow", "Category", None))
        self.actionEditZone.setText(_translate("MainWindow", "Edit Zone", None))

