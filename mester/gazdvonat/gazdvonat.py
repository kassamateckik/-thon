n = int(input())
arkoltseg = input().split()
ar = int(arkoltseg[0])
koltseg = int(arkoltseg[1])
fel = []
le = []
for i in range(n):
    sor = input().split()
    fel.append(int(sor[0]))
    le.append(int(sor[1]))

osszfel = 0
for i in range(n):
    osszfel += fel[i]

if osszfel * ar > koltseg * n:
    print("1")
else:
    print("0")