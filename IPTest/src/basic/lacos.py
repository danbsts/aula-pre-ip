false = False

# for i in range(1,5)
for i in range(5):  # exclusivo, so vai de 1 a 4
    print(i)

variavel = " <- valor de i"
print(i, variavel, 2, 3, 5, 6, end="\n\n", sep='---')


a = [2,3,4,2,5,666]
for numero in a:
    print(numero)


for i,j in zip(range(1,4), range(5,8)):
    print(f"{variavel}", j)

flag = True
while flag:
    print("xalala")
    flag = False
else:
    print("aoidasidoa")