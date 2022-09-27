from CI_transacciones import CI_Transacciones

class Lista_CI_T:
    def __init__(self) -> None:
        self.raiz = CI_Transacciones()
        self.ultimo = CI_Transacciones()

    
    def append(self, nuevaT):
        if self.raiz.idTransaccion is None:
            self.raiz = nuevaT
            self.ultimo = nuevaT
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaT
            self.ultimo = nuevaT
        else:
            self.ultimo.siguiente = nuevaT
            self.ultimo = nuevaT