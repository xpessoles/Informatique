from math import log

def limite () :
    """ renvoie une approxiamtion à 10**(-8) près de
    la limite de la suite (S_n) """
    k = 2
    u = (-1)**k/(k*log(k))               # u = S_k
    v = u + (-1)**(k+1)/((k+1)*log(k+1)) # v = S_{k+1}
    while abs(u-v) >= 2*10**(-8) :
        u = v
        k += 1
        v = u + (-1)**(k+1)/((k+1)*log(k+1))
        # invariant en sortie : u=S_k et v=S_{k+1}
        # variant : abs(u-v), réel positif
        # de limite nulle
    return (u+v)/2


limite()
