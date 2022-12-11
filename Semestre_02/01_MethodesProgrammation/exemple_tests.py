def produit_scalaire_v2(vecteur1, vecteur2):
    somme = 0
    for i in range(len(vecteur1)):
        somme += vecteur1[i]*vecteur2[i]
    return somme


def test_produit_scalaire_v2_01():
    assert produit_scalaire_v2([1, 1, 1], [1, 1, 1]) == 3

def test_produit_scalaire_v2_02():
    assert produit_scalaire_v2([1, 2, 3, 4], [0, 1, 0, 0]) == 2