class Cola:
    def __init__(self,counter=0, dpi = None, nombre = None, tiempo_atencion = 0, tiempo_espera=0) -> None:
        self.counter = counter
        self.dpi = dpi
        self.nombre = nombre
        self.tiempo_atencion = tiempo_atencion
        self.tiempo_espera = tiempo_espera
        self.siguiente = None