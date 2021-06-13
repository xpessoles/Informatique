# lissage :

"""
def lissage (t) :
  return [t[0]]+[(t[i-1]+t[i+1])/2 for i in range(1,len(t)-1)]+[t[-1]]

def lissage_it (t,n) :
  u = t.copy()
  for i in range(n) :
    u = lissage(u)
  return(u)
"""  

def diff (t) :
  return [abs(t[i]-t[i-1]) for i in range(1,len(t))]

def nblissages (t,diffmax) :
  n = len(t)
  nb = 0 # nombre de lissages effectués

  i = 1
  while i < n and abs(t[i]-t[i-1]) <= diffmax : # premier test : faut-il faire  premier
    # un lissage ?
    i += 1
  if i == n : # tous les éléments de t sont <= à diffmax
    return nb # on ne fait aucun lissage

  arret = 0
  
  while arret == 0 : #il faut encore lisser
    u=t.copy() # on copie t dans u, et on va modifier t à partir de u
    arret = 1 # on suppose qu'il n'y a plus besoin de lisser après le lissage
    # en cours, mais au fur et à mesure on vérifie, et on passe arret à 0
    # si besoin
    for i in range(1,n-1) :
      t[i] = (u[i-1]+u[i+1])/2
      if abs(t[i]-t[i-1]) > diffmax :
        arret = 0 # il faudra refaire un lissage
    if abs(t[n-1]-t[n-2]) > diffmax :
        arret = 0 # il faudra refaire un lissage
    nb += 1 # on a fait un de plus

  return nb
"""    
t = [1.292,1.343,3.322,4.789,-0.782,7.313,4.212]
diffmax = 1.120
"""
