# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'categoryParam.ui'
#
# Created: Tue Jun 16 15:34:18 2015
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

class Ui_CatParam(object):
    def setupUi(self, CatParam):
        CatParam.setObjectName(_fromUtf8("CatParam"))
        CatParam.resize(257, 264)
        self.layoutWidget = QtGui.QWidget(CatParam)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 210, 178, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btnSet = QtGui.QPushButton(self.layoutWidget)
        self.btnSet.setObjectName(_fromUtf8("btnSet"))
        self.horizontalLayout_5.addWidget(self.btnSet)
        self.btnDefault = QtGui.QPushButton(self.layoutWidget)
        self.btnDefault.setObjectName(_fromUtf8("btnDefault"))
        self.horizontalLayout_5.addWidget(self.btnDefault)
        self.layoutWidget_2 = QtGui.QWidget(CatParam)
        self.layoutWidget_2.setGeometry(QtCore.QRect(90, 20, 81, 54))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_4 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.label = QtGui.QLabel(self.layoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget_3 = QtGui.QWidget(CatParam)
        self.layoutWidget_3.setGeometry(QtCore.QRect(90, 80, 81, 54))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_4 = QtGui.QLabel(self.layoutWidget_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEdit_6 = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_3.addWidget(self.lineEdit_6)
        self.label_6 = QtGui.QLabel(self.layoutWidget_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.layoutWidget_4 = QtGui.QWidget(CatParam)
        self.layoutWidget_4.setGeometry(QtCore.QRect(90, 140, 81, 54))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_5 = QtGui.QLabel(self.layoutWidget_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEdit_7 = QtGui.QLineEdit(self.layoutWidget_4)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.horizontalLayout_4.addWidget(self.lineEdit_7)
        self.label_7 = QtGui.QLabel(self.layoutWidget_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.lineEdit_8 = QtGui.QLineEdit(self.layoutWidget_4)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.horizontalLayout_4.addWidget(self.lineEdit_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.retranslateUi(CatParam)
        QtCore.QMetaObject.connectSlotsByName(CatParam)

    def retranslateUi(self, CatParam):
        CatParam.setWindowTitle(_translate("CatParam", "Set Parameters", None))
        self.btnSet.setText(_translate("CatParam", "Set", None))
        self.btnDefault.setText(_translate("CatParam", "Default", None))
        self.label_2.setText(_translate("CatParam", "Motorcicles", None))
        self.lineEdit_4.setText(_translate("CatParam", "0", None))
        self.label.setText(_translate("CatParam", "-", None))
        self.lineEdit.setText(_translate("CatParam", "50", None))
        self.label_4.setText(_translate("CatParam", "Cars", None))
        self.lineEdit_6.setText(_translate("CatParam", "51", None))
        self.label_6.setText(_translate("CatParam", "-", None))
        self.lineEdit_3.setText(_translate("CatParam", "99", None))
        self.label_5.setText(_translate("CatParam", "Monster", None))
        self.lineEdit_7.setText(_translate("CatParam", "100", None))
        self.label_7.setText(_translate("CatParam", "-", None))
        self.lineEdit_8.setText(_translate("CatParam", "200", None))

