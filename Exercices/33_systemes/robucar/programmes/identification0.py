#Importation des modules
import matplotlib.pyplot as plt
import numpy as np

#Programme principal
fichier='premier_ordre0.csv'
f=open(fichier)
texte=f.readlines()
temps=[]
V=[]
for k in range(len(texte)):
    ligne=texte[k].split(";")
    temps.append(float(ligne[0]))
    V.append(float(ligne[1]))
    
temps2=np.linspace(0,3,len(temps))
V2=np.interp(temps2,temps,V)

fichier2='premier_ordre.csv'
f2=open(fichier,'w')
for k in range(len(temps2)):
    f2.write(str(temps2[k]))
    f2.write(";")
    f2.write(str(V2[k]))
    f2.write("\n")
    
plt.plot(temps,V)
plt.plot(temps2,V2)
plt.title('Reponse indicielle')
plt.xlabel('temps (s)')
plt.ylabel('Vitesse angulaire (rad/s)')
plt.legend()
plt.show()
    