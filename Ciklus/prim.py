p = int(input("p: "))

v = 0

# for i  in range(1, p + 1):
#     if p % i == 0:
#         v += 1
# if v == 1:
#     print("Prím!")
# else: 
#     print("Nem prím!")
db = 0
i = 1
while i <= p and db <= 2:
    if p % i == 0:
        db += 1
    i += 1
if db == 2:
    print("Prím!")
else:
    print("Nem prím!")