szamok = []
vége = False
"""
while not vége: 
    sz = int(input("Adj meg egy természetes számot [0: kilépés]: "))
    if sz == 0:
        vége = True
    else:
        szamok.append(sz)
"""
while True:
    sz = int(input("Adj meg egy természetes számot [0: kilépés]: ")) #bevitel
    if sz == 0: #leellenőrzi
        break
    else: 
        szamok.append(sz) #hozzáadja

i = 0
print("A megadott számsor: ", end="")
while i < len(szamok):
    print(szamok [i], end=" ") #kiírja
    i += 1

print()
print("A megadott számsor: ", end="")
for e in szamok:
    print(e, end=" ")
print()

összeg = 0
i = 0
while i < len(szamok):
    összeg = összeg + szamok[i]
    i += 1
    print(f"A számsor elemeinek összege: {szamok}")


"""
minhely = 0
minérték = szamok[minhely]

maxhely = 0
maxérték = szamok[maxhely]
i = 1
while i < len(szamok):
    if szamok[i] < minérték:
        minérték = szamok[i]
        minhely = 1
    if szamok[i] > maxérték:
        maxérték = szamok[i]
        maxhely = 1
    i += 1
    print(f"A legkisebb elem értéke: {minérték}")
    print(f"A legnagyobb elem értéke: {maxérték}") """