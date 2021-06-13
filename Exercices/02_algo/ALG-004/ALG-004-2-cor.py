def conversion (romain) :
    L = ["I","V","X","L","C","D","M"]
    decimal = 0
    n = len(romain)
    if n==0 :
        return -1
    for k in range(n) :
        if romain[k] in L :
            v = valeur(romain[k])
            if k+1 < n and v < valeur(romain[k+1]) :
                decimal -= v
            else :
                decimal += v
        else :
            return -1
    return decimal
