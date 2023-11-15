""" 
A kedvenc Sugar! cukrászdánk most nem a Nutella, hanem a Fudgy Chocolate Cake torták eladásainak alakulását szeretné elemezni. Ehhez az elmúlt 12 hét adatai állnak rendelkezésrünkre (a napi eladásokat most reprezentálja egy 3 és 9 közötti véletlenszám)
"""

""" 
A feladatokat most kétdimenziós lista (mátrix) segítségével oldjuk meg!
"""

import random

eladások = []
hét = []
i = 1
while i <= 12:
    j = 1
    while j < 7:
        hét.append(random.randint(3, 9))
        j += 1
    eladások.append(hét)
    i += 1
print(eladások)
""" 
Írjuk ki a mátrix tartalmát a példában látható módon!
PÉLDA
1. hét: [3, 7, 8, 4, 5, 5, 6]
2. hét: [4, 5, 6, 3, 3, 9, 4]
... 
12. hét: [4, 5, 6, 3, 3,  9, 4]
"""

i = 0
while i < len(eladások):
    print(f"{i + 1}. hét {eladások[i]}")
    i += 1
""" 
Írjuk ki a mátrix tartalmát a látható módon!
PÉLDA:
1. hét eladásai:
Hétfő: 3 db
"""

napok = ("Hétfő" "Kedd" "Szerda" "Csütörtök" "Péntek" "Szombat" "Vasárnap")

i = 0
while i < len(eladások):
    print(f"\n{i + 1}. hét eladásai:")
    j = 0
    while j < len(eladások[i]):
        print(f"{napok[j]}: {eladások[i][j]} db")
        j += 1
    i += 1