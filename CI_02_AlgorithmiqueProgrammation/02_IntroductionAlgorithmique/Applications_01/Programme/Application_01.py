# Exercice 1
def is_even(n):
    """
    Fonction permettant de savoir si un nombre est pair ou impair
    Entrées : 
     * n(int) : nombre entier
    Sorties : 
     * un booleén valant True si le nombre est pair, False sinon
    """
    return n%2==0


# Exercice 2
def somme_entiers_for(n):
    """
    Fonction permettant de calculer la somme des n premiers entiers
    Entreés : 
     * n(int) : nombre entier
    Sortie : 
     * S (int) : résultat
    """
    S=0
    for i in range(n+1):
       S = S+i
    return S

def somme_entiers_while(n):
    """
    Fonction permettant de calculer la somme des n premiers entiers
    Entreés : 
     * n(int) : nombre entier
    Sortie : 
     * S (int) : résultat
    """
    S=0
    i=n
    while i!=0: 
       S = S+i
       i=i-1
    return S

# Exercice 3
def P2_explicite(n):
    """
    Calcul de 2^n
    Entrée :
     * n (int) : un nombre entier
    Sortie :
     * x (int) : nieme puissance de 2
    """
    return math.pow(2,n)

def P2_iterative(n):
    """
    Calcul de 2^n
    Entrée :
     * n (int) : un nombre entier
    Sortie :
     * x (int) : nieme puissance de 2
    """
    x = 1
    while n>0 :
        x=2*x
        n=n-1
    return x
    

# Exercice 4
def Syracuse(n):
    """
    Entrées : 
     * n (int) : un nombre entier
    Sorties :
     * syr(int) : nième terme de la suite de Syracuse 
    """
    syr = n
    while syr != 1:
        if (syr%2)==0:
            syr = int(syr/2
        else : 
            syr = 3*syr + 1   
    return syr

print(Syracuse(10))
