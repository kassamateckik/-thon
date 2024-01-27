# Tantárgyak listája
targyak = ["Fizika", "Matek", "Testnevelés", "Irodalom", "Angol", "Történelem", "Progalap", "IKT", "Digitális kultúra", "ITA", "Webprog", "Adatbázis"]

# Szakmai tantárgy-e?
szakmai = [False, False, False, False, False, False, True, True, False, True,True, True,]

# Félév végi jegyek
jegyek = [3, 1, 2, 4, 5, 4, 2, 5, 5, 4, 1, 4]

#------------------------------------------------------------------
hossz = len(jegyek)

# F1
osszeg = 0
for i in range(hossz):
    osszeg += jegyek[i]
atlag = osszeg / hossz
print(f"1. Átlag: {round(atlag, 2)}")

# F2
teljesitett = 0
for i in range(hossz):
    if jegyek[i] != 1:
        teljesitett += 1
print(f"2. Teljesített tárgyak aránya: {round((teljesitett / hossz) * 100, 2)}%")

# F3
bukott = 0
for i in range(hossz):
    if jegyek[i] == 1 and szakmai[i] == True:
        bukott += 1
print(f"3. Bukott szakmai tárgyak száma: {bukott}")

# F4
maxindx = 0 
for i in range(1, hossz):
   if jegyek[i] > jegyek[maxindx]:
        maxindx = i
print(f"4. Kedvenc tantárgy: {targyak[maxindx]}")

# F5
db = 0
for i in range(hossz):
    if jegyek[i] > atlag:
        db += 1
print(f"5. Átlagfeletti tárgyak száma: {db}")

# F6
recosszeg = 0
for i in range(hossz):
    recosszeg += (1 / jegyek[i])
print(f"6. Jegyek harmonikus közepe: {round(hossz / recosszeg, 2)}")  

# F7
db = 0
for i in range(hossz - 1):
    if szakmai[i] == True and szakmai[i + 1] == True:
        db += 1
print(f"7. Szakmait ennyiszer követ szakmai: {db}")

# F8
minindex = 0
aktbetu = 0
utolso = hossz - 1
for i in targyak[utolso]:
    aktbetu += 1
    minbetu = aktbetu
for i in range(utolso - 1, -1, -1):
    aktbetu = 0
    akt = i
    for b in targyak[akt]:
        aktbetu += 1
        szam = akt
    if aktbetu < minbetu:
        minbetu = aktbetu
        minindex = szam
print(f"8. A legrövidebb nevű tárgy: {targyak[minindex]}")

# F8#2
legkisebb = float("inf")
for i in range(hossz - 1, -1, -1):
    meret = len(targyak[i])
    hely = i
    if meret < legkisebb:
        legkisebb = meret
        vegsohely = hely
print(f"8#2 A legrövidebb nevű tárgy: {targyak[vegsohely]}")

# F9
osszeg = 0
for i in range(hossz):
    if targyak[i] != "Matek":
        osszeg += jegyek[i]
atlagmost = osszeg / (hossz - 1)
print(f"9. Matek nélküli átlag: {round(atlagmost ,2)}")
 
# F10
db = 0
for i in range(hossz):
    akt = i
    for b in targyak[akt]:
        if b == "I":
            db += 1
print(f'10. Az "i" betűvel kezdődő tárgyak száma: {db}')

# F10#2
db = 0
for i in range(hossz):
    akt = targyak[i]
    if akt[0] == "I":
        db += 1
print(f'10#2. Az "i" betűvel kezdődő tárgyak száma: {db}')

# F11
diff = 0
maximum = diff
for i in range(hossz - 1):
    if jegyek[i] > jegyek[i + 1]:
        diff = jegyek[i] - jegyek[i + 1]
    elif jegyek[i] < jegyek[i + 1]:
        diff = jegyek[i + 1] - jegyek[i]
    else:
        diff = 0
    if diff > maximum:
        maximum = diff
print(f"11. A legnagyobb eltérés egymás alatti jegyeknél: {maximum}")

# F12
nemszakosszeg = 0
szakosszeg = 0
nemszakdarab = 0
szakdarab = 0
for i in range(hossz):
    if szakmai[i] == True:
        szakosszeg += jegyek[i]
        szakdarab += 1
    else:
        nemszakosszeg += jegyek[i]
        nemszakdarab += 1
szakatlag = szakosszeg / szakdarab
nemszakatlag = nemszakosszeg / nemszakdarab
print(f"12. A szakmai és a nem szakmai tárgyak átlaga: {round(szakatlag, 2)} {round(nemszakatlag, 2)}")