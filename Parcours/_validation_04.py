from capytale.autoeval import ValidateFunctionPretty

def _cor_longueur(ch:str) -> int :
    return len(ch)

def _cor_ajouter_lettre(mot:str,lettre:str) -> str :
    return mot+lettre

def _cor_ajouter_lettre_deb(mot:str,lettre:str) -> str :
    return lettre+mot

def _cor_compter_lettre(mot:str,lettre:str) -> int :
    cpt = 0
    for l in mot : 
        if l == lettre : 
            cpt = cpt+1
    return cpt

def _cor_remplacer_lettre(mot:str,lettre1:str,lettre2:str) -> str :
    res = ''
    for l in mot : 
        if l == lettre1 :
            res = res+lettre2
        else :
            res = res+l
    return res

target_values = ["","a","aa","aaa","aaaa"]
test_longueur = ValidateFunctionPretty("longueur",target_values,valid_function=_cor_longueur)

target_values = [("","x"),("a","x"),("aa","x"),("aaa","x"),("aaaa","x")]
test_ajouter_lettre = ValidateFunctionPretty("ajouter_lettre",target_values,valid_function=_cor_ajouter_lettre)

target_values = [("","x"),("a","x"),("aa","x"),("aaa","x"),("aaaa","x")]
test_ajouter_lettre_deb = ValidateFunctionPretty("ajouter_lettre_deb",target_values,valid_function=_cor_ajouter_lettre_deb)

target_values = [("aaa","a"),("bbb","a"),("bab","b"),("bab","b"),("ababa","a")]
test_compter_lettre = ValidateFunctionPretty("compter_lettre",target_values,valid_function=_cor_compter_lettre)

target_values = [("aaa","a","b"),("bbb","a","b"),("bab","b","b"),("bab","b","b"),("ababa","a","b")]
test_remplacer_lettre = ValidateFunctionPretty("remplacer_lettre",target_values,valid_function=_cor_remplacer_lettre)