        #self.connect(self.ventana.pushButton,SIGNAL('clicked()'),self.change)
# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mainWindow import Ui_MainWindow
from categoryParam import Ui_CatParam
from editZone import Ui_editZone
import csv

class Principal(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		self.mainWindow = Ui_MainWindow()
		self.mainWindow.setupUi(self)

		self.mainWindow.actionCategory.triggered.connect(self.openCategoryWindow)
		self.mainWindow.actionDirectoryPath.triggered.connect(self.searchPath)
		self.mainWindow.actionEditZone.triggered.connect(self.openEditZone)

		self.connect(self.mainWindow.btnConvert,SIGNAL('clicked()'),self.searchFiles)

	def openCategoryWindow(self):
		mainWindow = CategoryParam().exec_()

	def openEditZone(self):
		mainWindow = EditZone().exec_()

	def searchPath(self):
		dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
		self.mainWindow.lblPath.setText(dir_)
		print dir_
	
	def searchFiles(self):
		path = self.mainWindow.lblPath.text()
		strText = self.mainWindow.txtFile.toPlainText()
		f = open('/home/nano/Escritorio/a.csv')
		lns = csv.reader(f)
		for line in lns:
			self.mainWindow.txtFile.setPlainText(self.mainWindow.txtFile.toPlainText() + line[0])
			#self.ventana.txtFile.setPlainText("\ņ")

class CategoryParam(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)

        self.categoryParam = Ui_CatParam()
        self.categoryParam.setupUi(self)

class EditZone(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self)

		self.editZone = Ui_editZone()
		self.editZone.setupUi(self)

		self.createTable(self.editZone)

		self.connect(self.editZone.btnDeleteZone,SIGNAL('clicked()'),self.deleteZone)

	def deleteZone(self):
		f = open('/home/nano/Escritorio/Version 1.0/zones.txt','w')
		self.createTable(self.editZone)		

	def createTable(self,ventana):
		try:
			f = open('/home/nano/Escritorio/Version 1.0/zones.txt')
			zones = f.read().split("\n")
			self.editZone.tableWidget.setColumnCount(1)
			self.editZone.tableWidget.setRowCount(len(zones))
			for i,zone in enumerate(zones):
				newitem = QTableWidgetItem(zone)
				self.editZone.tableWidget.setItem(0,i,newitem)
		except:
			pass


   
if __name__ == '__main__':
	app = QApplication(sys.argv)
	principal = Principal()
	principal.show()
	sys.exit(app.exec_())