from random import randrange
from os import system
from tkinter import N

def sorsolas():
    szavak = ["hálózat", "python", "számítógép", "értelmes", "szavak", "dolgozat"]
    neo = szavak[randrange(len(szavak))]
    return neo

def kirajzol(s):
    print("Feladvány:")
    for i in range(len(s)):
        print(s[i], end=" ")
    print()

def kezdeti_allapot(n):
    eredmeny = []
    for i in range(n):
        eredmeny.append("_")
    return eredmeny

def csere(betu, aktualis, megoldas):
    for i in range(len(megoldas)):
        if betu == megoldas[i]:
            aktualis[i] = betu

def benne(a, lista):
    i = 0
    while i < len(lista) and lista[i] != a:
        i += 1
    return i < len(lista)    

def megoldottuk(aktualis, megoldas):
    for i in range(len(megoldas)):
        aktualis[i] = megoldas[i]

def kiiras(betu, aktualis, megoldas, hibak):
    system("cls")
    csere(betu, aktualis, megoldas)
    kirajzol(aktualis)
    print(f"Hibák: {hibak}")


def fordulo(aktualis, megoldas, hibak):
    betu = input("\nBetű: ")
    if betu == megoldas:
        megoldottuk(aktualis, megoldas)
        kiiras(betu, aktualis, megoldas, hibak)
        return
    if len(betu) != 1:
        kiiras(betu, aktualis, megoldas, hibak)
        return
    if not benne(betu, megoldas) and not benne(betu, hibak):
        hibak.append(betu)
    kiiras(betu, aktualis, megoldas, hibak)
        
def vege(hibak, megoldas):
    if len(hibak) <= 2:
        print("Nyertél!")
    else:
        print("Vesztettél!, Megoldás:", megoldas)

def jatek(megoldas):
    aktualis = kezdeti_allapot(len(megoldas))
    kirajzol(aktualis)
    hibak = []
    while benne("_", aktualis) and len(hibak) < 3:  # aktualis != list(megoldas)
        fordulo(aktualis, megoldas, hibak)
    vege(hibak, megoldas)


def main():
    system("cls")
    megoldas = sorsolas()
    jatek(megoldas)
    
main()