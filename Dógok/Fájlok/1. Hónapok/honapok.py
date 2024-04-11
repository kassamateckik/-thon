def befile(h):
    fr  = open("honapok.txt", "r") # visszatérési értéke a file (fr = file reader)
    n = int(fr.readline())
    for i in range(n):
        adat = fr.readline().strip()
        h.append(adat)
    fr.close()


def bekonzol(dzs):
    n = int(input())
    for i in range(n):
        adat = input()
        dzs.append(input(adat))

def main():
    honapok = []
    befile(honapok)
    print(honapok)


main()