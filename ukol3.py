#Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.

import json

# 1. Soubor si ulož a načti do slovníku.
with open("ukol03_body.json", mode="r", encoding="utf-8") as file:
    body = json.load(file)   #načtení souboru json do slovníku

print(body)

 #2. Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".

#práce s načteným slovníkem v json a tvorba nového zápisu, kdy hodnotou bude řetězec
results = {}

for name, points in body.items():
    if points >= 60:
        results[name] = "Pass"
    else:
        results[name] = "Fail"

print(results)

# 3.Výsledný slovník ulož jako JSON do souboru prospech.json.
with open("prospech03.json", mode="w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii = False)