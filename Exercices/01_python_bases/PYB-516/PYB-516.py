def mystere(L) :
    """Précondition : L est une liste de nombres"""
    x,n,i = L[0],len(L),1
    while i<n and x > L[i] :
        L[i-1],L[i] = L[i],L[i-1]
        i = i+1
    return None
        
    
