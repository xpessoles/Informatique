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
                    
    return dico


alphabet = [["a",0],["b",0],["c",0],["d",0],["e",0],
            ["f",0],["g",0],["h",0],["i",0],["j",0],
            ["k",0],["l",0],["m",0],["n",0],["o",0],
            ["p",0],["q",0],["r",0],["s",0],["t",0],
            ["u",0],["v",0],["w",0],["x",0],["y",0],
            ["z",0]]
    
dico=lire_fichier("liste_mots.txt")
mot = le_mot_le_plus_long(dico)
liste_mots(dico,25)
freq = compter_lettre(alphabet,dico)
#print(mot)
