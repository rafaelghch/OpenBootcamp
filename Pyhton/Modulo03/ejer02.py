#Ejercicio para calcular la índice de masa corporal

#solicito el Peso
peso = float(input("Ingrese su Peso(kg): "))
#solicito la Altura
altura = float(input("Ingrese su Altura(m): "))

#Calculamos IMC indicando 2 decimales
MasaCorporal = round(peso / (altura ** 2), 2)

#Se imprime el resultado
print(f"Su indice de Masa Corporal es: {MasaCorporal} ")