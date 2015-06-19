        #self.connect(self.ventana.pushButton,SIGNAL('clicked()'),self.change)
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mainWindow import Ui_MainWindow
from categoryParam import Ui_CatParam
from editZone import Ui_editZone

from classEditZone import EditZone
from classCategoryParam import CategoryParam

import sys
from database import DataBase
import glob
import csv
import sqlite3

class Principal(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.conn = None
		self.cursor = None

		self.mainWindow = Ui_MainWindow()
		self.mainWindow.setupUi(self)
		self.db = DataBase()
		self.db.open('dakar.sqlite')
		self.inputFiles()
		self.mainTable()


		self.mainWindow.actionCategory.triggered.connect(self.openCategoryWindow)
		self.mainWindow.actionDirectoryPath.triggered.connect(self.searchPath)
		self.mainWindow.actionEditZone.triggered.connect(self.openEditZone)

		self.connect(self.mainWindow.btnConvert,SIGNAL('clicked()'),self.searchFiles)
	def mainTable(self):
		rows = self.db.get_tables()
		self.mainWindow.tblGralStatus.setRowCount(len(rows))
		for i,table in enumerate(rows):
			for m,data in enumerate(table):
				if m != 0:
					self.mainWindow.tblGralStatus.setItem(i,m - 1,QTableWidgetItem(str(data)))
					if str(data) == 'OK':
						color = 'green'
					elif str(data) == 'NOK':
						color = 'red'
					else:
						color = 'white'
					self.mainWindow.tblGralStatus.item(i, m - 1).setBackground(QColor(color))
					self.mainWindow.tblGralStatus.resizeColumnsToContents()
				

	def openCategoryWindow(self):
		mainWindow = CategoryParam().exec_()

	def openEditZone(self):
		mainWindow = EditZone().exec_()

	def searchPath(self):
		dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
		self.mainWindow.lblPath.setText(dir_)
	
	def searchFiles(self):
		path = self.mainWindow.lblPath.text()
		strText = self.mainWindow.txtFile.toPlainText()
		f = open('/home/nano/Escritorio/a.csv')
		lns = csv.reader(f)
		for line in lns:
			self.mainWindow.txtFile.setPlainText(self.mainWindow.txtFile.toPlainText() + line[0])
			#self.ventana.txtFile.setPlainText("\ņ")

	def inputFiles(self):

		allFiles = glob.glob("gpsfile/*.csv")
		for oneFile in allFiles:
			f = open( oneFile, 'r')
			allData = f.readlines()
			conn = sqlite3.connect('dakar.sqlite')
			cursor = conn.cursor()

			numComptetitor = allData[2].split(";")[1]
			query = "SELECT * FROM data WHERE competidor = '%i'"%(int(numComptetitor))
			cursor.execute(query)
			check = cursor.fetchone()
			if check == None:
				nameCompetitor = " "
				numOrder = "1"
				category = "moto"
				
				if int(allData[8].split(";")[1]) == 0:
					wpt = "OK"
				else:
					wpt = "NOK"
				if int(allData[10].split(";")[1]) == 0:
					disc = "OK"
				else:
					disc = "NOK"
				try:
					if int(allData[15].split(";")[1]) == 0:
						dz = "OK"
					else:
						dz = "NOK"
				except:
					dz = "NOK"

				
				codNum = int(allData[5].split(";")[1])
				version = "2.0"
				gpsNumber = allData[3].split(";")[1]
				obs = " "

				
				mi_query = "INSERT INTO data (competidor,nombre, orden,categoria,wpt,dz,disc,cod,version,gps,obs) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(numComptetitor,nameCompetitor,numOrder,category,wpt,dz,disc,codNum,version,gpsNumber,obs)
				cursor.execute(mi_query)
				conn.commit()



   
if __name__ == '__main__':
	app = QApplication(sys.argv)
	principal = Principal()
	principal.show()
	sys.exit(app.exec_())