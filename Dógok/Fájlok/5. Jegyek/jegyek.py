from random import randint

def osztalyozas():
    fw = open("naplo.txt", "w", encoding="UTF-8")
    for i in range(16):
        jegy = randint(1, 5)
        sor = str(jegy) + "\n"
        fw.write(sor)
    fw.close()

def main():
    osztalyozas()

main()