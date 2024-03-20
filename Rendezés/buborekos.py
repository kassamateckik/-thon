from random import randint

def feltolt(n):
    x = []
    for i in range(n):
        r = randint(1, 9)
        x.append(r)
    return x

def csere(x, i, j):
    a = x[i]
    x[i] = x[j]
    x[j] = a

def buborekos(x):
    n = len(x)
    for i in range(n):
        # vanCsere = False 
        for j in range(n-i-1):
            if x[j] > x[j+1]:
                csere(x, j, j+1)
        #         vanCsere = True
        # if not vanCsere:
        #     return

def main():
    x = [5, 2, 7, 1, 2, 3]
    buborekos(x)
    print(x)

    x = feltolt(100000)
    buborekos(x)
    print(x)

main()