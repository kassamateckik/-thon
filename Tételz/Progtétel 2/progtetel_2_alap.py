x = [5, 1, 6, -3, 12, 8, 10, 29, 16, 6, 2, 11]
n = len(x)

# F0
i = 0
while i < n and not(x[i] == 6):
    i += 1
if i < n:
    print(f"0. Első hatos sorszáma: {i+1}")
else:
    print("0. Nincs a listában 6-os.")

# F1
i = 0
while i < n and not(x[i] % 2 == 0):
    i += 1
if i < n:
    print(f"1. Első páros szám: {x[i]}")
else:
    print("1. Nincs páros szám!")

# F2
i = 0
while i < n and not(10 <= x[i] and x[i] <= 20):
    i += 1
if i < n:
    print(f"2. Első 10 és 20 közötti szám sorszáma: {i + 1}")
else:
    print("2. Nincs a listában 10 és 20 közötti szám.")

# F3
i = 0
while i < n and not(x[i] % 3 == 0 and x[i] % 2 == 1):
    i += 1
if i < n:
    print(f"3. Első 3-mal osztható páratlan szám: {x[i]}")
else:
    print("3. Nincs 3-mal osztható páratlan szám!")

# F4
i = n-1
while i >= 0 and not(x[i] % 4 == 0):
    i -= 1
if i >= 0:
    print(f"4. Utolsó 4-gyel osztható szán: {x[i]}")
else:
    print("4. Nincs 4-gyel osztható szám!")


# 5
i = 1
while i < n and not(x[i] < x[0]):
    i += 1
if i < n:
    print("5. Nem első a legkisebb!")
else:
    print("5. Az első a legkisebb!")

# F6
s = 0
for i in range(n):
    s += x[i]
atl = s / n
i = 0
while not(x[i] >= atl):
    i += 1
print(f"6. Első legalább átlagos elem: {x[i]}") 

# F7
i = 0
while i < n-1 and not(x[i+1] < x[i]):
    i += 1
if i < n-1:
    print("7. Nem monoton növekvő!")
else:
    print("7. Monoton növekvő!")

# F8
i = 0
while i < n - 1 and not(x[i] > 0 and x[i+1] < 0 or x[i] < 0 and x[i+1] > 0):
    i += 1
if i < n - 1:
    print("8. Nem egyforma előjelűek!")
else:
    print("8. Egyforma előjelűek!")

#8/2
i = 1
while i < n and not(x[i] > 0 and x[0] < 0 or x[i] < 0 and x[0] > 0):
    i += 1
if i < n:
    print("8/2. Nem egyforma előjelűek!")
else:
    print("8/2. Egyforma előjelűek!")

#8/3
i = 1
while i < n and not(x[0] * x[i] < 0):
    i += 1
if i < n:
    print("8/3. Nem egyforma előjelűek!")
else:
    print("8/3. Egyforma előjelűek!")

# F9 


# F10 van lokális max? (nagyobbmndkétszomszédnál)
i = 1
while i < n - 1 and not(x[i-1] < x[i] and x[i+1] < x[i]):
    i += 1
if i < n-1:
    print(f"10. Van lokális maximum, helye: {i+1}, értéke: {x[i]}")
else:
    print("10. Nincs lokális maximum")

# F11


# F12

