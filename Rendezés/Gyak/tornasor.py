def csere(x, i, j):
    a = x[i]
    x[i] = x[j]
    x[j] = a

def minindex(x, n=0):
    mini = n
    for i in range(n+1, len(x)):
        if x[i] < x[mini]:
            mini = i
    return mini

def rendez(x):
    for i in range(len(x)):
        j = minindex(x, i)
        csere(x, i, j)

def rendez2(x, y):
    for i in range(len(x)):
        j = minindex(x, i)
        csere(x, i, j)
        csere(y, i, j)

def main():
    nevek = ["Robi", "Laci", "Anna",  "Dani", "Ricsi", "Marci"]
    magassagok = [175, 142, 150, 158, 172, 175]
    n = len(nevek)


    # F1 - Adjuk meg a névsort!
    # Feltehető, hogy nincs ékezet a nevekben!
    nevsor = nevek.copy()
    rendez(nevsor)
    print("1. Névsor:", nevsor)

    # F2 - Adjuk meg a tornasort (nevek)!
    # (Magasság szerinti növekvő sorrend.)
    rendez2(magassagok, nevek)
    print("2. Tornasor:")
    print("   Nevek:", nevek)
    print("   Magasságok:", magassagok)




    # F3 - Egyetlen rendezési függvényt használjunk!

    # F4 - Azonos magasságok esetén a névsor alapján rendezzünk!
    
    # F5 - Adjuk meg, hogy ki áll a tornasor közepén (medián)!
    print("5. A tornasor közepe: ", end="")


main()