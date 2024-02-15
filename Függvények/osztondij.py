'''
4,5-től : 60000
4-től : 42000
3,5-től : 28000
3-tól : 16000
alatta: 8000
'''

def osztondij(a):
    if a >= 4.5:
        dij = 60000
    elif a >= 4:
        dij = 42000
    elif a >= 3.5:
        dij = 28000
    elif a >= 3:
        dij = 16000
    else:
        dij = 8000
    return dij

print(osztondij(4.8))
print(osztondij(2.9))
print(osztondij(3.77))
print(osztondij(3.13))