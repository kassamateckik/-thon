n = int(input("Add meg az összeget: "))

if n < 1670:
    maradek = 1670 - n
    print(f"Sikertelen vásárlás! Hiányzik {170}Ft.")
elif n > 1670:
    vissza = n - 1670
    print(f"Sikeres vásárlás! Visszajáró: {vissza}Ft.")
else:
    print("Sikeres vásárlás! Nincs visszajáró!")