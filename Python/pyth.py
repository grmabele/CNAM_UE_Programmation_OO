fruits = ["pommes", "banane", "orange"]
fruits.append("kiwi")
fruits.remove("orange")
fruits[1] = "ananas"

print("La listes des fruits contients", len(fruits), "élements.")

fruits.sort()
print(fruits)

x=8
msg = "toto"
print(type(x))
print(type(msg))
#print(type(pi))
#type(msg)

x = y = 9
print(x, y)
a, b = 4, 8.33
print(a, b)

#Écrire un programme qui affiche les 20 premiers termes de la table de multiplication par 7.


nbre_term = 20
i = 1
for i in range(i, nbre_term + 1):
    resultat = 7*i
    print(f"7 X {i} = {resultat}")


nbr_term = 50
i = 1
for i in range(i, nbr_term + 1):
    result = 13*i
    if result % 7 == 0:
        print(f"13 X {i} = {result}")
            