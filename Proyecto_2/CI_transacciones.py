class CI_Transacciones:
    def __init__(self, idTransaccion = 0, cantidad = 0) -> None:
        self.idTransaccion = idTransaccion
        self.cantidad = cantidad
        self.siguiente = None