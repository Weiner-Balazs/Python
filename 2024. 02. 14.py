print()

adatok = []

f = open("2024. 02. 14.txt", encoding="UTF-8")

for sor in f:
    adatok.append(sor.replace("\n", "").strip().split())


i = 0
while i < len(adatok):
    j = 1 
    while j < len(adatok[i]):
        adatok[i][j] = int(adatok[i][j])
        j += 1
    i += 1

"""
1. feladat:
Olvassuk be minden süti egységárát és tároljuk el ezeket az értékeket egy listában!
PÉLDA:
Kókuszgolyó: 310
Gerbaud: 990
...
Málnás sajttorta: 1210
Túrógombóc torta: 1350
"""

árak = []
 
i = 0
while i < len(adatok):
    print(adatok[i][0].replace("_", " ") + ": ", end="")
    ár = int(input())
    árak.append(ár)
    i += 1

"""
2. feladat:
A példában látható módon írjuk ki, hogy az egyes tortákból hány darabot adott el a cukrászda a vizsgált időszakban és ebből mennyi bevétele származott
PÉLDA:
Kókuszgolyó: 567 db (134578 ft)
"""

print()

összeg = 0
i = 0
while i < len(adatok):
    heti = 0
    j = 1 
    print(adatok[i][0].replace("_", " ") + ": ", end="")
    while j < len(adatok[i]):
        heti += adatok[i][j]
        j += 1
    print(f"{heti} db ({heti * árak[i]} Ft)")
    összeg += heti * árak[i]
    i += 1

print(f"\nÖsszes bevétel: {összeg} Ft")



"""
3. feladat:
Igaz az az álítás, hogy szombaton a kókuszgolyó termelte a legkisebb bevételt a cukrászda számára?
PÉLDA:
Szombaton keletkezett bevételek süteményenként:
Kókuszgolyó: 36500 Ft
"""




"""
4. feladat (HF):
Melyik volt a legforgalmasabb nap az elmúlt héten (legnagyobb bevétel)?
Legforgalmasabb nap: vasárnap (986310)
"""

napok = ("Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap")

































f.close