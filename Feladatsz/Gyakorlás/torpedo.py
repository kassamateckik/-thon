from os import system
from random import randint
from time import sleep

def benne(a, lista):
    n = len(lista)
    i = 0
    while i < n and not a == lista[i]:
        i += 1
    return i < n 


def gridGen(m, hajok = []):
    if hajok == []:
        for i in range(1, m+1):
            for j in range(1, m+1):
                print([i, j], end=" ")
            print()
    else:
        idx = 0
        for i in range(1, m+1):
            for j in range(1, m+1):
                if idx < m and str(i) + str(j) == str(hajok[idx]):
                    idx += 1
                    print(["OO"], end=" ")
                else:
                    print([i, j], end=" ")
            print()
        

def gepgen(m, t):
    hajoi = []
    while len(hajoi) < m:
        r = randint(11, 10*m + m)
        if not benne(r, hajoi) and not benne(r, t):
            hajoi.append(r)
    return hajoi


def jHHelye(lista, n):
    for i in range(1, n+1):
        hely = int(input(f"{i}. Hajód: "))
        lista.append(hely)


def jatekosTipp(GH, TJ, jatekosTippjei):
    tipp = int(input("Tipp: "))
    if not benne(tipp, jatekosTippjei):
        jatekosTippjei.append(tipp)
    if benne(tipp, GH):
        TJ.append(tipp)
        print("Talált!")
    else: 
        print("Nem talált!")
    TJ.sort()


# ?????
def gepTipp(JH, TG, tiltottak, gepTippjei):
    tipp = randint(11, len(JH) + len(JH)*10) 
    tartsd = True 
    while tartsd:
        if benne(tipp, gepTippjei) or benne(tipp, tiltottak):
            gepTippjei.append(tipp)
            tipp = randint(11, len(JH) + len(JH)*10)
        else:
            gepTippjei.append(tipp)
            tartsd = False 
            print(f"Gép tipppje: {tipp}")
            if benne(tipp, JH) and not benne(tipp, TG):  
                TG.append(tipp)
            TG.sort()
# ?????


def tippeles(JH, GH, TJ, TG, tiltottak, gepTippjei, jatekosTippjei):
    jatekosTipp(GH, TJ, jatekosTippjei)
    gepTipp(JH, TG, tiltottak, gepTippjei)
    sleep(2)


def vege(talaltJatekos, gepHajok):
    if talaltJatekos == gepHajok:
        print("Nyertél!")
    else:
        print("Vesztettél!")


def tiltas(tiltottak, meret):
    for i in range(1, meret+1):
        for j in range(11, 10*i+10):
            if j > i*10+meret and not benne(j, tiltottak):
                tiltottak.append(j)
        tiltottak.append(i*10)
    tiltottak.sort()


def tippesgrid(talaltJatekos, talaltGep, jatekosTippjei, jatekosHajok, meret):
    for i in range(1, meret+1):
        for j in range(1, meret+1):
            if benne(int(str(i) + str(j)), talaltJatekos):
                print(["XX"], end=" ")
            elif benne(int(str(i) + str(j)), talaltGep):
                print(["xx"], end=" ")
            elif benne(int(str(i) + str(j)), jatekosHajok):
                print(["OO"], end=" ")
            elif benne(int(str(i) + str(j)), jatekosTippjei):
                print(["--"], end=" ")
            else:
                print([i, j], end=" ")
        print()


def main():
    system("cls")
    print("Játékszabályok (Nyomj entert a folytatáshoz):\n   Annyi hajód van neked és annyi a gépnek, amekkora a pálya szélessége\n   Egy körben egyszer tippelsz te, majd a gép(Tippelni az adott koordináta számainak vessző nélküli beírásával lehet\n      pl.: [1, 5] -> 15; [10, 11] -> 1011)\n   Az nyer, aki először lelövi az ellenfél összes hajóját\nJelölések:\n   [szám, szám] -> semleges négyzet\n   ['OO'] -> saját hajó\n   ['XX'] -> játékos álltal eltalált hajók\n   ['xx'] -> gép álltal eltalált hajók\n   ['--'] -> üres négyzetek")
    input()
    system("cls")
    meret = int(input("Tábla mérete(min. 3 az ajánlott): ")) 
    gridGen(meret)
    jatekosHajok = []
    jHHelye(jatekosHajok, meret)
    jatekosHajok.sort()
    tiltottak = []
    tiltas(tiltottak, meret)
    gepHajok = gepgen(meret, tiltottak)
    gepHajok.sort()
    system("cls")
    # print("tiltottak: ",tiltottak)
    gridGen(meret, jatekosHajok)
    # print(jatekosHajok)
    # print(gepHajok)
    talaltJatekos = []
    talaltGep = []
    gepTippjei = []
    jatekosTippjei = []
    while talaltJatekos != gepHajok and talaltGep != jatekosHajok:
        tippeles(jatekosHajok, gepHajok, talaltJatekos, talaltGep, tiltottak, gepTippjei, jatekosTippjei)
        system("cls")
        tippesgrid(talaltJatekos, talaltGep, jatekosTippjei, jatekosHajok, meret)
    vege(talaltJatekos, gepHajok)

main()