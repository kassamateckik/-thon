n = int(input("Méret: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(f"({i};{j})", end=" ")
    print()