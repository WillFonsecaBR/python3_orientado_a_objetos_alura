

class conta:
    def __init__(self, numero, titular, saldo, limite) -> None:
        print("construindo um objeto ....{}".format(self))
        self.numuro = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Valor R${} Titular{}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor
        print("o valor R${} foi depositado com sucesso!".format(valor))

    def saca(self, valor):
        self.saldo -= valor()
        print("o valor R${} foi sacado com sucesso!".format(valor))


if __name__ == "__main__":
    conta1 = conta(322, "Willian Alves Fonseca", 250.00, 2000.00)
    conta2 = conta(222, "Willian Alves Fonseca", 5000.00, 10000.00)
