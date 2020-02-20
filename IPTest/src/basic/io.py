nome = "daniel"
idade = 21
# if idade.isnumeric():
#     idade = int(idade)
print("%.0f" % (idade/2))

print(nome * 2)

print(idade * 2, "dobro", "da", "idade")
# o mesmo que
print("{} dobro da idade".format(idade*2)) # o numero tem que estar no range -> {}
# ou
print(str(idade*2) + " dobro da idade")

nan = float(input()) # same as float("xalala")
print(nan)


frase = input()
print(frase.split("a"))
print(frase.title())
print(' '.join(frase.split(" "))) # concatena espacos entre cada caracter da string se for uma lista, junta a lista usando espaco