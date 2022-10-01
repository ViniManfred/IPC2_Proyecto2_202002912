class CI_Transacciones:
    def __init__(self, idTransaccion = None, cantidad = None) -> None:
        self.idTransaccion = idTransaccion
        self.cantidad = cantidad
        self.siguiente = None