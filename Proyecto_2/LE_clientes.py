from clientes import Clientes

class Lista_C:
    def __init__(self) -> None:
        self.raiz = Clientes()
        self.ultimo = Clientes()

    
    def append(self, nuevoC):
        if self.raiz.dpi is None:
            self.raiz = nuevoC
            self.ultimo = nuevoC
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoC
            self.ultimo = nuevoC
        else:
            self.ultimo.siguiente = nuevoC
            self.ultimo = nuevoC