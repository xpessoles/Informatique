# Question 8
def a_un_voisin_rempli(grille: list,i:int,j:int):
    '''renvoie un booléen indiquant si l'un des voisins est rempli (valeur 2)'''
    test=False
    n=len(grille)
    if j+1<n and grille[i][j+1]==2: 
        test=True
    elif j-1>=0 and grille[i][j-1]==2 :
        test=True
    elif i-1>=0 and grille[i-1][j]==2:
        test=True
    elif i+1<n and grille[i+1][j]==2 :
        test=True
    return(test)