# 2. Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:
    def __init__(self, titulo, autor, info):
        self.tilulo = titulo
        self.autor = autor
        self.info = info
    def detalhes(self):
        print(f"Autor: {self.autor}\nTítulo: {self.tilulo}\nInfo: {self.info}")

titulo = (input("Insira o título do livro: "))
autor = input("Insira o autor do livro: ")
info = input("Insira uma descrição do livro: ")

livro = Livro(titulo, autor, info)
livro.detalhes()