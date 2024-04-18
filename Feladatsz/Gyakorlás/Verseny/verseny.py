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

def ln(p, i):
    maxi = i
    for j in range(i+1, len(p)):
        if p[j] > p[maxi]:
            maxi = j
    return maxi

def rendez(n, p):
    for i in range(len(p)):
        maxi = ln(p, i)
        p[i], p[maxi] = p[maxi], p[i]
        n[i], n[maxi] = n[maxi], n[i]

def kiir(n, p):
    fw = open("eredmeny.txt", "w", encoding="UTF-8")
    fw.write("Eredmenyek:\n")
    for i in range(len(n)):
        fw.write(f"{n[i]} - {p[i]}\n")
    fw.write(f"(\_/)\n(•.•)\n/>♥")
    fw.close()

def main():
    nev, pont = [], []
    maxpont = befajl(nev, pont)
    futtatas()
    ujversenyzo(nev, pont, maxpont)
    rendez(nev, pont)
    kiir(nev, pont)
main()