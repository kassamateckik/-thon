def sorn(sor, a, b):
    for i in range(sor):
        if i % 2 == 0:
            print(a, end=" ")
        else: 
            print(b, end=" ")
    print()

def sakktabla(sor, a, b):
    for i in range(sor):
        if i % 2 == 0:
            sorn(sor, a, b)
        else:
            sorn(sor, a, b)

def main():
    sor = int(input("Sorok száma: "))
    a = input("a: ")
    b = input("b: ")
    sakktabla(sor, a, b)
         

main()