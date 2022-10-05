from cola import Cola
from colorama import Fore

class Lista_Cola:
    def __init__(self) -> None:
        self.raiz = Cola()
        self.ultimo = Cola()

    
    def append(self, nuevaCola):
        if self.raiz.dpi is None:
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
        