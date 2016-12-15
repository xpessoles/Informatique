#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ================================
# Code de César
# ================================

def lire_dictionnaire(fichier):
    """
    Permet de lire un fichier texte en mettant chaque ligne dans une case d'un tableau.
    fichier est une chaine de caractere contenant le lien vers le fichier.
    """
    # Ouvrir un fichier
    fid=open(fichier, "r")
    tab=[]
    for ligne in fid:
       # Stocker les lignes du fichier dans un tableau en supprimant le retour chariot
        tab.append(fid.readline().rstrip('\n\r'))
    # Fermer le fichier
    fid.close()
    return tab

def lire_texte(fichier):
    """
    Permet de lire un fichier texte en mettant chaque ligne dans une case d'un tableau.
    fichier est une chaine de caractere contenant le lien vers le fichier.
    """
    # Ouvrir un fichier
    fid=open(fichier, "r")
    texte=""
    for ligne in fid:
       # Stocker les lignes du fichier dans un tableau en supprimant le retour chariot
       texte=texte+ligne
        #tab.append(fid.readline().rstrip('\n\r'))
    # Fermer le fichier
    fid.close()
    return texte


def le_mot_le_plus_long(tab):
    """
    Déterminer le mot le plus long du tableau
    """
    mot = ""
    compteur = 0
    for i in range(0,len(tab)):
        if len(tab[i])>compteur:
            compteur = len(tab[i])
            mot = tab[i]
    return mot

def comptage_lettres(tab):
    """
    Décompte du nombre de lettres.
    Renvoi un dictionnaire avec la lettre et sa fréquence
    """
    dico={
        "a":0,"b":0,"c":0,"d":0,"e":0,
        "f":0,"g":0,"h":0,"i":0,"j":0,
        "k":0,"l":0,"m":0,"n":0,"o":0,
        "p":0,"q":0,"r":0,"s":0,"t":0,
        "u":0,"v":0,"w":0,"x":0,"y":0,
        "z":0
        }
         
    for i in range(0,len(tab)):
        for j in range(0,len(tab[i])):
            if (tab[i][j]=="-")|(tab[i][j]==" ")|(tab[i][j]=="!")|(tab[i][j]=="'")|(tab[i][j]==")")|(tab[i][j]=="œ"):
                #On fait rien
                pass
            elif (tab[i][j]=="é")|(tab[i][j]=="è")|(tab[i][j]=="ë")|(tab[i][j]=="ê"):
                dico["e"]=dico["e"]+1
            elif (tab[i][j]=="î")|(tab[i][j]=="ï"):
                dico["i"]=dico["i"]+1
            elif (tab[i][j].lower()=="â")|(tab[i][j]=="à"):
                dico["a"]=dico["a"]+1
            elif (tab[i][j]=="û")|(tab[i][j]=="ü"):
                dico["u"]=dico["u"]+1
            elif (tab[i][j]=="ô"):
                dico["o"]=dico["o"]+1
            elif (tab[i][j]=="ç"):
                dico["c"]=dico["c"]+1
            else :
                try :
                    dico[tab[i][j].lower()]=dico[tab[i][j].lower()]+1
                except KeyError:
                    #print(tab[i])
                    pass

    return dico


def chiffrage_cesar(decalage,texte):
    """On chiffre avec le code de cesar. On decale les nombres de
    la valeur donnée on fait un modulo 26 sur le décalage"""
    decalage = decalage%26
    # Création du dictionnaire
    dico={
        "a":0,"b":1,"c":2,"d":3,"e":4,
        "f":5,"g":6,"h":7,"i":8,"j":9,
        "k":10,"l":11,"m":12,"n":13,"o":14,
        "p":15,"q":16,"r":17,"s":18,"t":19,
        "u":20,"v":21,"w":22,"x":23,"y":24,
        "z":25
        }
    dico_code={}
    for clef in dico :
        dico_code[(dico[clef]+decalage)%26]=clef
        
    texte_code=""
    for lettre in texte:
        if lettre == " ":
            texte_code = texte_code + " "
        else :
            try :
                texte_code = texte_code+dico_code[dico[lettre.lower()]]
            except KeyError:
                pass
    return texte_code

def broke_cesar(texteCode):
    dico={
        "a":0,"b":0,"c":0,"d":0,"e":0,
        "f":0,"g":0,"h":0,"i":0,"j":0,
        "k":0,"l":0,"m":0,"n":0,"o":0,
        "p":0,"q":0,"r":0,"s":0,"t":0,
        "u":0,"v":0,"w":0,"x":0,"y":0,
        "z":0
        }
    for lettre in texteCode:
        try :
            dico[lettre]=dico[lettre]+1
        except KeyError :
            pass
    print(dico)
    maxi = 0
    let = ""
    for lettre in dico :
        if dico[lettre]>maxi:
            let=lettre
            maxi = dico[lettre]
            
    print(let,maxi)
    dico={
        "a":0,"b":1,"c":2,"d":3,"e":4,
        "f":5,"g":6,"h":7,"i":8,"j":9,
        "k":10,"l":11,"m":12,"n":13,"o":14,
        "p":15,"q":16,"r":17,"s":18,"t":19,
        "u":20,"v":21,"w":22,"x":23,"y":24,
        "z":25
        }
    return dico[let]-dico["e"]

        

tab = lire_dictionnaire("liste_francais.txt")
mot = le_mot_le_plus_long(tab)
#dico = comptage_lettres(tab)
chiffrage_cesar(1,"coucou je mappelle tartampion")
texte = lire_texte("TexteClair.txt")

texte_code = chiffrage_cesar(1,texte)
code = broke_cesar(texte_code)
texte_decode=chiffrage_cesar(code,texte_code)

print(texte_decode)
