def dijkstra(G:dict,depart,fin,visited=[],distances={},peres={}):
    '''calcul le plus court chemin en partant de départ pour atteindre
    arrivée par l'algorithme de Dijkstra
    entrées :
    G : dict, dictionnaire d'adjacence du graphe pondéré sous forme de dictionnaire de dictionnaires
    départ : un sommet de G
    fin : un sommet de G
    sortie : None (ne renvoie rien)
    '''
    if depart not in G:
        raise TypeError('Le sommet de départ n\'est pas dans le graphe')
    if fin not in G:
        raise TypeError('Le sommet d\'arrivée n\'est pas dans le graphe')
    # condition de sortie de la boucle récursive
    if depart==fin:
        # on construit le plus court chemin et on l'affiche
        chemin=[]
        pred=fin
        while pred != None:
            chemin.append(pred)
            pred=peres.get(pred,None)
        chemin.reverse() # on retourne la liste dans le bon ordre
        print ('chemin le plus court :'+str(chemin)+' cout='+str(distances[fin]))

    else :
        # au premier passage, on initialise le coût à 0
        if visited==[] :
            distances[depart]=0
        # on visite les successeurs de depart
        for voisin in G[depart]:
            if voisin not in visited:
                distance_prov = distances[depart] + G[depart][voisin]
                if distance_prov < distances.get(voisin,float('inf')):
                    distances[voisin]=distance_prov
                    peres[voisin]=depart
        # On marque comme "visited"
        visited.append(depart)
        # Une fois que tous les successeurs ont été visités : récursivité
        # On choisit les sommets non visités avec la distance la plus courte
        # On ré-exécute récursivement Dijkstra en prenant depart='x'
        not_visited={}
        for k in G.keys():
            if not k in visited :
                not_visited[k] = distances.get(k,float('inf'))
        x=min(not_visited, key=not_visited.get)
        dijkstra(G,x,fin,visited,distances,peres)



G={1:{3:23,2:3},2:{1:3,4:46},3:{1:23,4:7,6:8},4:{2:46,3:7,5:10},5:{3:5,4:10,6:3},6:{3:8,5:3}}

# >>> dijkstra(G,6,2,[],{},{})
# peres
# {3: 6}
# {3: 6, 5: 6}
# {3: 6, 5: 6, 4: 5}
# {3: 6, 5: 6, 4: 5, 1: 3}
# {3: 6, 5: 6, 4: 5, 1: 3, 2: 4}
# {3: 6, 5: 6, 4: 5, 1: 3, 2: 1}
# chemin
# [2]
# [2, 1]
# [2, 1, 3]
# [2, 1, 3, 6]
# chemin le plus court :[6, 3, 1, 2] cout=34



