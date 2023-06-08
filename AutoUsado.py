from Autos import Auto

class Usado(Auto):
    __marca: str
    __patente:str
    __anio: str
    __kilometros: int

    def __init__(self, modelo, puertas, color, precio, marca, patente, anio, kilometros):
        super().__init__(modelo, puertas, color, precio)
        self.__marca = marca
        self.__patente = patente
        self.__anio =anio
        self.__kilometros = kilometros

    def getMarca(self):
        return self.__marca
    
    def getPatente(self):
        return self.__patente
    
    def getAño(self):
        return self.__anio
    
    def getKilometros(self):
        return self.__kilometros

    def PrecioVenta(self):
        a = super().getPrecio()
        b = 2023 - self.getAño()
        precioVenta = a-(b*a/100)
        if self.getKilometros() > 100000:
            precioVenta = precioVenta-(2*precioVenta/100)
        return precioVenta

    def __str__(self):
        super().__str__()
        cadena = f"Marca: {self.__marca}, Patente: {self.__patente}, Año: {self.__anio}, Kilometros: {self.__kilometros}"+"\n"
        cadena += f"Precio Venta: {self.PrecioVenta()}"
        return cadena