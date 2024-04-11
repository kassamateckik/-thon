'''
Sára nyakláncot készít piros, sárga és kék
színű gyöngyökből.

Egyetlen fontos szabály van:
piros gyöngyöt nem követhet kék!

Készíts függvényt nyaklanc(n) néven,
amely visszatérési értéke egy n hosszú
szöveg, amely P, S és K karakterekből áll
a fenti szabálynak megfelelően!

Pl.:
nyaklanc(2) lehetséges értékei:
"PP", "PS",
"SS", "SK", "SP"
"KK", "KS"

Vigyázat: nem csak "PK", de "KP" sem jó,
mert a nyaklánc két végét össze kell kötni!
'''
from random import randint

def szovegge(x):
    vissza = ""
    for i in range(len(x)):
        vissza += x[i]
    return vissza


def nyaklanc(n):
    ekszer = []
    while len(ekszer) != n:
        r = randint(1, 3)
        if r == 1:
            gy = "P"
        elif r == 2:
            gy = "S"
        else:
            gy = "K"
        if len(ekszer) != 0 and ekszer[len(ekszer)-1] == "P" and gy == "K":
            r = randint(1, 2)
            if r == 1:
                gy = "S"
            else:
                gy = "P"
        ekszer.append(gy)
    if ekszer[n-1] == "P" and ekszer[0] == "K":
        r = randint(1, 2)
        if r == 1:
            ekszer[0] = "S"
        else:
            ekszer[0] = "P"
    return szovegge(ekszer)



# Tesztelés
def main():
    print(nyaklanc(2))
    print(nyaklanc(3))
    print(nyaklanc(7))
    print(nyaklanc(15))

main()