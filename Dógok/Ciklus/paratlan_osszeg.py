n = int(input("n: "))

osszeg = 0
for i in range(1, n + 1, 2):
    osszeg += i
    
print("Páratlanok összege:", osszeg)