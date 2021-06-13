def picResonance(w,gain,phase):
    n=len(w)
    gr=gain[0]
    i=1
    while i<n and gr<=gain[i]:
        gr=gain[i]
        i+=1
    if i==1:
        return ()
    else:
        return (w[i-1],gr,phase[i-1])
