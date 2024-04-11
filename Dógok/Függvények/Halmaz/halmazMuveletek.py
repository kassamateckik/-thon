# Halmaz műveletek:
# Metszet
# Unio
# Különbség

def benne(n, lista):
    i = 0
    while i < len(lista) and not(lista[i] == n):
        i += 1 
    return i < len(lista)

def metszet(a, b):
    m = []
    for i in range(len(a)):
        if benne(a[i], b):
            m.append(a[i])
    return m

def unio(a, b):
    u = []
    for i in range(len(a)):
        u.append(a[i])
    for i in range(len(b)):
        if not benne(b[i], a):
            u.append(b[i])
    return u

def kulonbseg(a, b):
    k = []
    for i in range(len(a)):
        if not benne(a[i], b):
            k.append(a[i])
    return(k)

def szimdiff(a, b):
    return kulonbseg(unio(a, b), metszet(a, b))

def szimdiff2(a, b):
    return unio(kulonbseg(a, b), kulonbseg(b, a))

def main():
    a = [2, 7, 1, 5, 3]
    b = [1, 6, 8, 7]

    print("A metszet B:",metszet(a, b))
    print("B metszet A:",metszet(b, a))
    print("A U B:",unio(a, b))
    print("B U A:",unio(b, a))
    print("A \ B:",kulonbseg(a, b))
    print("B \ A:",kulonbseg(b, a))
    print("A delta B:",szimdiff(a, b))
    print("B delta A:",szimdiff2(b, a))
main()