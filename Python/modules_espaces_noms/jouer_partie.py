from tictactoe import grille_vierge, marquer, qui_gagne, match_nul, afficher, verifier_case_jouable

def jouer_partie():
    grille = grille_vierge()
    joueur_courant = "X"

    while True:
        afficher(grille)
        print(f"Tour du joueur {joueur_courant}")

        # Lecture d’un coup valide
        coup_valide = False
        while not coup_valide:
            try:
                case = input("Quelle case (ex: a1) ? ").strip()
                verif = verifier_case_jouable(grille, case)
                if verif[0]:
                    marquer(grille, joueur_courant, case)
                    coup_valide = True
                else:
                    print(verif[1])
        
            except Exception as e:
                print(str(e))
        
        # Test fin de partie
        gagnant = qui_gagne(grille)
        if gagnant:
            afficher(grille)
            print(f"Le joueur {gagnant} a gagné !")
            break
        if match_nul(grille):
            afficher(grille)
            print("Match nul !")
            break
        # Changement de joueur
        joueur_courant = "0" if joueur_courant == "X" else "X"

    jouer_partie()