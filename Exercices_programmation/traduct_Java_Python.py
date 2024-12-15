
mois_entree = input("Entrez un mois : ")

mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

numeroMois = -1

for i in range(len(mois)):
    if mois[i] == mois_entree:
        numeroMois = i + 1
        break
    
    
if numeroMois != -1:
    print(f"{mois_entree} est le mois numéro {numeroMois}")
else:
    print(f"{mois_entree} n'est pas valide")



