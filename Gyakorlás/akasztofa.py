from random import randrange
from os import system

def sorsolas():
    szavak = ["hálózat", "python", "számítógép", "értelmes", "szavak", "dolgozat"]
    neo = szavak[randrange(len(szavak))]
    return neo

def vonalak_kirajzol(s: str):
    print("Feladvány:")
    for i in range(len(s)):
        print("_", end=" ")
    print()

def main():
    system("cls")
    megoldas = sorsolas()
    print(megoldas)
    vonalak_kirajzol(megoldas)
    
    
main()