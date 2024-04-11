n = int(input())
k = int(input())
jok = []
for i in range(n):
    if int(input()) < k:
        jok.append(i+1)
print(len(jok), end=" ")
for i in range(len(jok)):
    print(jok[i], end=" ")