# 10. Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do computador e determinar o vencedor.

import random

print("Bem-vindo ao Pedra, Papel e Tesoura!")
print("Escolha: pedra, papel ou tesoura")
player_choice = input().lower()

computer_choices = ["pedra", "papel", "tesoura"]
computer_choice = random.choice(computer_choices)

print(f"Computador escolheu: {computer_choice}")

if player_choice == computer_choice:
    print("Empate!")
elif (player_choice == "pedra" and computer_choice == "tesoura") or \
     (player_choice == "papel" and computer_choice == "pedra") or \
     (player_choice == "tesoura" and computer_choice == "papel"):
    print("Você venceu!")
elif (player_choice != computer_choices):
    print('Opção inválida!')
else:
    print("O computador venceu!")
