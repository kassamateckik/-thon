from random import randrange
from os import system

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


def main():
    system("cls")
    megoldas = sorsolas()
    aktualis = kezdeti_allapot(len(megoldas))
    print(megoldas)
    kirajzol(aktualis)
    betu = input("\nBetű: ")
    csere(betu, aktualis, megoldas)
    
main()