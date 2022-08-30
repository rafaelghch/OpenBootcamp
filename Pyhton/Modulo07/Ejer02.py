from datetime import datetime, timedelta

#guardamos la hora actual del sistema
hora_actual = datetime.now()
#creamos un variable time que indique la hora de salida, es decir, las 7 horas
hora_salida = datetime(hora_actual.year, hora_actual.month, hora_actual.day, 7, 0)

#Comparamos ambas horas
if hora_actual > hora_salida:
    #si la hora actual es mayor a las 7 horas de trabajo, se imprime el mensaje de descansar
    print ("Hora de Descansar")
else:
    # en caso contrario calculamos la diferencia entre ambas horas para indicarle al usuario
    resultado = hora_salida - hora_actual
    print("Restan: ", resultado)