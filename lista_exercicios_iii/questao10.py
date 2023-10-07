# Escreva uma função que gera a sequência de Fibonacci até um determinado número de termos especificado pelo usuário.

def gerar_fibonacci(num_termos):
    fibonacci = [0, 1]

    while len(fibonacci) < num_termos:
        novo_termo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(novo_termo)

    return fibonacci[:num_termos]


# Solicitar o número de termos ao usuário
num_termos = int(input("Digite o número de termos para a sequência de Fibonacci: "))

# Chamar a função para gerar a sequência
sequencia_fibonacci = gerar_fibonacci(num_termos)

# Exibir a sequência
print(f"A sequência de Fibonacci com {num_termos} termos é: {sequencia_fibonacci}")
