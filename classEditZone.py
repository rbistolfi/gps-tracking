# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mainWindow import Ui_MainWindow
from categoryParam import Ui_CatParam
from editZone import Ui_editZone

import sys
from database import DataBase
import glob
import csv
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
		try:
			f = open('/home/nano/Escritorio/gps-tracking/zones.txt','r')
			zones = f.read().split("\n")
			self.editZone.tableWidget.setColumnCount(1)
			self.editZone.tableWidget.setRowCount(len(zones))
			for i,zone in enumerate(zones):
				newitem = QTableWidgetItem(zone)
				self.editZone.tableWidget.setItem(0,i,newitem)
				
		except:
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
		

