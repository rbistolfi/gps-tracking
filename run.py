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
		self.countZone = []
		self.mainWindow = Ui_MainWindow()
		self.mainWindow.setupUi(self)
		self.db = DataBase()
		self.db.open('dakar.sqlite')
		
		self.countZones()
		self.countVehicles()
		self.inputFiles()

		
		self.mainWindow.tblData.resizeRowsToContents()
		self.mainWindow.tblData.setColumnWidth(1, 70)
		self.mainWindow.lblWpt.setAlignment(Qt.AlignHCenter)
		self.mainWindow.lblDz.setAlignment(Qt.AlignHCenter)

		self.ctimer = QTimer()
		self.ctimer.start(10000)
		self.mainWindow.actionCategory.triggered.connect(self.openCategoryWindow)
		self.mainWindow.actionDirectoryPath.triggered.connect(self.searchPath)
		self.mainWindow.actionEditZone.triggered.connect(self.openEditZone)

		self.connect(self.ctimer,SIGNAL("timeout()"), self.checkNewFile)
		self.mainWindow.tblGralStatus.cellClicked.connect(self.otherTable)
	def countZones(self):
		check = self.db.countZone()
		for i in check:
			self.countZone.append(i[0])
	
	def mainTable(self):
		rows = self.db.get_tables()
		self.mainWindow.tblGralStatus.setRowCount(len(rows))

		for i,table in enumerate(rows):
			for m,data in enumerate(table):
				if m != 0:
					self.mainWindow.tblGralStatus.setItem(i,m - 1,QTableWidgetItem(str(data)))
					if str(data) == 'OK':
						color = QColor(133, 222, 84)
					elif str(data) == 'NOK':
						color = QColor(255, 64, 16)
					else:
						color = QColor("white")
					self.mainWindow.tblGralStatus.item(i, m - 1).setBackground(QColor(color))
					self.mainWindow.tblGralStatus.resizeColumnsToContents()
					self.mainWindow.tblGralStatus.resizeRowsToContents()
		self.mainWindow.tblGralStatus.setSortingEnabled(True)
		
				

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

		findWord = False

		for q,oneFile in enumerate(allFiles):
			zonePassed = []
			f = open( oneFile, 'r')
			allData = f.readlines()
			


			numCompetitor = allData[2].split(";")[1]
			check = self.db.getDataCompetitor(int(numCompetitor))
			if check == None:
				nameCompetitor = " "
				numOrder = "1"
				category = "Moto"
				if int(numCompetitor) >= self.minMoto and int(numCompetitor) <= self.maxMoto:
					category = "Moto"
				elif int(numCompetitor) >= self.minQuad and int(numCompetitor) <= self.maxQuad:
					category = "Quad"
				elif int(numCompetitor) >= self.minCar and int(numCompetitor) <= self.maxCar:
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
							self.db.insertDz(int(numCompetitor),dzValue)
							
				codNum = int(allData[5].split(";")[1])
				version = "2.0"
				gpsNumber = allData[3].split(";")[1]
				obs = " "
				self.db.insertData(numCompetitor,nameCompetitor,numOrder,category,wpt,dz,disc,codNum,version,gpsNumber,obs)
				for line in allData:
					try:
						if findWord:
							tmpnum = line.split(";")[3]
							num = tmpnum.split(":")[1]
							zonePassed.append(int(num))
						if line.startswith('InfosChronos') :
							findWord = True
					except:
						pass
				zoneDismiss = list(set(self.countZone) - set(zonePassed))
				for a in zoneDismiss:
					self.db.insertZoneDismiss(numCompetitor,a)
					
		self.countVehicles()
		self.mainTable()

	def countVehicles(self):
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
		f = open('path.txt')
		path = f.readline()
		allFiles = glob.glob(path + "/*.csv")
		if len(allFiles) > len(self.tmpCountFile):
			self.mainWindow.lblUpdate.setText("Hay nuevos archivos")
			self.inputFiles()
		else:
			self.mainWindow.lblUpdate.setText(" ")

	def otherTable(self):
		rowSelected = self.mainWindow.tblGralStatus.currentIndex()
		rowDisc = self.mainWindow.tblGralStatus.item(rowSelected.row(),6)
		numCompetitor = self.mainWindow.tblGralStatus.item(rowSelected.row(),0)

		check = self.db.getDataCompetitor(int(numCompetitor.text()))

		self.mainWindow.tblData.setItem(-1,1,QTableWidgetItem(str(check[1])))
		self.mainWindow.tblData.setItem(0,1,QTableWidgetItem(str(check[10])))
		self.mainWindow.tblData.setItem(1,1,QTableWidgetItem(str(check[2])))

		check = self.db.getDzCompetitor(int(numCompetitor.text()))
		

		if len(check) == 0:
			self.mainWindow.lstDzStatus.clear()
			self.mainWindow.lstDz.clear()
			self.mainWindow.lstDzStatus.addItem(QListWidgetItem("OK"))
			self.mainWindow.lstDzStatus.item(0).setBackground(QColor(133, 222, 84))
			self.mainWindow.lstDzStatus.item(0).setTextAlignment(Qt.AlignHCenter)
		else:
			self.mainWindow.lstDzStatus.clear()
			self.mainWindow.lstDz.clear()
			self.mainWindow.lstDzStatus.addItem(QListWidgetItem("NOK"))
			self.mainWindow.lstDzStatus.item(0).setBackground(QColor(255, 64, 16))
			self.mainWindow.lstDzStatus.item(0).setTextAlignment(Qt.AlignHCenter)
			self.mainWindow.lblWpt.setAlignment(Qt.AlignHCenter)
			for m,data in enumerate(check):
				self.mainWindow.lstDz.addItem(QListWidgetItem("%s"%str(data[0])))

		check = self.db.getZoneDismiss(int(numCompetitor.text()))
			
		
		if len(check) == 0:
			self.mainWindow.lstWptStatus.clear()
			self.mainWindow.lstWpt.clear()
			self.mainWindow.lstWptStatus.addItem(QListWidgetItem("OK"))
			self.mainWindow.lstWptStatus.item(0).setBackground(QColor(133, 222, 84))
			self.mainWindow.lstWptStatus.item(0).setTextAlignment(Qt.AlignHCenter)
		else:
			self.mainWindow.lstWpt.clear()
			self.mainWindow.lstWptStatus.clear()
			self.mainWindow.lstWptStatus.addItem(QListWidgetItem("NOK"))
			self.mainWindow.lstWptStatus.item(0).setBackground(QColor(255, 64, 16))
			self.mainWindow.lstWptStatus.item(0).setTextAlignment(Qt.AlignHCenter)
			for m,data in enumerate(check):
				self.mainWindow.lstWpt.addItem(QListWidgetItem("%s"%str(data[0])))
				self.mainWindow.lstWpt.item(m).setTextAlignment(Qt.AlignHCenter)


		self.mainWindow.lstDiscStatus.clear()
		if rowDisc.text() == 'OK':
			color = QColor(133, 222, 84)
		else:
			color = QColor(255, 64, 16)

		self.mainWindow.lstDiscStatus.addItem(QListWidgetItem(rowDisc.text()))
		self.mainWindow.lstDiscStatus.item(0).setBackground(color)
		self.mainWindow.lstDiscStatus.item(0).setTextAlignment(Qt.AlignHCenter)
				
		


   
if __name__ == '__main__':
	app = QApplication(sys.argv)
	principal = Principal()
	principal.show()
	sys.exit(app.exec_())