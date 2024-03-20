from random import randint
from time import time

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
        vanCsere = False 
        for j in range(n-i-1):
            if x[j] > x[j+1]:
                csere(x, j, j+1)
                vanCsere = True
        if not vanCsere:
            return

def minindex(x, n=0):
    mini = n
    for i in range(n+1, len(x)):
        if x[i] < x[mini]:
            mini = i
    return mini


def rendez(x):
    for i in range(len(x)):
        j = minindex(x, i)
        csere(x, i, j)

def teszt(n):
    x = feltolt(n)
    print("Lista")

    y = x.copy()
    kezdet = time()
    rendez(y)
    veg = time()
    print("Minkiv:", veg - kezdet)

    z = x.copy()
    kezdet = time()
    buborekos(z)
    veg = time()
    print("Bubo:", veg - kezdet)


teszt(10000)