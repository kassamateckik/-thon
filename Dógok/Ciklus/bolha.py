bolha = int(input("Bolha: "))

while bolha != 0:
    print(bolha, end=(" -> "))
    bolha *= (-1)
    maradek = bolha % 10
    if maradek == 0:
        maradek = 10
    if bolha > 0:
        bolha -= maradek
    else:
        bolha += maradek

print("0")