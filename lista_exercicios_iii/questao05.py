# Crie uma função que verifica se um número é primo ou não.

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


# Exemplo de uso:
num = int(input("Digite um número inteiro para verificar se é primo: "))

if eh_primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
