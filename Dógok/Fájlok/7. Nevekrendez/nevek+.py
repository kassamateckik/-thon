def befile(n, k, fr):
    sor = fr.readline()
    while sor != "":
        n.append(sor.split()[0])
        k.append(int(sor.split()[1]))
        sor = fr.readline()

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

def kifile(n, k, fw):
    for i in range(len(n)):
        fw.write(f"{n[i]} {k[i]}\n")


def main():
    nevek, korok = [], []
    f = open("nevek+.txt", "a+", encoding="UTF-8")
    # a+ esetén az olvasási pozíciót lehet változtetni, az írásit nem!(mindig a végére ír)
    f.seek(0)
    # print(f.tell()) hányadik bájtnál járok a fájlban?
    befile(nevek, korok, f)
    rendez(nevek, korok)
    f.truncate(0)
    kifile(nevek, korok, f)
    f.close()


main()