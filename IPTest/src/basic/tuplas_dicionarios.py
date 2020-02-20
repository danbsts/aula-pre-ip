tuplinha = (12, "daniel")

listaDeTuplas = [(1, "daniel"), (2, "alguem"), (3, "ninguem"), (4, 4)]  # vai dar bom?

for i, j in listaDeTuplas:
    print(i, j)  # :D

dicionario = {"daniel": "monitor", "alguem": "cpu", "ninguem": 2}
print(dicionario)

for (chave, valor) in dicionario.items():
    print(chave, valor)

for i in dicionario:  # only keys
    print(i)

print(dicionario.get(2), 'asddsadas')
dicionario[2] = "daniel"
dicionario['cpu'] = 'alguem'
print(dicionario)

print(dicionario.get(22))

del dicionario[2]
print(dicionario)