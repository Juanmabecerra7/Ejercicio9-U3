from Autos import Auto

class Nuevo(Auto):
    __version: str

    def __init__(self, modelo, puertas, color, precio, version):
        super().__init__(modelo, puertas, color, precio)
        self.__version = version

    def getVersion(self):
        return self.__version
    
    def PrecioVenta(self):
        a = super().getPrecio()
        precioVenta = a+(10*a/100)
        if "FULL" in self.getVersion():
            precioVenta = precioVenta+(2*precioVenta/100)
        return precioVenta

    def __str__(self):
        super().__str__()
        cadena = f"Version: {self.__version}"+"\n"+f"Precio Venta: {self.PrecioVenta()}"
        return cadena