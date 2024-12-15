class Livre:

    nombreTotalLivres = 0

    def __init__(self, titre, auteur, anneePublication,  nombreTotalLivres):
        self._titre = titre
        self._auteur = auteur
        self._anneePublication = anneePublication
        Livre.nombreTotalLivres += 1

    def get_titre(self):
        return self.titre
    
    def set_titre(self, titre):
        self.titre = titre
    
    def get_auteur(self):
        return self.auteur
    
    def set_auteur(self, auteur):
        self.auteur = auteur

    def get_anneePublication(self):
        return self.anneePublication 
    
    def set_anneePublication(self, anneePublication):
        self.anneePublication = anneePublication

    def get_nombreTotalLivres(cls):
        return cls.nombreTotalLivres

    def afficher_infos(self):
        return f"Titre: {self.titre}, Auteur: {self.auteur}, Année de publication: {self.annee_publication}"
    
    def main():
        livre1 = Livre("1984",  "George Orwell", 1949)
        livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupery", 1943)

        livre1.afficher_infos()
        print(livre1.afficher_infos())

        print(f"Modification du titre du premier livre...")
        livre1.set_titre("Nineteen Eighty-Four")

        print(livre1.afficher_infos())

        #print(f"Le nombre total de livres crées : {nombreTotalLivres}")

   # main()


    

    
