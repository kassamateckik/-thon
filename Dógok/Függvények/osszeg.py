x = [1, 95, 6, 32, 125, 20, -59, 63.5, -47.985]

def osszeg(a: list) -> float:
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s

def osszeg2(*a): # határozatlan számú paramétert fogad, listaként kezeli (tuple = konstans lista)
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s

print("-"*25)

print(osszeg(x))

print("-"*25) 

print(osszeg2(5))
print(osszeg2(5, 7))
print(osszeg2(3, -2, 1, 11, -10))

print("-"*25)