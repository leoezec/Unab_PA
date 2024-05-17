class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        """Devuelve la coordenada x del punto."""
        return self.x

    def eje_y(self):
        """Devuelve la coordenada y del punto."""
        return self.y

    def impresion(self):
        """Devuelve una representación en forma de string de las coordenadas del punto."""
        return f'({self.x}, {self.y})'

    def opuesto(self):
        """Devuelve el punto opuesto, con coordenadas negativas."""
        return Punto(-self.x, -self.y)

    def distancia_al_origen(self):
        """Devuelve la distancia del punto al origen (0,0)."""
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Ejemplo de uso
punto = Punto(3, 4)
print("Coordenada x:", punto.eje_x())  # Salida: Coordenada x: 3
print("Coordenada y:", punto.eje_y())  # Salida: Coordenada y: 4
print("Impresión:", punto.impresion())  # Salida: Impresión: (3, 4)
print("Opuesto:", punto.opuesto().impresion())  # Salida: Opuesto: (-3, -4)
print("Distancia al origen:", punto.distancia_al_origen())  # Salida: Distancia al origen: 5.0
