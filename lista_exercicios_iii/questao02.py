# Escreva uma função que calcula o fatorial de um número inteiro positivo fornecido pelo usuário.

def calcular_fatorial(n):
    if n < 0:
        return "O fatorial não está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, n + 1):
            fatorial *= i
        return fatorial


# Solicitar um número inteiro positivo ao usuário
num = int(input("Digite um número inteiro positivo para calcular o fatorial: "))

# Calcular o fatorial
resultado = calcular_fatorial(num)

# Exibir o resultado
print(f"O fatorial de {num} é {resultado}")
