def picResonance(w,gain,phase):
    n=len(w)
    gr=gain[0]
    L=[]
    i=1
    while i<n:
        if gain[i-1]<=gain[i]:
            i+=1
            while i<n and gain[i-1]<=gain[i]:
                i+=1
            if i<n:
                L.append((w[i-1],gain[i-1],phase[i-1]))
        i+=1 
    return L
