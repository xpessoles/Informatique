from tri import *

def chargeClassement(fichier):
    f=open(fichier,'r',encoding='utf8')
    fichier=f.readlines()
    f.close() #ne pas oublier de fermer le fichier...
    L=[]
    for ligne in fichier:
        ligne=ligne.split('\t') # coupe aux tabulations
        L1=[]
        L1.append(ligne[1])
        L1.append(ligne[2])
        L1.append(ligne[4])
        L.append(L1)
    return L


def convertirTemps(temps:str):
    '''temps est un str de la forme "06h 09' 39''" '''
    t_course=temps.split('h') #on peut aussi couper à h
    #print (t_course)
    heure=int(t_course[0])
    t_course2=t_course[1].split("'")
    #print (t_course2)
    duree=int(t_course2[1])+60*int(t_course2[0])+3600*heure
    return duree



def classement(fichier):
    L=chargeClassement(fichier)
    for element in L:
        element[2]=convertirTemps(element[2])
    return L

LG=classement('classement_general.txt')
L18=classement('etape_18.txt')


#Q4
def ajoutTemps(liste1:list,liste2:list)->list:
    LGN=[]
    for x in liste1:
        for y in liste2:
            if x[1]==y[1]:
                LGN+=[[x[0],x[1],y[2]+x[2]]]
    return LGN

def update_classement_general(liste1:list,liste2:list)->list:
    LGN=ajoutTemps(liste1:list,liste2:list)
    LGN.sorted(LGN,key=lambda colles:colles[2])
    return LGN

LGN=ajoutTemps(LG,L18)


