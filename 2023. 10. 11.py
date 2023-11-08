"""
A szokásos kis pékség egy 12 elemű listában tárolja, hogy tavaly havonta mennyi volt az eladott kakaóscsigák mennyisége (havi eladott mennyiség: [0...50] db).
Írj egy programot, amelyik válaszol a következő kérdésekre:
0. Adatok megjelenítése:
Január: 27 db
Február: 21 db
...
December: 4
1. Összesen tavaly hány kakaóscsigát adott el a pékség?
2. Eladások szempontjából melyik volt a legsikeresebb és leggyengégg hónap? válasz -> hónap neve, eladott mennyiség
3. Hány olyan hónap volt, amikor 10-nél kevesebb kakaóscsigát adott el a pékség
4. Volt-e olyan hónap (ha igen, akkor melyik), amikor 7-tel osztható mennyiségű kakaóscsigát adott el a pékség? 
válasz -> ha igen: hónap neve, eladott mennyiség
ha nem: nem volt ilyen hónap
"""
#Weiner Balázs
import random

eladások = []

i = 0
hónapok = ("Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember", "Október", "November", "December")
while i < 12:
    eladások.append(random.randint(0, 50))
    print(f"{hónapok[i]}: {eladások[i]} db")
    i += 1

print()

# 1. feladat (összegzés tétele)
i = 0
összeg = 0
while i < len(eladások):
    összeg = összeg + eladások[i]
    i += 1
print(f"Az tavalyi eladott kakaóscsigák száma: {összeg} db")

print()

minHely, maxHely = 0, 0
minÉrték, maxÉrték = eladások[minHely], eladások[maxHely]

i = 1

while i < len(eladások):
    if eladások[i] < minÉrték:
        minÉrték = eladások[i]
        minHely = 1
    if eladások[i] > maxÉrték:
        maxÉrték = eladások[i]
        maxHely = 1
    i += 1
print(f"\nA legsikeresebb hónap: {hónapok[maxHely].lower()} ({maxÉrték}) db")
print(f"A leggyengébb hónap: {hónapok[minHely].lower()} ({minÉrték}) db")


db = 0
i = 0
while i < len(eladások):
    if eladások[i] < 10:
        db += 1
    i += 1
print(f"{db} hónapon volt 10-nél kevesebb eladás")

# 4 feladat (lineáris keresés [kiválasztás] programozási tétele)

i = 0
while i < len(eladások) and eladások[i] % 7 != 0:
    i += 1
if i < len(eladások): 
    print(f"\nA feltételeknek megfelelő hónap: {hónapok[i].lower()} ({eladások})")
else:
    print(f"\nNincs a feltételeknek megfelelő hónap")