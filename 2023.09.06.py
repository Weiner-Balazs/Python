"""
Adj meg egy számot: 5
Adj meg egy másikat is: 7
5 + 7 = 12
5 - 7 = -2
5 * 7 = 35
"""
"""
print()

szam1 = int(input("Adj meg egy számot: "))

print()

szam2 = int(input("Adj meg egy másikat is: "))

(érték1) = (szam1) + (szam2) 
(érték2) = (szam1) - (szam2)
(érték3) = (szam1) * (szam2) 
print(szam1, " + ", szam2, " = ", érték1)
print(szam1, " - ", szam2, " = ", érték2)
print(szam1, " * ", szam2, " = ", érték3)
"""

"""

Add meg az első jelentkező nevét: András
Add meg a korát: 34
Add meg a második jelentkező nevét: Béla
Add meg neki is a korát: 12
András 22 évvel idősebb, mint Béla.
"""

név1 = (input("Add meg az első jelentkező nevét: "))
kor1 = int(input("Add meg a korát: "))
név2 = (input("Add meg a második jelentkező nevét: "))
kor2 = int(input("Add meg neki is a korát: "))
"""
különbség = kor1 - kor2
if különbség <= 0:
    különbség = különbség * -1
print(név1, különbség, "évvel idösebb, mint",  név2 )

if különbség == 0:
    print(név1, "és", név2, "egykorúak")
"""

név1 = (input("Add meg az első jelentkező nevét: "))
kor1 = int(input("Add meg a korát: "))
név2 = (input("Add meg a második jelentkező nevét: "))
kor2 = int(input("Add meg neki is a korát: "))


if kor1 > kor2:
    print(f"{név1} {kor2 - kor1}, évvel idősebb, mint {név2}.")
else:
    if kor2 > kor1:
        print(f"{név2} {kor2 - kor1} évvel idösebb, mint {név1}.")
    else:
        print(f"{név1} és {név2} egykorúak. ")
