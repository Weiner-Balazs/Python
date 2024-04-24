import Prog_2024_04_24_fv

"""
Hozzunk étre egy 5 sorból és 8 oszlopból álló, véletlenszerűen 0-ákat és 
1-eket tartalmazó mátrixot. Írjunk egy programot (függvényt használjunk hozzá),
amelyik megmondja, hogy melyik sorban van a legtöbb 1-es
"""
"""
mátrix = Prog_2024_04_24_fv.létrehoz(5, 8, 0, 1)

maxÉrték = Prog_2024_04_24_fv.egyesekSzáma(mátrix[0])
maxhely = 0

i = 1
while i < len(mátrix):
    t = Prog_2024_04_24_fv.egyesekSzáma(mátrix[i])
    if t > maxÉrték:
        maxÉrték = t
        maxhely= i
    i += 1

print(f"\nLegtöbb 1-es: {maxhely + 1}. sor ({maxÉrték})")

"""

"""
1. Feladat
Írjunk függvényt, amelyik beolvassa a fájl tartalmát egy változóba
"""

eladások = Prog_2024_04_24_fv.fájl("2024.04.24.txt")
print(eladások)

"""
2. Feladat
Add meg a város sorszámát [1...4]: 7
Hibás adatbevitel! Próbáld újra...
Add meg a város sorszámát [1...4]: 3
Debrecen múlt heti eladásai
Hétfő: x db
Kedd: x db
...
Vasárnap x db
"""

while True:
    adat = int(input(f"Add meg a város sorszámát [1...{len(eladások)}]: "))
    if adat >= 1 and adat <= 4:
        break
    print("Hibás adatbevitel! Próbáld újra...")

Prog_2024_04_24_fv.kiír(adat - 1)

print(f"{eladások[városok][1]}")

print()