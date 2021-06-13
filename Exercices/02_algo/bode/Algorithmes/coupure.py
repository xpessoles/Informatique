def pulsationCoupure(w,gain):
    n=len(w)
    i=0
    while i<n and gain[i]+3>0:
        i+=1
    if i==n:
        return -1
    else :
        return w[i-1]
