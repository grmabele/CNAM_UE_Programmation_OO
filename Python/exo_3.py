# Définition de la fonction salaire_mensuel
def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12
#une fonction appelée `salaire_hebdomadaire(salaire_mensuel)`
def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4
#fonction appelée `salaire_horaire(salaire_hebdomadaire, heures_travaillees)
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

def main():
    salaire_annuel = float(input("Saisissez votre salaire annuel :"))
    
    heures_travaillees = float(input("Saissisez votre nombre d'heures de travail par semaine :"))

    mensuel = salaire_mensuel(salaire_annuel) 
    hebdomadaire = salaire_hebdomadaire(mensuel)
    horaire = salaire_horaire(hebdomadaire, heures_travaillees)

    print("Votre salaire horaire est de :", horaire, "euros")
    
if __name__ == "__main__":
    main()


