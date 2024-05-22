import Prog_2024_05_22_fv

print()

"""
1. feladat:
Tárold el Bogi dobásait egy megfelelő adatszerkezetbe!
"""
import random
dobások = []
for _ in range(14):
    dobások.append(random.randint(1, 6))
print(dobások)

#dobások = [6, 1, 3, 3, 2, 4, 4, 4, 5, 1, 6, 6, 3, 2]

"""
2. feladat:
A példában látható módon írjuk ki a képernyőre a dobások eredményeit!
PÉLDA:
1. nap: 6
2. nap: 1
3. nap: 3
...
14. nap: 2
"""

i = 0
while i < len(dobások):
    print(f"{i + 1}. nap: {dobások[i]}")
    i += 1

"""
3. feladat:
A példában látható módon írjuk ki a képernyőre, hogy a vizsgált időszakban Bogi hányszor dobott egymás után 2 db 4-est!
PÉLDA:
Egymás utáni 2 db 4-esek száma: 2 db
vagy 
Nem volt 2 db egymás utáni 4-es a dobások között.
"""

db = 0
i = 0 
while i < len(dobások):
    if dobások[i] == 4 and dobások[i + 1] == 4:
        db += 1
    i += 1
if db > 0:
    print(f"Egymás utáni 2 db 4-esek száma: {db}")
else:
    print("Nem volt 2 db egymás utáni 4-es a dobások között.")
print()

"""
4. feladat:
A példában látható módon írjuk ki a képernyőre, hogy a vizsgált időszakban az egyes számokból Bogi összesen hányat dobott!
PÉLDA:
1: 2 db
2: 2 db 
3: 3 db
4: 3 db
5: 1 db
6: 3 db
"""

hiszt = [0 for _ in range(6)]

i = 0 
while i < len(dobások):
    hiszt[dobások[i] - 1] += 1
    i += 1

i = 0 
while i < len(hiszt):
    print(f"{i + 1}: {hiszt[i]} db")
    i += 1

print()
"""
5. feladat:
Minden egyes pötty a dobokockán 250 Ft-ot ér. Mennyi pénzt utal Bogi a Suhanj! alapítványnak?
"""

i = 0
ft = 0
while i < len(dobások):
    ft += dobások[i] * 250
    i += 1
print(f"Bogi {ft} Ft-ot gyűjtött az alapítványnak")

"""
6. feladat (HF):
Írj függvényt, amelyik beolvassa a forrésfájl tartalmát egy megfelelő 
adatszerkezetbe! A fájlban szereplő számok numerikus értékként legyenek 
eltárolva!
"""

lista = Prog_2024_05_22_fv.fájl("2024. 05. 22.txt")


"""
7. feladat (HF):
Hányadik napon dobták a legtöbb 6-ost a gyerekek?
"""