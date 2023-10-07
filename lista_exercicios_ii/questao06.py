# Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um
# método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade


# Exemplo de uso:
produto1 = Produto("Camiseta", 25.0, 3)
total_produto1 = produto1.calcular_total()
print(f"O total do produto {produto1.nome} é R${total_produto1:.2f}")
