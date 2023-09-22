#Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente métodos “depositar”
# e “sacar” para manipular o saldo.

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

conta = ContaBancaria("Yann Carvalho")

print(f"Saldo inicial da conta de {conta.titular}: R${conta.saldo:.2f}")

conta.depositar(1000)
print(f"Saldo após depósito: R$ {conta.saldo:.2f}")

conta.sacar(500)
print(f"Saldo após saque: R${conta.saldo:.2f}")

conta.sacar(700)