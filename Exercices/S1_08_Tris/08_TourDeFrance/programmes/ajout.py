def ajout(L_etape_triee,LG):
    ''' ajout au classement general le temps de la nouvelle etape et refait le classement'''
    new_classement=[]
    while est_vide(L_etape_triee)==False: #tant que la file n'est pas vide
        cycliste=defiler(L_etape_triee)# on prend le premier element et on l'enleve
        i=0
        new_classement.append(cycliste)# on place le nouvel arrivant a la queue de la liste
                                        # triee du classement general
        while cycliste[1]!=LG[i][1]: #on cherche le meme dossard de cycliste
            i=i+1
        new_classement[-1][-1]=new_classement[-1][-1]+LG[i][-1] #on additionne les temps du
                                                # classement general et du classement d'etape
        tri_insertion_modifie(new_classement) #on trie le nouveau classement
    return new_classement