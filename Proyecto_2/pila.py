class Pila:
    def __init__(self,counter=0, id = None, identificacion = None, encargado = None, estado=None) -> None:
        self.counter = counter
        self.id = id
        self.identificacion = identificacion
        self.encargado = encargado
        self.estado = estado
        self.siguiente = None