class Animal:
    def __init__(self, id, nom, espece, age, regime):
        self.id = id
        self.nom = nom
        self.espece = espece
        self.age = age
        self.regime = regime

    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.id == other.id
        return False

    def __str__(self):
        return f"{self.espece} \"{self.nom}\" (ID: {self.id}), {self.age} ans, {self.regime}"

    def __hash__(self):
        return hash(self.id)

class Zoo:
    def __init__(self):
        self.animaux = {}

    def ajouter_animal(self, animal):
        self.animaux[animal.id] = animal

    def retirer_animal(self, id):
        return self.animaux.pop(id, None)

    def rechercher_animal(self, id):
        return self.animaux.get(id)

    def rechercher_par_espece(self, espece):
        return [animal for animal in self.animaux.values() if animal.espece.lower() == espece.lower()]

    def afficher_animaux(self):
        for animal in self.animaux.values():
            print(animal)

    def nombre_animaux(self):
        return len(self.animaux)

    def moyenne_age_espece(self, espece: str):
        animaux_espece = self.rechercher_par_espece(espece)
        if not animaux_espece:
            return 0
        return sum(animal.age for animal in animaux_espece) / len(animaux_espece)

def main():
    zoo = Zoo()

    # Création et ajout d’animaux
    zoo.ajouter_animal(Animal(1, "Simba", "Lion", 5, "Carnivore"))
    zoo.ajouter_animal(Animal(2, "Dumbo", "Éléphant", 10, "Herbivore"))
    zoo.ajouter_animal(Animal(3, "George", "Singe", 3, "Omnivore"))
    zoo.ajouter_animal(Animal(4, "Nala", "Lion", 4, "Carnivore"))

    print("Animaux dans le zoo :")
    zoo.afficher_animaux()

    # Recherche par ID
    print("\nRecherche de l’animal avec ID 2 :")
    print(zoo.rechercher_animal(2))

    # Recherche par espèce
    print("\nLions dans le zoo :")
    for lion in zoo.rechercher_par_espece("Lion"):
        print(lion)

    # Calcul de la moyenne d’âge
    print(f"\nÂge moyen des lions : {zoo.moyenne_age_espece('Lion'):.1f} ans")

    # Retrait d’un animal
    print("\nRetrait de l’animal avec ID 3...")
    zoo.retirer_animal(3)
    print("Animaux restants dans le zoo :")
    zoo.afficher_animaux()
    print(f"\nNombre total d’animaux : {zoo.nombre_animaux()}")

if __name__ == "__main__":
    main()
