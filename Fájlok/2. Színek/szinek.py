
def befile(sz):
    fr = open("szinek.txt", "r")
    print(fr.readlines()) # NE!!
    fr.close()

def main():
    szinek = []
    befile(szinek)
    print(szinek)


main()