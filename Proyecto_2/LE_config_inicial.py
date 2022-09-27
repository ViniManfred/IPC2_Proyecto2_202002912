from config_inicial import config_inicial

class Lista_CI:
    def __init__(self) -> None:
        self.raiz = config_inicial()
        self.ultimo = config_inicial()

    
    def append(self, nuevaCI):
        if self.raiz.id is None:
            self.raiz = nuevaCI
            self.ultimo = nuevaCI
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaCI
            self.ultimo = nuevaCI
        else:
            self.ultimo.siguiente = nuevaCI
            self.ultimo = nuevaCI