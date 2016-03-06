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







# tracé des courbes
def affiche(L):







#Fonction maxi1
def maxi1(L):
   
   
   
   
   
   
   
   
            
#Fonction maxi2
def maxi2(L):








# moyenne glissante
def filtre_mg(L,N):
   
   
   
   
   
# détermination de la vitesse par intégration
pas_temps=temps[1]-temps[0]   # calcul du pas temporel
vitesse=[0] # vitesse initiale




# détermination de la position par intégration
position=[0] # position initiale




