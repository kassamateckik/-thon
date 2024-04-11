a = int(input("Szám: "))
d = int(input("Környezet: "))

min = a - d
max = a + d

for i in range(min + 1, max):
    print(i, end=" ")

