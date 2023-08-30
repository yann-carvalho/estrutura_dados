# 6. Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número.

numero = int(input("Insira um número e o programa calculará seu fatorial: ") )

resultado = 1
count = 1

resultado=1
for n in range(1,numero+1):
    resultado *= n

print(f'O fatorial do número inserido é {resultado}')