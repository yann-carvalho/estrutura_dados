# 7. Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.

def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


valor_limite = int(
    input("Digite um valor limite para a sequência de Fibonacci: "))

if valor_limite < 0:
    print("Insira um valor não negativo.")
else:
    sequencia = fibonacci(valor_limite)
    print("Sequência de Fibonacci até", valor_limite, ":")
    print(sequencia)
