# Escreva um programa que recebe um número inteiro positivo e calcula a soma de seus dígitos.

def calcular_soma_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma


# Solicitar um número inteiro positivo ao usuário
num = int(input("Digite um número inteiro positivo: "))

# Verificar se o número é positivo
if num < 0:
    print("O número fornecido não é positivo.")
else:
    # Calcular a soma dos dígitos
    soma = calcular_soma_digitos(num)
    print(f"A soma dos dígitos de {num} é {soma}.")
