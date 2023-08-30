# 9. Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começam com a letra 'A'.

nomes = input("Digite os nomes separados por vírgula: ").split(',')
nomes_com_a = [nome.strip() for nome in nomes if nome.strip().lower().startswith('a')]
print("Nomes que começam com 'A':")
print("\n".join(nomes_com_a))