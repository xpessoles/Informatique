def pulsationCoupure(w,gain):
    a=0
    b=len(w)
    while b-a>1:
        m=(a+b)//2
        if (gain[a]+3)*(gain[m]+3)<0:
            b=m
        else:
            a=m
    if a==len(w)-1:
        return -1
    else :
        return w[a]
