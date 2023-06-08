import json
from pathlib import Path
class Auto(object):
    __modelo: str
    __puertas: int
    __color: str
    __precio: int

    def __init__(self, modelo, puertas, color, precio):
        self.__modelo = modelo
        self.__puertas = puertas
        self.__color = color
        self.__precio = precio

    def getPrecio(self):
        return self.__precio

    def __str__(self):
        cadena = f"Modelo: {self.__modelo}, Puertas: {self.__puertas}, Color: {self.__color}, Precio: {self.__precio}"
        print(cadena)

    def getPatente(self):
        pass

    def PrecioVenta(self):
        pass

    def modificarPrecioBase(self):
        nuevo_precio = int(input("Ingrese el nuevo precio: "))
        self.__precio = nuevo_precio

    def getInfo(self):
        print(f"MODELO: {self.__modelo}")
        print(f"PUERTAS: {self.__puertas}")
        print(f"PRECIO DE VENTA: {self.PrecioVenta()}")
    
    def toJSON(self):
        if self.__class__.__name__ == 'Usado':
            d = dict(
                __class__ = self.__class__.__name__,
                __atributos__ = dict(
                    modelo = self.__modelo,
                    puertas = self.__puertas,
                    color = self.__color,
                    precio = self.__precio,
                    patente = self.getPatente(),
                    kilometros = self.getKilometros(),
                    anioo = self.getAño()
                )   
            )
        else:
            d = dict(
                __class__ = self.__class__.__name__,
                __atributos__ = dict(
                    modelo = self.__modelo,
                    puertas = self.__puertas,
                    color = self.__color,
                    precio = self.__precio,
                    version = self.getVersion()
                )   
            )
        return d