#Solicito el numero de Inicio
inicio = int(input("Ingrese El Numero de Inicio: "))

#Solicito el numero Final
final = int(input("Ingrese El Numero Final: "))

#lista que guardara los numeros impares
impares = []

#valido que el numero final no sea menor que el numero de inicio 
if final > inicio:
    for numero in range(inicio+1, final):
        if numero % 2 != 0:
            impares.append(numero)
else:
    print("el Numero Inicial debe ser Menor al Numero Final")
    
if len(impares) == 0:
    print("No existen Numeros Impares en el Rango Indicado")
else:
    print(f"Los Numero impares encontrados son: {impares}")