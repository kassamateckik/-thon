def befile(x, y):
    fr = open("gyumolcsok.txt", "r", encoding = "UTF-8")
    sor = fr.readline().strip()
    while sor != "":
        x.append(sor.split()[0])
        y.append(int(sor.split()[1]))
        sor = fr.readline().strip()
    fr.close()
    
def atlag(x):
    s = 0
    for i in range(len(x)):
        s += x[i]
    return s / len(x)

def main():
    gyumik = []
    arak = []
    befile(gyumik, arak)
    print("Átlag: ",atlag(arak))

main()