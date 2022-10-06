from pila import Pila
from colorama import Fore
import os 

class Lista_Pila:
    def __init__(self) -> None:
        self.raiz = Pila()
               
    def append(self, nuevaPila):
        if self.raiz is None:
            self.raiz = nuevaPila
        elif self.raiz.encargado is None:
            self.raiz = nuevaPila
        else:
            nuevaPila.siguiente = self.raiz
            self.raiz = nuevaPila

    def printer(self):
        nodoAux = self.raiz
        cadena =Fore.MAGENTA+''
        while True:
            if nodoAux.id is not None:
                cadena +=str(nodoAux.counter)+ "ID:" + str(nodoAux.id) + " Identificacion:" + nodoAux.identificacion + " Encargado:" + nodoAux.encargado
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += "\n"
                else:
                    break
            else:
                break
        print(cadena)
    
    def desapilar(self):
        actual=self.raiz
        try:
            if actual.encargado is not None:
                self.raiz = actual.siguiente
                actual.siguiente = None
        except:
            print("No hay escritorios para desactivar")
    
    def proximo_atendido(self):
        nodoAux1 = self.raiz
        calcule=1000000
        while True:
            if nodoAux1.encargado is not None:
                if nodoAux1.clientes_escritorio_pila.ultimo.tiempo_atencion<calcule:
                    calcule = nodoAux1.clientes_escritorio_pila.ultimo.tiempo_atencion
                else:
                    if nodoAux1.siguiente is not None:
                        nodoAux1 = nodoAux1.siguiente
                    else:
                        break
            else:
                break
        return calcule

    def proximo_atender(self):
        nodoAux1 = self.raiz
        calcule=1000000
        while True:
            if nodoAux1.encargado is not None:
                if nodoAux1.clientes_escritorio_pila.ultimo.tiempo_atencion<calcule:
                    node=nodoAux1
                    calcule = nodoAux1.clientes_escritorio_pila.ultimo.tiempo_atencion
                    
                else:
                    if nodoAux1.siguiente is not None:
                        nodoAux1 = nodoAux1.siguiente
                    else:
                        break
            else:
                break
        return node

    def recalcular(self,red):
        nodoAux1=self.raiz
        asociation=red
        while True:
            if nodoAux1.encargado is not None:
                tesla=nodoAux1.clientes_escritorio_pila.ultimo.tiempo_atencion-asociation
                myRoundNumber = round(tesla, 2)
                nodoAux1.clientes_escritorio_pila.ultimo.tiempo_atencion=myRoundNumber
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
                if nodoAux.encargado is not None:
                    red=nodoAux.encargado.replace(' ', '')
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
        file = open("./grafica_pila.dot", "w+")
        file.write(cadena)
        file.close()
        os.system("dot -Tpng grafica_pila.dot -o grafica_pila.png")


