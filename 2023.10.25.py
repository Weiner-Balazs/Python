""" 
Adott egy 14 elemű lista, amiben a Sugar! cukrászda tartja nyílván az elmúlt két hétben eladott Nutella torták számát. A napi eladásokat most egy 0 és 9 közötti véletlenszám reprezentálja!
"""

""" 
1. feladat:
Töltsd fel a listát a megadott értékű elemekkel!
"""
#1
import random

torta = []
i = 1
while i <= 7:
    torta.append(random.randint(0,9))
    i += 1


torta.clear()


for e in range(0,14):
    torta.append(random.randint(0,9))

""" 
2. feladat:
Összesen hány Nutella tortát adott el a cukrászda a megadott időszakban?
"""
#2
összeg = 0
i = 0
while i < len(torta):
    összeg += torta[i]
    i += 1
print(f"Ebben az időszakban eladott torták száma: {összeg}")

összeg = 0
for e in torta:
    összeg += e 
print(f"Ebben az időszakban eladott torták száma: {összeg}")

""" 
3. feladat:
Bővítsük az adatbázisunkat 4 hetesre!
"""
#3
for e in range(0,14):
    torta.append(random.randint(0,9))

""" 
4. feladat:
Írjuk ki a lista elemeit a következő módon
1. hét eladásai:
Hétfő: 6 db
Kedd: 4 db
Szerda: 0 db
"""
#4
napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

i = 0
while i < len(torta) / 7:
    print(f"\n{i + 2}. hét eladásaid:")
    # Egy hét adatainak kiírása
    j = 0
    while j < 7:
        print(f"{napok[j]}: {torta[i * 7 + j]} db")
        j += 1
    i += 1


""" 
Hány olyan nap volt a vizsgált időszakban, amikor az egy napon eladott maximális Nutella torta  mennyiségénél eggyel kevesebb Nutella tortát adott el a cukrászda
"""

maxÉrték = torta[0]
i = 1
while i < len(torta):
    if torta[i] > maxÉrték:
        maxÉrték = torta[i]
    i += 1
print(f"\nLegtöbb eladás: {maxÉrték}")

maxÉrték = torta[0]
for e in torta:
    if e > maxÉrték:
        maxÉrték = e
print(f"Legtöbb eladás: {maxÉrték} db")

db = 0
i = 0

while i < len(torta):
    if torta[i] == maxÉrték-1:
        db += 1
    i += 1
print(f"\nA feltételeknek megfelelő elemek száma: {db} db")

db = 0 
for e in torta:
    if e == maxÉrték - 1:
        db += 1
print(f"A feltételeknek megfelelő elemek száma: {db} db")

print()