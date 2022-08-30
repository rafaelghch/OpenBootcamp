def AnnoBisiesto(a):
    if a % 4 == 0 and ( a % 100 != 0 or a % 400 ==0):
        return "Es Bisiesto"
    else:
        return "NO es Bisiesto"

anno = int(input("ingrese el Anno: "))

print(AnnoBisiesto(anno))