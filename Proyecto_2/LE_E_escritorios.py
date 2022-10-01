from E_escritorios import Escritorios

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