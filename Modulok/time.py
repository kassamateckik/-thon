from time import time
# time mosulból a time függvény

#print(f"Idő: {time()}")
#1970.01.01(Unix-idő kezdete)-től letelt másodpercek

#0-99-ig random szám időből:
random = int(time() * 100) % 100
print("Random szám: ", random)

#nagyobb intervallumú random szám:
random = int(time() * 1000000000) % 1000000000
print("Random szám: ", random)