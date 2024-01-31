print()

adatok = []

#Fájl megnyitása
f = open("2024. 01. 31.txt", "r", encoding="UTF-8")

#Kétdimenziós lista (mátrix) létrehozása
for sor in f:
    adatok.append(sor.replace("\n", "").strip().split())
#print(adatok)

#Adatok konvertálása a mátrixban
i = 0
while i < len(adatok):
    j = 0
    while j < len(adatok[i]):
        adatok[i][j] = int(adatok[i][j])
        j += 1
    i += 1
print(adatok)

"""
1. Feladat
A példában látható módon írjuk ki az adatszerkezet tartalmát
PÉLDA:
1. adatsor: 23 10 -56 35 86 63
2. adatsor: 56 7 45 43 78 
... 
8. adatsor: 8 94 38 55
"""

i = 0
while i < len(adatok):
    print(f"\n{i + 1}. adatsor: ", end="")
    j = 0
    while j < len(adatok[i]):
        print(adatok[i][j], end=" ")
        j += 1
    print()
    i += 1

"""
2. Feladat:
Melyik a leghosszabb adatsor?
PÉLDA:
A leghosszabb adatsor: 4. (15 adat)
"""

maxÉrték = len(adatok[0])
maxHely = 0

i = 1
while i < len(adatok):
    if len(adatok[i]) > maxÉrték:
        maxÉrték = len(adatok[i])
        maxHely = i
    i += 1
print(f"\nA leghosszabb adatsor: {maxHely + 1}. ({maxÉrték} adat)")

"""
3. Feladat: (HF)
Igaz-e, hogy van olyan adatsor, amelyikben bármely két egymást követő elem értékének a különbsége 5?
PÉLDA:
Nem igaz az állítás.
vagy
Igat az állítás: 4.sor (13. és 14. elem)
"""









































#Fájl bezárása
f.close