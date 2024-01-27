n = int(input("n: "))

i = 1
fakt = 1
while i <= n:
    fakt *= i
    i += 1

print(f"{n} faktoriális: {fakt}")