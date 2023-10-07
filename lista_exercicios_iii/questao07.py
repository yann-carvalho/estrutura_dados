# Crie uma função que calcula o índice de massa corporal (IMC) de uma pessoa com base em sua altura e peso.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)


# Exemplo de uso:
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = calcular_imc(peso, altura)
print(f"O IMC é: {imc:.2f}")
