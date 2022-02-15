#!/usr/bin/python3 # -*- coding: utf-8 -*-
import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox 
import math

class base(QMainWindow):
    

    
    def __init__(self):
        super().__init__()
        uic.loadUi("bases.ui",self)
        self.btnCalcular.clicked.connect(self.mostrar)
          
    def mostrar(self):
        self.label_5.setText("el resultado es  "+self.resultado(self.txtNumero.text(),self.txtBaseuno.text(),self.txtBasedos.text()))

    def debase10_a_otra_base(self,numero_b,baseFinal): #transforma de base 10 a otra base 
        numero_b=int(numero_b)   
        baseFinal=int(baseFinal)
        dividendo=numero_b
        divisor=baseFinal
        residuo=1
        cociente=1
        lita_mostrar=[]
        while(dividendo>=divisor):  
            residuo=dividendo%divisor
            cociente=dividendo//divisor
            dividendo=cociente
            lita_mostrar.append(residuo)
        lita_mostrar.append(cociente)
        resultado=self.delista_a_str(lita_mostrar)
        return resultado
    
    def de_otrabase_a_base10(self,numero_b,baseInicial): #toma de base 10 a otra base y la transforma a la base que se indique
        
        digitos=len(str(numero_b))
        baseInicial=int(baseInicial)
        uno=1
        resultado=0
        for n in str(numero_b):
            numeroFinal=int(n)*baseInicial**(digitos-uno)
            resultado=resultado+numeroFinal
            uno=uno+1
        return resultado
    
    def comprobar_si_cumple(self,numero_b,baseInicial): # esta comprueba si el numero cumple con la base que se puso 
        
        for n in numero_b:
            if (int(n)>=int(baseInicial)):
                validacion=1
                break
            else:
                validacion=0
        return validacion
    
    def resultado(self,numero_b,baseInicial,baseFinal): #
        
        if (self.comprobar_si_cumple(numero_b,baseInicial)==0  ):
            if (baseInicial == "10"):
                resultado=self.debase10_a_otra_base(numero_b,baseFinal)
                return resultado
            elif (baseInicial != "10"):
                pre_resultado_de_numero=self.debase_a_otra_base(numero_b,baseInicial)
                resultado=self.debase10_a_otra_base(pre_resultado_de_numero,baseFinal)
                return resultado
        else:
            resultado="que ha introducido un numero_b invalido"
            return resultado
        
    def delista_a_str (self,lista):
        string=" "
        
        
        for n in lista :
            string=str(n)+string
            
        return string
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = base()
    ex.show()
    sys.exit(app.exec_())