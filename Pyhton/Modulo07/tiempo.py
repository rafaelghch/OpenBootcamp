import datetime

def restar_hora(self,hora1,hora2):
        formato = "%H:%M:%S"
        h1 = datetime.strptime(hora1, formato)
        h2 = datetime.strptime(hora2, formato)
        resultado = h1 - h2
        return str(resultado)