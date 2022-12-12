''' 11 - Bases des graphes'''
from Affichage import *
import pdb
import os
## 11-3 - A star

## Création de l'image

# Initialisation

Nl,Nc = 5,9
Image = 255*np.ones((Nl,Nc,3),dtype='uint8')

# Obstacles

Noir = [0,0,0]

for l in range(1,4):
    Image[l,4] = Noir

for c in range(4,6):
    Image[1,c] = Noir

# Depart - Arrivee

'''ATTENTION: partir d'un point blanc'''
lDep,cDep = 3,7
lA,cA = 0,1
Rouge = [255,0,0]
Image[lDep,cDep] = Rouge
Bleu = [0,0,255]
Vert = [0,180,0]
Image[lA,cA] = Bleu

Depart = (lDep,cDep)
Arrivee = (lA,cA)

# Affichage

Affiche(1,Image,True)




###Heuristique


from math import sqrt



def distance_man(l,c,la,ca):
    dec=min(abs(la-l),abs(c-ca))
    return int(10*(abs(l-la)-dec)+10*(abs(c-ca)-dec)+dec*14)


def f_man0(l,c,la,ca):
    d_fin = distance_man(l,c,la,ca)
    d_debut = distance_man(l,c,lDep,cDep)
    return d_fin

def f_man(l,c,la,ca):
    d_fin = distance_man(l,c,la,ca)
    d_debut = distance_man(l,c,lDep,cDep)
    return d_fin+d_debut

def f_man2(Dist_depuis_depart,la,ca):
    d_fin = distance_man(l,c,la,ca)
    d_debut = Dist_depuis_depart
    return d_fin+d_debut

# def f_man(l,c,la,ca):
#     d_fin = distance_man(l,c,la,ca)
#     d_debut = distance_man(l,c,lDep,cDep)
#     return d_debut



Affiche_distance(1,Image,True,f_man0,Arrivee)


# Fonction de comparaison de pixels

def Test_Pix(P1,P2):
    Res = True
    for i in range(3):
        Test = P1[i]==P2[i]
        Res = Res & Test
    return Res

# Initialisation de Dico_Voisins

Noir = [0,0,0]
Dico_Voisins = {}
for l in range(Nl):
    for c in range(Nc):
        Pix = Image[l,c]
        Case = (l,c)
        if Test_Pix(Pix,Noir)==False:
            Dico_Voisins[Case] = []


# Fonction de traitement des voisins d'une case

from math import sqrt

def Couples_Voisins(l,c):
    Case = (l,c)
    for li in range(l-1,l+2):
        for ci in range(c-1,c+2):
            Case_i = (li,ci)
            # Ne pas traiter la case actuelle
            test_case = (Case_i != Case)
            # Etre dans l'image
            test_image = (0 <= li < Nl and 0 <= ci < Nc)
            if test_case and test_image:
                Pixi = Image[li,ci]
                if Test_Pix(Pixi,Noir)==False:
                    Di = int(sqrt((li-l)**2+(ci-c)**2)*10)
                    Couple = [Case_i,Di]
                    Dico_Voisins[Case].append(Couple)

# Remplissage de Dico_Voisins

for Case in Dico_Voisins.keys():
    l,c = Case
    Pix = Image[l,c]
    Couples_Voisins(l,c)





#Initialisation ds distances

Distances = np.inf*np.ones([Nl,Nc])
Distances[lDep,cDep] = 0
# Provenances = {}
Reste = Dico_Voisins.copy()
S = (lDep,cDep)
del Reste[S]
Image_Anim=Image.copy()




#On recherche l'heuristique pour les voisins de S
chemin=[(S,f_man2(Distances[lDep,cDep],lA,cA),distance_man(lDep,cDep,lA,cA),Distances[lDep,cDep])]
visited={S:(f_man2(Distances[lDep,cDep],lA,cA),distance_man(lDep,cDep,lA,cA),Distances[lDep,cDep])}
it=0

Voisins_g = Dico_Voisins[S]
Voisins=Voisins_g


while S!=(lA,cA) and len(Reste)>0:
    Min=np.inf
    Min2=np.inf
    S0=S
    for V in Voisins_g:
        s,_ = V
        if s in Reste:
            l,c=s
            Distances[l,c]=min(distance_man(l,c,S0[0],S0[1])+Distances[S0[0],S0[1]],Distances[l,c])
            heuristique=f_man2(Distances[l,c],lA,cA)
            visited[s]=(heuristique,distance_man(l,c,lA,cA),Distances[l,c])
            Image_Anim[s] = Vert
            if [s,Distances[l,c]] not in Voisins_g:
                Voisins_g.append([s,Distances[l,c]])
            if heuristique<Min:
                Min=heuristique
                Min2=distance_man(l,c,lA,cA)
                S=s
            elif heuristique==Min and distance_man(l,c,lA,cA)<Min2:
                Min=heuristique
                Min2=distance_man(l,c,lA,cA)
                S=s
    Voisins_g.remove([S,Distances[S[0],S[1]]])
    Voisins= Dico_Voisins[S]
    for V in Voisins:
        Voisins_g.append(V)
    it+=1
    l,c=S
    print(S,Min,Min2,Distances[l,c])
    chemin.append((S,Min,Min2,Distances[l,c]))
    Image_Anim[S] = Rouge
    # for x in Chemin_final:
    #     Image_Anim[x]=Bleu
    Chemin_image = "Animations/Astar/"+str(it)+".png"
    plt.clf()
    Affiche_Save(22,Image_Anim,True,Chemin_image,visited)
    del Reste[S]

