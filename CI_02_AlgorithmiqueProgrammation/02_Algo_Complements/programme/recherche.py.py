tab = [17,38,10,25,72,4,98,32,11]


def recherche_while(tab,nb):
    """
    Fonction permettant de savoir si la nombre nb
    appartient au tableau tab non trié """
    i = 0
    # On verifie que si nb = tab[i] et qu'on ne sort pas du tableau
    while tab[i] != nb and i < len(tab) :
        i=i+1
    # Si le nombre a été rencontré dans le tableau, on est sorti de
    # la boucle et i est bien inférieur à en tab donc on retourne True
    # Si le nombre n'a pas été rencontré, i vaut len(tab) et donc on
    # False est renvoyée
    return i < len(tab)


def recherche_for_if(tab,nb):
    for i in range(0,len(tab)):
        if tab[i]==nb:
            return True
    return False

def recherche_for_if_py(tab,nb):
    #Variante de l'algo précédent en utilisant les possiblités de python
    for element in tab:
        if element == nb:
            return True
    return False


def retourne_index_nb(tab,nb):
    # Si un élément appartient au tableau on retourne l'index
    # sinon on retourne None
    for i in range(0,len(tab)):
        if tab[i]==nb:
            return i
    return None

def retourne_index_nb_py(tab,nb):
    for index,element in enumerate(tab):
        if element == nb:
            return index
    return None

def recherche_dichotomique(x,a):
    # x est un tableau (trié)
    # a valeur à rechercher
    g = 0        # Premier index du tableau
    d = len(a)-1 # Dernier index du tableau
    while g <=d :
        # Index de l'élément médian du tableau
        # On fait une division dans IN car s'il y a un nombre
        # impair d'éléments dans le tableau, m est dans IR.
        m = (g+d)//2
        if a[m]==x : # Au moment ou l'element median sera l'element recherche
            return m #On renvoie l'index
        if a[m]<x : # On regarde dans la partie droite du tableau
            g=m+1 #on restreint la zone du tableau qu'on va considérer
        else :
            d=m-1 # Dans ce cas, on regarde dans la partie gauche du tableau
    # Attention dans le programme donné, None n'est pas bien indenté !
    # Les élèves doivent détecter cette erreur
    return None 
 

print(recherche_dichotomique(17,tab))
