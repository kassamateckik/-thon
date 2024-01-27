a = int(input("a: "))

db = 0
paros = 0
while db < 40:
    if a % 2 == 0:
        paros += 1
    print(a, end=" ")
    a = (a * 3) % 7
    db += 1
szazalek = paros / 0.4
print(f"\nA tagok {round(szazalek, 2)}%-a páros")

