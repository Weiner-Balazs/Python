#Függvények

def létrehoz(sor, oszlop, alsó, felső):
    import random
    lst = []
    i = 1
    while i <= sor:
        j = i
        belső = []
        while j <= oszlop:
            belső.append(random.randint(alsó, felső))
            j += 1
        lst.append(belső)
        i += 1
    return lst

def egyesekSzáma(sor):
    egyes = 0
    for i in sor:
        if i == 1:
            egyes += 1
    return egyes

def fájl(fájlnév):
    lst = []
    f = open(fájlnév, "r", encoding="UTF-8")
    for sor in f:
        lst.append(sor.replace("\n", " ").split())
    f.close()
    i = 0
    while i < len(lst):
        j = 1
        while j < len(lst[i]):
            lst[i][j] = int(lst[i][j])
            j += 1
        i += 1
    return lst

def kiír(városok):
    napok = ("Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap")
    
    