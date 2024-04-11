def parose(n):
    # if n % 2 == 0:
    #     return True
    # else: 
    #     return False
    return n % 2 == 0


def parosakSzama(x):
    darab = 0
    for i in range(len(x)):
        if parose(x[i]):
            darab += 1
    return darab


def main():
    x = [5, 3, 2, 8, 1]
    db = parosakSzama(x)
    print("Párosak száma:", db)
main()