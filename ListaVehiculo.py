from Autos import Auto
from AutoUsado import Usado
from AutoNuevo import Nuevo
from Nodo import Nodo
from Coleccion import IColeccion

class Lista(IColeccion):
    __comienzo = Nodo
    __actual = Nodo
    __indice: int
    __top: int

    
    def __init__(self) -> None:
        self.__comienzo = None
        self.__actual = None
        self.__top = 0
        self.__indice = 0

    def __str__(self) -> str:
        for vehiculo in self:
            print (vehiculo)

    def __iter__ (self):
        return self

    def __next__ (self):
        if self.__indice == self.__top:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregarElemento(self, vehiculo):
        nodo = Nodo (vehiculo)
        nodo.setSiguiente (self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__top += 1

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            autos=[auto.toJSON() for auto in self]
            )
        return d
    
    def buscarPosicion(self, posicion):
        indice = 0
        aux = self.__comienzo
        print(self.__top)
        while indice < self.__top:
            if posicion == indice:
                print("Se encontro")
                if isinstance(aux.getDato(), Usado):
                    print("El objecto de esta posicion es un Auto Usado")
                elif isinstance(aux.getDato(), Nuevo):
                    print("El objecto que se encuentra en esta posicion es un Auto Nuevo")
                print(aux.getDato())
            aux = aux.getSiguiente()
            indice += 1

    def buscarPatente(self, patente):
        aux = self.__comienzo
        while aux != None:
            if aux.getDato().getPatente() == patente:
                print("Se encontro")
                aux.getDato().modificarPrecioBase()
                print("El precio de Venta ahora es de: ", aux.getDato().PrecioVenta())
            aux = aux.getSiguiente()

    def autoEconomico(self):
        min = 10000000000
        aux= self.__comienzo
        while aux != None:
            if min > aux.getDato().PrecioVenta():
                ant = aux
                min = aux.getDato().PrecioVenta()
            aux = aux.getSiguiente()
        print(ant.getDato())

    def mostrarInfo(self):
        aux = self.__comienzo
        while aux != None:
            aux.getDato().getInfo()
            aux = aux.getSiguiente()

    def mostrar(self):
        return self.__comienzo.getDato()