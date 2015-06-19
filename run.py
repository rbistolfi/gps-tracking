        #self.connect(self.ventana.pushButton,SIGNAL('clicked()'),self.change)
# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mainWindow import Ui_MainWindow
from categoryParam import Ui_CatParam
from editZone import Ui_editZone
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
		


   
if __name__ == '__main__':
	app = QApplication(sys.argv)
	principal = Principal()
	principal.show()
	sys.exit(app.exec_())