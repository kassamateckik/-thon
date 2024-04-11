n = int(input())
bev = []
akt = 0
db = 0
for i in range(n):
    bev.append(int(input()))
    if bev[i] > akt:
        akt = bev[i]
        db += 1
print(db) 