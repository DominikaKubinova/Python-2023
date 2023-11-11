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

#01
class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, volne = True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.volne = volne
    
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


"""Otestuj, že program nedovolí půjčit stejné auto dvakrát."""