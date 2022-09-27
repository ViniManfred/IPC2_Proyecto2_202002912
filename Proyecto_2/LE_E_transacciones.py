from E_transacciones import E_Transacciones

class Lista_E_T:
    def __init__(self) -> None:
        self.raiz = E_Transacciones()
        self.ultimo = E_Transacciones()

    
    def append(self, nuevaT):
        if self.raiz.id is None:
            self.raiz = nuevaT
            self.ultimo = nuevaT
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaT
            self.ultimo = nuevaT
        else:
            self.ultimo.siguiente = nuevaT
            self.ultimo = nuevaT