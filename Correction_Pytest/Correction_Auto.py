# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:29:40 2022

@author: Xavier Pessoles
"""

import os
import shutil as sh
import codecs


# Répetoire contenant les scripts des élèves
REP_ELEVE = "scripts_eleves" 

# Répertoire de correction
REP_COR = "travail"


def make_list_files(rep:str)-> list:
    """
    Liste des fichiers des élèves

    Parameters
    ----------
    rep : str
        dossier provenant de moodle.

    Returns
    -------
    List(str) : liste des chemins

    """
    liste_py = []
    for root, dirs, files in os.walk(rep): 
        for file in files:
            liste_py.append(rep+"/"+os.path.basename(root)+"/"+file)
        
    return liste_py


def corriger_eleve(file_py,rep_travail):
    """
    Corriger un fichier python

    Parameters
    ----------
    file_py : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    # Récupération du nom du fichier
    nom = file_py.split("/")
    nom = nom[-1][:-3] # On récupere le nom sans l'extension .py
    
    # Copie du fichier python dans le répertoire de correction
    sh.copy(file_py,rep_travail+"/RechercheCheminEleve.py")
    os.chdir(rep_travail)
    nom = nom+".txt"
    
    commande = 'pytest >> '+nom
    print(commande)
    #os.system(commande)


files_eleves = make_list_files(REP_ELEVE)
files_eleves_py = make_list_files("fichiers_py")

# Génération des PDF des élèves
def make_pdf(files_eleves_py):
    for f in files_eleves_py : 
        print(f)
        nom_fichier = f.split("/")[-1]
        sh.copy("fichiers_py/"+nom_fichier,"compil/eleve.py")
        os.chdir("compil")
        os.system("pdflatex PythonEleve")
        os.chdir("..")
    
        sh.copy("compil/PythonEleve.pdf","pdf_eleves/"+nom_fichier+".pdf")

def make_pytest(files_eleves_py):
    for f in files_eleves_py : 
        print(f)
        nom_fichier = f.split("/")[-1]
        sh.copy("fichiers_py/"+nom_fichier,"travail/eleve.py")
        os.chdir("travail")
        
        file_diff = "test.diff"
        print("Pytest")
        os.system("pytest >> "+file_diff)
        
        print("Conversion du diff en utf8")
        #read input file
        with codecs.open(file_diff, 'r', encoding = 'ansi') as file:
            lines = file.read()

        #write output file
        with codecs.open(file_diff, 'w', encoding = 'utf8') as file:
            file.write("``` diff \n")
            file.write(lines)
            file.write("```")
            
        print("Pandoc")
        os.system("pandoc -o file_diff.pdf "+file_diff)
        os.remove(file_diff)
        os.chdir("..")     
    
        sh.copy("travail/file_diff.pdf","pdf_eleves/"+nom_fichier+"_diff.pdf")
        
    
make_pytest(files_eleves_py)

#for f in files_eleves :
    #sh.copy(f,"fichiers_py")
    
#file_py = files_eleves[0]
#corriger_eleve(file_py, REP_COR)