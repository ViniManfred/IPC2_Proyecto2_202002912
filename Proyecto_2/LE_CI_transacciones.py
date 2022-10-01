from CI_transacciones import CI_Transacciones

class Lista_CI_T:
    def __init__(self) -> None:
        self.raiz = CI_Transacciones()
        self.ultimo = CI_Transacciones()

    
    def append(self, nuevaTI):
        if self.raiz.idTransaccion is None:
            self.raiz = nuevaTI
            self.ultimo = nuevaTI
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaTI
            self.ultimo = nuevaTI
        else:
            self.ultimo.siguiente = nuevaTI
            self.ultimo = nuevaTI