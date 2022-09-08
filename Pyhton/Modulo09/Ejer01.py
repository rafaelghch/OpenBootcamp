#Solicitamos la lista de paises
paises = input("Ingrese Lista de Paises(Separados por coma): ")

#convertimos el string en una lista, que no contenga elementos repetidos
#y ordenamos
listaPaises = sorted(list(set(paises.split(','))))

#mostramos por pantalla los elementos de la lista
print(','.join(listaPaises))