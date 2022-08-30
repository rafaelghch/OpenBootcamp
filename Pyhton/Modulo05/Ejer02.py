def NumeroPrimo(n):
    for i in range(2,n):
        if (n%i) == 0:
            return "El numero no Es Primo"
    return "El Numero es Primo"

numero = int(input("ingrese un Numero: "))

print(NumeroPrimo(numero))