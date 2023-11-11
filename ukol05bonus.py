#Krom teplot máme k dispozici i informaci o dnu v týdnu:

teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]
#Pomocí dict comprehension vytvoř slovník, který bude mít následující formát, kde klíčem bude den v týdnu, a hodnotou průměrná teplota ten den.

#{den: průměrná teplota}

# dict comprehension
prumerna_teplota = {den[0]: round(sum(den[1:]) / len(den[1:]), 2) for den in teploty}

print(prumerna_teplota)

#dict
prumerna_teplota = {}
for den in teploty:
    den_nazev, *teploty_den = den
    prumerna_teplota[den_nazev] = round(sum(teploty_den) / len(teploty_den), 2)
print(prumerna_teplota)

""" Tento zápis vytváří slovník slovnik_teplot, kde klíčem je první prvek v každém seznamu teploty (tj. název dne) a hodnotou je zbytek seznamu (teploty pro různé časy). Vysvětlení:
for den in teploty: To je cyklus for, který projde všechny seznamy v seznamu teploty. Každý seznam při průchodu označím jako den.
den[0]: Tímto se dostanu k prvnímu prvku aktuálního seznamu den, což je název dne (např. "pondělí"). Tento název dne použiju jako klíč ve slovníku.
den[1:]: Tímto dostanu podseznam obsahující všechny prvky od druhého prvku až do konce seznamu den. To jsou teploty pro různé časy. Tento podseznam použiju jako hodnotu ve slovníku.
Celý tento výraz tedy vytvoří slovník, kde klíče jsou názvy dnů a hodnoty jsou seznamy teplot pro různé časy. Přesně tak, jak to bylo v původním seznamu teploty. """