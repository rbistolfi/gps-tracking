# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Thu Jun 25 11:47:20 2015
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
        MainWindow.resize(1065, 575)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lblPath = QtGui.QLabel(self.centralwidget)
        self.lblPath.setGeometry(QtCore.QRect(0, 480, 1062, 21))
        self.lblPath.setFrameShape(QtGui.QFrame.Panel)
        self.lblPath.setFrameShadow(QtGui.QFrame.Raised)
        self.lblPath.setText(_fromUtf8(""))
        self.lblPath.setObjectName(_fromUtf8("lblPath"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 702, 152))
        self.groupBox.setStyleSheet(_fromUtf8("border-radius:2px;border:2px solid grey;\n"
"background-color:rgb(149, 180, 159)"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 40, 581, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sawasdee"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("border:0px solid grey;\n"
""))
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
        self.lnCountCar = QtGui.QLineEdit(self.splitter)
        self.lnCountCar.setStyleSheet(_fromUtf8("background-color: rgb(250, 250, 250)"))
        self.lnCountCar.setObjectName(_fromUtf8("lnCountCar"))
        self.tblGralStatus = QtGui.QTableWidget(self.centralwidget)
        self.tblGralStatus.setGeometry(QtCore.QRect(10, 190, 702, 271))
        self.tblGralStatus.setMinimumSize(QtCore.QSize(120, 271))
        self.tblGralStatus.setStyleSheet(_fromUtf8("border-radius:1px;border:1px solid grey;\n"
""))
        self.tblGralStatus.setObjectName(_fromUtf8("tblGralStatus"))
        self.tblGralStatus.setColumnCount(11)
        self.tblGralStatus.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tblGralStatus.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tblGralStatus.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tblGralStatus.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tblGralStatus.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblGralStatus.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tblGralStatus.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tblGralStatus.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tblGralStatus.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tblGralStatus.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tblGralStatus.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tblGralStatus.setHorizontalHeaderItem(10, item)
        self.tblData = QtGui.QTableWidget(self.centralwidget)
        self.tblData.setGeometry(QtCore.QRect(731, 10, 211, 152))
        self.tblData.setObjectName(_fromUtf8("tblData"))
        self.tblData.setColumnCount(1)
        self.tblData.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.tblData.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblData.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblData.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblData.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tblData.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tblData.setHorizontalHeaderItem(0, item)
        self.lblUpdate = QtGui.QLabel(self.centralwidget)
        self.lblUpdate.setGeometry(QtCore.QRect(10, 480, 371, 17))
        self.lblUpdate.setText(_fromUtf8(""))
        self.lblUpdate.setObjectName(_fromUtf8("lblUpdate"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(731, 190, 211, 271))
        self.groupBox_2.setStyleSheet(_fromUtf8("border:2px solid grey;"))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lblDisc = QtGui.QLabel(self.groupBox_2)
        self.lblDisc.setGeometry(QtCore.QRect(90, 220, 30, 17))
        self.lblDisc.setMinimumSize(QtCore.QSize(30, 10))
        self.lblDisc.setMaximumSize(QtCore.QSize(88, 16777215))
        self.lblDisc.setStyleSheet(_fromUtf8("border:0px solid grey;"))
        self.lblDisc.setObjectName(_fromUtf8("lblDisc"))
        self.lstDiscStatus = QtGui.QListWidget(self.groupBox_2)
        self.lstDiscStatus.setGeometry(QtCore.QRect(60, 240, 88, 21))
        self.lstDiscStatus.setMaximumSize(QtCore.QSize(88, 21))
        self.lstDiscStatus.setStyleSheet(_fromUtf8("border:1px solid grey;"))
        self.lstDiscStatus.setObjectName(_fromUtf8("lstDiscStatus"))
        self.lstWpt = QtGui.QListWidget(self.groupBox_2)
        self.lstWpt.setGeometry(QtCore.QRect(13, 64, 88, 151))
        self.lstWpt.setMaximumSize(QtCore.QSize(88, 200))
        self.lstWpt.setStyleSheet(_fromUtf8("border:1px solid grey;"))
        self.lstWpt.setObjectName(_fromUtf8("lstWpt"))
        self.lstDz = QtGui.QListWidget(self.groupBox_2)
        self.lstDz.setGeometry(QtCore.QRect(110, 64, 88, 151))
        self.lstDz.setMaximumSize(QtCore.QSize(88, 200))
        self.lstDz.setStyleSheet(_fromUtf8("border:1px solid grey;"))
        self.lstDz.setObjectName(_fromUtf8("lstDz"))
        self.lblWpt = QtGui.QLabel(self.groupBox_2)
        self.lblWpt.setGeometry(QtCore.QRect(43, 10, 30, 17))
        self.lblWpt.setMinimumSize(QtCore.QSize(30, 10))
        self.lblWpt.setMaximumSize(QtCore.QSize(88, 16777215))
        self.lblWpt.setStyleSheet(_fromUtf8("border:0px solid grey;"))
        self.lblWpt.setObjectName(_fromUtf8("lblWpt"))
        self.lstWptStatus = QtGui.QListWidget(self.groupBox_2)
        self.lstWptStatus.setGeometry(QtCore.QRect(13, 34, 88, 21))
        self.lstWptStatus.setMaximumSize(QtCore.QSize(88, 21))
        self.lstWptStatus.setStyleSheet(_fromUtf8("border:1px solid grey;"))
        self.lstWptStatus.setObjectName(_fromUtf8("lstWptStatus"))
        self.lblDz = QtGui.QLabel(self.groupBox_2)
        self.lblDz.setGeometry(QtCore.QRect(140, 10, 30, 21))
        self.lblDz.setMinimumSize(QtCore.QSize(30, 21))
        self.lblDz.setStyleSheet(_fromUtf8("border:0px solid grey;"))
        self.lblDz.setObjectName(_fromUtf8("lblDz"))
        self.lstDzStatus = QtGui.QListWidget(self.groupBox_2)
        self.lstDzStatus.setGeometry(QtCore.QRect(110, 34, 88, 21))
        self.lstDzStatus.setMaximumSize(QtCore.QSize(88, 21))
        self.lstDzStatus.setStyleSheet(_fromUtf8("border:1px solid grey;"))
        self.lstDzStatus.setObjectName(_fromUtf8("lstDzStatus"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1065, 27))
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
        self.label.setText(_translate("MainWindow", "DESAFIO RUTA 40 - 2015                     ETAPA    1", None))
        self.lblMoto.setText(_translate("MainWindow", "Motos", None))
        self.lblQuad.setText(_translate("MainWindow", "Quad", None))
        self.lblAuto.setText(_translate("MainWindow", "Autos", None))
        item = self.tblGralStatus.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Competidor N°", None))
        item = self.tblGralStatus.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre", None))
        item = self.tblGralStatus.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "N° Orden", None))
        item = self.tblGralStatus.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Categoría", None))
        item = self.tblGralStatus.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "WPT", None))
        item = self.tblGralStatus.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "DZ", None))
        item = self.tblGralStatus.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Disc", None))
        item = self.tblGralStatus.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Cod", None))
        item = self.tblGralStatus.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Version", None))
        item = self.tblGralStatus.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "GPS N°", None))
        item = self.tblGralStatus.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Observaciones", None))
        item = self.tblData.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Competidor N°:", None))
        item = self.tblData.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "GPS N°:", None))
        item = self.tblData.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre:", None))
        item = self.tblData.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fecha:", None))
        item = self.tblData.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Hora:", None))
        item = self.tblData.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data", None))
        self.lblDisc.setText(_translate("MainWindow", "Disc", None))
        self.lblWpt.setText(_translate("MainWindow", "WPT", None))
        self.lblDz.setText(_translate("MainWindow", "DZ", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuOpen.setTitle(_translate("MainWindow", "Open", None))
        self.menuParametres.setTitle(_translate("MainWindow", "Parametres", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionFile.setText(_translate("MainWindow", "File", None))
        self.actionFolder.setText(_translate("MainWindow", "Folder", None))
        self.actionDirectoryPath.setText(_translate("MainWindow", "Directory Path", None))
        self.actionCategory.setText(_translate("MainWindow", "Category", None))
        self.actionEditZone.setText(_translate("MainWindow", "Edit Zone", None))

