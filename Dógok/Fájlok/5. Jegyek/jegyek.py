from random import randint

def osztalyozas():
    fw = open("naplo.txt", "w", encoding="UTF-8")
    for i in range(16):
        jegy = randint(1, 5)
        # fw.write(str(jegy) + "\n")
        fw.write(f"{jegy}\n")
    fw.close()

def main():
    osztalyozas()

main()