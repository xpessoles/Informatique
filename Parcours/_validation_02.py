from capytale.autoeval import ValidateFunctionPretty
from math import pi

def _cor_somme(n:int) -> int :
    res = 0
    for i in range(n+1):
        res = res + i
    return res

def _cor_inv_somme(n:int) -> int :
    res = 0
    for i in range(1,n+1):
        res = res + 1/i
    return res

def _cor_wallis(n:int) -> float:
    p = 1
    for i in range(1,n+1):
        p = p*4*i*i/(4*i*i-1)
    return p*2

def _cor_valeur_absolue(x:float) -> float :
    if x >= 0 : 
        return x
    else : 
        return -x

def _cor_syracuse(n,N):
    if n == 0 : 
        return N
    u = N
    for i in range(n):
        if u%2 == 0 : 
            u = u/2
        else :
            u = 3*u + 1
    return u

target_values = [11,101,1001,10001,100001]
test_somme = ValidateFunctionPretty("somme",target_values,valid_function=_cor_somme)

target_values = [11,101,1001,10001,100001]
test_inv_somme = ValidateFunctionPretty("inv_somme",target_values,valid_function=_cor_inv_somme)

target_values = [11,101,1001,10001,100001]
test_wallis = ValidateFunctionPretty("wallis",target_values,valid_function=_cor_wallis)

target_values = [-3.12,-1.234,0,1,12]
test_valeur_absolue = ValidateFunctionPretty("valeur_absolue",target_values,valid_function=_cor_valeur_absolue)

target_values = [(5,5),(11,15),(5,21),(15,21),(20,40)]
test_syracuse = ValidateFunctionPretty("syracuse",target_values,valid_function=_cor_syracuse)