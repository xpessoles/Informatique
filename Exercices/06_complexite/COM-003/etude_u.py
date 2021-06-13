import matplotlib.pyplot as plt
import timeit
from numpy import ones,asarray
from scipy import stats
from math import log

def u(n):
    """u_n, n : entier naturel"""
    v = 2
    # Inv : v = u_0
    for k in range(n):
        # Inv : v = u_k
        v = v*v
        # Inv : v = u_k**2 = u_k+1
    # Inv : au dernier tour, k = n-1, donc v = u_n
    return v

# nb de répétitions de chaque test pour mesurer le temps
REPEAT=3

def duree(f, x):
  """Calcule le temps mis par Python pour calculer f(x).
  Cette fonction effectue en fait le calcul de f(x) REPEAT fois
  et garde la valeur la plus petite
  (l'idée est d'éliminer les éventuelles perturbations provoquées
  par d'autres processus tournant sur la machine)"""
  t = timeit.Timer(stmt=lambda : f(x))
  time = min(t.repeat(REPEAT, number=1))
  return time

def trace_u(N,nom_de_fichier):
    """Trace la duree d'exécution de u(k)
       pour  k in range(N), en échelle 
       Effectue une régression linéaire par moindres carrés"""
    with open(nom_de_fichier+'.csv','w') as f :
        f.write('k'+';'+'duree u(k)\n')
        x = []
        y = []
        for k in range(N):
            t = duree(u,k)
            x.append(k)
            y.append(log(t,10))
            f.write(str(k)+';'+str(log(t,10))+'\n')
    x = asarray(x)
    y = asarray(y)
    plt.clf()
    plt.cla()
    plt.plot(x,y,'bo')
    plt.xlabel('$k$')
    plt.ylabel('$\\log_{10} \\left( \\frac{t(k)}{t_0}\\right)$, $t_0 = 1s$')
    plt.title('Temps de calcul de $u_k$, échelle semi-logarithmique')
    plt.savefig(nom_de_fichier+'.png')
    return None

if __name__ == '__main__':
    trace_u(30,'COM-003')
