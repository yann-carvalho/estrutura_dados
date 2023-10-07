# Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado
# “calcular_media” que retorna a média das notas do aluno.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


# Exemplo de uso:
aluno1 = Aluno("João", [8, 9, 7, 10])
media_aluno1 = aluno1.calcular_media()
print(f"A média de {aluno1.nome} é {media_aluno1:.2f}")
