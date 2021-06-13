# boites factorielles

def boites (nbp) :
    m = nbp
    p = 1
    fact = 1 # fact = p!
    while fact*(p+1) <= nbp :
        p += 1
        fact *= p # fact = p!
    # en sortie de la boucle while, p ! <= n < (p+1)!
    q = p
    t = [0]*p
    while m > 0 :
        t[p-1] = m // fact
        m = m % fact
        fact //= p
        p -= 1
    return q,t
    
