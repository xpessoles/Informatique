# grenouilles

def grenouilles (nbg, nbt, t) :
  """ nbg : nombre de grenouilles
      nbt : nombres de tours
      t : tableau ayant nbt éléments, chaque élément est un couple :
          (n° de la grenouille qui avance, longueur de son saut)"""
  pos = [0]*nbg # pos[i] est la position de la grenouille numéro i
  tete = [0]*nbg # tete[i] est le nb de tours où la grenouille numéro i
                  # s'est trouvée strictement en tête de la course
  for e in t :
    pos[e[0]] += e[1] # la grenouille n° e[0] avance de e[1] longueurs
    # on cherche si une grenouille est la seule à être devant les autres,
    # et on augmente tete en conséquence
    i = 0 # grenouille la plus avancée au début de la boucle
    position = pos[i] # position la plus avancée au début de la boucle
    for j in range(1,nbg) :
      if pos[j] > position :
        position = pos[j] #position de la grenouille de la tête parmi les
        # grenouilles parcourues
        i = j # nméro de cette grenouille
      elif pos[j] == position : # il n'y a pas une grenouille seule en tête
        i = -1 # on indique cela
        break
    if i != -1 : # s'il y a une grenouille seule en tête, on augmente
      # le nombre de tours où elle mène
      tete[i] += 1
  # maintenant on annonce le vainqueur
  gagne = 0 # la gagnante temporaire est la grenouille 0
  for j in range(1,nbg) :
      if tete[j] > tete[gagne] :
        gagne = j # la gagnante temporaire est la grenouille j
    # si tete[j] <= tete[gagne], la gagnante temporaire est encore
    # la grenouille gagne, car en cas d'égalité on renvoie le plus petit numéro
  return gagne

"""
nbg = 4
nbt = 6
t = [[1,2],[0,2],[2,3],[3,1],[1,2],[2,1]]
"""
