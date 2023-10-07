# Escreva um programa que recebe uma string e conta a quantidade de vogais (a, e, i, o, u) presentes nela.

def contar_vogais(frase):
    vogais = 'aeiouAEIOU'
    quantidade = 0
    for letra in frase:
        if letra in vogais:
            quantidade += 1
    return quantidade


# Solicitar uma string ao usuário
frase = input("Digite uma frase: ")

# Chamar a função para contar vogais
quantidade_vogais = contar_vogais(frase)

# Exibir o resultado
print(f"A quantidade de vogais na frase é: {quantidade_vogais}")
