# x az egy lokális változó, csak itt létezik az egész programban
def novel(x):
    x += 1

szam = 5
novel(szam)
print(szam)

# a függvény def.-ban léfő x nem ugyanaz, mint ez az x
x = 5
novel(x)
print(x)

# a bentebbkezdés a hatókör(scope)t jelenti(ami ott van, ott mükszik)

print("-"*25)
# -------------------------------------------------------------------------------------------------

def modosit(x):
    x[0] = 404
# lista értékmódosítás (teljes lista felülírás NEM) és listaműveletek működnek!
lista = [5, 4, 2]
print(lista)
modosit(lista)
print(lista)