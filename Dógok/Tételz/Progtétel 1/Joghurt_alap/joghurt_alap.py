napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat"]
epres = [30, 20, 12, 27, 29, 23]
barackos = [18, 25, 19, 22, 21, 12]

n = len(napok)
# F1
print("1. Bevétel epres joghurtokból a hét egyes napjain: ")
for i in range(n):
    print(f"   - {napok[i]}: {epres[i] * 189}")

# F2
db = 0
for i in range(n):
    if epres[i] > barackos[i]:
        db += 1
print(f"2. Ennyi napon fogyott több epres, mint barackos: {db}")

# F3
eperossz = 0
barackossz = 0
for i in range(n):
    eperossz += epres[i]
    barackossz += barackos[i]
ossz = eperossz + barackossz
szazalek = (eperossz / ossz) * 100
print(f"3. A vásárolt joghurtok {round(szazalek, 2)}%-a volt epres!")
# F4
minelter = abs(epres[0] - barackos[0])
for i in range(1, n):
    elter = abs(epres[i] - barackos[i])
    if elter < minelter:
        minelter = elter
print(f"4. Legkisebb eltérés az epres és barackos joghurtok mennyiségében: {minelter}")