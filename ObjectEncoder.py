import json
from pathlib import Path
from ListaVehiculo import Lista
from AutoNuevo import Nuevo
from AutoUsado import Usado

class ObjectEncoder(object):
    def decodificarDiccionario(self, d, LV):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_ = eval(class_name)
            if class_name=='Lista':
                autos=d['autos']
                dAuto = autos[0]
                Lista = class_()
                for i in range(len(autos)):
                    dAuto=autos[i]
                    class_name=dAuto.pop('__class__')
                    class_=eval(class_name)
                    atributos=dAuto['__atributos__']
                    unAuto=class_(**atributos)
                    LV.agregarElemento(unAuto)
                return Lista
    
    
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
            print ('Se guardó el archivo correctamente')

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)