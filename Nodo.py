from Autos import Auto
class Nodo:
    __autos: Auto
    __siguiente: object

    def __init__(self, autos):
        self.__autos = autos
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__autos
    