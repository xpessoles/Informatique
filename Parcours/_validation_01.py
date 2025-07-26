from capytale.autoeval import ValidateFunctionPretty
from math import pi

def _cor_perimetre_cercle(R:float) -> float :
    return 2*pi*R

def _cor_aire_disque(R:float) -> float :
    return pi*R*R

def _cor_est_pair(n):
    return n%2 == 0

def _cor_valeur_absolue(x:float) -> float :
    if x >= 0 : 
        return x
    else : 
        return -x
    
target_values = [0,1,2,3,4,5]
test_perimetre_cercle = ValidateFunctionPretty("perimetre_cercle",target_values,valid_function=_cor_perimetre_cercle)

target_values = [0,1,2,3,4,5]
test_cor_aire_disque = ValidateFunctionPretty("aire_disque",target_values,valid_function=_cor_aire_disque)

target_values = [0,1,2,3,4,5]
test_cor_est_pair = ValidateFunctionPretty("est_pair",target_values,valid_function=_cor_est_pair)

target_values = [-3.12,-1.234,0,1,12]
test_cor_valeur_absolue = ValidateFunctionPretty("valeur_absolue",target_values,valid_function=_cor_valeur_absolue)