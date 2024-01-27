n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
i = 0
while i < n-1 and not(m[i] > m[i+1]):
    i += 1
if i < n-1:    
    print(i+2)
else: 
    print("-1")
