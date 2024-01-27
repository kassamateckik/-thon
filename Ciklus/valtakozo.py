n = int(input("n: ")) 

osszeg = 0
for i in range(1, n + 1):
    i *= i
    if i % 2 == 0:
        osszeg -= i
    else:
        osszeg += i

print(osszeg)
