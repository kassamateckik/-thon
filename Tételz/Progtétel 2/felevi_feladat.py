# Tantárgyak listája
targyak = [
    "Fizika", "Matek",
    "Testnevelés", "Irodalom",
    "Angol", "Történelem",
    "Progalap", "IKT",
    "Digitális kultúra", "ITA",
    "Webprog", "Adatbázis"
]

# Szakmai tantárgy-e?
szakmai = [
    False, False,
    False, False,
    False, False,
    True, True,
    False, True,
    True, True,
]

# Félév végi jegyek
jegyek = [3, 1, 2, 4, 5, 4, 2, 5, 5, 4, 1, 4]

#------------------------------------------------------------------
n = len(jegyek)

# F1: Igaz-e, hogy minden tárgyból átment? (nem igaz)
i = 0
while i < n and not(jegyek[i] == 1):
    i += 1
if i < n:
    print("Nem ment át minden tantárgyból")
else:
    print("Átment minden tantárgyból")

# F2: Melyik a leghosszabb nevű tantárgy? (Digitális kultúra)
maxidx = 0
for i in range(n):
    if len(targyak[i]) > len(targyak[maxidx]):
        maxidx = i
print("Leghosszabb nevű tantárgy:", targyak[maxidx])

# F3: Van-e olyan tantárgy, amiből ugyanolyan jegyet szerzett, mint irodalomból?
# Feltehető, hogy van "Irodalom" nevű tantárgy!
# Van: (Történelem)
i = 0
while i < n and not(targyak[i] == "Irodalom"):
    i += 1
irodjegy = i
i = 0
while i < n and not(jegyek[irodjegy] == jegyek[i]) or targyak[i] == "Irodalom":
    i += 1
if i < n:
    print("Van: ",targyak[i])

# F4: Van-e olyan szakmai tárgy, amiből 3-as jegynél rosszabbat kapott?
# Ha igen, akkor add meg az utolsó ilyen tárgy nevét! (Webprog)
i = n - 1
while i > 0 and not(szakmai[i] == True and jegyek[i] < 3):
    i -= 1
if i > 0:
    print("Utolsó 3-asnál rosszabb szakmai tárgy neve:", targyak[i])
else:
    print("Nincs ilyen tárgy")

# F5: Van-e két egymást követő tantárgy, ami ugyanazzal a betűvel kezdődik?
# Ha igen, add meg a nevüket! (most nincs, de próbáld ki olyan listával is, amikor van))
i = 1
while i < n and not(targyak[i][0] == targyak[i-1][0]):
    i += 1
if i < n:
    print(targyak[i-1], targyak[i])
else:
    print("Nincs ilyen")