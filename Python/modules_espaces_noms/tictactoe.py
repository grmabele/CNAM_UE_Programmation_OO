
def grille_vierge():
    """
    Fonction qui renvoie une grille de tic-tac-toe vide.
    """
    tab = [[[' '],[' '],[' ']], \
           [[' '],[' '],[' ']], \
           [[' '],[' '],[' ']]]
    dico = dict()
    lig = 0
    col = 0
    for colonne in ['a','b','c']:
        lig = 0
        for ligne in ['1', '2', '3']:
            dico[colonne + ligne] = tab[col][lig]
            lig += 1
        col += 1
    return (tab,dico)

def marquer(grille, signe, caseref):
    '''
    Fonction qui marque un signe dans une case d'une grille. Ce signe
    doit être 'X' ou 'O'. La case est désignée par le paramètre caseref
    '''
    if not signe in ['X','O']:
        raise Exception('signe incorrect : ' + signe)
    if grille[1][caseref][0] == ' ':
        grille[1][caseref][0]=signe
    else:
        raise Exception('case déjà occupée')

def same_syms(sig1, sig2, sig3):
    '''
    Fonction qui teste si les trois symboles de trois cases passées en
    paramètre sont égaux et différent de ' '.
    '''
    return sig1 == sig2  and sig2 == sig3 and sig1[0] != ' '
    
def qui_gagne(grille):
    '''
    Donne le signe 'X' ou 'O' du vainqueur de la grille passée en paramètre
    ou None s'il n'y a pas encore de vainqueur.
    '''
    # test diagonale
    if same_syms(grille[0][0][0],grille[0][1][1],grille[0][2][2]):
        return grille[0][0][0][0]
    # test autre diagonale
    if same_syms(grille[0][0][2],grille[0][1][1],grille[0][2][0]):
        return grille[0][0][2][0]
    # test lignes et colonnes
    for i in range(0,3):
        if same_syms(grille[0][i][0],grille[0][i][1],
                     grille[0][i][2]):
            return grille[0][i][0][0]
        if same_syms(grille[0][0][i],grille[0][1][i],
                     grille[0][2][i]):
            return grille[0][0][i][0]
    return None
        
def match_nul(grille):
    ''' 
    Fonction qui teste si la grille donnée en paramètre est celle d'une
    partie nulle.
    '''
    for case in grille[1].values():
        if case[0] == ' ':
            return False
    return not qui_gagne(grille)

def afficher(grille):
    '''
    Affiche la grille passée en paramètre.
    '''
    st = '  '
    cols = ['a','b','c']
    for col in cols:
        st = st+col+' '
    for lig in ['1', '2', '3']:
        st = st+"\n" + lig + ' '
        for col in cols:
            st = st + grille[1][col+lig][0] + ' '
    print(st)
    print()
    
def jouer_automatiquement_un_coup(grille, marque):
    '''
    Fonction qui joue automatiquement (et plutôt bêtement) un coup
    en inscrivant la marque donnée en paramètre dans une case libre
    de la grille.
    '''
    if grille[1]['b2'][0]==' ':
        grille[1]['b2'][0]=marque
    else:
        for case in grille[1].values():
            if case[0] == ' ':
                case[0]=marque
                return
        raise Exception('Plus de case libre')

def verifier_case_jouable(grille, caseref):
    '''
    Fonction qui teste si une case est jouable. La résultat est un tuple
    comportant un booléen et une chaîne correspondant à un message d'erreur
    si le booléen vaut False. Sinon, cette chaîne est 'ok'.
    '''
    caseref = caseref.strip()
    try:
        if grille[1][caseref][0] == ' ':
            return (True,'ok')
        else:
            return (False,'case déjà occupée')
    except KeyError:
        return (False,"cette case n'existe pas")

                
def jouer_interactivement_un_coup(grille, marque):
    '''
    Fonction qui lit au clavier la case où l'utilisateur veut jouer.
    La grille et la marque du joueur sont passés en paramètre.
    Cette fonction ne renvoie pas de valeur.
    '''
    input_ok = (False,'')
    while not input_ok[0]:
        if input_ok[1]:
            print(input_ok[1])
        print("Quelle case? ")
        caseref = input()
        input_ok = verifier_case_jouable(grille,caseref)
    marquer(grille,marque,casereef)
