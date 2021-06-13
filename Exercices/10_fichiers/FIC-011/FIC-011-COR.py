#f=open('complot_contre_lamerique.txt','r',encoding='utf8')




def carac(nom_de_fichier):
    """Renvoie une liste contenant le nombre de caractères
       de chaque ligne de nom_de_fichier"""
    with open(nom_de_fichier,'r',encoding='utf8') as f:
        lignes = f.readlines()
    return [len(x.strip('\n').strip('\t')) for x in lignes]

def somme_carac(nom_de_fichier):
    """Renvoie la somme nombre de caractères
       du texte entier"""
    L=carac(nom_de_fichier)
    S=0
    for x in L:
        S+=x
    return S




nom_de_fichier='complot_contre_lamerique.txt'
T=carac(nom_de_fichier)

def compte_carac(carac,nom_de_fichier):
    '''renvoie pour un caractère de l'alphabet son nombre d'occurence sans tenir compte de la casse contenu dans le fichier nom_de_fichier'''
    with open(nom_de_fichier,'r',encoding='utf8') as f:
        ligne='_'
        S=0
        while ligne!='':
            ligne = f.readline().lower()
            for c in ligne:
                if c==carac.lower():
                    S+=1
        return S

def compte_carac2(carac,nom_de_fichier):
    '''renvoie pour un caractère de l'alphabet son nombre d'occurence sans tenir compte de la casse contenu dans le fichier nom_de_fichier'''
    with open(nom_de_fichier,'r',encoding='utf8') as f:
        texte=f.read()
        return texte.lower().count(carac)

def stat_carac(nom_de_fichier):
    '''renvoie une liste de 26 éléments donnant le nombre d'occurrences de chaque lettre de l'alphabet contenu dans le texte nom_de_fichier sans tenir compte de la casse'''
    alphabet='abcdefghijklmnopqrstuvwxyz'
    occurrences=[]
    for car in alphabet:
        occurrences.append(compte_carac(car,nom_de_fichier))
    return occurrences

import matplotlib.pyplot as plt
from numpy import arange



def tracer_occurrences(nom_de_fichier):
    ''' trace en fonction du numéro de la lettre dans l'alphabet son occurrence dans le fichier \pyv{nom_de_fichier}'''
    y=stat_carac(nom_de_fichier)
    plt.clf()
    plt.plot(y,'ro')
    plt.xlabel("Numéro de la lettre dans l'alphabet")
    plt.ylabel('occurrences')
    plt.savefig('tp06_vosnoms_q10.png')

alphabet='abcdefghijklmnopqrstuvwxyz'
alphabet_liste=len(alphabet)*[]
for c in alphabet:
    alphabet_liste.append(c)
def trace_stat_carac_bis(nom_de_fichier):
    y=stat_carac(nom_de_fichier)
    plt.clf()
    for i,yi in enumerate(y):
        plt.plot([i,i],[0,yi],'r-',linewidth=5)
    plt.ylabel('occurrences')
    plt.xticks(arange(26),tuple(alphabet_liste))
    plt.savefig('histo_occurences.png')
    plt.show()


def tracer_stat_occurrences(nom_de_fichier):
    y=stat_carac(nom_de_fichier)
    S=somme_carac(nom_de_fichier)
    plt.clf()
    for i,yi in enumerate(y):
        plt.plot([i,i],[0,100*yi/S],'r-',linewidth=5)
    plt.ylabel('Fréquences de caractères en %')
    plt.grid()
    plt.title(" Texte de Philip Roth",fontsize=10)
    plt.xticks(arange(26),tuple(alphabet_liste))
    plt.savefig('tp06_vosnoms_q11.png')




def stat_carac_wikipedia(nom_de_fichier):
    '''à partir du fichier nom_du_fichier contenant les statistiques de fréquences de caractères renvoie une liste donnant en fonction de la position de la lettre dans l'alphabet sa fréquence en %.'''
    occurences=[]
    with open(nom_de_fichier,'r',encoding='utf8') as f:
        ligne = f.readline()
        while ligne!='':
            occurences.append(float(ligne.strip('\n').split(';')[1]))
            ligne = f.readline()
    return occurences

occurences_wikipedia=stat_carac_wikipedia('frequence_wikipedia.csv')


def comparaison_stat_carac_pourcent(nom_de_fichier):
    y=stat_carac(nom_de_fichier)
    S=somme_carac(nom_de_fichier)
    y_francais=stat_carac_wikipedia('frequence_wikipedia.csv')
    plt.clf()
    plt.subplot(1,2,1)
    plt.title(" Texte de Philip Roth",fontsize=10)
    for i,yi in enumerate(y):
        plt.plot([i,i],[0,100*yi/S],'r-',linewidth=5)
    plt.ylabel('Fréquences de caractères en %')
    plt.xticks(arange(26),tuple(alphabet_liste))
    plt.grid()
    plt.ylim([0,15])
    plt.subplot(1,2,2)
    plt.title("Articles français de Wikipédia",fontsize=10)
    for i,yi in enumerate(y_francais):
        plt.plot([i,i],[0,yi],'b-',linewidth=5)
    plt.ylabel('Fréquences de caractères en %')
    plt.xticks(arange(26),tuple(alphabet_liste))
    plt.grid()
    plt.ylim([0,15])
    plt.savefig('histo_occurences_pourcent_comparaison.png')



def tracer_stat_wikipedia():
    y_francais=stat_carac_wikipedia('frequence_wikipedia.csv')
    plt.clf()
    plt.title("Articles français de Wikipédia",fontsize=10)
    for i,yi in enumerate(y_francais):
        plt.plot([i,i],[0,yi],'b-',linewidth=5)
    plt.ylabel('Fréquences de caractères en %')
    plt.xticks(arange(26),tuple(alphabet_liste))
    plt.grid()
    plt.ylim([0,15])
    plt.savefig('tp06_vosnoms_q13.png')






