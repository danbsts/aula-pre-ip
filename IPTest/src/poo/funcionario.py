import abc


class Funcionario(abc.ABC):

    @abc.abstractmethod
    def getCPF(self):
        pass
