from puntos_atencion import Puntos_Atencion
from colorama import Fore
class Lista_PA:
    def __init__(self) -> None:
        self.raiz = Puntos_Atencion()
        self.ultimo = Puntos_Atencion()

    def append(self, nuevoPA):
        if self.raiz.direccion is None:
            self.raiz = nuevoPA
            self.ultimo = nuevoPA
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoPA
            self.ultimo = nuevoPA
        else:
            self.ultimo.siguiente = nuevoPA
            self.ultimo = nuevoPA

    def printer(self):
        nodoAux1 = self.raiz
        cadena1 = ''
        while True:
            if nodoAux1.nombre is not None:
                cadena1 += "ID: "+ nodoAux1.id + " Nombre: " + nodoAux1.nombre +" Direccion: "+nodoAux1.direccion+"\n          Escritorios\n"+nodoAux1.E_escritorios.printer()+"\n"
                if nodoAux1.siguiente is not None:
                    nodoAux1 = nodoAux1.siguiente
                    cadena1 += " \n"
                else:
                    break
            else:
                break
        return cadena1

    def print(self):
        nodoAux1 = self.raiz
        cadena1 = Fore.MAGENTA+''
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

    def busquedaID(self, id):
        nodoAux = self.raiz
        while nodoAux.id!= id:
            if nodoAux.siguiente is not None:
                nodoAux = nodoAux.siguiente
            else:
                return None
        return nodoAux
    
    