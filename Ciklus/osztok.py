n = int(input("n: "))

print("A szám osztói:")

for i  in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")


        