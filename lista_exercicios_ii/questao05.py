# Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método
# chamado “falar” que imprime uma mensagem com o nome da pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"{self.nome} está falando.")


# Exemplo de uso:
pessoa1 = Pessoa("João", 30)
pessoa1.falar()  # Isso imprimirá "João está falando."
