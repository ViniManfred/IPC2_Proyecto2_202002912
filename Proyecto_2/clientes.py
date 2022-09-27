from LE_CI_transacciones import Lista_CI_T
class Clientes:
    def __init__(self, dpi = 0, nombre = None) -> None:
        self.dpi = dpi
        self.nombre = nombre
        self.transacciones = Lista_CI_T()
        self.siguiente = None
        