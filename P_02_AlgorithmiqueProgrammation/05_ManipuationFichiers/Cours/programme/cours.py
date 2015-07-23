#!/usr/bin/python
          # -*- coding: utf-8 -*-

f=open("Mesure_axe_Emericc2.txt","r")  # ouverture fichier


numero,position,consigne=[],[],[]
for i in range(100):
    ligne = f.readline()              # lecture d'une ligne 
    ligne=ligne.rstrip("\n\r")        # suppression retour chariot
    ligne=ligne.replace(",",".")      # changement , en .
    ligne_data=ligne.split("\t")      # découpage aux tabulations
    numero.append(int(ligne_data[0]))
    position.append(float(ligne_data[1]))    # Ajout aux tableaux
    consigne.append(float(ligne_data[2]))

f.close()        # Fermeture fichier

#plot(position)   # Tracé de la courbe de position

"""
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
"""
