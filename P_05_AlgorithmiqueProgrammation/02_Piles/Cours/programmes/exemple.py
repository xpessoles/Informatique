
def empiler(pile,el):
    """
    Ajouter un élément à une pile.
    Entrée : 
     * pile(tuple)
     * el : elément de n'importe quel type (mais a priori du même type que les autres élements de la pile.
    Sortie : 
     * pile (tuple)
    """
    return None

def depiler(pile):
    assert len(pile)>0
    return pile.pop()

def defiler(file):
    assert len(file)>0
    el = file[0]
    del file[0]
    return el