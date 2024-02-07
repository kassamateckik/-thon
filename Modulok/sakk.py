sor = int(input("Sorok száma: "))
oszlop = int(input("Oszlopok száma: "))

for i in range(sor):
    for j in range(oszlop):
        if i % 2 == 0 and j % 2 == 0:
            print("X", end=" ")
        else:
            print("0", end=" ")
    print()