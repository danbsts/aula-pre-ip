a = 2

def minhaFuncaoHumilde(x, y=2, z=4):
    global a
    a = x * y
    print(a)
    return a + z


print(a)
z = minhaFuncaoHumilde(a)
print(a)

print(z)
