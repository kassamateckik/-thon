def benne(x, lista):
    i = 0
    while i < len(lista) and not(lista[i] == x):
        i += 1 
    return i < len(lista)
    # if i < len(lista):            
    #     return True       Ha igaz -> igaz
    # else: 
    #     return False      Ha hamis -> hamis


def egyediek(lista):
    halmaz = []
    for i in range(len(lista)):
        if not(benne(lista[i], halmaz)):
            halmaz.append(lista[i])
    return halmaz


def main():
    lista = [3, 5, 2, 5, 2, 3, 3, 5, 2, 5, 3, 2, 2, 3]
    halmaz = egyediek(lista)
    print(lista, halmaz)


main()