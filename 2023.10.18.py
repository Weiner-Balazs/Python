"""

Add meg a csillagok számát [3...20]: 6
******
"""
"""
while True:
    csillag = int(input("Add meg a csillagok számát [3..20]: "))
    if csillag >= 3 and csillag <= 20:
        break
    print("Hibás adatbevitel, próbáld meg újra")

i = 1
while i <= csillag:
    print("*", end="")
    i += 1
print()
"""

"""
Add meg a minta hosszát [3...20]: 6
*----*
"""
"""
while True: 
    csillag = int(input("Add meg a minta hosszát [5...20]: "))
    if csillag >= 5 and csillag <= 20:
        break
    print("Hibás adatbevitel, próbáld meg újra")

i = 1 
print("*", end="")
while i <= csillag - 2:
    print("-", end="")
    i += 1
print("*")

i = 1 
while i <= csillag:
    if i == 1 or i == csillag:
        print("*", end="")
    else:
        print("-", end="")
    i += 1
print()


i = 1 
print("**", end="")
while i <= csillag -4:
    print("-", end="")
    i += 1
print("**")

i = 1
while i <= csillag:
    if i == 1 or i == 2 or i == csillag - 1 or i == csillag:
        print("*", end="")
    else:
        print("-", end="")
    i += 1
print()

#Picit sufnituning megoldás

i = 1
while i <= csillag:
    if i == 1 or i == csillag - 1:
        print("**", end="")
        i += 1
    else:
        print("-", end="")
    i += 1
print()
"""
while True:
    sorok = int(input("Add meg a sorok számát [3...10]: "))
    
    if sorok >= 3 and sorok <= 10:
        break
    print("Hibás adatbevitel, próbáld meg újra")

while True:
    oszlopok = int(input("Add meg az oszlopok számát [5...15]: "))
    if oszlopok >= 5 and oszlopok <= 15:
        break
    print("Hibás adatbevitel, próbáld meg újra")

i = 1
while i <= sorok:
    j = 1
    while j <= oszlopok:
        print("*", end="")
        j += 1
    print()
    i += 1
