from LE_CI_escritorios import Lista_CI_E
from LE_clientes import Lista_C
class config_inicial:
    def __init__(self, id = None, idEmpresa = None, idPunto = None) -> None:
        self.id = id
        self.idEmpesa = idEmpresa
        self.idPunto = idPunto
        self.CI_escritorios = Lista_CI_E()
        self.clientes = Lista_C()
        self.siguiente = None