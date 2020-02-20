#referencia falar de copy

lista = ["daniel", "aula", "de", "python", "hoje eu nao dormi"]

for i, palavra in enumerate(lista):
    print(palavra)

lista.append("dale final")
print(lista)

print(lista[2])

lista.insert(-1, "opa?") # lista[8] falharia - nao possui posicao especificada
print(lista)

lista.remove("daniel")
print(lista)

# cria uma lista de 0 a 6 pulando de 2 em 2 - exlucisvo, sem 6
print(list(range(0, 6, 2)))

print(lista[1:])

# matriz :D

x = int(input())
y = int(input())


matriz = []

for i in range(x):
    matriz.append([])
    for j in range(y):
        matriz[i].append(int(input()))

print(matriz)

lista.sort()