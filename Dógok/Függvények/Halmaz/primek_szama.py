def primE(n: int):
    if n == 1:
        return False
    else:
        i = 2
        while i < n and not(n % i == 0):
            i += 1
        return not(i < n) and n != 1


def primekSzama(x: list):
    db = 0
    for i in range(len(x)):
        if primE(x[i]):
            db += 1
    return db


def main():
    x = [5, 3, 2, 8, 1]
    db = primekSzama(x)
    print("Prímek száma:", db)


main()