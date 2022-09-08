from functools import reduce

#Solicimos la lista de numeros
numeros = input("Ingrese Lista de Numeros: ")

#guardamos los valores en una lista y validamos que sean enteros
listaInicial = list(map(int, numeros.split(',')))

#realizamos la suma de los numeros impares de la lista
resultado = reduce(lambda a, b: a + b, filter(lambda numero: numero % 2 != 0 , listaInicial))

print(resultado)