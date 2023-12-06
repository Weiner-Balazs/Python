import random

while True:
    hetek_száma = int(input("Add meg a hetek számát[1...5]: "))
    if  hetek_száma >= 1 and hetek_száma <= 5:
        break
    print("Hibás adatbevitel! Próbáld meg újra...")
    

támadások = []
i = 1
while i <= hetek_száma * 7:
    támadások.append(random.randint(3,9))
    i += 1

i = 0
while i < len(támadások) / 7:
    print(f"{i + 1}. hét: ",end="")
    j = 0
    while j < 7:
        print(támadások[i * 7 + j],end=" ")
        j += 1
    print()
    i += 1
    
összeg = 0
i = 0
while i < len(támadások):
    összeg += i
    i += 1
print(f"\nÖsszes támadás száma: {összeg} db")

i = 0
db = 0
while i < len(támadások):
    if támadások[i] > 5 and támadások[i] < 8:
        db += 1
    i += 1
print(f"\nFeltételnek megfelelő napok száma: {db} db")

napok = ("Hétfő","Kedd","Szerda","Csütörtök","Péntek","Szombat","Vasárnap")
maxhely = 0
maxérték = támadások[maxhely]

i = 1
while i < len(támadások):
    if támadások[i] >= maxérték:
        maxérték = támadások[i]
        maxhely = i
    i += 1
print(f"Egy napon megtörtént legtöbb támadás száma: {maxérték} db")
print(f"Helye: {maxhely // 7 + 1}.hét, {napok[maxhely % 7].lower()}")

voltIlyen = False

i = 0
while i < len(támadások):
    if támadások[i] % 2 == 1:
        if voltIlyen:
            if támadások[i] < minérték:
                minérték = támadások[i]
                minhely = i
        else:
            voltIlyen = True
            minhely = i
            minérték = támadások[i]
    i += 1

if voltIlyen:
    if minérték == 5:
        print("\nIgaz az állítás")
    else:
        print("\nNem igaz az állítás")
else:
    print("Nincs a feltételmek megfelelő elem a listában.")
    
i = 0
while i < len(támadások) and támadások[i] % 3 != 0:
    i += 1

if i < len(támadások):
    print("\nVan 3-mal osztható szám a listában.")
else:
    print("\nNincs a listában 3-mal osztható érték.")




i = 0
while i < len(támadások):
    if támadások[i] % 3 == 0:
        break
    i += 1

if i < len(támadások):
    print("\nVan 3-mal osztható szám a listában.")
else:
    print("\nNincs a listában 3-mal osztható érték.")

