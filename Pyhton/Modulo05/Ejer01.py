AreaTriangulo = lambda b=0, a=0: (b*a)/2

AreaCirculo = lambda r=0: 3.14 * r**2
    
base = int(input("ingrese la Base del triangulo: "))
altura = int(input("ingrese la Altura del triangulo: "))

resultado = AreaTriangulo(base,altura)
print(f"El Area del Trianglo es igual a {resultado}")

radio = float(input("ingrese el Radio del Circulo: "))

resultado = AreaCirculo(radio)
print(f"El Area del Circulo es igual a {resultado}")