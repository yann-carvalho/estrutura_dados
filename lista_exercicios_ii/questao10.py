# Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um
# método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário
# do funcionário.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual):
        self.salario += (self.salario * percentual / 100)


# Exemplo de uso:
funcionario1 = Funcionario("João", 3000, "Analista")
print(f"Salário antes do aumento: R${funcionario1.salario:.2f}")
funcionario1.aumentar_salario(10)  # Aumento de 10%
print(f"Salário após o aumento: R${funcionario1.salario:.2f}")
