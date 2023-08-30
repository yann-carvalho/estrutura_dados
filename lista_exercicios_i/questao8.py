# 8. Faça um programa que determine se um número é primo ou não.

numero = int(input("Digite um número: "))

if numero <= 1:
    primo = False
else:
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break

if primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")