x = [5, 1, -8, 2, 32, 12, 17, 32, -3, 5, 2]
hossz = len(x)
#-------------------------------------------------------------
# 1. A 4-gyel oszthatók száma => 4

print("1. A 4-gyel oszthatók száma:")
db = 0
for i in range(hossz):
    if x[i] % 4 == 0:
        db += 1
print(db)

#-------------------------------------------------------------
# 2. A 10-nél kisebbek szorzata => 2400

print("2. A 10-nél kisebbek szorzata:")
s = 1
for i in range(hossz):
    if x[i] < 10:
        s *= x[i]
print(s)


#-------------------------------------------------------------
# 3. A legnagyobb szám (több esetén az első) sorszáma => 5

print("3. A legnagyobb szám sorszáma:")
maxindex = 0
for i in range(1, hossz):
    if x[i] > x[maxindex]:
        maxindex = i
print(maxindex + 1)


#-------------------------------------------------------------
# 4. Hány lokális maximum van? => 3
# Lokális maximum: nagyobb mindkét szomszédjánál
# Magyarázat: x[4] és x[7] és x[9] lokális maximumok

print("4. A lokális maximumok száma:")
db = 0
for i in range(1, hossz - 1):
    if x[i] > x[i-1] and x[i] > x[i+1]:
        db += 1
print(db)
