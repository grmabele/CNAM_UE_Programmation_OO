
def test_variables():
    from variables import nom, prenom, age, taille, est_etudiant

    assert isinstance(nom, str)
    assert isinstance(prenom, str)
    assert isinstance(age, int)
    assert isinstance(taille, float)
    assert isinstance(est_etudiant, bool)


    assert nom != ""
    assert prenom != ""
    assert age > 0
    assert taille > 0