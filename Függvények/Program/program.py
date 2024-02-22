def beolvasas(szinek):
    n = int(input())
    for i in range(n):
        szinek.append(input())

def legrovidebb(szinek):  
    mini = 0
    for i in range(len(szinek)):
        if len(szinek[i]) < len(szinek[mini]):
            mini = i
    return szinek[mini]

def kiiras(szin):
    print("Legrövidebb:", szin)
    
def main():
    szinek = []
    beolvasas(szinek)
    legrovidebbSzin = legrovidebb(szinek)
    kiiras(legrovidebbSzin)

main()

