# Escreva um programa que converte uma temperatura em Celsius para Fahrenheit ou vice-versa, dependendo da escolha do usuário.

def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Solicitar a escolha do usuário
print("Escolha a opção de conversão:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")

opcao = int(input("Digite o número da opção desejada: "))

if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius} graus Celsius equivalem a {fahrenheit:.2f} graus Fahrenheit.")
elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit} graus Fahrenheit equivalem a {celsius:.2f} graus Celsius.")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
