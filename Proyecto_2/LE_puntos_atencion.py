from puntos_atencion import Puntos_Atencion

class Lista_PA:
    def __init__(self) -> None:
        self.raiz = Puntos_Atencion()
        self.ultimo = Puntos_Atencion()

    
    def append(self, nuevoPA):
        if self.raiz.id is None:
            self.raiz = nuevoPA
            self.ultimo = nuevoPA
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoPA
            self.ultimo = nuevoPA
        else:
            self.ultimo.siguiente = nuevoPA
            self.ultimo = nuevoPA