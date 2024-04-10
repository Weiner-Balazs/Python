# Föprogram

import Prog_2024_04_10_fv

# Függvény meghívása (használatba vétele)
# Prog_2024_04_10_fv.első()

"""
Prog_2024_04_10_fv.üzenet("A Bayer meccse is döntetlen volt...")
Prog_2024_04_10_fv.üzenet(2)
Prog_2024_04_10_fv()
"""
"""
Írjunk függvényt, amelyik a paraméterül kapott két számnak kiírja az összegét, különbségét, szorzatát
"""

"""
szám1 = 6
szám2 = 7

Prog_2024_04_10_fv.feladat1(szám1, szám2)
Prog_2024_04_10_fv.feladat1(-4, 8)
print(szám1, szám2)
#Érték szerinti paraméter átadás
"""


"""
Írjunk függvényt, amelyik a paraméterül megadott elemszámú, véletlenszerűen 0-ákat és 1-eket tartalmazó listát generál!
"""

"""
számok = []
számok1 = []
Prog_2024_04_10_fv.feladat2(15, számok)
Prog_2024_04_10_fv.feladat2(45, számok1)
print(számok)
print(számok1)
"""

számok = Prog_2024_04_10_fv.feltölt(20)
print(számok)
print(Prog_2024_04_10_fv.feltölt(5))

"""
(HF):
Hozzunk étre egy 5 sorból és 8 oszlopból álló, véletlenszerűen 0-ákat és 
1-eket tartalmazó mátrixot. Írjunk egy programot (függvényt használjunk hozzá),
amelyik megmondja, hogy melyik sorban van a legtöbb 1-es
"""

import random
lista = []

