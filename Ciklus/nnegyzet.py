n = int(input("Szám: "))

for i in range(n):
    i = i ** 2
    print(i, end=" ")
print("\n")
'''
for i in range(n):
    i = i ** 2
    if i <= n:
        print(i, end=" ")
'''
i = 0
while i ** 2 <= n:
    print(i ** 2, end=" ")
    i += 1 
