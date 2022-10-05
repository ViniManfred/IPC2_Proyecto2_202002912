from empresas import Empresas
from colorama import Fore

class Lista_E:
    def __init__(self) -> None:
        self.raiz = Empresas()
        self.ultimo = Empresas()

    def append(self, nuevaE):
        if self.raiz.nombre is None:
            self.raiz = nuevaE
            self.ultimo = nuevaE
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaE
            self.ultimo = nuevaE
        else:
            self.ultimo.siguiente = nuevaE
            self.ultimo = nuevaE
        
    def printer(self):
        nodoAux1 = self.raiz
        cadena1 = ''
        while True:
            if nodoAux1.nombre is not None:

                cadena1 += "ID: "+ nodoAux1.id + " Nombre: " + nodoAux1.nombre +" Abreviatura: "+nodoAux1.abreviatura +"\n          TRANSACCIONES\n"+nodoAux1.E_transacciones.print()+"\n          PUNTOS DE ATENCION\n"+nodoAux1.puntos_atencion.printer()
                if nodoAux1.siguiente is not None:
                    nodoAux1 = nodoAux1.siguiente
                    cadena1 += " \n"
                else:
                    break
            else:
                break
        print(cadena1)

    def print(self):
        nodoAux1 = self.raiz
        cadena1 = Fore.LIGHTBLUE_EX+''
        while True:
            if nodoAux1.nombre is not None:
                cadena1 += str(nodoAux1.counter)+". "+nodoAux1.nombre
                if nodoAux1.siguiente is not None:
                    nodoAux1 = nodoAux1.siguiente
                    cadena1 += " \n"
                else:
                    break
            else:
                break
        print(cadena1)

    def busqueda(self, counter):
        nodoAux = self.raiz
        while nodoAux.counter!= counter:
            if nodoAux.siguiente is not None:
                nodoAux = nodoAux.siguiente
            else:
                return None
        return nodoAux
    
    def busquedaID(self,id):
        nodoAux = self.raiz
        while nodoAux.id!= id:
            if nodoAux.siguiente is not None:
                nodoAux = nodoAux.siguiente
            else:
                return None
        return nodoAux