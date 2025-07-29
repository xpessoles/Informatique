from capytale.autoeval import ValidateFunctionPretty

def _cor_somme_pairs(n:int) -> int :
    res = 0
    i = n
    while i>=0 : 
        if i%2 == 0 : 
            res = res + i
        i = i-1
    return res

def _cor_factorielle(n:int) -> int :
    if n == 0 :
        return 1
    i = n
    res = 1
    while i>0 :
        res = res*i
        i=i-1
    return res

def _cor_nb_chiffres(n:int) -> int :
    if n == 0 :
        return 1
    res = 0
    nb = n 
    while nb != 0 and res < 10 :
        nb = nb // 10
        res = res + 1
    return res

def _cor_inverse_int(n:int) -> int:
    nb = n
    res = 0
    while nb > 0 :
        last_chiffre = nb % 10
        
        res = res * 10 + last_chiffre
        
        nb = nb // 10
    return res

def _cor_fibonacci(n:int) -> int :
    if n <= 1 : 
        return n
    res = 0
    i = 1 
    u = 0
    v = 1
    while i < n :
        res = u + v
        u = v
        v = res
        i = i+1
    return res


target_values = [0,11,101,1001,10001]
test_somme_pairs = ValidateFunctionPretty("somme_pairs",target_values,valid_function=_cor_somme_pairs)

target_values = [0,1,11,21,31]
test_factorielle = ValidateFunctionPretty("factorielle",target_values,valid_function=_cor_factorielle)

target_values = [11,101,1001,10001,100001]
test_nb_chiffres = ValidateFunctionPretty("nb_chiffres",target_values,valid_function=_cor_nb_chiffres)

target_values = [1,12,124,1248,54321]
test_inverse_int = ValidateFunctionPretty("inverse_int",target_values,valid_function=_cor_inverse_int)

target_values = [1,11,101,1001,10001]
test_fibonacci = ValidateFunctionPretty("fibonacci",target_values,valid_function=_cor_fibonacci)