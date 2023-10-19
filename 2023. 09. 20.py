"""

Van egy kis pékség, ahol az elmúlt héten naponta eladott kókuszgolyó mennyiséget egy adatszerkezetben tartják nyílván.
Az eladott kókuszgolyók számát reprezemtálja egy 5 és 15 közötti véletlen szám.
"""



import random



eladások = []


i = 0
while i < 7:
    eladások.append(random.randint(5, 15))
    i += 1
print(f"A héten eladott kókuszgolyók száma: {eladások}")

eladások.clear()

for i in range (7):
    eladások.append(random.randint(5, 15))
print(f"A héten eladott kókuszgolyók száma: {eladások}")

"""
Írjuk ki a lista elemeit a következő módon:
1. elem: 6 db
2. elem: 11 db
...
7. elem 12 db
"""
i = 0
while i < len(eladások):
    print(f"{i + 1}. elem: {eladások[i]} db")
    i += 1

print()

for i in range (len(eladások)):
    print(f"{i + 1}. elem: {eladások[i]} db")


napok = ("Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap")
i = 0
while i < len(eladások):
    print(f"{napok[i]}: {eladások[i]} db")
    i += 1

print()

for i in range (len(eladások)):
    print(f"{napok[i]}: {eladások[i]} db")

"""
Hány kókuszgolyót adott el a pékség a múlt hétem?
PÉLDA:
Eladott kókuszgolyók mennyisége: 72 db
"""

print()

összeg = 0
i = 0
while i < len(eladások):
    összeg = összeg + eladások[i]
    i += 1 # értékadás
print(f"Eladott kókuszgolyók mennyisége: {összeg} db")

összeg = 0
for elem in eladások:
    összeg += elem
print(f"Eladott kókuszgolyók mennyisége: {összeg} db")

"""
Melyik napon adta el a pékség a legkevesebb kókuszgolyót?
PÉLDA:
Nap: szerda, eladott mennyiség: 5 db
"""


minhely = 0
minérték = eladások[minhely]

i = 1

while i < len(eladások):
    if eladások[i] < minérték:
        minérték = eladások[i]
        minhely = 1
    i += 1
print(f"Nap: {napok[minhely].lower()}, eladott mennyiség: {minérték} db ")









