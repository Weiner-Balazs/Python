print()

""" 
A Sugar! cukrászdában nyilván tartják az elmúlt 8 hét Fudgy Chocolate Cake torták eladását. A napi eladások most reprezentálja egy 0 és 9 közötti véletlen szám.
"""

""" 
1. feladat:
Tároljuk ez az adatokat egy 2 dimenziós listában!
"""
"""
import random

eladások = []
hét = []

for e1 in range(8):
    for e2 in range(7):
        hét.append(random.randint(0, 9))
    eladások.append(hét.copy())
    hét.clear()
print(eladások)
"""

import random
eladások = []

i = 1
while i <= 8:
    j = 1
    hét = []
    while j <= 7:
        hét.append(random.randint(0, 9))
        j += 1
    eladások.append(hét)
    i += 1
print(eladások)

""" 

2. feladat:
Írjuk ki az eladások lista tartalmát a példában látható módon!
PÉLDA:
1. hét: [1, 2, 5, 7, 0, 0, 6]
2. hét: [0, 0, 2, 6, 6, 1, 3]
... 
8. hét: [4, 7, 9, 9, 1, 2, 0]
"""

i = 0
while i <= len(hét):
    print(f"{i + 1}. hét: {eladások[i]}")
    i += 1

""" 

3. feladat:
Írjuk ki az eladások lista tartalmát a példában látható módon!
PÉLDA:
1. hét eladásai:
Hétfői: 1 db
Kedd: 2 db 
... 

2. hét eladásai:
Hétfő: 0 db
Kedd: 0 db
... 

8. hét eladásai:
Hétfő: 4 db
Kedd: 7 db
... 
Vasárnap: 0
"""
print()

napok = ("Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap")

i = 0
while i <= len(hét):
    print(f"\n{i + 1}. hét eladásai:")
    j = 0
    while j < len(eladások[i]):
        print(f"{napok[j]}: {eladások[i][j]} db")
        j += 1
    i += 1

""" 
4. feladat:
Mennyi volt az egyes heteken és a teljes vizsgált intervallumban az eladott torták száma?
PÉLDA:
1. hét: 35 db
2. hét: 19 db
... 
8. hét: 46 db
Összesen eladott torta mennyisége: 367 db
"""
print()


teljesösszeg = 0
i = 0
while i < len(eladások):
    összeg = 0
    j = 0
    while j < len(eladások[i]):
        összeg += eladások[i][j]
        j += 1
    print(f"{i + 1}. hét: {összeg} db")
    teljesösszeg += összeg
    i += 1
print(f"Összesen eladott torta mennyisége: {teljesösszeg} db")

""" 
5. feladat:
Hány olyan hét volt a vizsgált időszakban, amikor legalább 40 tortát adott el a cukrászda egy héten?
PÉLDA:
Feltételeknek megfelelő hetek száma: 2 db
"""

i = 1
while i <= len(eladások):
    if összeg >= 40:
        print(f"Feltételeknek megfelelő hetek száma: {i} db")
    else: 
        print("Nem volt a feltételeknek megfelelő hét")
    i += 1












































































