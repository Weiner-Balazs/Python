# Fájlkezelés  
print()

#Fájl megnyitás
f = open("2024. 01. 17.2.txt", "r", encoding="UTF-8")

"""
#Fájl olvasása
adat = f.read(8)
print(type(adat))
print(adat)

adat += f.read(1)
print(adat)
"""

"""
#Teljes fájl beolvasása
print(f.readlines())
"""

"""
#Fájl feldolgozása soronként
for sor in f:
    print(sor.replace("\n", ""))

#Fájlmutató mozgatása
f.seek(5)

for sor in f:
    print(sor.replace("\n", ""))
"""

"""
Írjuk ki a fájl tartalmát a látható módon és mondjuk meg hogy mennyi fájlban lévő számok összege!
PÉLDA:
1. sor: 1
2. sor: 2
... 
10. sor: 10
A fájlban lévő számok összege: 55
"""
"""
összeg = 0
i = 1
for sor in f:
    print(f"{i}. sor: {int(sor)}")
    összeg += int(sor)
    i += 1
print(f"A fájlban lévő számok összege: {összeg}")
"""
"""
Adj meg egy egész számot: -34
A -34 nem szerepel a fájlban.
vagy 
A -34 helye a fájlban: 8. sor
"""


"""
j = 1
v = False

szám = int(input("Adj meg egy egész számot: "))

for adat in f:
    if int(adat) == szám:
        v = True
        break
    j += 1

if v: 
    print(f"\nA(z) {szám} helye a fájlban: {j}. sor")
else:
    print(f"\nA {szám} nem szerepel a fájlban.")
"""

"""
    "python.terminal.executeInFileDir": true,
EOF : End of File
"""
"""
A példában látható módon írjuk ki a képernyőre a fájlban látató lekgissebb és legnagyobb szám értékét és helyét?
PÉLDA:
Legkisseb szám értéke: -969, helye: 9. sor 
Legnagyobb szám értéke: 4456: helye: 4. sor
"""
"""
kh = 1
ké = f(kh)
nh = 1
né = f(nh)

for i in f:
    if f(i) < ké:
        ké == f(i)
        kh == 1
    if f(i) > né:
        né == f(i)
        nh == 1
    print("")
"""

"""
minérték = int(f.readline())
maxérték = minérték
minhely, maxhely = 1, 1
sorszám = 2

for adat in f:
    if int(adat) < minérték:
        minérték = int(adat)
        minhely = sorszám
    if int(adat) > maxérték:
        maxérték = int(adat)
        maxhely = sorszám
    sorszám += 1


print(f"Legkisseb szám értéke: {minérték}, helye: {minhely}. sor")
print(f"Legnagyobb szám értéke: {maxérték}: helye: {maxhely}. sor")
"""

"""
A példában látható módon írjuk ki a képernyőre a fájlban található legnagyobb negatív szám értékét és helyét!
PÉLDA:
A legnagyobb negatív szám értéke: -3, helye 7. sor
vagy
Nincs negatív szám
"""


volt = False
i = 1

for adat in f:
    if int(adat) < 0:
        if volt:
            #Volt már korábban negatív szám a fájlban
            if int(adat) > maxérték:
                maxérték = int(adat)
                maxhely = i
        else: 
            #Ez az első negatív szám a fájlban
            volt = True
            maxérték = int(adat)
            maxhely = i
    i += 1

if volt: 
    print(f"Legnagyobb negatív szám értéke: {maxérték}: helye: {maxhely}. sor")
else:
    print("Nincs negatív szám")


#Fájl bezárása
f.close()

print()