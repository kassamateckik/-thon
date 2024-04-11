from random import randint

n = int(input("n: "))
Fdb = 0
Idb = 0
for i in range(n):
    r = randint(1, 2)
    if r == 1:
        # print("F", end=" ")
        Fdb += 1
    else:
        # print("I", end=" ")
        Idb += 1
print(f"\nFej: {Fdb}; Írás:{Idb}")
print(f"\nFej rel. gyak.: {Fdb/n}; Írás rel. gyak.:{Idb/n}")