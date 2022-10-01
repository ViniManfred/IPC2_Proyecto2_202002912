from LE_puntos_atencion import Lista_PA
from LE_E_transacciones import Lista_E_T
class Empresas:
    def __init__(self,counter=0, id = None, nombre = None, abreviatura = None) -> None:
        self.counter = counter
        self.id = id
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.puntos_atencion = Lista_PA()
        self.E_transacciones = Lista_E_T()
        self.siguiente = None
        