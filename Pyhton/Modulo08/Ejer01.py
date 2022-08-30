nombre = "prueba.txt"

print("** CREACION DE ARCHIVO **")


#Validacion para saber si el archivo existe o no
try:
    #Abrimos el Archivo si existe
    archivo = open(nombre, 'a')
except FileNotFoundError:
    #En el caso de no existir lo creamos
    archivo = open(nombre, 'x')

#Escribimos en el Archivo
archivo.write('Hola Mundo!!!!!\n')
#Cerramos el Archivo
archivo.close()

print("\n** LECTURA DE ARCHIVO ** ")

#Abrimos el Archivo solo Lectura
archivo = open(nombre, 'r')
#Guardamos el contenido del Archivo
contenido = archivo.readlines()
#Impimimos en Pantalla el Contenido
for linea in contenido:
    print(linea)
#Cerramos el Archivo
archivo.close()