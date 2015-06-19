#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       database.py
#
#       Copyright 2013 Recursos Python - www.recursospython.com
#       
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
    def get_table_info(self, table):
        """Retorna las columnas"""

        q = self.cursor.execute("PRAGMA table_info(%s)" % table)
        return q.fetchall()
    def get_table_items(self, table):
        """Retorna las filas"""
        print "#####",table
        q = self.cursor.execute("SELECT * FROM " + table)
        return q.fetchall()
    def commit(self):
        """Guardar cambios"""
        self.conn.commit()
    def close(self):
        self.cursor.close()
        self.conn.close()