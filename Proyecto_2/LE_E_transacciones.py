from E_transacciones import E_Transacciones

class Lista_E_T:
    def __init__(self) -> None:
        self.raiz = E_Transacciones()
        self.ultimo = E_Transacciones()

    def append(self, nuevaT):
        if self.raiz.nombre is None:
            self.raiz = nuevaT
            self.ultimo = nuevaT
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaT
            self.ultimo = nuevaT
        else:
            self.ultimo.siguiente = nuevaT
            self.ultimo = nuevaT
    
    def print(self):
        nodoAux1 = self.raiz
        cadena1 = ''
        while True:
            if nodoAux1.nombre is not None:

                cadena1 += "ID: "+ nodoAux1.id + " Nombre: " + nodoAux1.nombre +" Tiempo: "+str(nodoAux1.tiempoA)
                if nodoAux1.siguiente is not None:
                    nodoAux1 = nodoAux1.siguiente
                    cadena1 += " \n"
                else:
                    break
            else:
                break
        return cadena1

    def busquedaID(self,id):
        nodoAux = self.raiz
        while nodoAux.id!= id:
            if nodoAux.siguiente is not None:
                nodoAux = nodoAux.siguiente
            else:
                return None
        return nodoAux.tiempoA

    def busquedaCounter(self,counter):
        nodoAux = self.raiz
        while nodoAux.counter!= counter:
            if nodoAux.siguiente is not None:
                nodoAux = nodoAux.siguiente
            else:
                return None
        return nodoAux.tiempoA

    def printer(self):
        nodoAux1 = self.raiz
        cadena1 = ''
        while True:
            if nodoAux1.nombre is not None:

                cadena1 +=" "+str(nodoAux1.counter)+". "+nodoAux1.nombre
                if nodoAux1.siguiente is not None:
                    nodoAux1 = nodoAux1.siguiente
                    cadena1 += " \n"
                else:
                    break
            else:
                break
        print(cadena1)
    