def befile(n, k):
    fr = open("nevek.txt", "r", encoding="UTF-8")
    sor = fr.readline()
    while sor != "":
        n.append(sor.split()[0])
        k.append(int(sor.split()[1]))
        sor = fr.readline()
    fr.close()

def legkisebb(i, k):
    mini = i
    for i in range(i, len(k)):
        if k[mini] > k[i]:
            mini = i
    return mini

def rendez(n, k):
    for i in range(len(k)):
        mini = legkisebb(i, k)
        k[i], k[mini] = k[mini], k[i]
        n[i], n[mini] = n[mini], n[i]

def kifile(n, k):
    fw = open("eletkor.txt", "w", encoding="UTF-8")
    for i in range(len(n)):
        fw.write(f"{n[i]} {k[i]}\n")
    fw.close()



def main():
    nevek, korok = [], []
    befile(nevek, korok)
    rendez(nevek, korok)
    kifile(nevek, korok)



main()