class Auteur:

    def __init__(self, nom):
        self.nom = nom
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)


class Livre:

    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        auteur.ajouter_livre(self)


auteur1 = Auteur("Victor Hugo")
auteur2 = Auteur("Albert Camus")

livre1 = Livre("Les Mis´erables", auteur1)
livre2 = Livre("Notre-Dame de Paris", auteur1)
livre3 = Livre("L’´Etranger", auteur2)
