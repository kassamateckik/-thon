# Halmaz:
# 1. Elemeknek nincs sorrendje!
# 2. Egy elem csak egyszer lehet benne!
lista1 = [1, 4, 3] 
halmaz1 = {1, 4, 3}

lista2 = [1, 3, 4] 
halmaz2 = {1, 3, 4}

print("lista1 == lista2: ",lista1 == lista2)
print("halmaz1 == halmaz2: ",halmaz1 == halmaz2)

# halmaz1[1] ILYEN NINCS!! 


# rendezetten tárolja a python: (tilos kihasználni!)
print(halmaz1)
print(halmaz2)


halmaz = {5, 6, 9, 7}
halmaz.add(8)
print(halmaz) # {5, 6, 7, 8, 9}
halmaz.add(5)
print(halmaz) # {5, 6, 7, 8, 9}


# set(lista) listából halmaz