print()

ösvények = []
f = open("osvenyek.txt", "r", encoding="UTF-8")
for sor in f:
    ösvények.append(sor.replace("\n", "").strip().split())
f.close()


dobások = []
segéd = []
f = open("dobasok.txt", "r", encoding="UTF-8")
for sor in f:
    segéd.append(sor.replace("\n", "").strip().split())
f.close

i = 0
while i < len(segéd[0]):
    dobások.append(int(segéd[0][i]))
    i += 1

print("2. feladat")

print(f"A dobások száma: {len(dobások)}")
print(f"Az ösvények száma: {len(ösvények)}")

print()

print("3. feladat")
maxÉrték = len(ösvények[0])
maxHely = 0
i = 1
while i < len(ösvények):
    if len(ösvények[i]) > maxÉrték:
        maxÉrték = len(ösvények[i])
        maxHely = i
    i += 1
print(f"Az egyik leghosszabb a(z) {maxHely}. ösvény, hossza: {maxÉrték}")

print("4. feladat")
sorszám = int(input("Adja meg egy ösvény sorszámát! "))
játékosok = int(input("Adja meg a játékosok számát! "))












































































