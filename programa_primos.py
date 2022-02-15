#!/usr/bin/python3 # -*- coding: utf-8 -*-
import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox 
import math

class n_primos(QMainWindow):
    
    divisores_del_rango=2
    
    lista_a_mostrar=[]
    
    def __init__(self):
        super().__init__()
        uic.loadUi("primos.ui",self)
        self.btnCalcular.clicked.connect(self.mostrar)
    def mostrar(self):
        self.labSalida.setText("el resultado es"+str(self.calcularPrimo(int(self.txtRangodos.text()),int(self.txtRangouno.text()))))
        #  con la funcion len por pereza  con los resultados que me retorno los calcular primos asi saco los elementos
        self.labSalida_2.setText("hay esta cantidad de elementos: "+str(len((self.calcularPrimo(int(self.txtRangodos.text()),int(self.txtRangouno.text()))))))
    def calcularPrimo(self,final,inicial):
        divisores_del_rango=2
        lista_a_mostrar =[]
        # funcion para avanzar de un rango uno a el rango 
        for i in range(0,final-inicial+1):
            numero_inicial=inicial+i
            raizcadauno=math.sqrt(numero_inicial)
           # recordar que si la raiz del numero es menor a 2  es un numero primo 
            if (divisores_del_rango>math.sqrt(numero_inicial)):
                primo=1
            # funcion para divisores_del_rango del producto 
            while (divisores_del_rango<=raizcadauno):
                primo=1
               # se rompe cuando el reciduo es igual a cero por lo tanto no me interesa
                if numero_inicial%divisores_del_rango == 0:
                    primo=0
                    break
                divisores_del_rango=divisores_del_rango + 1
            divisores_del_rango=2
            if (primo == 1 and inicial+i != 1):
                lista_a_mostrar.append(inicial+i)
        return lista_a_mostrar

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = n_primos()
    ex.show()
    sys.exit(app.exec_())