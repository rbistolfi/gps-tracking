# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editZone.ui'
#
# Created: Thu Jun 18 10:27:56 2015
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

class Ui_editZone(object):
    def setupUi(self, editZone):
        editZone.setObjectName(_fromUtf8("editZone"))
        editZone.resize(315, 357)
        self.buttonBox = QtGui.QDialogButtonBox(editZone)
        self.buttonBox.setGeometry(QtCore.QRect(210, 30, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tableWidget = QtGui.QTableWidget(editZone)
        self.tableWidget.setGeometry(QtCore.QRect(60, 30, 101, 241))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.btnDeleteZone = QtGui.QPushButton(editZone)
        self.btnDeleteZone.setGeometry(QtCore.QRect(30, 310, 111, 27))
        self.btnDeleteZone.setObjectName(_fromUtf8("btnDeleteZone"))
        self.widget = QtGui.QWidget(editZone)
        self.widget.setGeometry(QtCore.QRect(200, 260, 71, 85))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lnZone = QtGui.QLineEdit(self.widget)
        self.lnZone.setObjectName(_fromUtf8("lnZone"))
        self.verticalLayout.addWidget(self.lnZone)
        self.btnAdd = QtGui.QPushButton(self.widget)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.verticalLayout.addWidget(self.btnAdd)

        self.retranslateUi(editZone)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), editZone.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), editZone.reject)
        QtCore.QMetaObject.connectSlotsByName(editZone)

    def retranslateUi(self, editZone):
        editZone.setWindowTitle(_translate("editZone", "Zones", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("editZone", "Zones", None))
        self.btnDeleteZone.setText(_translate("editZone", "Delete All Zones", None))
        self.label.setText(_translate("editZone", "Add Zones", None))
        self.btnAdd.setText(_translate("editZone", "Add", None))

