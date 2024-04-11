from random import randint

def csere(x, i, j):
    a = x[i]
    x[i] = x[j]
    x[j] = a

def minindex(x, n=0):
    mini = n
    for i in range(n+1, len(x)):
        if x[i] < x[mini]:
            mini = i
    return mini

def maxindex(x, n=0):
    mini = n
    for i in range(n+1, len(x)):
        if x[i] > x[mini]:
            mini = i
    return mini

def rendez(x, jel):
    if jel == "+":
        for i in range(len(x)):
            j = minindex(x, i)
            csere(x, i, j)
    else:
        for i in range(len(x)):
            j = maxindex(x, i)
            csere(x, i, j)

def feltolt(n):
    x = []
    for i in range(n):
        r = randint(1, 9)
        x.append(r)
    return x


def main():
    x =[5, 2, 7, 1, 2, 3]
    rendez(x, "+")
    print(x)
    rendez(x, "-")
    print(x)

    x = feltolt(100)
    print(x)
    rendez(x, "+")
    print(x)
    rendez(x, "-")
    print(x)


main()