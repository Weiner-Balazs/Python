

"""
Írj egy programot, amelyik ciklus segítségével kiírja 1-től 10-ig egymás mellé az egész számokat
PÉLDA:
A számsor: 1 2 3 4 5 6 7 8 9 10
"""
i = 1
print("A számsor: ", end="")
while i  <= 10:
    print(i, end=" ")
    i += 1
print()

print("A számsor: ", end="")
for i in range(1, 11):
    print(i, end=" ")
print()
"""
Add meg a kezdőértéket [1...5]: 7
Hibás adatbevitel! Próbáld újra...
Add meg a kezdőértéket [1...5]: 4
Add meg a befejező értéket [6...10]: 8
Add meg a lépésközt [1...3]: 2
A generált számsor: 4 6 8

"""
while True:
    kezdö = int(input("Add meg a kezdőértéket [1...5]: "))
    if kezdö >= 1 and kezdö <= 5:
        break
    print("Hibás adatbevitel! Próbáld újra...")

helyesadatbevitel = False

while not helyesadatbevitel:

    befej = int(input("Add meg a befejező értéket [6...10]: "))
    if befej < 6 or befej > 10:
        print("Hibás adatbevitel! Próbáld újra...")
    else:
        helyesadatbevitel = True
    
while True:
    lép = int(input("Add meg a lépésközt [1...3]: "))
    if lép >= 1 and lép <= 3:
        break
    print("Hibás adatbevitel! Próbáld újra...")
    
print("A generált számsor: ", end="")
i = kezdö
while i <= befej:
    print(i, end=" ")
    i += lép
    


"""
'fizz-buzz' játék
1
2
fizz
4
buzz
fizz
7
8
fizz
"""
"""
i = 1
while i <= 100:
    if i / 3 == 1: 
        print("fizz")
    if i / 5 == 1:
        print("buzz")
    else: print(i)
    i += 1
    """