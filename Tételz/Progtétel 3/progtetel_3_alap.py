x = [5, 1, 2, -6, 7, 7, 16, 2, 2, 32, -3, 5, 6]
n = len(x)

# F1 - Másolás tétel
# Másold át az elemeket egy másik listába!
y = []
for i in range(n):
    y.append(x[i])
print("1. Másolt lista:", y)

# F2
# Másold át az elemek négyzeteit egy másik listába!
negyzetek = []
for i in range(n):
    negyzetek.append(x[i]**2)
print("2. Négyzetek:", negyzetek)

# F3 - Kiválogatás tétele
# Válogasd ki a 10 alatti elemeket egy másik listába!
tizAlattiak = []
for i in range(n):
    if x[i] < 10:
        tizAlattiak.append(x[i])
print("3. 10 alattiak:", tizAlattiak)

# F4
# Válogasd ki a negatív elemek indexeit egy másik listába!
negativak = []
for i in range(n):
    if x[i] < 0:
        negativak.append(i)
print("4. Negatívak indexei:", negativak)

print("Negatívak értékei:", end=" ")
neg2 = []
for i in range(len(negativak)):
    neg2.append(x[negativak[i]])
print(neg2)

# F5 - Szétválogatás tétele
# Válogasd szét a páros és a páratlan elemeket!
prs = []
ptln = []
for i in range(n):
    if x[i] % 2 == 0:
        prs.append(x[i])
    else:
        ptln.append(x[i])
print("5. Párosak:", prs)
print("5. Páratlanok:", ptln)

# F6
# Válogasd ki a loális minimumok indexeit
lokmin = []
for i in range(1, n-1):
    if x[i] < x[i-1] and x[i] < x[i+1]:
        lokmin.append(i)
print("6. Lokális minimumok:", lokmin)

# F7
# előzőhöz képest nő/csökknet/állandó
no = []
csokk = []
allando = []
for i in range(1, n):
    if x[i] > x[i-1]:
        no.append(i)
    elif x[i] < x[i-1]:
        csokk.append(i)
    else:
        allando.append(i) 
print(f"7.  Növekedők: {no}\n    Csökkenők:{csokk}\n    Állandók:{allando}")

    