# Clase Vehiculo
class Vehiculo:
    def __init__(self,velocidad,capacidad,color) -> None:
        self.velocidad = velocidad
        self.color = color
        self.capacidad = capacidad

    def __str__(self) -> str:
         return 'Velocidad: '+ str(self.velocidad) +  ' Capacidad: ' + str(self.capacidad) + ' Color: ' + str(self.color) 
    
    def Circular(self):
        """
        Metodo circular de Vehiculos
        """
        print('Circulando...')

vehiculo = Vehiculo(120,4,"Verde")
print(vehiculo)

# Clase Animal
class Animal():
    def __init__(self,peso,tipo) -> None:
        self.peso = peso
        self.tipo = tipo

    def __str__(self) -> str:
        return "Peso: " + str(self.peso) + " Tipo: " + str(self.tipo)
    
animal = Animal(50,"perro")
print(animal)    
