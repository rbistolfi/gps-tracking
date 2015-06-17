from PyQt4.QtCore import *
from PyQt4.QtGui import *
from form import Ui_Dialog
import sys
 
class Principal(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args)
 
        contenedor = QVBoxLayout()
        self.setLayout(contenedor)
 
        btnAbrir = QPushButton("Abrir ventana",None)
        contenedor.addWidget(btnAbrir)
        self.connect(btnAbrir, SIGNAL("clicked()"), self.abrir)
 
        btnSalir = QPushButton("Salir",None)
        contenedor.addWidget(btnSalir)
        self.connect(btnSalir, SIGNAL("clicked()"), self.salir)
 
    def abrir(self):
        ventana = Secundaria().exec_()
 
    def salir(self):
        exit()
 
class Secundaria(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)

        self.ventana = Ui_Dialog()
        self.ventana.setupUi(self)
 
        
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    sys.exit(app.exec_())