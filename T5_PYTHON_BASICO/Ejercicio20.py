class Estudiante:
    nombre = ""
    edad = 0
    promedio = 0.0
    
    #Constructor
    def __init__(self,nombre,edad,promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio
    
    def infoEstudiante(self):
        aprobado = "SI"
        if self.promedio <7: aprobado = "NO"
        else: aprobado = "SI"
        
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nPromedio: {self.promedio}\nAprobado: {aprobado}\n")
    
estudiante = Estudiante("Manuel", 25, 6.5)
estudiante2 = Estudiante("Vicente", 31, 7.8)
estudiante.infoEstudiante()
estudiante2.infoEstudiante()