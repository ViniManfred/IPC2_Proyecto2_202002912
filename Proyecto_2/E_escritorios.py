class Escritorios:
    def __init__(self, id = 0, identificacion = None, encargado = None) -> None:
        self.id = id
        self.identificacion = identificacion
        self.encargado = encargado
        self.siguiente = None