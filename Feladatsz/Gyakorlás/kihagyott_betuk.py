from random import *

'''
Készíts függvényt betuk(s) néven, amely
paraméterként kap egy szöveg és a szöveg minden
szóköztől különböző betűjét 20% valószínűséggel kicseréli "_" jelre!
A szóközöket biztosan megtartja!

Pl.: betuk("abc") lehetséges értékei:
"abc", "ab_", "a_c", "_bc", "__c", "_b_", "a__", "___"
'''
# def betuk(s: str):
#     seged = list(s)
#     lyukas = ""
#     for i in range(len(seged)):
#         r = randint(1, 5)
#         if r == 3:
#             seged[i] = "_"
#         lyukas += seged[i]
#     return lyukas

def betuk(s: str):
    lyukas = ""
    for i in range(len(s)):
        r = randint(1, 5)
        if r == 3 and s[i] != " ":
            lyukas += "_"
        else:
            lyukas += s[i]
    return lyukas

def main():
    print(betuk("Szerencsekerék"))
    print(betuk("Igen"))
    print(betuk("Még nyílnak a völgyben a kerti virágok"))
    print(betuk("Volt egyszer egy óriási kisegér"))

main()