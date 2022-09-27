from LE_puntos_atencion import Lista_PA
from LE_E_transacciones import Lista_E_T
class Empresas:
    def __init__(self, id = 0, nombre = None, abreviatura = None) -> None:
        self.id = id
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.escritorios = Lista_PA()
        self.clientes = Lista_E_T()
        self.siguiente = None
        