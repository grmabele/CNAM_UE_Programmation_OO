class Case:

    def __init__(self):
        self.valeur = ""
    
    def est_vide(self):
        return self.valeur == ""
    
    def marquer(self, symbole):
        if not self.est_vide():
            raise Exception("Case déjà occupée")
        self.valeur = symbole
    
    def __str__(self):
        return self.valeur
    
class Grille:
    def __init__(self):
        # Cr´eation du tableau 3x3
        self.cases = [[Case() for _ in range(3)] for _ in range(3)]

        # Creation du dictionnaire de référencement
        self.references = {}
        for i, col in enumerate(['a', 'b', 'c']):
            for j, lig in enumerate(['1', '2', '3']):
                self.references[col + lig] = self.cases[i][j]

    
    def qui_gagne(self):
        # Test des lignes et colonnes
        for i in range(3):

            if (not self.cases[i][0].est_vide() and
                self.cases[i][0].valeur == self.cases[i][1].valeur ==
                self.cases[i][2].valeur):
                return self.cases[i][0].valeur
            
            if (not self.cases[0][i].est_vide() and
                self.cases[0][i].valeur == self.cases[1][i].valeur ==
                self.cases[2][i].valeur):
                return self.cases[0][i].valeur
            
        # Test des diagonales
        if (not self.cases[0][0].est_vide() and
            self.cases[0][0].valeur == self.cases[1][1].valeur ==
            self.cases[2][2].valeur):
            return self.cases[0][0].valeur
        
        if (not self.cases[0][2].est_vide() and
            self.cases[0][2].valeur == self.cases[1][1].valeur ==
            self.cases[2][0].valeur):
            return self.cases[0][2].valeur
        
        return None
    
    def match_nul(self):
        for ligne in self.cases:
            for case in ligne:
                if case.est_vide():
                    return False
            return self.qui_gagne() is None
        
    def afficher(self):
        print(" a b c")

        for i, ligne in enumerate(['1', '2', '3']):
            print(f"{ligne} ", end='')
            
            for j in range(3):
                print(self.cases[j][i], end='')
            print()
        print()


if __name__ == "__main__":
    # Création d'une grille
    grille = Grille()

    # Affichage de la grille vide
    print("Grille vide :")
    grille.afficher()

    # Marquer quelques cases
    grille.references['a1'].marquer('X')
    grille.references['b1'].marquer('X')
    grille.references['c1'].marquer('X')

    # Affichage de la grille après avoir marqué quelques cases
    print("Grille après avoir marqué quelques cases :")
    grille.afficher()

    # Vérification du gagnant
    gagnant = grille.qui_gagne()
    if gagnant:
        print(f"Le joueur {gagnant} a gagné !")
    else:
        print("Aucun gagnant pour l'instant.")

    # Vérification du match nul
    if grille.match_nul():
        print("Match nul !")
    else:
        print("Le match n'est pas encore nul.")
            