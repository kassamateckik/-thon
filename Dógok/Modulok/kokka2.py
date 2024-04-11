from random import randint

n = int(input("Dobás: "))
k = int(input("Kocka: "))
# számláló tömb techinka
gy = []

for i in range(k): 
    gy.append(0)

for i in range(n):
    r = randint(1, k)
    gy[r-1] += 1

# print(gy)
for i in range(k):
    print(gy[i], end=" ")