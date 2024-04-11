lista = [5, 3, 7, 4, 12, -9, 31, 7, 11]

print("F1:", end=" ")
for i in lista:
    print(i, end=" ")

print()

print("F2:", end=" ")
for i in range(len(lista)):
    if i < len(lista) - 1:
        print(lista[i], end="; ")
    else:
        print(lista[i], end=" ")

