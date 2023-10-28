#Nepovinný bonus 1
#Zkus svoji první funkci upravit tak, že si bude umět poradit s mezerami v telefonním čísle. Mezer se zbavíš například tak, že použiješ metodu .replace(). První parametr metody replace je znak, který chceš nahradit, a druhý parametr nový znak. Pokud se chceš nějakého znaku zbavit, "nahraď" ho prázdným řetězcem "".

#Odkaz na dokumentaci metody replace: https://docs.python.org/3/library/stdtypes.html#str.replace

def overeni_cisla(cislo):
    
    cislo = cislo.replace(" ","")

    if (cislo[:5] == "00420" and len(cislo) == 14) or (cislo[:4] == "+420" and len(cislo) == 13) or (len(cislo) == 9):
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