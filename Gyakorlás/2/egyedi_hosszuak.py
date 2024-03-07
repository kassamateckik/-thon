'''
Készíts függvényt egyedi_hosszuak(x) néven, amely
megadja az x lista azon elemeit,
amelyek előtt nincs velük azonos hosszú elem!

Paraméterek:
x: szövegeket tartalmazó lista

Visszatérési érték:
Egy lista a megfelelő (egyedi) elemekkel!
'''
def egyedi_hosszuak(x): # Bennevan függvény 
    


def main():
    print(egyedi_hosszuak(["alma", "banan", "korte", "barack"]) == ["alma", "banan", "barack"])
    print(egyedi_hosszuak(["piros", "feher", "zold", "barna", "lila"]) == ["piros", "zold"])
    print(egyedi_hosszuak(["abc", "aab", "abba", "baba"]) == ["abc", "abba"])

main()