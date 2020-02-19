import math

x = 15
y = 2

print(x == int(y))
print(x < y)
print(x >= y)

if not x == y:
    print("e igual mesmo")
else:
    print("sai dai")


xDivididoYInteiro = x//y
xDivididoY = x/y

print(xDivididoYInteiro)
print(xDivididoY)
print(math.floor(xDivididoY))
