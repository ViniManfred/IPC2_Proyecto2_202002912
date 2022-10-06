class E_Transacciones:
    def __init__(self,counter=0, id = None, nombre = None, tiempoA=None) -> None:
        self.counter=counter
        self.id = id
        self.nombre = nombre
        self.tiempoA =tiempoA
        self.siguiente = None