#!/usr/bin/python3 # -*- coding: utf-8 -*-
import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox 
import math

class numerofibo(QMainWindow):
    

    
    def __init__(self):
        super().__init__()
        uic.loadUi("numero_fibo.ui",self)
        self.btnCalcular.clicked.connect(self.mostrar)
          
    def mostrar(self):
        self.label_5.setText("el resultado es"+str(self.fiboRange(int(self.txtPrimero.text()),int(self.txtSegundo.text()))))


    #hecho por definicion de 
    def fiboRange(self,numeroInicial,numeroFinal):
        n_base=1
        numero_1=1
        numero_2=1
        numero_3=0
        mostrar=[]
        
        if (numeroInicial>numeroFinal):
            return (" que no indicaste un rango valido")

        while(n_base<=numeroFinal):  # este bucle es que el hace la suma del numero de fibonachi 
            numero_3=numero_1+numero_2
            numero_1=numero_2
            numero_2=numero_3
            if (numero_3 >= numeroInicial and numero_3<=numeroFinal): # esta condicion lo que hace es que  determinar en el rango cuales numeros 
                mostrar.append(numero_3)# seran los que apareceran en mostrar al usuario 
            n_base=n_base+1
        if (len(mostrar)==0):
            return (" ninguno porque no hay numeros de fibo en este rango")
        return(mostrar)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = numerofibo()
    ex.show()
    sys.exit(app.exec_())