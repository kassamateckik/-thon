# positional argument: számít a sorrend
# keyword argumnet: kulcsszó alapján azonosít
# positional NEM követhet keyword-öt (meghívásnál); default NEM követhet non-default-ot (definíciónál)

def koszon(forma, knev, vnev=""):
    # ha nem adom meg ez lesz, ha megadok az lesz
    if vnev != "":        
        print(f"{forma} {vnev} {knev}!")
    else:
        print(f"{forma} {knev}!")

koszon("Szia", "Béla", "Fazekas")
koszon("János", "Fekete", "Hello")
koszon(knev="János", vnev="Fekete", forma="Hello")
# koszon("Jó reggelt", "Eszter")
koszon(forma="Jó reggelt", knev="Eszter")
koszon("Jó reggelt", "Eszter")
koszon("Csáó", "Károly", vnev="Kovács")