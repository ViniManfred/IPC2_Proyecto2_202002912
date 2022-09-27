from LE_E_escritorios import Escritorios
class Puntos_Atencion:
    def __init__(self, id = 0, nombre = None, direccion = None) -> None:
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.E_escritorios = Escritorios()
        self.siguiente = None