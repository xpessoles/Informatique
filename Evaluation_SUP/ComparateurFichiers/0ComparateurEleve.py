# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:23:08 2014

@author: Xavier Pessoles
"""


class StatEleve(object):
    """
    L'objet stat élève contient :
        * le nom de l'élève
        * un id
        * son tableau de stat
    """
    def __init__(self,file,id_eleve):
        self.nom = file[0:-3]
        self.id_eleve = id_eleve
        self.stats = generateStats(file)
    
    
def generateStats(fichier):
    fid = open(fichier,"r")
    donnees = fid.readlines()
    fid.close()
    dico={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,
              "g":0,"h":0,"i":0,"j":0,"k":0,"l":0,
              "m":0,"n":0,"o":0,"p":0,"q":0,"r":0,
              "s":0,"t":0,"u":0,"v":0,"w":0,"x":0,
              "y":0,"z":0,"A":0,"B":0,"C":0,"D":0,
              "E":0,"F":0,"G":0,"H":0,"I":0,"J":0,
              "K":0,"L":0,"M":0,"N":0,"O":0,"P":0,
              "Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,
              "W":0,"X":0,"Y":0,"Z":0,"0":0,"1":0,
              "2":0,"3":0,"4":0,"5":0,"6":0,"7":0,
              "8":0,"9":0,"²":0,"&":0,"é":0,"\"":0,
              "'":0,"(":0,"-":0,"è":0,"_":0,"ç":0,
              "à":0,")":0,"=":0,"~":0,"#":0,"{":0,
              "[":0,"|":0,"`":0,"\\":0,"^":0,"@":0,
              "]":0,"}":0,"$":0,"£":0,"%":0,"ù":0,
              "*":0,"<":0,">":0," ":0,",":0,";":0,
              ":":0,"!":0,"?":0,".":0,"/":0,"§":0,
              "+":0,"\n":0,"\t":0,"Ã":0,"©":0,"¨":0}
    for ligne in donnees:
        for lettre in ligne:
            try :
                dico[lettre]=dico[lettre]+1
            except :
                print("Carcactere ignore : "+lettre)
    return dico

def generation_combinaisons(nb):
    """ Génération des combinaisons de 2 nombres parmis """
    tab=[]
    for i in range(nb-1):
        for j in range (i+1,nb):
            tab.append([i,j])
    return tab
    

def compare(dicoa,dicob):
    res=[]
    for char in dicoa :
        if dicoa[char]>5:
            #On ne fait des comparaisons que si le nombre d'occurence du caractere est supérieur à 5
            mini = dicoa[char]
            maxi = dicob[char]
            if mini >maxi :
                mini,maxi=maxi,mini
            ressemblance = (100- 100*abs(maxi-mini)/maxi)
           # print(char+"\t"+str(dicoa[char])+"\t" + str(dicob[char])+"\t"+str(ressemblance))
           # print(abs(dicoa[char]-dicob[char])/dicoa[char])
            res.append([char,ressemblance])
    somme=0
    for e in res:
        somme = somme + e[1]

    return somme/len(res)

###### MAIN ######
#def main():
liste_fichier=os.listdir()
del(liste_fichier[0])
#liste_fichier=['Billiottet.py','Fischini.py']
print(liste_fichier)
tab=[]
i=0
for fichier in liste_fichier:
    print(fichier)
    #dico = generateStats(fichier)
    tab.append(StatEleve(fichier,i))
    i+=1
combinaisons = generation_combinaisons(len(liste_fichier))
res=[]
for combi in combinaisons:
    res.append([compare(tab[combi[0]].stats,tab[combi[1]].stats),
                tab[combi[0]].nom,
                tab[combi[1]].nom])
                

#main()
res.sort()
tracex=[]
tracey=[]
i=0
for e in res : 
    tracex.append(i)
    tracey.append(e[0])
    i+=1
    print(str(e[0])+"  "+e[1]+" <=> "+e[2])

plt.plot(tracex,tracey,'r.')
plt.show()