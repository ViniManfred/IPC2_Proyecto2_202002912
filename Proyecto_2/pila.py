from LE_clientes_escritorio_pila import Lista_Clientes_escritorio_pila
class Pila:
    def __init__(self,counter=0, id = None, identificacion = None, encargado = None, estado=None) -> None:
        self.counter = counter
        self.id = id
        self.identificacion = identificacion
        self.encargado = encargado
        self.estado = estado
        self.clientes_escritorio_pila = Lista_Clientes_escritorio_pila()
        self.siguiente = None