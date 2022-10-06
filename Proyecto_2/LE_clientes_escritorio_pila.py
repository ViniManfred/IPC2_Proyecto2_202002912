from cliente_escritorio_pila import Clientes_escritorio_pila
from colorama import Fore

class Lista_Clientes_escritorio_pila:
    def __init__(self) -> None:
        self.raiz = Clientes_escritorio_pila()
        self.ultimo = Clientes_escritorio_pila()

    
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

    def recalcular(self):
        nodoAux1=self.raiz
        red=self.raiz.tiempo_espera
        while True:
            if nodoAux1.nombre is not None:
                    myRoundNumber = round(red, 2)
                    nodoAux1.tiempo_espera=myRoundNumber
                    red=nodoAux1.tiempo_espera+nodoAux1.tiempo_atencion
                    if nodoAux1.siguiente is not None:
                        nodoAux1 = nodoAux1.siguiente
                    else:
                        break
            else:
                break

    def buscar(self, time):
        nodoAux = self.raiz
        while nodoAux.tiempo_espera!= time:
            if nodoAux.siguiente is not None:
                nodoAux = nodoAux.siguiente
            else:
                return None
        return nodoAux

