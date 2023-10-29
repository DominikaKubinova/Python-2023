#Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# 1.Vytvoř seznam průměrných teplot pro každý den.
prumerne_teploty = []
for den in teploty:
    prumerne_teploty.append(round(sum(den) / len(den),2))
print(f"Seznam průměrných teplot pro každý den: {prumerne_teploty}.")
# řešení pomocí list comprehension
prumerne_teploty = [round(sum(den) / len(den),2) for den in teploty]
print(f"Seznam průměrných teplot pro každý den: {prumerne_teploty}.")

# 2.Vytvoř seznam ranních teplot.
ranni_teploty = []
for den in teploty:
    ranni_teploty.append(den[0])
print(f"Seznam ranních teplot pro každý den: {ranni_teploty}.")
# řešení pomocí list comprehension
ranni_teploty = [den[0] for den in teploty]
print(f"Seznam ranních teplot pro každý den: {ranni_teploty}.")

# 3.Vytvoř seznam nočních teplot.
nocni_teploty = []
for den in teploty:
    nocni_teploty.append(den[3])   #nebo den[-1]
print(f"Seznam nočních teplot pro každý den: {nocni_teploty}.")
# řešení pomocí list comprehension
nocni_teploty = [den[3] for den in teploty]   #nebo den[-1]
print(f"Seznam nočních teplot pro každý den: {nocni_teploty}.")

# 4.Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
poledni_nocni_teploty = []
for den in teploty:
    poledni_nocni_teploty.append([den[1], den[3]])    #nebo ([den[1], den[-1]])
print(f"Seznam poledních a nočních teplot pro každý den: {poledni_nocni_teploty}.")
# řešení pomocí list comprehension
poledni_nocni_teploty = [[den[1], den[3]] for den in teploty]   #nebo [den[1], den[-1]
print(f"Seznam poledních a nočních teplot pro každý den: {poledni_nocni_teploty}.")

