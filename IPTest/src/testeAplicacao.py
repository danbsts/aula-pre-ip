from poo.aplicacao import Aplicacao
from poo.conta import Conta
from poo.porquinho import Porquinho
from poo.poupanca import Poupanca
from poo.funcionario import Funcionario

porquinho = Porquinho()

aplicacao = Aplicacao(0)

print(aplicacao.criarAplicacao(porquinho))

poupanca = Poupanca(13, 0.05, "Daniel", 21, 0, 1000)

print(poupanca.getConstante())
poupanca.constante += 1
print(poupanca.getConstante())
print(Poupanca.getConstanteStatic())
print(Conta.getConstanteClass())
Conta.constante += 1
print(Poupanca.getConstanteStatic())

print(Funcionario())
