ora = 8
perc = 0

while ora < 18:
    if perc + 25 >= 60:
        perc = perc + 25 -60
        ora += 1
    else:
        perc += 25
    if ora < 10:
        orakiir = f"0{ora}"
    else:
        orakiir = ora
    if perc < 10:
        perckiir = f"0{perc}"
    else:
        perckiir = perc

    print(f"{orakiir}:{perckiir}")
    