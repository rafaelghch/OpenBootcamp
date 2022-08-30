class vehiculo:
    color = "Negro"
    ruedas = 4
    puertas = 5
    
    def getColor(self):
        print("Color: ", self.color)
        
    def getRuedas(self):
        print("Ruedas: ", self.ruedas)
        
    def getPuertas(self):
        print("Puertas: ", self.puertas)        
        
    def setColor(self, c):
        self.color = c
        
    def setRuedas(self, r):
        self.ruedas = r
        
    def setPuertas(self, p):
        self.puertas = p
    
class coche(vehiculo):
    velocidad = 100
    cilindrada = 4
    
    def getVelocidad(self):
        print("Velocidad: ", self.velocidad)
        
    def getCilindrada(self):
        print("Cilindrada: ", self.cilindrada)
        
    def setVelocidad(self, v):
        self.velocidad = v
        
    def setCilindrada(self, c):
        self.cilindrada = c      

variable = coche()
variable.getPuertas()
variable.getRuedas()
variable.getColor()
variable.getVelocidad()
variable.getCilindrada()