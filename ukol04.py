#Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
#Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
#Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
#Tvůj program bude obsahovat dvě funkce:

#1. První funkce ověří telefonní číslo. 
"""Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (POKUD je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False."""
#2. Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
#Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

#Tipy:
#Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
#Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420".

# první fce, přidala jsem si tam ještě možnost zadání 00420
def overeni_cisla(cislo):
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