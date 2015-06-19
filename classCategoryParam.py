# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mainWindow import Ui_MainWindow
from categoryParam import Ui_CatParam
from editZone import Ui_editZone

from classEditZone import EditZone

import sys
from database import DataBase
import glob
import csv
import sqlite3


class CategoryParam(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self)

		self.categoryParam = Ui_CatParam()
		self.categoryParam.setupUi(self)

		self.showParam()

		self.connect(self.categoryParam.btnSet,SIGNAL('clicked()'),self.setParam)
		self.connect(self.categoryParam.btnDefault,SIGNAL('clicked()'),self.setDefault)
	def setDefault(self):
		conn = sqlite3.connect('dakar.sqlite')
		cursor = conn.cursor()

		query = "UPDATE category set minRange ='0' ,maxRange ='50' where id = 1"
		cursor.execute(query)
		query = "UPDATE category set minRange ='51' ,maxRange ='99' where id = 2"
		cursor.execute(query)
		query = "UPDATE category set minRange ='100' ,maxRange ='200' where id = 3"
		cursor.execute(query)
		conn.commit()

		self.showParam()

	def setParam(self):
		conn = sqlite3.connect('dakar.sqlite')
		cursor = conn.cursor()

		minMoto = self.categoryParam.lnMinMoto.text()
		maxMoto = self.categoryParam.lnMaxMoto.text()
		minQuad = self.categoryParam.lnMinQuad.text()
		maxQuad = self.categoryParam.lnMaxQuad.text()
		minCar = self.categoryParam.lnMinCar.text()
		maxCar = self.categoryParam.lnMaxCar.text()

		query = "UPDATE category set minRange ='%i' ,maxRange ='%i' where id = 1"%(int(minMoto),int(maxMoto))
		cursor.execute(query)
		query = "UPDATE category set minRange ='%i' ,maxRange ='%i' where id = 2"%(int(minQuad),int(maxQuad))
		cursor.execute(query)
		query = "UPDATE category set minRange ='%i' ,maxRange ='%i' where id = 3"%(int(minCar),int(maxCar))
		cursor.execute(query)
		conn.commit()

		self.showParam()
	def showParam(self):
		self.db = DataBase()
		self.db.open('dakar.sqlite')
		rows = self.db.get_category()

		self.categoryParam.lnMinMoto.setText(str(rows[0][2]))
		self.categoryParam.lnMaxMoto.setText(str(rows[0][3]))
		self.categoryParam.lnMinQuad.setText(str(rows[1][2]))
		self.categoryParam.lnMaxQuad.setText(str(rows[1][3]))
		self.categoryParam.lnMinCar.setText(str(rows[2][2]))
		self.categoryParam.lnMaxCar.setText(str(rows[2][3]))


