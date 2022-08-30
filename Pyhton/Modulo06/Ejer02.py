class Alumno:
    nombre = ""
    nota = 0
    
    def __init__(self):
        self.nombre = ""
        self.nota = 0
    
    def getNombre(self):
        print("Nombre: ", self.nombre)
        
    def getNota(self):
        print("Nota: ", self.nota)
        
    def setNombre(self, n):
        self.nombre = n
        
    def setNota(self, n):
        self.nota = n
        
    def getAprobo(self):
        if self.nota > 9:
            return "Aprobo"
        else:
            return "No Aprobo"
        
variable = Alumno()
variable.setNombre("Rafael Hernandez")
variable.setNota(11)
variable.getNombre()
variable.getNota()
print(variable.getAprobo())
variable.setNombre("Guillermo Hernandez")
variable.setNota(9)
variable.getNombre()
variable.getNota()
print(variable.getAprobo())