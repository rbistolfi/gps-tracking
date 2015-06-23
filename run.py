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
		self.minMoto = 0
		self.maxMoto = 0
		self.minQuad = 0
		self.maxQuad = 0
		self.minCar = 0
		self.maxCar = 0
		self.tmpCountFile = 0
		self.mainWindow = Ui_MainWindow()
		self.mainWindow.setupUi(self)
		self.db = DataBase()
		self.db.open('dakar.sqlite')
		self.inputFiles()
		self.mainWindow.tblDz.setColumnWidth(0, 40)
		self.mainWindow.tblDz.setColumnWidth(1, 70)
		self.ctimer = QTimer()
		self.ctimer.start(10000)
		self.mainWindow.actionCategory.triggered.connect(self.openCategoryWindow)
		self.mainWindow.actionDirectoryPath.triggered.connect(self.searchPath)
		self.mainWindow.actionEditZone.triggered.connect(self.openEditZone)

		self.connect(self.ctimer,SIGNAL("timeout()"), self.checkNewFile)
		self.connect(self.mainWindow.btnUpdate,SIGNAL('clicked()'),self.inputFiles)
		self.connect(self.mainWindow.btnNewFile,SIGNAL('clicked()'),self.checkNewFile)
		self.mainWindow.tblGralStatus.cellClicked.connect(self.otherTable)
	
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
					self.mainWindow.tblGralStatus.resizeRowsToContents()
		
				

	def openCategoryWindow(self):
		mainWindow = CategoryParam().exec_()

	def openEditZone(self):
		mainWindow = EditZone().exec_()

	def searchPath(self):
		dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
		f = open('path.txt','w')
		f.write(dir_)
		f.close()
		self.mainWindow.lblPath.setText("Current Path: " + dir_)
		self.inputFiles()
	
	def inputFiles(self):
		f = open('path.txt')
		path = f.readline()
		self.mainWindow.lblPath.setText("Current Path: " + path)
		allFiles = glob.glob(path + "/*.csv")
		self.tmpCountFile = allFiles
		for q,oneFile in enumerate(allFiles):
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
				category = "Moto"
				if int(numComptetitor) >= self.minMoto and int(numComptetitor) <= self.maxMoto:
					category = "Moto"
				elif int(numComptetitor) >= self.minQuad and int(numComptetitor) <= self.maxQuad:
					category = "Quad"
				elif int(numComptetitor) >= self.minCar and int(numComptetitor) <= self.maxCar:
					category = "Car"
				
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
				except:
					dz = "NOK"
					dzDismiss = allData[15].split(";")
					for i,dzValue in enumerate(dzDismiss):
						if i !=0:
							query = "INSERT INTO dz (competitor,dz) VALUES ('%i','%s')"%(int(numComptetitor),dzValue)
							cursor.execute(query)
							conn.commit()
				codNum = int(allData[5].split(";")[1])
				version = "2.0"
				gpsNumber = allData[3].split(";")[1]
				obs = " "
				mi_query = "INSERT INTO data (competidor,nombre, orden,categoria,wpt,dz,disc,cod,version,gps,obs) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(numComptetitor,nameCompetitor,numOrder,category,wpt,dz,disc,codNum,version,gpsNumber,obs)
				cursor.execute(mi_query)
				conn.commit()
			self.countVehicles()
			self.mainTable()

	def countVehicles(self):
		self.db = DataBase()
		self.db.open('dakar.sqlite')
		rows = self.db.get_category()

		self.minMoto = rows[0][2]
		self.maxMoto = rows[0][3]
		self.minQuad = rows[1][2]
		self.maxQuad = rows[1][3]
		self.minCar = rows[2][2]
		self.maxCar = rows[2][3]

		countMoto = 0
		countQuad = 0
		countCar = 0

		rows = self.db.get_tables()
		for row in rows:
			if row[1] >= self.minMoto and row[1] <= self.maxMoto:
				countMoto += 1
			elif row[1] >= self.minQuad and row[1] <= self.maxQuad:
				countQuad += 1
			elif row[1] >= self.minCar and row[1] <= self.maxCar:
				countCar += 1
		self.mainWindow.lnCountMoto.setText(str(countMoto))
		self.mainWindow.lnCountQuad.setText(str(countQuad))
		self.mainWindow.lnCountCar.setText(str(countCar))
	def checkNewFile(self):
		
		allFiles = glob.glob("gpsfile/*.csv")
		if len(allFiles) > len(self.tmpCountFile):
			self.mainWindow.lblUpdate.setText("Hay nuevos archivos")
			self.inputFiles()
		else:
			self.mainWindow.lblUpdate.setText(" ")

	def otherTable(self):
		rowSelected = self.mainWindow.tblGralStatus.currentIndex()
		numComptetitor = self.mainWindow.tblGralStatus.item(rowSelected.row(),0)

		conn = sqlite3.connect('dakar.sqlite')
		cursor = conn.cursor()

		query = "SELECT * FROM data WHERE competidor = '%i'"%(int(numComptetitor.text()))
		cursor.execute(query)
		check = cursor.fetchone()

		self.mainWindow.tblData.setItem(-1,1,QTableWidgetItem(str(check[1])))
		self.mainWindow.tblData.setItem(0,1,QTableWidgetItem(str(check[10])))
		self.mainWindow.tblData.setItem(1,1,QTableWidgetItem(str(check[2])))
		#self.mainWindow.tblData.resizeColumnsToContents()
		self.mainWindow.tblData.resizeRowsToContents()
		query = "SELECT dz FROM dz WHERE competitor = '%i'"%(int(numComptetitor.text()))
		cursor.execute(query)		

		check = cursor.fetchall()

		if len(check) == 0:
			self.mainWindow.tblDz.setHorizontalHeaderLabels(['DZ','OK'])
			self.mainWindow.tblDz.setRowCount(0)
		else:
			self.mainWindow.tblDz.setHorizontalHeaderLabels(['DZ','NOK'])

			self.mainWindow.tblDz.setRowCount(len(check))
			for m,data in enumerate(check):
				self.mainWindow.tblDz.setItem(m,1,QTableWidgetItem(str(data[0])))
				self.mainWindow.tblDz.setColumnWidth(0, 40)
				self.mainWindow.tblDz.setColumnWidth(1, 70)
				self.mainWindow.tblDz.resizeRowsToContents()
				
			


   
if __name__ == '__main__':
	app = QApplication(sys.argv)
	principal = Principal()
	principal.show()
	sys.exit(app.exec_())