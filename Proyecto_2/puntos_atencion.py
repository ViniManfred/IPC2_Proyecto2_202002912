from LE_E_escritorios import Lista_E
class Puntos_Atencion:
    def __init__(self,counter=0, id = None, nombre = None, direccion = None) -> None:
        self.counter = counter
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.E_escritorios = Lista_E()
        self.siguiente = None