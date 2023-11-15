"""
1. Pomocí nástroje regex101 vymysli regulární výraz, který označí platná data a neoznačí 

platná data:
2.2.2022
13. 8. 1999
4/5/2001
 
neplatná data:
5.123.458.91
21.4
8./9"""

#REGULÁRNÍ VÝRAZ UKOL07/01
(\d{1,2})[\./] ?(\d{1,2})[\./] ?\d{4}
 
"""Zkopíruj si obsah souboru posta.txt do regex101 jako testovací řetězec. Vymysli regulární výraz, který označí všechny "poslední řádky adresy" v textu. Poslední řádka adresy zpravidla obsahuje PSČ a název obce, například 190 16 PRAHA 916 nebo 742 45 FULNEK. Celkem by jich mělo být 18."""

#REGULÁRNÍ VÝRAZ UKOL07/02
\d{3} \d{2} .+