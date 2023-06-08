import unittest
from AutoNuevo import Nuevo
from AutoUsado import Usado
from ListaVehiculo import Lista
from ObjectEncoder import ObjectEncoder
from test import TestAutos
if __name__=="__main__":
    jsonF = ObjectEncoder()
    LV = Lista()
    while 1 != 0:
        print("1: Cargar un Vehiculo en un posicion")
        print("2: Insertar un Auto")
        print("3: Mostrar de que clase es el objecto que se encuentra en una posicion dada")
        print("4: Modificar el precio base de un Auto")
        print("5: Mostrar Todos los Datos")
        print("6: Mostrar los Vehiculo")
        print("7: Almecenar los vehiculos de la lista en un archivo JSON")
        print("8: Salir")
        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            print("¿El auto es usado o no?")
            print("1: SI      2: NO")
            num = int(input())
            if num == 1:
                print("----Carga de Auto Usado----")
                modelo = input("Ingrese el modelo del auto: ")
                puertas = int(input("Ingrese la cantidad de puertas del auto: "))
                color = input("Ingrese el color del auto: ")
                precio = float(input("Ingrese el precio del auto: "))
                marca = input("Ingrese la marca del auto: ")
                patente = input("Ingrese la patente del auto: ")
                anio = int(input("Ingrese el año del auto: "))
                kilometros = int(input("Ingrese los kilometros que tiene el auto: "))
                unAuto = Usado(modelo, puertas, color, precio, marca, patente, anio, kilometros)
                posicion = input("Ingrese la posicion donde lo desea agregar: ")
                LV.agregarElemento(unAuto)
            elif num == 2:
                print("----Carga de Auto Nuevo----")
                modelo = input("Ingrese el modelo del auto: ")
                puertas = int(input("Ingrese la cantidad de puertas del auto: "))
                color = input("Ingrese el color del auto: ")
                precio = int(input("Ingrese el precio del auto: "))
                version = input("Ingrese el tipo de version del auto: BASE o FULL: ")
                unAuto = Nuevo(modelo, puertas, color, precio, version)
                posicion = input("Ingrese la posicion donde lo desea agregar: ")
                LV.agregarElemento(unAuto)
        elif opcion == 2:
            print("¿El auto es usado o no?")
            print("1: SI      2: NO")
            num = int(input())
            if num == 1:
                print("----Carga de Auto Usado----")
                modelo = input("Ingrese el modelo del auto: ")
                puertas = int(input("Ingrese la cantidad de puertas del auto: "))
                color = input("Ingrese el color del auto: ")
                precio = float(input("Ingrese el precio del auto: "))
                marca = input("Ingrese la marca del auto: ")
                patente = input("Ingrese la patente del auto: ")
                anio = int(input("Ingrese el año del auto: "))
                kilometros = int(input("Ingrese los kilometros que tiene el auto: "))
                unAuto = Usado(modelo, puertas, color, precio, marca, patente, anio, kilometros)
                posicion = input("Ingrese la posicion donde lo desea agregar: ")
                LV.agregarElemento(unAuto)
            elif num == 2:
                print("----Carga de Auto Nuevo----")
                modelo = input("Ingrese el modelo del auto: ")
                puertas = int(input("Ingrese la cantidad de puertas del auto: "))
                color = input("Ingrese el color del auto: ")
                precio = int(input("Ingrese el precio del auto: "))
                version = input("Ingrese el tipo de version del auto: BASE o FULL: ")
                unAuto = Nuevo(modelo, puertas, color, precio, version)
                posicion = input("Ingrese la posicion donde lo desea agregar: ")
                LV.agregarElemento(unAuto)
        elif opcion == 3:
            posicion = int(input("Ingrese la posicion a buscar: "))
            posicion = posicion -1
            LV.buscarPosicion(posicion)
        elif opcion == 4:
            pat = input("Ingrese la patente del auto a modificar Precio Base: ")
            LV.buscarPatente(pat)
        elif opcion == 5:
            LV.autoEconomico()
        elif opcion == 6: 
            LV.mostrarInfo()
        elif opcion == 7:
            d=LV.toJSON()
            jsonF.guardarJSONArchivo(d,'autos.json')
            diccionario=jsonF.leerJSONArchivo('autos.json')
            autos=jsonF.decodificarDiccionario(diccionario, LV)
        elif opcion == 8:
            exit()
        elif opcion == 9:
            suite = unittest.TestLoader().loadTestsFromTestCase(TestAutos)
            unittest.TextTestRunner(verbosity=2).run(suite)