# Crie uma função que calcula o índice de massa corporal (IMC) de uma pessoa com base em sua altura e peso.
class IMC:

    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
    def imc(self):
        imc = self.peso/self.altura**2
        print(f"Seu IMC é {imc:.2f} kg/m²")
        return imc

imc = IMC(77.5, 1.70)
imc1 = imc.imc()