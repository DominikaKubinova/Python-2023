#01
"""Evidence aut
Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:

Registrační značka 4A2 3020 a 1P3 4747	
Značka a typ vozidla Peugeot 403 Cabrio a Škoda Octavia	
Počet najetých kilometrů  47534 a 41253

Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:

registrační značka automobilu registracni_znacka,
značka a typ vozidla typ_vozidla,
počet najetých kilometrů najete_km,
informaci o tom, jestli je vozidlo aktuálně volné dostupne (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).

Vytvoř metodu __init__() pro třídu Auto. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu. Poslední atribut rovnou nastav jako True, tj. na začátku je vozidlo vždy volné."""

#02 
"""Vytvoř objekty, které reprezentují oba automobily půjčovny."""

#03
"""Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu dostupne, který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici"."""

#04
"""Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a typ vozidla) jako řetězec."""

#05
"""Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto()."""

#06
"""Otestuj, že program nedovolí půjčit stejné auto dvakrát."""


# NEPOVINNÝ BONUS

#07
"""Přidej třídě Auto metodu vrat_auto(), která bude mít (krom obligátního self) 2 parametry, a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal. Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné."""

#08
"""Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden, a 300 Kč na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova return."""



#01
class Auto:

    cena_pujcovneho = 400   #méně než týden
    cena_pujcovneho_delsi_nez_tyden = 300    #týden (včetně) a více

    def __init__(self, registracni_znacka, typ_vozidla, najete_km, volne = True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.volne = True
    
    #03
    def pujc_auto(self):
        if self.volne:
            self.volne = False
            return "Potvrzuji zapůjčení vozidla."
        else:
            return "Vozidlo není k dispozici."
        
    #04
    def get_info(self):
        return f"Vozidlo s registrační značkou {self.registracni_znacka} a typem {self.typ_vozidla}."
    
     #07 a #08
    def vrat_auto(self, stav_tachometru, pocet_dni_uzivani, volne = True):
        self.stav_tachometru = stav_tachometru
        self.pocet_dni_uzivani = pocet_dni_uzivani
        self.volne = True
        najete_km = stav_tachometru - self.najete_km
        
        if pocet_dni_uzivani >= 7:
            celkova_cena = Auto.cena_pujcovneho_delsi_nez_tyden * pocet_dni_uzivani
        else:
            pocet_dni_uzivani < 7
            celkova_cena = Auto.cena_pujcovneho * pocet_dni_uzivani
        return f"Cena půjčovného je {celkova_cena}"
    

#02
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, True)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253, True)

#05
volba_znacky = input("Zadejte značku auta, které si chcete půjčit (Peugeot/Škoda): ")

if volba_znacky == "Peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
elif volba_znacky == "Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())
else:
    print("Zvolte si odpovídající značku z uvedených možností.")

#08
stav_tachometru = int(input("Zadej stav tachometru při vrácení auta: "))
pocet_dni_uzivani = int(input("Zadej počet dní, po kterou jste měl auto půjčené: "))

print(auto1.vrat_auto(stav_tachometru, pocet_dni_uzivani))
print(auto2.vrat_auto(stav_tachometru, pocet_dni_uzivani))