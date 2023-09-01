#1. Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado “calcular_area” que retorna a área do círculo.

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return math.pi * (self.raio**2)
area = Circulo(7)
print(f"A área do círculo é igual a {area.area():.2f} cm")