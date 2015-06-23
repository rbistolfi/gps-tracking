# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editZone.ui'
#
# Created: Mon Jun 22 11:45:25 2015
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
        editZone.resize(660, 555)
        self.buttonBox = QtGui.QDialogButtonBox(editZone)
        self.buttonBox.setGeometry(QtCore.QRect(210, 30, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tblZone = QtGui.QTableWidget(editZone)
        self.tblZone.setGeometry(QtCore.QRect(10, 30, 141, 241))
        self.tblZone.setObjectName(_fromUtf8("tblZone"))
        self.tblZone.setColumnCount(2)
        self.tblZone.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblZone.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblZone.setHorizontalHeaderItem(1, item)
        self.btnDeleteZone = QtGui.QPushButton(editZone)
        self.btnDeleteZone.setGeometry(QtCore.QRect(30, 310, 111, 27))
        self.btnDeleteZone.setObjectName(_fromUtf8("btnDeleteZone"))
        self.groupBox = QtGui.QGroupBox(editZone)
        self.groupBox.setGeometry(QtCore.QRect(180, 140, 121, 191))
        self.groupBox.setStyleSheet(_fromUtf8("border: 2px solid gray; \n"
"     border-radius: 3px;"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 30, 81, 135))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.lnNumZone = QtGui.QLineEdit(self.widget)
        self.lnNumZone.setObjectName(_fromUtf8("lnNumZone"))
        self.verticalLayout_2.addWidget(self.lnNumZone)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.lnZone = QtGui.QLineEdit(self.widget)
        self.lnZone.setObjectName(_fromUtf8("lnZone"))
        self.verticalLayout_2.addWidget(self.lnZone)
        self.btnAdd = QtGui.QPushButton(self.widget)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.verticalLayout_2.addWidget(self.btnAdd)
        self.groupbox = QtGui.QGroupBox(editZone)
        self.groupbox.setGeometry(QtCore.QRect(190, 190, 91, 141))
        self.groupbox.setObjectName(_fromUtf8("groupbox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupbox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.retranslateUi(editZone)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), editZone.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), editZone.reject)
        QtCore.QMetaObject.connectSlotsByName(editZone)

    def retranslateUi(self, editZone):
        editZone.setWindowTitle(_translate("editZone", "Zones", None))
        item = self.tblZone.horizontalHeaderItem(0)
        item.setText(_translate("editZone", "Num Zone", None))
        item = self.tblZone.horizontalHeaderItem(1)
        item.setText(_translate("editZone", "Zone", None))
        self.btnDeleteZone.setText(_translate("editZone", "Delete All Zones", None))
        self.groupBox.setTitle(_translate("editZone", "Add New Zones", None))
        self.label_2.setText(_translate("editZone", "Num Zone", None))
        self.label.setText(_translate("editZone", "Zone", None))
        self.btnAdd.setText(_translate("editZone", "Add", None))

