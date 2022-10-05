from clientes_escritorio import Clientes_escritorio
from colorama import Fore

class Lista_Clientes_escritorio:
    def __init__(self) -> None:
        self.raiz = Clientes_escritorio()
        self.ultimo = Clientes_escritorio()

    
    def append(self, nuevoCE):
        if self.raiz.dpi is None:
            self.raiz = nuevoCE
            self.ultimo = nuevoCE
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoCE
            self.ultimo = nuevoCE
        else:
            self.ultimo.siguiente = nuevoCE
            self.ultimo = nuevoCE
        
    def print(self):
        nodoAux1 = self.raiz
        cadena1 = Fore.CYAN+''
        while True:
            if nodoAux1.nombre is not None:
                cadena1 +="  "+str(nodoAux1.counter)+". "+nodoAux1.nombre+" E:"+str(nodoAux1.tiempo_espera)+" A:"+ str(nodoAux1.tiempo_atencion)
                if nodoAux1.siguiente is not None:
                    nodoAux1 = nodoAux1.siguiente
                    cadena1 += " \n"
                else:
                    break
            else:
                break
        print(cadena1)

    def espera_promedio(self):
        nodoAux1 = self.raiz
        calcule = 0
        while True:
            if nodoAux1.nombre is not None:
                calcule += nodoAux1.tiempo_espera
                if nodoAux1.siguiente is not None:
                    nodoAux1 = nodoAux1.siguiente
                else:
                    break
            else:
                break
        div= self.ultimo
        response=calcule/div.counter
        myRoundNumber = round(response, 2)
        return myRoundNumber

    def atencion_promedio(self):
        nodoAux1 = self.raiz
        calcule = 0
        while True:
            if nodoAux1.nombre is not None:
                calcule += nodoAux1.tiempo_atencion
                if nodoAux1.siguiente is not None:
                    nodoAux1 = nodoAux1.siguiente
                else:
                    break
            else:
                break
        div= self.ultimo
        response=calcule/div.counter
        myRoundNumber = round(response, 2)
        return myRoundNumber

    def atencion_maxima(self):
        nodoAux1 = self.raiz
        calcule=0
        while True:
            if nodoAux1.nombre is not None:
                if nodoAux1.tiempo_atencion>calcule:
                    calcule = nodoAux1.tiempo_atencion
                else:
                    if nodoAux1.siguiente is not None:
                        nodoAux1 = nodoAux1.siguiente
                    else:
                        break
            else:
                break
        return calcule

    def atencion_minima(self):
        nodoAux1 = self.raiz
        calcule=1000000
        while True:
            if nodoAux1.nombre is not None:
                if nodoAux1.tiempo_atencion<calcule:
                    calcule = nodoAux1.tiempo_atencion
                else:
                    if nodoAux1.siguiente is not None:
                        nodoAux1 = nodoAux1.siguiente
                    else:
                        break
            else:
                break
        return calcule

    def espera_maxima(self):
        nodoAux1 = self.raiz
        calcule=0
        while True:
            if nodoAux1.nombre is not None:
                if nodoAux1.tiempo_espera>calcule:
                    calcule = nodoAux1.tiempo_espera
                else:
                    if nodoAux1.siguiente is not None:
                        nodoAux1 = nodoAux1.siguiente
                    else:
                        break
            else:
                break
        return calcule

    def espera_minima(self):
        nodoAux1 = self.raiz
        calcule=1000000
        while True:
            if nodoAux1.nombre is not None:
                if nodoAux1.tiempo_espera<calcule and nodoAux1.tiempo_espera!=0:
                    calcule = nodoAux1.tiempo_espera
                else:
                    if nodoAux1.siguiente is not None:
                        nodoAux1 = nodoAux1.siguiente
                    else:
                        break
            else:
                break
        return calcule