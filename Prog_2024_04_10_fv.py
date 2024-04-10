# Függvények

def első():
    #Függvénytörzs
    print("Ez az első függvényem :)")
    print("De jóóóóóóóóóóóó :D")
    print("Tegnap döntetlen lett a Real Madrid meccse...")

def üzenet(szöveg):
    print(f"\nEz az én üzenetem: {szöveg}")
    print()

def feladat1(szám1, szám2):
    print(f"{szám1} + {szám2} = {szám1 + szám2}")
    print(f"{szám1} - {szám2} = {szám1 - szám2}")
    print(f"{szám1} * {szám2} = {szám1 * szám2}")
    szám1 = 23
    szám2 = 45
    print()

def feladat2(elemszám, lst):
    import random
    for _ in range(elemszám):
        lst.append(random.randint(0, 1))

def feltölt(elemszám):
    import random
    lst = []
    for _ in range(elemszám):
        lst.append(random.randint(0, 1))
    # Függvény értékének visszaküldése a hívás helyére
    return lst

def max(lst):
    