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

def rendez(x):
    for i in range(len(x)):
        j = minindex(x, i)
        csere(x, i, j)

def main():
    x =[5, 2, 7, 1, 2, 3]
    rendez(x)
    print(x)

main()