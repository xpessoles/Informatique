def zeros(n):
    """
    Crée une matrice de zéros de taille nxn
    Entrée : 
     * n(int) : nombre entier positif
    Sortie :
     * m(list) : liste de taille nxn de zéros
    """
    # En utilisant une liste de compréhension, on pourrait procéder ainsi :
    #return [[0 for j in range(n)] for i in range(n)]
    m = []
    for i in range(n):
        mm = []
        for k in range(n):
            mm.append(0)
        m.append(mm)
    return m


def extraire(M,l,c):
    """
    Supprime la ligne l et la colonne c de la matrice M
    Entrées :
     * M(list(list)) : matrice de taille nxn
     * l(int) : numéro de ligne à supprimer
     * c(int) : numéro de colonne à supprimer
    Sortie : 
     * MM(list(list)) : matrice de taille n-1 x n-1 en ayant supprimer la ligne l et la colonne c
    """
    n = len(M)
    MM = zeros(n-1)
    p=-1
    for i in range(n):
        if i!= l:
            p=p+1
            q=-1
            for j in range(n):
                if j!= c:
                    q=q+1
                    MM[p][q]=M[i][j]
    
    return MM

def determinant(M):
    """
    Calcule le déterminant de la matrice M.
    Entrée : 
     * M(list) : matrice de taille nxn
    Sortie : 
     * d(flt) : déterminant de la matrice
    """
    n = len(M)
    if len(M)==1:
        return M[0][0]
    else :
        d=0
        for i in range(n):
            d = d+(-1)**i * M[i][0]*determinant(extraire(M,i,0))
    return d
        
    
 
    
MM = [[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]]
M = [[2,2,0,0],[2,1,2,0],[0,0,1,0],[0,0,0,1]]
print(extraire(MM,0,0))
print(extraire(MM,1,0))
print(extraire(MM,2,0))
print(extraire(MM,3,0))

print(determinant(MM))
from numpy import linalg
print(linalg.det(MM))





# def extraire(M,l,c): ## A REVOIR
#     """
#     Supprime la ligne l et la colonne c de la matrice M
#     Entrées :
#      * M(list(list)) : matrice de taille nxn
#      * l(int) : numéro de ligne à supprimer
#      * c(int) : numéro de colonne à supprimer
#     Sortie : 
#      * MM(list(list)) : matrice de taille n-1 x n-1 en ayant supprimer la ligne l et la colonne c
#     """
#     n = len(M)
#     liste_indices = [] 
#     MM = zeros(n-1)
#     for i in range(n):
#         for j in range(n):
#             if i!=l and j!=c:
#                 if i<l :
#                     if j<l :
#                         MM[i][j]=M[i][j]
#                     else :
#                         MM[i][j-1]=M[i][j]
#                 else :
#                     if j<l :
#                         MM[i-1][j]=M[i][j]
#                     else :
#                         MM[i-1][j-1]=M[i][j]
#     
#     return MM
