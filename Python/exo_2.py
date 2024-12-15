liste = input("Saisissez une liste de nombres entiers séparée par des virgules : ")

liste = liste.split(',')

print(list)

somme = 0
for nombre in liste:
    somme += int(nombre)
print(f"La somme des nombres est : {somme}")

moyenne = somme / len(liste)
print("Moyenne des nombres :", moyenne)

nombre_sup_moyenne = 0
for nombre in liste:
    if int(nombre) > moyenne:
        nombre_sup_moyenne += 1
print("Nombre de nombres entier supérieur à la moyenne :", nombre_sup_moyenne)

nombre_pair = 0
i = 0
while i < len(liste):
    if int(liste[i]) % 2 == 0:
        nombre_pair +=1
    i += 1
print("Nombre de nombres pairs :", nombre_pair)