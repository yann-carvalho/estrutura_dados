# Escreva um programa que converte uma temperatura em Celsius para Fahrenheit ou vice-versa, dependendo da escolha do usuário
class Temperatura:
    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit
    def conversao(self):
        self.fahrenheit = ((self.celsius * 1.8) + 32)
        print(f"A temperatura {self.celsius}°C é equivalente a {self.fahrenheit:.0f}°F")
        return self.fahrenheit

grau = Temperatura(25, 0)
grau = grau.conversao()