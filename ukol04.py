
# první fce, přidala jsem si tam ještě možnost zadání 00420
def overeni_cisla(cislo):
    if (cislo[:5] == "00420" and (len(cislo) == 10 or len(cislo) == 14)) or (cislo[:4] == "+420" and (len(cislo) == 9 or len(cislo) == 13)):
        return True
    else:
        return False
    
# druhá fce
def cena_zpravy(delka):
    pocet_pismen = len(delka)
    cena = (pocet_pismen // 180) * 3
    if pocet_pismen % 180 != 0:
        cena = cena + 3
    return cena

tel_cislo = input("Zadej telefonní číslo, kam chceš zaslat SMS zprávu: ")
if overeni_cisla(tel_cislo):
    zprava = input("Napiš SMS zprávu: ")
    cena = cena_zpravy(zprava)
    print(f"SMS zpráva Tě bude stát: {cena} Kč")
else:
    print("Zadej telefonní číslo ve správném formátu.")