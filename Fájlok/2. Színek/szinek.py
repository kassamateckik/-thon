
def befile(sz):
    fr = open("szinek.txt", "r", encoding="UTF-8")
    # print(fr.readlines()) # NE!!
    sor = fr.readline()
    while sor != "":
        sor = sor.strip()
        sz.append(sor)
        sor = fr.readline()
    fr.close()

def main():
    szinek = []
    befile(szinek)
    print(szinek)


main()