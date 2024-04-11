x = float(input("X koordináta: "))
y = float(input("Y koordináta: "))

if x > 0 and y > 0:
    sn = 1
elif x < 0 and y > 0:
    sn = 2
elif x < 0 and y < 0:
    sn = 3
else:
    sn = 4

print(f"A megadott pont a(z) {sn}. síknegyedben van.")