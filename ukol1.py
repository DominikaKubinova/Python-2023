#UKOL 01
#Napiš program, který bude obsahovat jednu proměnnou jmeno. Tato proměnná bude obsahovat libovolné křestní jméno (třeba tvoje). Tvůj program vytvoří e-mailovou adresu na základě této proměnné, s doménou czechitas.cz a tuto e-mailovou adresu vypíše.
jmeno = "Dominika"
print(jmeno + "@czechitas.cz")


#NEPOVINNÝ BONUS
#Napiš program, který bude obsahovat proměnnou jmeno_a_prijmeni. Obsah proměnné načti od uživatele pomocí funkce input. Tvůj program postupně vypíše několik způsobů formátování jména:
jmeno_a_prijmeni = input("Zadej své jméno a příjmení: ")
#všechna písmena velká (vypíše např. JANA MALÁ)
print(jmeno_a_prijmeni .upper())
#všechna písmena malá (vypíše např. jana malá)
print(jmeno_a_prijmeni .lower())
#.capitalize() převede na velké jen první písmeno prvního slova
#standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá)
print(jmeno_a_prijmeni .title())
#iniciály (vypíše např. J. M.)
inicialy = '.'.join(word[0].upper() for word in jmeno_a_prijmeni.split())
print(inicialy+".")
#křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)
#rozdělení jména a příjmení
jmeno, prijmeni = jmeno_a_prijmeni.split()
#pokud je křestní jméno delší než 5 znaků, zkrátíme ho na první písmeno
if len(jmeno) > 5:
    jmeno_zkracene = jmeno[0].upper() + "."
else:
    jmeno_zkracene = jmeno.capitalize()
#vytvoření výsledného jména
vysledne_jmeno = jmeno_zkracene + " " + prijmeni.capitalize()
print(vysledne_jmeno)

""" řešení od Maryny: 
parts = jmeno_a_prijmeni.split()
res = parts[0][0].capitalize() + '. ' + parts[1][0].capitalize() + '.'
print(res)
nebo trochu pokročilejší:

parts = jmeno_a_prijmeni.split()
res = map(lambda x: x[0].capitalize() + '.', parts)
print(' '.join(res))"""