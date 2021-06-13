def parfait (n) :
    """ Renvoie la valeur de "n est un nombre parfait"
        Précondition : n est un entier naturel """
    s = 0
    # Inv. en début de boucle : s est la somme de tous les diviseurs de n entre 1 et 0.
    for d in range(1,n) :
        
        # Inv. en entrée de tour de boucle : 
        # s est la somme de tous les diviseurs de n
        # compris entre 1 et d-1
        
        if n %d ==0 :
            s = s + d
            
        # Inv. en sortie de tour de boucle : 
        # s est la somme de tous les diviseurs de n
        # compris entre 1 et d

    # Au dernier tour de boucle, d = n-1
    # Invariant : s est la somme de tous les diviseurs de n
    # compris entre 1 et n-1

    if s == n :
        return True
    else :
        return False
    # On pouvait écrire : 
    # return s == n
