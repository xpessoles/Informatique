#! /usr/bin/env python
# -*- coding: utf-8 -*-

# =====================================
# Ressources pour le TP Codage de César
# =====================================

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

alphabet = [["a",0],["b",0],["c",0],["d",0],["e",0],
            ["f",0],["g",0],["h",0],["i",0],["j",0],
            ["k",0],["l",0],["m",0],["n",0],["o",0],
            ["p",0],["q",0],["r",0],["s",0],["t",0],
            ["u",0],["v",0],["w",0],["x",0],["y",0],
            ["z",0]]


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


texte_chiffre="yr unyy qrager gnvg senvf pbzzr ha pnirnh zef qnyybjnl cbegn yn znva  frf lrhk yhpl yn srzzr qr punzoer ersrezn yn cbegr rg ra ragraqnag yr oehvffrzrag qr frf whcrf pynevffn rhg yvzcerffvba qger har eryvtvrhfr dhv n dhvgg yr zbaqr rg frag fr ersrezre fhe ryyr yrf ibvyrf snzvyvref rg yrf nagvraarf qr ybssvpr genqvgvbaaryf yn phvfvaver fvssybgnvg qnaf yn phvfvar ryyr ragraqvg yr pyvdhrgvf qr yn znpuvar  pever pgnvg fn ivr rg vapyvanag yn ggr iref yn gnoyr qh unyy qrager pbzzr qnaf har nggvghqr qr fbhzvffvba ryyr fr fragvg oavr chevsvr rg fr qvg gbhg ra ceranag yr oybpabgrf b gnvg vafpevg ha zrffntr gycuba dhr qrf zbzragf pbzzr pryhvpv fbag qrf obhetrbaf fhe yneoer qr yn ivr  pr fbag qrf syrhef qr ybzoer fr qvgryyr pbzzr fv har ebfr enivffnagr fgnvg bhiregr cbhe frf frhyf lrhk"

         
#dico=lire_fichier("liste_mots.txt")
#mot = le_mot_le_plus_long(dico)
#liste_mots(dico,25)
#freq = compter_lettre(alphabet,dico)

