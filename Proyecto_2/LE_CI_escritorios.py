from CI_escritorios import CI_Escritorios

class Lista_CI_E:
    def __init__(self) -> None:
        self.raiz = CI_Escritorios()
        self.ultimo = CI_Escritorios()

    
    def append(self, nuevoEA):
        if self.raiz.idEscritorio is None:
            self.raiz = nuevoEA
            self.ultimo = nuevoEA
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoEA
            self.ultimo = nuevoEA
        else:
            self.ultimo.siguiente = nuevoEA
            self.ultimo = nuevoEA