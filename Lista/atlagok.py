lista = [5, 3, 7, 4, 12, -9, 31, 7, 11]
n = len(lista)

print("F8:", end=" ")
for i in range(n - 1):
    atlag = (lista[i] + lista[i + 1]) / 2
    print(atlag, end=" ")

print()

print("F9:", end=" ")
osszeg = 0
for i in range(n):
    osszeg += lista[i]
print(osszeg)