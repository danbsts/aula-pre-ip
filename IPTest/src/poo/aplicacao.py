class Aplicacao:

    def __init__(self, saldo):
        self.saldo = saldo

    def criarAplicacao(self, conta):
        self.saldo = conta.getSaldo() * 1.05
        return self.saldo