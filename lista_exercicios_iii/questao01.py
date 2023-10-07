# Escreva um programa que recebe cinco notas de um aluno e calcula a média. Em seguida, exiba se o
# aluno foi aprovado (média maior ou igual a 7) ou reprovado (média menor que 7).

def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


# Receber as cinco notas do aluno
notas = []
for i in range(5):
    nota = float(input(f"Informe a nota {i + 1}: "))
    notas.append(nota)

# Calcular a média
media = calcular_media(notas)

# Verificar se o aluno foi aprovado ou reprovado
status = verificar_aprovacao(media)

# Exibir o resultado
print(f"A média do aluno é {media:.2f}")
print(f"O aluno está {status}")
