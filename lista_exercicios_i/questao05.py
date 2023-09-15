# 5. Faça um programa que leia uma lista de números e retorne a média dos números pares.

def calcular_media_numeros_pares(lista):
    numeros_pares = [num for num in lista if num % 2 == 0]

    if len(numeros_pares) == 0:
        return 0

    media = sum(numeros_pares) / len(numeros_pares)
    return media

numeros = []

n = int(input("Digite os número a serem inseridos na lista: "))
for _ in range(n):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

media_pares = calcular_media_numeros_pares(numeros)

print(f"A média dos números pares da lista é: {media_pares:.2f}")