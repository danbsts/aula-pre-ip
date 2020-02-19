tuplinha = (12, "daniel")

listaDeTuplas = [(1, "daniel"), (2, "alguem"), (3, "ninguem"), (4, 4)]  # vai dar bom?

for i, j in listaDeTuplas:
    print(i, j)  # :D

dicionario = {"daniel": "monitor", "alguem": "cpu", "ninguem": 2}
print(dicionario)

for (i, j) in dicionario.items():
    print(i, j)

for i in dicionario:  # only keys
    print(i)

dicionario[2] = "daniel"
print(dicionario)

print(dicionario.get(22))

del dicionario[2]
print(dicionario)