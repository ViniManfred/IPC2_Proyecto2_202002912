from LE_clientes_escritorio import Lista_Clientes_escritorio



class Escritorios:
    def __init__(self,counter=0, id = None, identificacion = None, encargado = None, estado=None) -> None:
        self.counter = counter
        self.id = id
        self.identificacion = identificacion
        self.encargado = encargado
        self.estado = estado
        self.clientes_escritorio = Lista_Clientes_escritorio()
        self.siguiente = None