def befile(c, e):
    fr = open("filmek.csv", "r", encoding = "UTF-8")
    sor = fr.readline().strip()
    while sor != "":
        c.append(sor.split(";")[0])
        e.append(float(sor.split(";")[1]))
        sor = fr.readline().strip()
    fr.close()

def legjobb(c, e):
    maxi = 0 
    for i in range(1, len(e)):
        if e[i] > e[maxi]:
            maxi = i
    return c[maxi]

def main():
    cimek, ertekek = [], []
    befile(cimek, ertekek)
    print("Legjobb film:", legjobb(cimek, ertekek))
main()