def retourneListes(nomFichier):
    f=open(nomFichier,"r")
    f.readline()
    w=[]
    gain=[]
    for x in f:
        L=x.split(";")
        w.append(float(L[0]))
        gain.append(float(L[1]))
    f.close()
    return w,gain

       
