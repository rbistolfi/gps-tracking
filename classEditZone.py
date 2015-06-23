# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from editZone import Ui_editZone

import sqlite3
class EditZone(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self)

		self.editZone = Ui_editZone()
		self.editZone.setupUi(self)

		self.createTable()
		self.connect(self.editZone.btnDeleteZone,SIGNAL('clicked()'),self.deleteZone)
		self.connect(self.editZone.btnAdd,SIGNAL('clicked()'),self.addZone)

	def deleteZone(self):
		f = open('/home/nano/Escritorio/gps-tracking/zones.txt','w')
		self.createTable()		

	def createTable(self):
		
		conn = sqlite3.connect('dakar.sqlite')
		cursor = conn.cursor()

		query = "SELECT * FROM zone"
		cursor.execute(query)
		rows = cursor.fetchall()
		print rows
		self.editZone.tblZone.setRowCount(len(rows))
		for i,table in enumerate(rows):
			for m,data in enumerate(table):
				if m != 0:
					self.editZone.tblZone.setItem(i,m - 1,QTableWidgetItem(str(data)))
					self.editZone.tblZone.resizeColumnsToContents()
			
		
			pass
	def addZone(self):
		valueZone = self.editZone.lnZone.text()
		f = open('/home/nano/Escritorio/gps-tracking/zones.txt','a+')
		if f.readline() != "":
			f.write('\n')
		f.write(valueZone)
		f.close()
		self.editZone.lnZone.setText("")
		self.createTable()
		

