#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ================================
# Code de César
# ================================

def lire_fichier(fichier):
    """
    Retourne un tableau avec un mot par ligne
    Keyword arguments :
    fichier -- chaine de caractere contenant le lien vers le fichier.
    """
    # Ouvrir un fichier
    fid=open(fichier, "r")
    tab=[]
    for ligne in fid:
       # Stocker les lignes du fichier dans un tableau en supprimant le retour chariot
        tab.append(ligne.rstrip('\n\r'))
    # Fermer le fichier
    fid.close()
    return tab

def le_mot_le_plus_long(tab):
    """
    Retourne le mot le plus long (String)
    Keyword arguments :
    tab -- tableau avec un mot par ligne
    """
    long_mot = 0
    mot = ""
    for i in range(0,len(tab)):
        if len(tab[i])>long_mot:
            mot = tab[i]
            long_mot = len(tab[i])
    return mot

def liste_mots(tab,n):
    """
    Ecrit la liste des mots de n lettres
    Keyword arguments :
    tab -- tableau avec un mot par ligne
    n -- nombre de lettres
    """
    for i in range(0,len(tab)):
        if len(tab[i])==n:
            print(tab[i])


def recherche_lettre(lettre):
    """
    Retourne la position d'une lettre dans l'alphabet
    Keyword arguments :
    lettre : "lettre" simple
    """
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in range(0,len(alphabet)):
        if alphabet[i]==lettre:
            return i

def compter_lettre(alphabet,dico):
    """
    Retourne une liste avec la fréquence d'appartion de chacune des lettres
    Keyword arguments :
    alphabet -- tableau comprenant dans chacune des cases, la lettre ainsi que sa
    fréquence d'appartion
    dictionnaire -- liste de mots
    """
    for mot in dico:
        for lettres in mot:
            index = recherche_lettre(lettres)
            try :
                alphabet[index][1]=alphabet[index][1]+1
            except TypeError:
                pass
                    
    return alphabet


def codage_cesar(texte_clair,clef):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    texte_code = ""
    for lettre in texte_clair:
        if lettre==" ":
            texte_code = texte_code + " "
        else :
            index = recherche_lettre(lettre.lower())
            try :
                index_code = (index+clef%26)%26
                texte_code = texte_code + alphabet[index_code]
            except TypeError:
                pass
                                                  
    return texte_code

def decodage_cesar(texte_code,clef):
    return codage_cesar(texte_code,-clef)

def broke_cesar(alphabet,texte_code):
    """
    Recherche de la clef du code de cesar
    """

    #Calcul de la fréquence d'appartion de chacune des lettres
    for lettre in texte_code:
        index = recherche_lettre(lettre)
        try :
            alphabet[index][1]=alphabet[index][1]+1
        except TypeError:
            pass

    # Determination de la lettre apparaissant le plus souvent dans le texte code.
    maxi=0
    index = 0
    for i in range(0,len(alphabet)):
        if (alphabet[i][1]>maxi):
            index = i
            maxi = alphabet[i][1]
    #La clef correspond à l'écart entre la position de l'index et la position de
    # e dans l'alphabet (4) index - 4
    
    return index-4



    
texte="Le hall d'entrée était frais comme un caveau. Mrs Dalloway porta la main à ses yeux. Lucy, la femme de chambre, referma la porte, et, en entendant le bruissement de ses jupes, Clarissa eut l'impression d'être une religieuse qui a quitté le monde et sent se refermer sur elle les voiles familiers et les antiennes de l'office traditionnels. La cuisinière sifflotait dans la cuisine. Elle entendit le cliquetis de la machine à écrire. C'était sa vie, et inclinant la tête vers la table du hall d'entrée, comme dans une attitude de soumission, elle se sentit bénie, purifiée, et se dit, tout en prenant le bloc-notes où était inscrit un message téléphoné, que des moments comme celui-ci sont des bourgeons sur l'arbre de la vie ; ce sont des fleurs de l'ombre, se dit-elle (comme si une rose ravissante s'était ouverte pour ses seuls yeux)"
texte2="js jkkjy, qf qjyywj j jxy ywjx kwjvzjsyj js kwfshfnx "
texte3="kdjh stkgxto tigt rdbqat, rpg kdjh tc igdjktgtop atcsgdxi xcsxfjt spch ap ewgpht hjxkpcit"
texte4="spch ath puupxgth st a’psdgpqat bdchxtjg bpgixc"
alphabet = [["a",0],["b",0],["c",0],["d",0],["e",0],
            ["f",0],["g",0],["h",0],["i",0],["j",0],
            ["k",0],["l",0],["m",0],["n",0],["o",0],
            ["p",0],["q",0],["r",0],["s",0],["t",0],
            ["u",0],["v",0],["w",0],["x",0],["y",0],
            ["z",0]]



#a=codage_cesar(texte,13)
#print(a)
#print(broke_cesar(alphabet,a))
b=decodage_cesar(texte2,broke_cesar(alphabet,texte2))
print(b+"\n")
b=decodage_cesar(texte3,broke_cesar(alphabet,texte3))
print(b+"\n")

for i in range(0,25):
    b=decodage_cesar(texte4,i)
    print(b+"\n")
    
b=decodage_cesar(texte4,broke_cesar(alphabet,texte4))
print(b+"\n")
         
#dico=lire_fichier("liste_mots.txt")
#mot = le_mot_le_plus_long(dico)
#liste_mots(dico,25)
#freq = compter_lettre(alphabet,dico)

