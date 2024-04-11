n = int(input("n: "))

szf = 1
for i in range(n, 0, -2):
    szf *= i

print(f"{szf}!!")