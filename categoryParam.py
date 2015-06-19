# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'categoryParam.ui'
#
# Created: Fri Jun 19 16:38:07 2015
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
        self.widget = QtGui.QWidget(CatParam)
        self.widget.setGeometry(QtCore.QRect(90, 20, 81, 176))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lnMinMoto = QtGui.QLineEdit(self.widget)
        self.lnMinMoto.setObjectName(_fromUtf8("lnMinMoto"))
        self.horizontalLayout.addWidget(self.lnMinMoto)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lnMaxMoto = QtGui.QLineEdit(self.widget)
        self.lnMaxMoto.setObjectName(_fromUtf8("lnMaxMoto"))
        self.horizontalLayout.addWidget(self.lnMaxMoto)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lnMinQuad = QtGui.QLineEdit(self.widget)
        self.lnMinQuad.setObjectName(_fromUtf8("lnMinQuad"))
        self.horizontalLayout_4.addWidget(self.lnMinQuad)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.lnMaxQuad = QtGui.QLineEdit(self.widget)
        self.lnMaxQuad.setObjectName(_fromUtf8("lnMaxQuad"))
        self.horizontalLayout_4.addWidget(self.lnMaxQuad)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lnMinCar = QtGui.QLineEdit(self.widget)
        self.lnMinCar.setObjectName(_fromUtf8("lnMinCar"))
        self.horizontalLayout_3.addWidget(self.lnMinCar)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lnMaxCar = QtGui.QLineEdit(self.widget)
        self.lnMaxCar.setObjectName(_fromUtf8("lnMaxCar"))
        self.horizontalLayout_3.addWidget(self.lnMaxCar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.retranslateUi(CatParam)
        QtCore.QMetaObject.connectSlotsByName(CatParam)

    def retranslateUi(self, CatParam):
        CatParam.setWindowTitle(_translate("CatParam", "Set Parameters", None))
        self.btnSet.setText(_translate("CatParam", "Set", None))
        self.btnDefault.setText(_translate("CatParam", "Default", None))
        self.label_2.setText(_translate("CatParam", "Motorcicles", None))
        self.lnMinMoto.setText(_translate("CatParam", "0", None))
        self.label.setText(_translate("CatParam", "-", None))
        self.lnMaxMoto.setText(_translate("CatParam", "50", None))
        self.label_5.setText(_translate("CatParam", "Quad", None))
        self.lnMinQuad.setText(_translate("CatParam", "100", None))
        self.label_7.setText(_translate("CatParam", "-", None))
        self.lnMaxQuad.setText(_translate("CatParam", "200", None))
        self.label_4.setText(_translate("CatParam", "Cars", None))
        self.lnMinCar.setText(_translate("CatParam", "51", None))
        self.label_6.setText(_translate("CatParam", "-", None))
        self.lnMaxCar.setText(_translate("CatParam", "99", None))

