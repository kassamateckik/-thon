x = [1, 95, 6, 32, 125, 20, -59, 63.5, -47.985]

def osszeg(a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s

print(osszeg(x))