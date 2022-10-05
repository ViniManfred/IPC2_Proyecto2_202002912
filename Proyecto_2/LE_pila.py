from pila import Pila

class Lista_Pila:
    def __init__(self) -> None:
        self.raiz = Pila()
        self.ultimo = Pila()
               
    def append(self, nuevaPila):
        if self.raiz.encargado is None:
            self.raiz = nuevaPila
            self.ultimo = nuevaPila
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaPila
            self.ultimo = nuevaPila
        else:
            self.ultimo.siguiente = nuevaPila
            self.ultimo = nuevaPila

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
        print(cadena)
    
    def desapilar(self):
        nodoAux=self.raiz
        ultimo=self.ultimo
        while True:
            if nodoAux.id is not None:
                if nodoAux.siguiente!=ultimo:
                    nodoAux = nodoAux.siguiente
                else:
                    break
            else:
                break
        return nodoAux.siguiente
        nodoAux.siguiente=None
