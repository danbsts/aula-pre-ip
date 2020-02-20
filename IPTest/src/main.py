from poo.conta import Conta

conta = Conta("Daniel", 21, 1000)
conta2 = Conta("Daniel", 2, 10)


print(conta.constante)
print(conta2.constante)
print(conta.getSaldo())
print(type(conta), end="nandamovei")
print("""
QUERO IMPRIMIR ESSE TEXTAO AQUI PORQUE A VIDA TEM DESSAS :star-struck:
quebrando linhas u.u <- mas nao quebrando regras
"""
)

# dicionario = input()
# print(dicionario)
print(conta.facaNada())
print(conta.better_have_my_money(100000))

conta3 = conta
print(id(conta3))
print(id(conta))


print('exemplo que eu quero')
print(conta.getConstante())
conta.constante += 1
dale = Conta('e ai?', 2, 2)
Conta.kakakak = 1
print(Conta.kakakak)
print(conta2.kakakak)
conta2.kakakak += 1
Conta.kakakak += 3
print(Conta.kakakak)
print(conta2.kakakak)
print(conta2.getConstante())
conta2.constante += 1
print(conta.getConstanteStatic(), ' <- here')
print(conta.getConstante())
print(Conta.constante)

valor = 1
if (conta.getSaldo() >= valor):
    conta.transferir(conta2, valor)
else:
    printa("oi")