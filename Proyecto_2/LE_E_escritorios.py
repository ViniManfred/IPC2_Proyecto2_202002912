from E_escritorios import Escritorios

class Lista_E:
    def __init__(self) -> None:
        self.raiz = Escritorios()
        self.ultimo = Escritorios()

    
    def append(self, nuevoE):
        if self.raiz.id is None:
            self.raiz = nuevoE
            self.ultimo = nuevoE
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoE
            self.ultimo = nuevoE
        else:
            self.ultimo.siguiente = nuevoE
            self.ultimo = nuevoE