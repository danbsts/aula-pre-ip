class Conta:
    constante = 1

    def __init__(self, nome, idade, saldo, limite=1000):
        self.nome = nome
        self._idade = idade
        self.__saldo = saldo
        self.limite = 1000
        Conta.constante += 1

    def getSaldo(self):
        return self.__saldo

    # None here is == Null in Java
    # This is a comment
    def facaNada(self):
        pass

    def better_have_my_money(self, ammount):
        if self.__saldo >= ammount:
            self.__saldo -= ammount
            return self.__saldo
        else:
            print("b**** better have my money!!")

    def transferir(self, destino, quantia):
        if(self.__saldo - quantia >= 0):
            self.__saldo -= quantia
            return True
        else:
            return False

    # Can't access directly
    def getConstante(self):
        return self.constante

    @staticmethod # doesn't need the `self` reference
    def getConstanteStatic():
        return Conta.constante

    @classmethod
    def getConstanteClass(cls):
        return cls.constante

    def sacar(self, quantia):
        if (self.__saldo - quantia >= 0):
            self.saldo -= quantia
            return quantia
        else:
            return 0
