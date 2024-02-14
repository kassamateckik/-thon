from random import randint

n = int(input("n: "))
x =["datolya", "szilva", "kaki", "sárkánygyümölcs", "sárgadinnye"]
hossz = len(x)
for i in range(n):
    r = randint(0, hossz-1)
    print(i+1, x[r])
