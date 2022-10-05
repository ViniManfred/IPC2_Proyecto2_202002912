from E_escritorios import Escritorios
from colorama import Fore

class Lista_E:
    def __init__(self) -> None:
        self.raiz = Escritorios()
        self.ultimo = Escritorios()
               
    def append(self, nuevoE):
        if self.raiz.encargado is None:
            self.raiz = nuevoE
            self.ultimo = nuevoE
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoE
            self.ultimo = nuevoE
        else:
            self.ultimo.siguiente = nuevoE
            self.ultimo = nuevoE
    
    def printer(self):
        nodoAux = self.raiz
        cadena = ''
        while True:
            if nodoAux.id is not None:
                cadena += "ID:" + str(nodoAux.id) + " Identificacion:" + nodoAux.identificacion + " Encargado:" + nodoAux.encargado +" Estado:"+nodoAux.estado
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += "\n"
                else:
                    break
            else:
                break
        return cadena

    def print(self):
        nodoAux = self.raiz
        cadena = ''
        while True:
            if nodoAux.id is not None:
                cadena += "ID:" + str(nodoAux.id) + " Identificacion:" + nodoAux.identificacion + " Encargado:" + nodoAux.encargado +" Estado:"+nodoAux.estado
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += "\n"
                else:
                    break
            else:
                break
        print(cadena)
    
    def busquedaID(self,id):
        nodoAux = self.raiz
        while nodoAux.id!= id:
            if nodoAux.siguiente is not None:
                nodoAux = nodoAux.siguiente
            else:
                return None
        return nodoAux

    def busqueda_estado(self,estado):
        counter=0
        nodoAux = self.raiz
        for x in range(self.ultimo.counter):
            if nodoAux.estado==estado:
                counter+=1
                nodoAux = nodoAux.siguiente
            else:
                nodoAux = nodoAux.siguiente
        return counter

    def busqueda_desactivos(self,counter):
        nodoAux = self.raiz
        while nodoAux.counter!= counter:
            if nodoAux.siguiente is not None:
                nodoAux = nodoAux.siguiente
            else:
                return None
        nodoAux.estado="activo"
        return nodoAux
        
    
    def print_inactivos(self):
        nodoAux = self.raiz
        cadena = ''
        while True:
            if nodoAux.id is not None:
                if nodoAux.estado == "inactivo":
                    cadena +="  "+str(nodoAux.counter) + ". " + nodoAux.identificacion+"\n"
                    if nodoAux.siguiente is not None:
                        nodoAux = nodoAux.siguiente
                    else:
                        break
                else:
                    if nodoAux.siguiente is not None:
                        nodoAux = nodoAux.siguiente
                    else:
                        break
            else:
                break
        print(cadena)