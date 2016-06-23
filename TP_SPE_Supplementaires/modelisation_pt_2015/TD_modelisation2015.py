# -*- coding: utf-8 -*-
"""
Created on Wed May  6 06:55:01 2015

@author: upsti
"""

from pylab import *

#-------------------------------------------------------------------------------
# Simulation numérique de la démodulation d'amplitude
#-------------------------------------------------------------------------------

dt=0.1 #Pas de temps
Tmax=2 #Durée de la simulation en s
f=13.56*10**6 #Fréquence de la porteuse: 13.56 MHz

# la fonction E
# def E(E0,f,t):
#     return (E0*sin(2*pi*f*t))
    

#Q1
def init_T(Tmax,dt):
    """
    Fonction qui renvoie une liste de temps de 0 à Tmax par pas dt
    Si Tmax n'est pas un multiple de dt, la la dernière valeur de la liste est arrondie au 
    multiple entier immédiatement supérieur
    n n'est pas une valeur imposée, elle est à déterminer dans la fonction
    """
    T=[]
    if Tmax%dt==0:
        N=int(Tmax//dt)+1
    else:
        N=int(Tmax//dt)+2
    for i in range(N):
        T.append(i*dt)
    return T
    

#Q1_bis
def init_T_bis(Tmax,dt):
    """
    Fonction qui renvoie une liste de temps de 0 à Tmax par pas dt
    Si Tmax n'est pas un multiple de dt, la la dernière valeur de la liste est arrondie au 
    multiple entier immédiatement supérieur
    n n'est pas une valeur imposée, elle est à déterminer dans la fonction
    """
    T=[]
    i=0
    while i<Tmax+dt:
        T.append(i)
        i+=dt
    return T
    
#Q2
def init_E(T,f):
    """
    Fonction qui renvoie la liste des valeurs e(t) aux instants ti de la liste des temps T,
    pour une porteuse sinusoïdale de fréquence f
    """
    E=[]
    delta_t=T[1]-T[0]
    message=[0,1,0]
    Emin=1.3
    Emax=1.5
    for i in range(len(T)):
        j=int(i*delta_t//(16/f))
        val=message[j]
        if val==0:
            e0=Emin
        else:
            e0=Emax
        E.append(e0*sin(2*pi*f*T[i]))
    return E
    
#Q2 bis
def init_E_bis(T,f):
    """
    Fonction qui renvoie la liste des valeurs e(t) aux instants ti de la liste des temps T,
    pour une porteuse sinusoïdale de fréquence f
    """
    E=[]
    n=len(T)
    i=0
    while i<n and T[i]<16/f:
        E.append(1.3*sin(2*pi*f*T[i]))
        i+=1
    while i<n and T[i]<32/f:
        E.append(1.5*sin(2*pi*f*T[i]))
        i+=1
    while i<n:
        E.append(1.3*sin(2*pi*f*T[i]))
        i+=1
    return (E)
    

#Q3 euler explicite
#(s(t_i+1)-s(t_i))/delta_t+s(t_i)/tau=0
#S[i+1]=S[i]*(1-delta_t/tau)

#Q4 euler implicite
#(s(t_i+1)-s(t_i))/delta_t+s(t_i+1)/tau=0
#S[i+1]=S[i]*(tau/(delta_t+tau))

#Q5
def solve(T,E,tau):
    """
    Fonction qui renvoie la liste des valeurs s(t) aux instants ti de la liste des temps T,
    en tenant compte du caractère passant ou bloqué de la diode induit par la valeur de
    l'entrée E[ti] à l'instant ti et de la constante de temps tau, dans le cas d'un montage
    à détection d'enveloppe.
    """
    diode="passante" #Diode supposee etre passante au depart
    S=[0]*(len(E)) #Condition initiale nulle s(0)=0
    delta_t=T[1]-T[0]
    for i in range(1,len(E)-1):
        if diode=="passante":  #cas diode passante
            S[i]=E[i]
            S[i+1]=S[i]*(tau/(delta_t+tau))
            if  S[i+1]>E[i+1]:
                diode="bloquee"
        else:                       #cas diode bloquee
            S[i]=(1-delta_t/tau)*S[i-1]
            S[i+1]=S[i]*(1-delta_t/tau)
            if S[i+1]<=E[i+1]:
                diode="passante"
    return S
    
les_T=init_T(3000*10**(-9),10**(-9))
les_E=init_E_bis(les_T,f)
les_S=solve(les_T,les_E,10**-6)

plt.plot(les_T,les_E)
plt.plot(les_T,les_S)
plt.xlabel('temps en s')
plt.ylabel('tension en V')
plt.legend()
plt.show()


#Q6
# figure 1 : delta_t=100ns donc 30 mesures sur Tmax. A comparer à la fréquence du signal T=1/f
# T=7.374631268436579e-08s=73.74ns
# figure 2 : delta_t=10ns donc 300 mesures
# figure 3 : delta_t=1ns donc 3000 mesures

# Q7
# cas delta_t=100ns, les résultats concernant l'état de la diode sont incohérents et inexploitables
# cas delta_t=10ns, les résultats concernant l'état de la diode présentent qqs zones incertaines
# cas delta_t=1ns, les résultats concernant l'état de la diode sont exploitables
# 
# Q8
# seul le résultat pour delta_t=1ns est exploitable pour la détermination de E0, les variations de S sont limitées dans un intervalle Smax et Smax-0.1V (lecture de la courbe). L'écart à déterminer est entre 1.5V et 1.3V. OK. Il faut delta_t/tau petit, facteur 1000 semble convenir.

# Q9
# (5)10=(0101)2 bit de parité 0
# (16)10=(10000)2 bit de parité 1
# (37)10=(100101)2 bit de parité 1

#-------------------------------------------------------------------------------
# Vérification de l'intégrité des données et correction des erreurs
#-------------------------------------------------------------------------------
   
#Q10
def parite(bits):
    """
    Fonction qui renvoie la valeur du bit de parite d'un mot binaire donné sous forme
    d'une liste de 0 et de 1 nommée bits
    """
    somme_bits=0
    for i in range(len(bits)): #calcul de la somme des bits
        somme_bits+=bits[i] 
    if somme_bits%2==0: #test de la parite de la somme des bits
        return 0
    else:
        return 1

#Q10 bis
def parite2(bits):
    """
    Fonction qui renvoie la valeur du bit de parite d'un un mot binaire donne sous forme
    d'une liste de 0 et de 1 nommee bits
    """
    somme_bits = sum( bits ) #calcul de la somme des bits
    if somme_bits % 2 : #test de la parite de la somme des bits
        return 1
    else:
        return 0
        
# #Q11
# pas de détection de la permutation de deux bits 1 et 0
# pas de correction possible car l'emplacement de l'erreur n'est pas déterminé


#Q12
def encode_hamming(donnee):
    """
    Fonction qui renvoie un message encode par le code de hamming de 7 bits
    a partir d'un argument, nomme donnee, qui est un message de 4 bits sous forme d'une liste
    de 1 et de 0
    """
    d1,d2,d3,d4=[donnee[i] for i in range(len(donnee))]
    p1=parite([d1,d2,d4]) #calcul de parite du triplet 1
    p2=parite([d1,d3,d4]) #calcul de parite du triplet 2
    p3=parite([d2,d3,d4]) #calcul de parite du triplet 3 
    return [p1,p2,d1,p3,d2,d3,d4]

#Q12 bis
def encode_hamming2(donnee):
    """
    Fonction qui renvoie un message encode par le code de hamming de 7 bits
    a partir d'un argument, nomme donnee, qui est un message de 4 bits sous forme d'une liste
    de 1 et de 0
    """
    d1,d2,d3,d4=donnee
    p1=parite([d1,d2,d4]) #calcul de parite du triplet 1
    p2=parite([d1,d3,d4]) #calcul de parite du triplet 2
    p3=parite([d2,d3,d4]) #calcul de parite du triplet 3 
    return [p1,p2,d1,p3,d2,d3,d4]


#Q13
def decode_hamming(message):
    """
    Fonction qui renvoie le message decode, et corrige en cas d'erreur detectee par la 
    technique de hamming
    """
    m1,m2,m3,m4,m5,m6,m7=[message[i] for i in range(len(message))]
    c1=parite([m4,m5,m6,m7])
    c2=parite([m2,m3,m6,m7])
    c3=parite([m1,m3,m5,m7])
    message_decode=[message[2],message[4],message[5],message[6]]
    if c1==0 and c2==0 and c3==0:
        return message_decode #message decode retourne s'il n'y pas d'erreur
    else:
        position_erreur=c1*4+c2*2+c3 #calcul de la position de l'erreur dans le message decode
        print("une erreur de transmission a ete detectee pour le bit en position ",position_erreur)
        if message_decode[position_erreur-1]==1: #permutation de la valeur du bit errone
            message_decode[position_erreur-1]=0
        else:
            message_decode[position_erreur-1]=1       
        return message_decode #message decode retourne corrige en cas d'erreur

    
#Q13 bis
def decode_hamming2(message):
    """
    Fonction qui renvoie le message decode, et corrige en cas d'erreur detectee par la 
    technique de hamming
    """
    m1,m2,m3,m4,m5,m6,m7 = message
    c1 = parite([m4,m5,m6,m7])
    c2 = parite([m2,m3,m6,m7])
    c3 = parite([m1,m3,m5,m7])
    message_decode = [message[2],message[4],message[5],message[6]]
    if c1 == 0 and c2 == 0 and c3 == 0:
        return message_decode #message decode retourne s'il n'y pas d'erreur
    else:
        position_erreur=c1*4+c2*2+c3 #calcul de la position de l'erreur dans le message decode
        print("une erreur de transmission a ete detectee pour le bit en position ",position_erreur)
        if message_decode[position_erreur-1] == 1: #permutation de la valeur du bit errone
            message_decode[position_erreur-1] = 0
        else:
            message_decode[position_erreur-1] = 1       
        return message_decode #message decode retourne corrige en cas d'erreur        


#-------------------------------------------------------------------------------
# Utilisation des données de la puce pour autoriser ou non le passage
#-------------------------------------------------------------------------------
# fichier = open('0001.txt')
# lignes = fichier.readlines()
# fichier.close()
# 
# # ligne 1: recuperation de l'identifiant du titre
# id_titre = int(lignes[0])
# 
# 
# # ligne 2: recuperation des donnees du titre de transport
# donnees_titre = lignes[1].rstrip('\n').split(',')
# zones = [ int(donnees_titre[0]) , int(donnees_titre[1]) ]
# ch_date_fin=donnees_titre[2].split('-')
# date_fin=[ int(ch_date_fin[0]), int(ch_date_fin[1]), int(ch_date_fin[2]) ]
# 
# 
# 
# #Q17: stockage des données dans une liste de liste
# passages=[]
# for i in range(2,5):
#     data = lignes[i] # doit aller de 2 à 4 inclus
#     data = data.rstrip('\n').split(',')
#     liste=[]
#     [liste.append(data[0].split('-')[j]) for j in range (3)]
#     [liste.append(data[1].split(':')[k]) for k in range (3)]
#     liste.append(data[2])
#     passages.append(liste)
    

#Q17bis: stockage des données dans une liste de tuples (correspond moins à l'esprit du sujet)
#passages=[]
#for i in range(2,5):
#    data = lignes[i] # doit aller de 2 à 4 inclus
#    data = data.rstrip('\n').split(',')
#    data = data[0].split('-') , data[1].split(':') , data[2] 
#    passages.append (data)

#Q18
def estAvant(date1,date2):
    if date1[0]<=date2[0]:
        if date1[1]<=date2[1]:
            if date1[2]<=date2[2]:
                return True
    else:
        return False

#Q18bis
#def estAvant(date1,date2):
#    return date1[0] <= date2[0] and date1[1] <= date2[1] and date1[2] <= date2[2]
    
#Q19
def nbSecondesEntre(heure1, heure2):
    return (heure1[0]-heure2[0])*3600 + (heure1[1]-heure2[1])*60 + (heure1[2]-heure2[2])

#Q20
#def testPassage(id_titre):
#    passage = 0 # 0 pas d'erreur, ok pour passer
#    if id_titre in Liste_noire :
#        print ("Titre refusé") #test liste noire
#        passage +=1
#    if Zone not in zones : #zone ok
#        print("Non valide dans cette zone")
#        passage +=1
#    date = maintenant[:,3]
#    if estAvant( date_fin, date) : #date ok
#        print ("Titre expiré")
#        passage +=1
#    if Id_Point == passages[0,6]: #pas validé ici depuis 450s
#        if nbSecondesEntre( Mainteant , passages[0, 5 premiers élèments !]) > 450
#            print("Titre déjà validé") # A COMPLETER (extract propre, et faire pour les 3 lignes de passages)
#    if passage = 0:
#        return True
#    else:
#        return False


def testPassage(id_titre, zones, date_fin,passages) :
    if id_titre in Liste_noire : #test liste noire
        print ("Titre refusé") 
        return False
    if Zone not in zones : #test zone
        print("Non valide dans cette zone")
        return False
    date = Maintenant[:,3]
    if estAvant( date_fin, date) : #test date
        print ("Titre expiré")
        return False
    i=2
    while (i>=0) and (passage[i][6]==Id_point):
        heureactuelle=Maintenant[3, :]
        heuredernierpassage=passages[i][3, :]
        if nbSecondesEntre(heureactuelle,heuredernierpassage)<450:
            print ('Titre déjà validé')
            return False
        i=i-1
    return True




#Q21
#SELECT date, heure in passages ...

#Q22
#SELECT 