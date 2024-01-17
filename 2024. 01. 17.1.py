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

összeg = 0
i = 1
for sor in f:
    print(f"{i}. sor: {int(sor)}")
    összeg += int(sor)
    i += 1
print(f"A fájlban lévő számok összege: {összeg}")

"""
Adj meg egy egész számot: -34
A -34 nem szerepel a fájlban.
vagy 
A -34 helye a fájlban: 8. sor
"""

szám = int(input("Adj meg egy egész számot: "))

i = 0

#Fájl bezárása
f.close()

print()
"""
    "python.terminal.executeInFileDir": true,
EOF : End of File
"""