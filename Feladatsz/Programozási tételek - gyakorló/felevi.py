#F1
n = int(input())
nev, magyar, matek, tori = [], [], [], []
for i in range(n):
    sor = input().split()
    nev.append(sor[0])
    magyar.append(int(sor[1]))
    matek.append(int(sor[2]))
    tori.append(int(sor[3]))

#F2
toriossz = 0
for i in range(n):
    toriossz += tori[i]
print("2. feladat:", round(toriossz/n, 3))


#F3
db = 0
for i in range(n):
    if matek[i] == 1:
        db += 1
print("3. feladat:", db)


#F4
atlagok = []
maxi = 0
for i in range(n):
    atlagok.append((matek[i]+magyar[i]+tori[i])/3)
    if atlagok[i] > atlagok[maxi]:
        maxi = i
print("4. feladat:", nev[maxi])


#F5
i = 0
while i < n and not(matek[i] > magyar[i]):
    i += 1
if i < n:
    print("5. feladat:", nev[i])
else:
    print("5. feladat: Nincs")



# F6
asok = []
db = 0
for i in range(n):
    if nev[i][len(nev[i])-1] == "a":
        asok.append(nev[i])
        db += 1
print("6. feladat:", db, end=" " )
for i in range(len(asok)):
    print(asok[i], end=" ")

# F7
i = 0
while i < n and not(matek[i] == magyar[i] and magyar[i] == tori[i]):
    i += 1
if i < n:
    print("\n7. feladat: Van")
else:
    print("\n7. feladat: Nincs")
    

# F8
i = 0
while i < n and not(magyar[i] == 5):
    i += 1
if i < n: 
    minmatek = 5
    mini = n-1
    for i in range(n-1, -1, -1):
        if matek[i] < minmatek and magyar[i] == 5:
            minimatek = matek[i]
            mini = i
    print("8. feladat:", nev[mini])
else:
    print("8. feladat: -1")


# F9
bukott = 0
for i in range(n):
    if matek[i] == 1 or magyar[i] == 1 or tori[i] == 1:
        bukott += 1
szazalek = bukott/(n/100)
print(f"9. feladat: {round(szazalek, 2)}%")


# F10
print("10. feladat:", end=" ")
for i in range(1, n-1):
    if matek[i] < matek[i+1] and matek[i] < matek[i-1]:
        print(i+1, end=" ")
