from LE_E_escritorios import Lista_E
from LE_clientes import Lista_C
from LE_cola import Lista_Cola
from LE_pila import Lista_Pila
class Puntos_Atencion:
    def __init__(self,counter=0, id = None, nombre = None, direccion = None) -> None:
        self.counter = counter
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.E_escritorios = Lista_E()
        self.pila= Lista_Pila()
        self.clientes = Lista_C()
        self.cola = Lista_Cola()
        self.siguiente = None