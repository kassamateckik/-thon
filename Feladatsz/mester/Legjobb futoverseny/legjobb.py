nap = int(input())
hely = []
percek = []
sec = []

for i in range(nap):
    sor = input().split()
    hely.append(int(sor[0]))
    percek.append(int(sor[1]))
    sec.append(int(sor[2]))

mine = hely[0]
for i in range(1, nap):
    if hely[i] < mine:
        mine = hely[i]

db = 0
for i in range(nap):
    if hely[i] == mine:
        db += 1


print(mine, db)