lista = [5, 3, 7, 4, 12, -9, 31, 7, 11]
hossz = len(lista)

print("F3:", end=" ")
for i in range(hossz):
    print(lista[i] * 2, end=" ")

print()

print("F4:", end=" ")
for i in range(1, hossz, 2):
    print(lista[i], end=" ")

print()

print("F5:", end=" ")
for i in range(hossz):
    if lista[i] % 3 == 0:
        print(lista[i], end=" ")

print()

print("F6:", end=" ")
for i in range(hossz - 1, -1, -1):
    print(lista[i], end=" ")

print()

print("F7:", end=" ")
for i in range(hossz):
    print((lista[i]) + i, end=" ")