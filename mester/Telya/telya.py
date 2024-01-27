n = int(input())
marka = input()
osszar = int(input())
for i in range(n-1):
    aktmrk = input()
    if aktmrk == marka:
        osszar += int(input())
    else:
        szemet = int(input())
print(osszar)