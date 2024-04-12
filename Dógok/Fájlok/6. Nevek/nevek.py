def main():
    fa = open("nevek.txt", "a", encoding="UTF-8") # append
    nev = input("Neved: ")
    if nev != "Farkas Norbert":
        fa.write(f"{nev}\n")
    fa.close()


main()