trame = 'U005+012+004-023-002+0420083'




def lect_mesures():
    while True : 
        carac_recu = com.read(1)
        if  carc_recu=="U" or carc_recu=="I" or carc_recu=="P":
            break
    mesures=[]
    mesures.append(carac_recu)
    # On recherche le nombre de données 
    nb_donnees=int(com.read(3))
    data = []
    for i in range(nb_donnnes):
        # Ajout des données
        data.append(int(com.read(4)))
    mesures.append(data)
    # Ajout de la checksum
    mesures.append(int(com.read(4)))
    return mesures
    

def lect_mesures_test(trame):
    """
    ###On suppose que suite à l'appel d'affectation carac_recu=com.read(1)
    ###carac_recu contient "U", "I" ou "P".
    """
    res=[]
    carac_recu = trame[0]
    nb_donnees=int(trame[1:4])
    
    trame=trame[4:len(trame)]
    res.append(carac_recu)
    
    data = []
    for i in range(nb_donnees):
        chaine = trame[0:4]
        trame = trame[4:len(trame)]
        data.append(int(chaine))
    
    res.append(data)
    res.append(int(trame[:]))
    return res


def check(mesure,cs):
    somme = 0
    for i in range(len(mesure)):
        somme = somme + abs(mesure[i])
    somme = somme %10000
    return somme == cs
    
    
data = lect_mesures_test(trame)
mesures = data[1]
cs = data[2]

print(mesures)
print(check(mesures,cs))
    





def make_leaf (symbol , weight ):
    return (symbol , weight)
def test (x):
    return isinstance (x, tuple ) and \
    len(x) == 2 and \
    isinstance (x[0] , str) and \
    isinstance (x[1] , int)
    
    
def get1(x):
    return x[0]

def get2(x):
    return x[1]

def get3(huff_tree):
    return huff_tree[0]

def get4 (huff_tree):
    return huff_tree[1]

def get5(huff_tree):
    if test(huff_tree):
        return [get1(huff_tree)] # Attention le symbole est dans une liste
    else :
        return huff_tree[2]

def get6(huff_tree):
    if test(huff_tree):
        return get2(huff_tree) # ??get2q(huff_tree)
    else :
        return huff_tree [3]

def make_huffman_tree ( left_branch , right_branch ):
    return [left_branch,
            right_branch,
            get5(left_branch) + get5(right_branch),
            get6(left_branch) + get6(right_branch)]

### entr \'{e}e : string txt et retourne un dictionnaire contenant chaque
### caractere avec son occurrence dans le string txt
def freq_table (txt):
    ftble = {}
    for c in txt:
        if c not in ftble :
            ftble [c] = 1
        else :
            ftble [c] += 1
    return ftble
    

### Fonction de comparaison qui permet de comparer
### les noeuds de Huffman entre eux selon leur occurrence .
def freq_cmp (node1 , node2 ):
    freq1,freq2 = get6(node1), get6(node2)
    if freq1 < freq2 :
        return -1
    elif freq1 > freq2 :
        return 1
    else :
        return 0
### ins \`{e}re un item \`{a} sa place appropri \'{e}e dans une liste de noeuds et feuilles
def insert_item (item,lst,pos):
    if pos == len(lst):
        lst. append ( item )
    elif freq_cmp (item , lst[pos ]) <= 0 :
        lst. insert (pos , item )
    else :
        insert_item (item , lst , pos +1)
    return

### Construction de l' arbre de Huffman
def build_huffman_tree (txt):
    ### 1. construire une table des occurrences \`{a} partir de txt
    ftble = freq_table (txt)
    ### 2. obtenir la liste des feuilles de Huffman
    lst = list ( ftble . items ())
    ### 3. classer leaf_lst par occurrence de la plus petite \`{a} la plus
    ### grande
    lst. sort (key= lambda lst: lst [1])
    ### 4. construction de l' arbre de huffman
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst [0]
    else :
        ## 5. _____________________________________________________________
        while len(lst) > 2:
            ## 6. _________________________________________________________
            new_node = make_huffman_tree (lst [0] , lst [1])
            ## 7. _________________________________________________________
            del lst [0]
            del lst [0]
            ## 8. _________________________________________________________
            insert_item ( new_node , lst , 0)
        else :
            return make_huffman_tree (lst [0] , lst [1])
"""
import numpy as np
import math
import matplotlib.pyplot as plt
def solve(k,p):
    res=[0]
    e=[0]
    t=[0]
    i=1
    while i<=100:
        e.append(math.sin(i/10))
        res.append(res[i-1]-k*p*(res[i-1]-e[i-1])/10)
        t.append((i/10))
        i=i+1
    return t,res,e
t,res,e=solve(0.5,0.1)
plt.plot(t,e)
plt.plot(t,res)
plt.show()
"""