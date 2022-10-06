from cola import Cola
from colorama import Fore
import os 

class Lista_Cola:
    def __init__(self) -> None:
        self.raiz = Cola()
        self.ultimo = Cola()

    
    def append(self, nuevaCola):
        if self.raiz is None:
            self.raiz = nuevaCola
        elif self.raiz.dpi is None:
            self.raiz = nuevaCola
            self.ultimo = nuevaCola
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaCola
            self.ultimo = nuevaCola
        else:
            self.ultimo.siguiente = nuevaCola
            self.ultimo = nuevaCola

    def desencolar(self):
        actual=self.raiz
        try:
            if actual.nombre is not None:
                self.descontar()
                self.raiz = actual.siguiente
                actual.siguiente = None
            else:
                print("La cola esta vacia")
        except:
            print("La cola esta vacia")

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

    def descontar(self):
        nodoAux1=self.raiz
        time=self.raiz.tiempo_atencion
        while True:
            if nodoAux1.nombre is not None:
                time_descontar=nodoAux1.tiempo_espera-time
                myRoundNumber = round(time_descontar, 2)
                nodoAux1.tiempo_espera=myRoundNumber
                if nodoAux1.siguiente is not None:
                    nodoAux1 = nodoAux1.siguiente
                else:
                    break
            else:
                break

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

    def graficar(self):
        nodoAux = self.raiz
        cadena = 'digraph { '  
        while True:
            if nodoAux is not None:
                if nodoAux.nombre is not None:
                    red=nodoAux.nombre.replace(' ', '')
                    cadena +=red
                    if nodoAux.siguiente is not None:
                        nodoAux = nodoAux.siguiente
                        cadena += " -> "
                    else:
                        break
                else:
                    break
            else:
                break
        cadena += "}"
        file = open("./grafica_cola.dot", "w+")
        file.write(cadena)
        file.close()
        os.system("dot -Tpng grafica_cola.dot -o grafica_cola.png")





        