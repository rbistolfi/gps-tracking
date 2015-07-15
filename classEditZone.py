# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from editZone import Ui_editZone
from database import DataBase

import sqlite3
class EditZone(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self)

		self.editZone = Ui_editZone()
		self.editZone.setupUi(self)
		self.conn = None
		self.cursor = None
		self.db = DataBase()
		self.db.open('dakar.sqlite')

		self.createTable()
		self.connect(self.editZone.btnDeleteZone,SIGNAL('clicked()'),self.deleteZone)
		self.connect(self.editZone.btnAdd,SIGNAL('clicked()'),self.addZone)

	def deleteZone(self):
<<<<<<< HEAD
		self.editZone.lnNumZone.setText("1")
=======
>>>>>>> 8cf44df154c2383fb4efb11491b89f3ca093d1bc
		self.db.deleteZone()
		self.createTable()		

	def createTable(self):
		
		rows = self.db.getZone()
		self.editZone.tblZone.setRowCount(len(rows))
		for i,table in enumerate(rows):
			for m,data in enumerate(table):
				if m != 0:
					self.editZone.tblZone.setItem(i,m - 1,QTableWidgetItem(str(data)))
					self.editZone.tblZone.resizeColumnsToContents()
					self.editZone.tblZone.resizeRowsToContents()
			
		
			pass
	def addZone(self):
		valueZone = self.editZone.lnZone.text()
		numZone = self.editZone.lnNumZone.text()
<<<<<<< HEAD
		tmpZone = int(numZone) + 1
		self.db.insertZone(numZone,valueZone)
		self.editZone.lnNumZone.setText(str(tmpZone))
=======

		self.db.insertZone(numZone,valueZone)
		
>>>>>>> 8cf44df154c2383fb4efb11491b89f3ca093d1bc
		self.editZone.lnZone.setText("")
		self.editZone.lnNumZone.setText("")
		self.createTable()
		

