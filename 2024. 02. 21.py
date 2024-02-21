print()

""" 
Egy Skodákat forgalmazó vállalatnak 5 telephelye van az országban. Az elmúlt évben havonta eladott Octavia RS modellek darabszámát egy fájlban tartja nyilván.
"""

""" 
1. feladat:
Olvasd be a fájl tartalmát egy megfelelő adatszerkezetbe! Ügyelj arra. hogy a numerikus értékek számként legyenek tárolva.
"""



f = open("2024. 02. 21.txt", "r", encoding="UTF-8")

skoda = []

for sor in f:
    skoda.append(sor.replace("\n", "").strip().split())
print(skoda)

#Adatok konvertálása
i = 0
while i < len(skoda):
    j = 1
    while j < len(skoda[i]):
        skoda[i][j] = int(skoda[i][j])
        j += 1
    i += 1

""" 
2. feladat: 
A példában látható módon írjuk ki az adatokat!
PÉLDA:
Város: Budapest
Január: 2 db
Február: 4 db
Március: 1 db
...
"""

hónapok = ("Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember", "November", "December")

i = 0
while i < len(skoda):
    j = 1
    print(f"\nVáros: {skoda[i][0]}")
    while j < len(skoda[i]):
        print(f"{hónapok[j - 1]}: {skoda[i][j]} db")
        j += 1
    i += 1

""" 
3. feladat:
A példában látható módon írjuk ki a képernyőre hány olyan hónap volt, amikor egy autót sem adtak el!
"""

össz = 0
i = 0
print("\nEladásmentes hónapok városonként:")
while i < len(skoda):
    db = 0
    j = 1
    while j < len(skoda[i]):
        if skoda[i][j] == 0:
            db += 1
        j += 1
    print(f"{skoda[i][0]}: {db} hónap")
    össz += db
    i += 1

"""
4. feladat: 
Írjuk ki a képernyőre, hogy az elmúlt évben meylik hónapban adták el a legtöbb autót a kereskedés összes telephelyen!
"""

segéd = []
i = 0
print("\nHavonta eladott Octavia RS autók száma:")
while i < len(hónapok):
    összeg = 0
    j = 0
    while j < len(skoda):
        összeg += skoda[j][i + 1]
        j += 1
    segéd.append(összeg)
    print(f"{hónapok[i]}: {összeg} db")
    i += 1

maxÉrték = segéd[0]
maxHely = 0
i = 1
while i < len(segéd):
    if segéd[i] > maxÉrték:
        maxÉrték = segéd[i]
        maxHely = i
    i += 1
print(f"Legsikeresebb hónap: {hónapok[maxHely].lower()} ({maxÉrték} db)")



"""
5. feladat (HF)
Igaz-e az az állítás, hogy minden telephelyen volt legalább 3 db olyan hónap, amikor legalább 3 autót eladtak?
"""
f.close()