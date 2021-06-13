def valeur (caractere) :
    """ renvoie la valeur décimale d'un caractère
    s'il est utilisé dans la numération romaine
    renvoie 0 sinon.
    Précondition : caractere est une lettre de l'alphabet
    latin """
    if caractere == "I" :
        return 1
    elif caractere == "V" :
        return 5
    elif caractere == "X" :
        return 10
    elif caractere == "L" :
        return 50
    elif caractere == "C" :
        return 100
    elif caractere == "D" :
        return 500
    elif caractere == "M" :
        return 1000
    else :
        return 0
    
        
