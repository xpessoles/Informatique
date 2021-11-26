def estPair(n): 
    """Cette fonction renvoie True si l'entier n est pair
    False sinon (on suppose que n>=0)""" 
    if n==0: 
        return True 
    return estImpair(n-1) 
    
def estImpair(n): 
    """Cette fonction renvoie True si l'entier n est impair
    False sinon (on suppose que n>=0)""" 
    if n==0: 
        return False 
    return estPair(n-1)

