class E_Transacciones:
    def __init__(self, id = None, nombre = None, tiempoA=None) -> None:
        self.id = id
        self.nombre = nombre
        self.tiempoA =tiempoA
        self.siguiente = None