class Escritorios:
    def __init__(self, id = None, identificacion = None, encargado = None, estado=None) -> None:
        self.id = id
        self.identificacion = identificacion
        self.encargado = encargado
        self.estado = estado
        self.siguiente = None