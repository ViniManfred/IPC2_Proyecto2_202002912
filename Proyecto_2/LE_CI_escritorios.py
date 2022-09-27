from CI_escritorios import CI_Escritorios

class Lista_CI_E:
    def __init__(self) -> None:
        self.raiz = CI_Escritorios()
        self.ultimo = CI_Escritorios()

    
    def append(self, nuevoE):
        if self.raiz.idEscritorio is None:
            self.raiz = nuevoE
            self.ultimo = nuevoE
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoE
            self.ultimo = nuevoE
        else:
            self.ultimo.siguiente = nuevoE
            self.ultimo = nuevoE