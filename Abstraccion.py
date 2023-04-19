#Crhistropher Isram Mancilla Laure
#Abstraccion

#tenemos que importar la clase base abstracta y el decorador para el método abstracto 
from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return self.lado * 4

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio * self.radio
    
    def perimetro(self):
        return 2 * 3.1416 * self.radio
    
c1 = Cuadrado(5)

print("El area es: ", c1.area())
print("El perimetro es: ", c1.perimetro())

c2 = Circulo(5)

print("El area es: ", c2.area())
print("El perimetro es: ", c2.perimetro())