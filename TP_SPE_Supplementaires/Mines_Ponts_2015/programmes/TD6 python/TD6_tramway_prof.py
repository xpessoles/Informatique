import matplotlib.pyplot as plt
# comptage du nombre de ligne
fichier = open('tramway.txt','r')    # Ouverture d'un fichier en lecture:
lecture = fichier.readlines()
nb_lignes = len(lecture)        
fichier.close()                      # Fermeture du fichier

# extraction des données utiles
fichier = open('tramway.txt','r')
fichier.readline() # saut d'une ligne (non prise en compte des intitulés temps,..)

# initialisation des listes
temps=[]
acceleration=[]
accel_lat=[]

for i in range(nb_lignes-2):
    ligne=fichier.readline()            # lecture d'une ligne
    ligne=ligne.rstrip ("\n\r")         # suppression retour chariot
    ligne=ligne.replace(",",".")        # changement , en .
    ligne_data=ligne.split("\t")        # découpage aux tabulations
    
# Création des listes
    temps.append(ligne_data[1])         # extraction temps
    acceleration.append(ligne_data[5])  # extraction acceleration longitudinal (selon y)
    accel_lat.append(ligne_data[3])     # extraction acceleration latéral (selon x)

fichier.close() # Fermeture du fichier

# conversion en flottant et en unité SI
for k in range(len(temps)):
    temps[k]=float(temps[k])
    acceleration[k]=float(acceleration[k])*9.81 # m.s-2
    accel_lat[k]=float(accel_lat[k])*9.81

# tracé des courbes
def affiche(L):
    plt.plot(temps,L)
    plt.xlabel("temps (en s)")
    plt.show()
    

#Fonction maxi1
def maxi1(L):
    if len(L)==0:
        return None
    elif len(L)==1:
        return L[0]
    else:
        x=maxi1(L[1:len(L)])
        if x>=L[0]:
            return x
        else:
            return L[0]
            
#Fonction maxi2
def maxi2(L):
    if len(L)==0:
        return None
    elif len(L)==1:
        return L[0]
    else:
        n=len(L)
        x=maxi2(L[0:n//2])
        y=maxi2(L[n//2:n])
        if x>y:
            return x
        else:
            return y

# moyenne glissante
def filtre_mg1(L,N):
    mg=[]
    for p in range(len(L)):
        mg_k=0
        for k in range(N):
            mg_k=mg_k+(L[p-k])/N
        mg=mg+[mg_k]
    return mg

# détermination de la vitesse par intégration
pas_temps=temps[1]-temps[0]   # calcul du pas temporel
vitesse=[0] # vitesse initiale
for i in range (len(temps)-1):
    vitesse=vitesse+[vitesse[i]+acceleration[i]*pas_temps] 

# détermination de la position par intégration
position=[0] # position initiale
for i in range (len(temps)-1):
    position=position+[position[i]+vitesse[i]*pas_temps]
    
#affiche(position) 
#affiche(vitesse)  
#affiche(acceleration) 
affiche(filtre_mg(accel_lat,5))

