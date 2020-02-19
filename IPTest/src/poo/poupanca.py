from poo.conta import Conta


class Poupanca(Conta):
    taxaSaque = 5.50

    def __init__(self, terminacao, rendimento, nome, idade, saldo, limite):
        super().__init__(nome, idade, saldo, limite)
        self.terminacao = terminacao
        self.rendimento = rendimento

    def sacar(self, quantia):
        saqueConta = super()
        if saqueConta == 0:
            return 0
        self.__saldo -= (quantia + Poupanca.taxaSaque)
        return quantia

    # same as toString()
    def __str__(self):
        pass
