print()

f = open("adat.txt", "r", encoding="UTF-8")

adatok = []

for sor in f:
    adatok.append(sor.replace("\n", "").split())

print("3. feladat")

i = 0
while i < len(adatok):
    i += 1

print(f"Jancsi és Juliska {i} napon keresztül tátszottak pénzfelddobósat")

#print(f"Jancsi és Juliska {len(dobások)} napon keresztül tátszottak pénzfelddobósat")

print()

print("4. feladat")

össz = 0
i = 0
while i < len(adatok):
    print(f"{i + 1}. nap:", end=" ")
    összeg = 0
    j = 0
    while j < len(adatok[i]):
        összeg += 1
        j += 1
    össz += összeg
    print(f"{összeg} dobás")
    i += 1
print(f"Összesen {össz} dobás volt a játék teljes ideje alatt")

"""
ssz = 1
összeg = 0
for sor in dobások:
    összeg += len(sor)
    print(f"{ssz}. nap: {len(sor)} dobás")
    ssz += 1
print(f"Összesen {összeg} dobás volt a játék teljes ideje alatt.")
"""

print()

print("5. feldat")
"""
minÉ = 0

i = 1
while i < len(adatok):
    if minÉ <= len(adatok):
        i += 1
        minÉ += i
print(f"Leghosszabb játék: {i}. nap ({minÉ} dobás)")
"""

maxÉ = len(adatok[0])
maxH = 0
i = 1 
while i < len(adatok):
    if len(adatok[i]) > maxÉ:
        maxÉ = len(adatok[i])
        maxH = i
    i += 1
print(f"Leghosszabb játék: {maxH + 1}. nap ({maxÉ} dobás)")

print()

print("6. feladat")
volt = False
nap = 1
for sor in adatok:
    i = 0
    while i < len(sor) - 3:
        if sor[i] == "F" and sor[i + 1] == "F" and sor[i + 2] == "F" and sor[i + 3] == "F":
            volt = True
            break
        i += 1
    if volt:
        break
    nap += 1
if volt:
    print(f"Volt a felrételnek megfelelő nap ({nap}.) a játék teljes ideje alatt.")
else:
    print("Nem volt a feltételnek megfelelő nap a játék teljes ideje alatt.")
f.close()