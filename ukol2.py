"""ZADÁNÍ ÚKOL 02"""
"""Vyvíjíš software pro obchod s elektronickými součástkami. Firma eviduje informace o počtu součástek na skladě ve slovníku. Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě."""

#slovnik
sklad = {
  "1N4148": 250, # kod součástky je klíč a číslo je hodnota klíče (počet součástek skladem)
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
"""Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník. Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. Obě informace si ulož. Následně naprogramuj následující varianty:
1. Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
2. Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
3. Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem."""

# dotaz na kód součástky od zákazníka
kod_soucastky = input("Zadej kód součástky: ")
if kod_soucastky in sklad:
    #sklad[kod_soucastky] = počet ks dané součástky, sklad = slovník,, kod_soucastky je klíč a proto, že je v hranatých závorkách, tak mi vytáhne hodnotu ze slovníku = tady je hodnotou počet ks dané součástky"""
    dostupne_mnozstvi = sklad[kod_soucastky]
    pozadovane_mnozstvi = int(input("Zadej počet ks: "))
    print(f"Součástka je skladem.")
    if pozadovane_mnozstvi <= dostupne_mnozstvi:
        sklad[kod_soucastky] = sklad[kod_soucastky] - pozadovane_mnozstvi  
        print(f"Poptávku lze uspokojit v plné výši. Na skladě zbývá {sklad[kod_soucastky]} ks {kod_soucastky}.")
    else:
        print(f"Lze prodat pouze {dostupne_mnozstvi} ks {kod_soucastky}.")
        odebrana_soucastka = sklad.pop(kod_soucastky)  #odeberu vyprodanou součástku
else:
    print(f"Součástka není skladem.")


"""BONUS 1

Napiš program, který se uživatele zeptá na text, který chce zapsat v Morseově abecedě. Uvažuj disciplinovaného uživatele, který zadává pouze znaky bez diakritiky, malá písmena atd. Na začátku uvažuj i to, že uživatel nezadává mezery.

Projdi řetězec zadaný uživatelem. Najdi každý znak ve slovníku a vypiš ho na obrazovku v Morseově abecedě.

Abychom měli celý kód vypsaný na jedné řádce, požádáme funkci print(), aby na konci výpisu nevkládala znak pro konec řádku, ale mezeru. To uděláme tak, že jako druhý argument funkce dáme argument end=" ".

Nyní přidáme mezery. Uvažuj, že uživatel může zadat mezeru. Před tím, než budeš hledat znak ve slovníku, zkontroluj, zda znak není mezera. Pokud ano, vypiš znak lomítka /. Bez definice funkce."""

morse_code = {

"0": "-----",
"1": ".----",
"2": "..---",
"3": "...--",
"4": "....-",
"5": ".....",
"6": "-....",
"7": "--...",
"8": "---..",
"9": "----.",
"a": ".-",
"b": "-...",
"c": "-.-.",
"d": "-..",
"e": ".",
"f": "..-.",
"g": "--.",
"h": "....",
"i": "..",
"j": ".---",
"k": "-.-",
"l": ".-..",
"m": "--",
"n": "-.",
"o": "---",
"p": ".--.",
"q": "--.-",
"r": ".-.",
"s": "...",
"t": "-",
"u": "..-",
"v": "...-",
"w": ".--",
"x": "-..-",
"y": "-.--",
"z": "--..",
".": ".-.-.-",
",": "--..--",
"?": "..--..",
"!": "-.-.--",
"-": "-....-",
"/": "-..-.",
"@": ".--.-.",
"(": "-.--.",
")": "-.--.-",
}

text = input("Zadej text, který chceš přeložit do Morseovi abecedy (bez diakritiky a bez mezer: ")

# Převod textu na Morseovu abecedu a výpis
text_morse = ""
for words in text:
    if words.lower() in morse_code:
        text_morse += morse_code[words.lower()] + " "
    else:
        text_morse += "/ "  #pokud tam bude jiný znak než malé písmeno, místo toho ta bude lomítko
print(text_morse, end=" ")


    