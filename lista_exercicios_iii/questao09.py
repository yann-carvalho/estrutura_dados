# Crie uma calculadora que realiza operações de adição, subtração, multiplicação e divisão, com base na escolha do usuário.

def adicao(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"


# Solicitar operação ao usuário
print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = int(input("Digite o número da operação desejada: "))

# Solicitar números para operação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Executar a operação escolhida
if opcao == 1:
    resultado = adicao(num1, num2)
    operacao = "+"
elif opcao == 2:
    resultado = subtracao(num1, num2)
    operacao = "-"
elif opcao == 3:
    resultado = multiplicacao(num1, num2)
    operacao = "*"
elif opcao == 4:
    resultado = divisao(num1, num2)
    operacao = "/"

# Exibir o resultado
print(f"O resultado de {num1} {operacao} {num2} é {resultado}")
