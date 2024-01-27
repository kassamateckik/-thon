n = int(input("Osztályzat: "))

jo = 1 <= n and n <= 5
# not jo = 1 > n or n > 5
while not jo:
    n = int(input("Nem jó! Próbáld újra: "))
    jo = 1 <= n and n <= 5

print("Jó!")
