from random import randrange, randint   

#[5..12]:
print("Randrange:")
for i in range(20):
    r = randrange(5, 13)
    # ugyanúgy működik mint a range()
    print(r, end=" ")

print("\n")

print("Randint:")
for i in range(20):
    r = randint(5, 12)
    # randint(kezdo, utolso)
    print(r, end=" ")

print("\n")
# Véletlen páratlan számok az 5, 12 intervallumon:

print("Ptln [5..12]:")
for i in range(20):
    r = randrange(5, 13, 2)
    print(r, end=" ")

print("\n")

print("Prs ☻ [5..12](rangdint):")
for i in range(20):
    r = randint(3, 6) * 2 
    print(r, end=" ")

print("\n")

print("Ptln ☺ [5..12](rangdint):")
for i in range(20):
    r = randint(3, 6) * 2 - 1 
    print(r, end=" ")
