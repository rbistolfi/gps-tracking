#!/usr/bin/env python
# -*- coding: utf-8 -*-
      
import sqlite3
class DataBase:
    def __init__(self):
        self.conn = None
        self.cursor = None
    def open(self, dbname):
        """Abrir conexión y establecer un cursor"""
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()
    def get_tables(self):
        """Retorna las tablas"""
        q = self.cursor.execute("SELECT * FROM data")
        return q.fetchall()
    def get_category(self):
        """Retorna las tablas de Categoria"""
        q = self.cursor.execute("SELECT * FROM category")
        return q.fetchall()
    def commit(self):
        """Guardar cambios"""
        self.conn.commit()
    def deleteZone(self):
        q = "DELETE FROM zone"
        self.cursor.execute(q)
        self.conn.commit()
    def deleteData(self):
        q = "DELETE FROM data"
        self.cursor.execute(q)
        self.conn.commit()
        q = "DELETE FROM zonedismiss"
        self.cursor.execute(q)
        self.conn.commit()
        q = "DELETE FROM dz"
        self.cursor.execute(q)
        self.conn.commit()
<<<<<<< HEAD

=======
>>>>>>> change-design
    def insertZone(self,numZone,valueZone):
        q = "INSERT INTO zone (numZone,zone) VALUES ('%i','%s')"%(int(numZone),valueZone)
        self.cursor.execute(q)
        self.conn.commit()
    def getZone(self):
        q = self.cursor.execute("SELECT * FROM zone")
        return q.fetchall()
    def countZone(self):
        q = self.cursor.execute("SELECT numZone FROM zone ")
        return q.fetchall()
    def getDataCompetitor(self,numCompetitor):
        q = self.cursor.execute("SELECT * FROM data WHERE competidor = '%i'"%(numCompetitor))
        return q.fetchone()
    def getDzCompetitor(self,numCompetitor):
        query = "SELECT dz FROM dz WHERE competitor = '%i'"%(numCompetitor)
        q = self.cursor.execute(query)       
        return q.fetchall()
    def getZoneDismiss(self,numCompetitor):
        query = "SELECT zone FROM zonedismiss WHERE competitor = '%i'"%(numCompetitor)
        q = self.cursor.execute(query)       
        return q.fetchall()
    def insertDz(self, numCompetitor,dzValue):
        query = "INSERT INTO dz (competitor,dz) VALUES ('%i','%s')"%(numCompetitor,dzValue)
        q = self.cursor.execute(query)
        self.commit()
<<<<<<< HEAD
    def insertData(self,numCompetitor,nameCompetitor,category,wpt,dz,disc,codNum,version,gpsNumber,obs):
        query = "SELECT max(orden) FROM data"
        q = self.cursor.execute(query)
        maxNum = q.fetchone()

        if maxNum[0] == None:
            numOrder = 1
        else:
            numOrder = maxNum[0] + 1
=======
    def insertData(self,numCompetitor,nameCompetitor,numOrder,category,wpt,dz,disc,codNum,version,gpsNumber,obs):
>>>>>>> change-design
        query = "INSERT INTO data (competidor,nombre, orden,categoria,wpt,dz,disc,cod,version,gps,obs) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(numCompetitor,nameCompetitor,numOrder,category,wpt,dz,disc,codNum,version,gpsNumber,obs)
        self.cursor.execute(query)
        self.commit()
    def insertZoneDismiss(self,numCompetitor,a):
        query = "INSERT INTO zonedismiss (competitor,zone) VALUES ('%s','%s')"%(numCompetitor,a)
        self.cursor.execute(query)
        self.commit()
    def close(self):
        self.cursor.close()
        self.conn.close()
    def updateData(self,title,idCompetitor,cell):
        query = "UPDATE data  SET '%s'='%s' WHERE competidor ='%s'"%(title,cell,idCompetitor)
        self.cursor.execute(query)
        self.commit()
