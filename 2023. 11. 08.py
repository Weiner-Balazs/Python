import random

támadások = []

i = 1
while i <= 56:
    támadások.append(random.randint(5,50))
    i += 1

támadások.clear()

for _ in range(0,56):
    támadások.append(random.randint(5,50))


""" 
2. feladat:
Írjuk ki az adatszerkezet tartalmát a következő módon:
Támadások száma a(z) 1. héten:
Hétfő: 34 támadás
Kedd: 27 támadás
... 
Vasárnap: 12 támadás
"""

napok = ("Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap")
i = 0
while i < len(támadások) / 7:
    print (f"\nTámadások száma a(z) {i + 1}. héten:")
    j = 0
    while j < 7:
        print(f"{napok[j]}: {támadások[i * 7 + j]} támadás")
        j += 1
    i += 1

""" 
Hány támadás volt a teljes időszakban?
"""

összeg = 0
i = 0
while i < len(támadások):
    összeg += támadások[i]
    i += 1


print()
print(f"{összeg} támadás volt összesen")


összeg = 0
for t in támadások:
    összeg += t
print()
print(f"{összeg} támadás volt összesen.")
print()

""" 
Hány olyan nap volt a teljes időszakban, amikor a napi támadások száma 20 és 30 közé esik?
"""

db = 0
i = 0 
while i < len(támadások):
    if támadások[i] >= 20 and támadások[i] <= 30:
        db += 1
    i += 1
print(f"\n{db} nap volt amikor 20 és 30 között volt a támadások száma")

""" 
Írjuk ki, hogy az egyes heteken összesen mennyi támadás érte a lázadó seregeket!
PÉLDA:
1. hét: 234 támadás
2. hét: 137 támadás
... 
8. hét: 86 támadás
"""

heti = []
i = 0
while i < len(támadások) / 7:
    összeg = 0
    j = 0
    while j < 7:
        összeg += támadások[i * 7 + j]
        j += 1
    print(f"{i + 1}. hét: {összeg} támadás")
    heti.append(összeg)
    i += 1
""" 
melyik héten érte a legkevesebb támadás a lázadó seregeket?
"""

minHely = 0
minÉrték = heti[minHely]

i = 1 
while i < len(heti):
    if heti[i] < minÉrték:
        minÉrték = heti[i]
        minHely = 1
    i += 1
print(f"\nA legkevesebb támadás: {minÉrték} db ({minHely + 1}). hét")

""" 
Melyik héten volt a legkevesebb 250-nél több támadás egy héten?
PÉLDA: 
Legkevesebb 250-nél több támadás: 6. hét (261 támadás)
vagy
Nincs a feltételnek megfelelő támadásszám!
"""
minHely250 = 0
minÉrték250 = heti[minHely250]

i = 1