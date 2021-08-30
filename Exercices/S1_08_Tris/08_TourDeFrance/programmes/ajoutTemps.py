def ajoutTemps(L1,L2):
    '''L1 est la classement de l'etape et L2 le classement general certains ont ete
    disqualifies ou ont abandonne'''
    assert len(L1)<=len(L2)
    Lnew=deepcopy(L1)
    n=len(Lnew)
    for i in range(n):
        d=Lnew[i][1]
        j=0
        while d!=L2[j][1]: #attention certains n'ont pas fait l'etape completement
        # et sont disqualifies
            j+=1
        Lnew[i][-1]=Lnew[i][-1]+L2[j][-1]
    return Lnew