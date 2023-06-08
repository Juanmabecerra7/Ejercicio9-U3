import unittest
from Autos import Auto
from AutoNuevo import Nuevo
from AutoUsado import Usado
from ListaVehiculo import Lista

class TestAutos(unittest.TestCase):
    def setUp(self):
        self.__lista_vehiculos = Lista()
        self.__vehiculo1 = Nuevo("NISSAN", 3, "BLANCO" , 113000, "FULL")
        self.__vehiculo2 = Usado("TOYOTA", 3, "NEGRO", 65000, "SUPRA", "ASK-900", 2017, 87000)

    def test_agregar_vehiculo(self):
        self.__lista_vehiculos.agregarElemento(self.__vehiculo1)
        print(self.__lista_vehiculos.mostrar(0))
        self.assertEqual(self.__lista_vehiculos.mostrar(1)==(self.__vehiculo1))

    def test_insertar_vehiculo(self):
       self.__lista_vehiculos.agregarElemento(self.__vehiculo1)
       self.__lista_vehiculos.insertarElemento(1, self.__vehiculo2)
       self.assertEqual(self.__lista_vehiculos.mostrarInfo(0), self.__vehiculo2)

    def test_obtener_vehiculo(self):
        self.__lista_vehiculos.agregarElemento(self.__vehiculo1)
        vehiculo_obtenido = self.__lista_vehiculos.mostrarInfo(0)
        self.assertEqual(vehiculo_obtenido, self.__vehiculo1)

    def test_modificar_precio_base(self):
        self.__lista_vehiculos.mostrarInfo(self.__vehiculo1)
        nuevo_precio = 12000
        self.__vehiculo1.modificarPrecioBase(nuevo_precio)
        self.assertEqual(self.__vehiculo1.getPrecio(), nuevo_precio)