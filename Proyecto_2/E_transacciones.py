class E_Transacciones:
    def __init__(self, id = 0, nombre = None, tiempoA=0) -> None:
        self.id = id
        self.nombre = nombre
        self.tiempoA =tiempoA
        self.siguiente = None