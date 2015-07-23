#!/usr/bin/python
          # -*- coding: utf-8 -*-
#---------------------------
# Lecture d'un fichier binaire

f = open("TP_Fichiers/tongue.bmp", "rb")

while True:
	bytes = f.read(1) # lecture d'un octet
	if bytes == "":
	    break;
	# Affichage de l'octet lu en hexadécimal :
	print "%02X " % ord(bytes[0]),

f.close()

# Ecriture d'un fichier binaire
f=open("TP_Fichiers/monFichier.bin","wb")

f.write("PCSI1")
f.write(int8(83))
f.write(int8(76))
f.write(float32(2.3))

f.close()

#---------------------------
# Lecture d'un fichier texte ligne à ligne

f=open("TP_Fichiers/Mesure_axe_Emericc.txt","r")  # ouverture fichier

ligne = f.readline()                  # lecture d'une ligne
print "%s" % ligne                    # affichage pour vérification
ligne=ligne.rstrip("\n\r")            # suppression retour chariot
noms_grandeurs=ligne.split("\t")      # découpage aux tabulations
noms_grandeurs=noms_grandeurs[1:3]    # suppression de "noms"

for i in range(10):
    ligne = f.readline()  # saut de 10 lignes

ligne = f.readline()                  # lecture d'une ligne 
print "%s" % ligne                    # affichage pour vérification
ligne=ligne.rstrip("\n\r")            # suppression retour chariot
ligne_nbpoints=ligne.split("\t")      # découpage aux tabulations
nb_points=int(ligne_nbpoints[1])      # convertion en entier

numero=[] ; position=[] ; consigne=[] # initialisation tableaux

for i in range(nb_points):
    ligne = f.readline()              # lecture d'une ligne 
    ligne=ligne.rstrip("\n\r")        # suppression retour chariot
    ligne=ligne.replace(",",".")      # changement , en .
    ligne_data=ligne.split("\t")      # découpage aux tabulations
    numero.append(int(ligne_data[0]))
    position.append(float(ligne_data[1]))    # Ajout aux tableaux
    consigne.append(float(ligne_data[2]))

f.close()        # Fermeture fichier

plot(position)   # Tracé de la courbe de position


#---------------------------
# Lecture d'un fichier texte formaté
import numpy

f=open("TP_Fichiers/Mesure_axe_Emericc_formate.txt","r")  # ouverture fichier formaté

# Charger un tableau de données
a=loadtxt("TP_Fichiers/Mesure_axe_Emericc_formate.txt",
          dtype={'names': ('numero', 'position', 'consigne'),
          'formats': ('i2', 'f4', 'f4')},delimiter='\t')
a['numero']
a['position']
a['consigne']
plot(a['numero'],a['position'],'b',a['numero'],a['consigne']/10,'r')

# Idem mais en stockant le résultat dans plusieurs variables
a,b,c=loadtxt("TP_Fichiers/Mesure_axe_Emericc_formate.txt",dtype={'names': ('numero', 'position', 'consigne'),'formats': ('i2', 'f4', 'f4')},delimiter='\t',unpack=True)


# lecture d'une seule colonne de type entier
x=loadtxt("TP_Fichiers/Mesure_axe_Emericc_formate.txt",usecols = (0,),dtype='i4')

x,y=loadtxt("TP_Fichiers/Mesure_axe_Emericc_formate.txt",usecols = (1,2),unpack=True)

f.close()        # Fermeture fichier


#---------------------------
# Ecriture d'un fichier texte ligne à ligne

f=open("TP_Fichiers/monFichier.txt","w")  # ouverture fichier

f.write("La température est froide l'hiver.\n")
f.write("Il fait {:f} degrés.".format(10))

f.close()        # Fermeture fichier


#---------------------------
# Ecriture d'un fichier formaté

f=open("TP_Fichiers/monFichier.txt","w")  # ouverture fichier

x=linspace(-20,20,100)
y=sin(x)/x

for i in range(0,len(x)):
    f.write("{:d} \t {:f} \t {:f}\n".format(i,x[i],y[i]))

f.close()        # Fermeture fichier



