m = float(input("Hány kg a csomag? "))
s = float(input("Mekkora a távolság km-ben? "))

if m < 5 and s < 500:
    p = 20
elif m < 5 and s >= 500:
    p = 35
elif m >= 5 and s < 500:
    p = 30
else:
    p = 50

print(f"A szállítási kőltség {p}$.")