from random import randint

def befajl(n, p):
    fr = open("be.txt", "r", encoding="UTF-8")
    max = int(fr.readline())
    sor = fr.readline().split(": ")
    while sor != [""]:
        n.append(sor[0])
        p.append(int(sor[1]))
        sor = fr.readline().split(": ")
    fr.close()
    return max

def futtatas():
    f = open("naplo.txt", "a+", encoding="UTF-8")
    f.seek(0)
    n = 1
    sor = f.readline()
    while str(sor) != "":
        n += 1
        sor = f.readline()
    f.write(f"A program {n}. alkalommal futott sikeresen!\n")
    f.close()

def ujversenyzo(n, p, m):
    n.append("Aloe Vera")
    p.append(randint(0, m))


def main():
    nev, pont = [], []
    maxpont = befajl(nev, pont)
    futtatas()
    ujversenyzo(nev, pont, maxpont)
main()