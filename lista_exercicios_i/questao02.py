# 2. Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.

num = float(input('Insira um número e o programa irá informar se é par ou ímpar: '))

if num % 2 == 0:
    print('O número informado é par!')
else:
    print('O número informado é ímpar!')