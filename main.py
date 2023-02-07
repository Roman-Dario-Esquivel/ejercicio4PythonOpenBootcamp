"""def determina_anio(dias):
    if dias==366:
        print("Es año biciesto")
    else:
        print("No es año biciesto")
    
    
determina_anio(int(input("ingrese cantidad de dias que tiene el año:")))"""
"""class Vehiculo:
    Color = None
    Ruedas = None
    Puertas = None
    def __init__(self,color,ruedas,puertas):
        self.Color = color
        self.Ruedas = ruedas
        self.Puertas = puertas
        
class Coche(Vehiculo):
    Velocidad = None
    Cilindrada = None
    def __init__(self,color,ruedas,puertas,velocidad,cilindrada):
        Coche.Color = color
        Coche.Ruedas = ruedas
        Coche.Puertas = puertas
        Coche.Velocidad = velocidad
        Coche.Cilindrada = cilindrada
    def mostrar(self):
        print("El color de coche es ",Coche.Color," la cantidad de ruedas que tiene es ", Coche.Ruedas," la cantidad de puertas que tiene es ",Coche.Ruedas, " la Velocidad es ",Coche.Velocidad," las cilindrada es ",Coche.Cilindrada)
        
        

        

movil = Coche("azul",4,5,120,12)
movil.mostrar()"""

class alumno:
    Nombre = None
    Nota = None
    
    def set_Nombre(self,nombre):
        alumno.Nombre = nombre
        
    def set_Nota(self, nota):
        alumno.Nota = nota
    
    def get_Nombre(self):
        return alumno.Nombre
    
    def get_Nota(self):
        return alumno.get_Nota
    
    def mostrarNombre(self):
        print("El nombre del alumno es: ",alumno.Nombre)
    
    def mostrarNota(self):
        print("la nota del alumno es : ",alumno.Nota)
     
    def condicionAlumno(self):
        if(alumno.Nota>=6):
            print("El alumno aprobo con: ",alumno.Nota)
        else :
            print("El alumno desaprobo con: ",alumno.Nota)
    
    
alu = alumno()
alu.set_Nombre(input("Ingrese el Nombre del alumno: "))
alu.mostrarNombre()
alu.set_Nota(int(input("Ingrese la nota del alumno: ")))
alu.mostrarNota
alu.condicionAlumno()
    