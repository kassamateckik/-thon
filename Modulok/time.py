from time import time, sleep
# time modulból a time függvény
# time modulból a sleep függvény késleltet x másodpercet

#print(f"Idő: {time()}")
#1970.01.01(Unix-idő kezdete)-től letelt másodpercek

#0-99-ig random szám időből:
#random = int(time() * 100) % 100
#print("Random szám: ", random)

#nagyobb intervallumú random szám:
#random = int(time() * 1000000000) % 1000000000
#print("Random szám: ", random)

for i in range(40):
    ido = time()
    r = int(ido * 1000000) % 10
    print(r, end=" ")
    sleep(0.001)
#a számok valószínűsége nem egyenlő!
