def moyenne(fichier_notes,fichier_moyennes,sep=','):
    """Lit les notes dans fichier_notes
    Calcule les moyennes de chaque élève et les écrit dans fichier_moyennes"""
    with open(fichier_notes,'r') as f :
        T = f.readline().strip('\n').split(',') # Titres
        etudiants = f.readlines()
    moyennes = []
    for e in etudiants :
        L = e.strip('\n').split(',')
        prenom = L[0]
        m,nb = 0,0
        for n in L[1:]:
            if n != '' :
                m = m + float(n)
                nb = nb + 1
        m = m / nb
        moyennes.append(prenom + sep + str(m) + '\n')
    with open(fichier_moyennes,'w') as f :
        f.write(T[0] + sep + 'Moyennes\n')
        for m in moyennes :
            f.write(m)
    return None
