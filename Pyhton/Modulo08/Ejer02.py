import pickle

#Clase Basica Vehiculo
class Vehiculo:
    modelo = None
    placa  = None
    ruedas = None
    color  = None

    def __init__(self,modelo,placa,ruedas,color):
        self.modelo = modelo
        self.placa  = placa
        self.ruedas = ruedas
        self.color  = color

    def getModelo(self):
        return self.modelo

    def getPlaca(self):
        return self.placa

    def getRuedas(self):
        return self.ruedas

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def setPlaca(self, placa):
        self.placa = placa

    def setRuedas(self, ruedas):
        self.ruedas = ruedas

    def setColor(self, color):
        self.color = color

#Creamos el Objeto
objVehiculo = Vehiculo("2022","123DFG",4,"Negro")

nombre = "prueba.bin"

print("** CREACION DE ARCHIVO BINARIO**")

#Validacion para saber si el archivo existe o no
try:
    #Abrimos el Archivo si existe
    archivo = open(nombre, 'ab')
except FileNotFoundError:
    #En el caso de no existir o creamos
    archivo = open(nombre, 'xb')

#Escribimos en el Archivo Binario
pickle.dump(objVehiculo, archivo)
#Cerramos el Archivo
archivo.close()

print("\n** LECTURA DE ARCHIVO ** ")

#Abrimos el Archivo binario en Modo solo Lectura
archivo = open(nombre, 'rb')
#Guardamos el contenido del Archivo Binario
contenido = pickle.load(archivo)
#Cerramos el Archivo
archivo.close()

#Mostramos en Pantalla el contenido del Archivo Binario
print("Info del Vehiculo Contenido en el Archivo Binario")
print(f'Modelo: {contenido.getModelo()}')
print(f'Placa: {contenido.getPlaca()}')
print(f'Cantidad de Ruedas: {contenido.getRuedas()}')
print(f'Color: {contenido.getColor()}')