n = int(input())
hok = []
maxi = 0
for i in range(n):
    hok.append(int(input()))
    if hok[i] > hok[maxi]:
        maxi = i
print(maxi + 1)