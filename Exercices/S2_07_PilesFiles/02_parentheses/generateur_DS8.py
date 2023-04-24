#!/usr/bin/python3
import pdb
import scipy.stats as ss

"""Calcule les solutions du DS
   Usage :

   python3 generateur.py p q

   écrit sur la sortie standard un csv (séparateur : ";") pour les
   valeurs du paramètre alpha dans range(p, q). L'entête comporte les
   numéros des questions, la valeur de alpha est en première colonne."""

from math import sqrt, floor, ceil, log

motifs='0123456789+-*()[]{}'

def Lu(alpha):
    """u_n, u_0 = alpha"""
    x = 0
    M=''
    n=500+(-1)**alpha*2*alpha%97
    a=137
    c=187
    m=2**8
    maxi=len(motifs)
    for i in range(n):
        x = (a * x+c) % m
        if x<maxi:
            M+=motifs[x]
    return M

for a in range(1,100):
    texte=Lu(a)
    with open('expression_parenthesee_'+str(a)+'.txt','w') as f:
        f.write(texte)

def charger_expression_parenthesee(alpha):
    with open('expression_parenthesee_'+str(alpha)+'.txt','r') as f:
        code=f.read()
    return code

alpha=99
L=Lu(alpha)
r1=len(L)
r2=L.count('(')




print('r1 : \n',r1)
print('r2 : \n',r2)
# print('r3 : \n',r3)
# print('r4 : \n',r4)
# print('r5 : \n',r5)
# print('r6 : \n',r6)
# print('r7 : \n',r7)
# print('r8 : \n',r8)
# print('r9 : \n',alphabet_crypte)
# print('r10 : \n',r10)
# print('r11 : \n',r11)
# print('r12 : \n',r12)


# def reponses():
#     "Génère le csv des réponses"""
#     header = ('alpha,R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14\n')
#     with open('d08s_reponses.csv','w') as f:
#         f.write(header)
#         for a in range(1,100):
#             L=Lu(a)
#             r1=len(L)
#             r2=max(L)
#
#             #L = [a,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12]
#             L = [a,r1,r2]
#             ligne = ','.join([str(t) for t in L])+'\n'
#             f.write(ligne)
#     return None
#



def corrige(alpha_sol):
    """Produit un tableau t contenant les valeurs attendues pour le DS,
        en fontion du paramètre alpha.
        t[0] contient la valeur de alpha et t[i] pour i=1, ..., 18
        contient la valeur attendue pour la question i."""
    sol = [alpha_sol]
    L=Lu(alpha_sol)
    r1=len(L)
    r2=L.count('(')
    # u_alpha=compter_u(L)
    # r3=sum(u_alpha)
    # r4=compter_doublon(u_alpha)
    # r5=u_alpha[alpha_sol]
    # t=counting_sort(L)
    # r6=t[alpha_sol]
    # r7=u(alpha_sol,100)
    # r8=chiffrement_cesar('franz',r7)
    # r9=chiffrement_cesar(alphabet,r7)
    # code=chiffrement_cesar(mess,r7)
    # r10=code.count('a')
    # code=charger_texte_crypter(alpha_sol)
    # r11=code.count('e')
    # r12=decryptage_cesar1(code)





    #Qu 1
    sol.append(r1)



    #Q2
    sol.append(r2)

    # #Q4
    # sol.append(r3)
    #
    # #Q5
    # sol.append(r4)
    #
    # #Q6
    # sol.append(r5)
    #
    # #Q7
    # sol.append(r6)
    #
    # #Q8
    # sol.append(r7)
    #
    # #Q9
    # sol.append(r8)
    #
    # #Q10
    # sol.append(r9)
    #
    # #Q11
    # sol.append(r10)
    #
    # #Q12
    # sol.append(r11)
    #
    # #Q13
    # sol.append(r12)

    # Q14
    # sol.append(r13)
    #
    # Q15
    # sol.append(r14)


    return sol

def convv(v):
    """Convertis la valeur v en chaîne de caractère. Dans le cas d'un
       flottant, on arrondit à 3 chiffres après la virgule."""
    if isinstance(v, float):
        return "{:.3f}".format(v)
    return str(v)

def conv(v):
    """Convertis la valeur v en chaîne de caractère. Dans le cas d'un
       flottant, on arrondit à 5 chiffres après la virgule."""
    if isinstance(v, float):
        return "{:.5f}".format(v)
    return str(v)


def conv10(v):
    """Convertis la valeur v en chaîne de caractère. Dans le cas d'un
       flottant, on arrondit à 5 chiffres après la virgule."""
    if isinstance(v, float):
        return "{:.10f}".format(v)
    return str(v)

def print_line(l):
    """Affiche les valeurs de la ligne l, séparées par des ";". """
    print(';'.join(convv(v) for v in l))

def renvoie_line(l):
    """Affiche les valeurs de la ligne l, séparées par des ";". """
    return(';'.join(conv(v) for v in l))

def generer_tableau_sol(alpha):
    t = ['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12']
    sols=corrige(alpha)
    tableau_tex='\\textbf{Exemples de réponse pour $\\alpha='+str(alpha)+'$}\n\n'
    tableau_tex+='\\begin{tabular}{|c|c|} \n '
    tableau_tex+='\\hline\nQuestion & Réponse \\\\\n\\hline\n'
    i=0
    for sol in sols[1:]:
        if t[i]=='Q20':
            tableau_tex+=t[i]+' & '+conv10(sol)+' \\\\\n\\hline\n'
        else:
            tableau_tex+=t[i]+' & '+conv(sol)+' \\\\\n\\hline\n'
        i+=1
    tableau_tex+='\\end{tabular}'
    with open('/Users/emiliendurif/Dropbox/cpge/ipt_mpsi_ds/exos/solution_ds/fiches_reponses_exemple_DS8_2021_2022.tex','w') as f0:
        f0.write(tableau_tex)

from sys import argv

def main():
  #alphas=range(int(argv[1]),int(argv[2]))
  alphas=range(1,99)
  t = ['0','Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12']
  t[0] = 'alpha'
  print_line(t)
  tableau_tex='\\begin{longtable}{|'+len(t)*'c|'+'} \n '
  with open('reponses.csv','w') as f0:
    line=renvoie_line(t)
    tableau_tex+='\\textbf{'+line.replace(';','}&\\textbf{')+'}\\endhead \n\\hline \n'
    f0.write(line+'\n')
    for ax in alphas:
        line=corrige(ax)
        print_line(line)
        f0.write(renvoie_line(corrige(ax)))
        tableau_tex+=renvoie_line(corrige(ax)).replace(';','&')+'\\\\ \n\\hline \n'
        f0.write('\n')
    tableau_tex+='\\end{longtable}\n'
    #print(tableau_tex)
    with open('/Users/emiliendurif/Dropbox/cpge/ipt_mpsi_ds/exos/solution_ds/fiches_reponses_exemple_DS8_2021_2022-cor.tex','w',encoding='utf8') as f1:
        f1.write(tableau_tex)
  # for a in alphas:
  #   print_line(corrige(a))

# if __name__ == "__main__":
#    main()


def generer_note(fichier_resultats,erreur1,erreur2):
    #fichier_resultats='DS5_machine_ipt_2020_2021.csv'
    with open(fichier_resultats,'r',encoding='utf8') as f:
        data=f.readlines()
    notes=[]
    notes_valeurs=[]
    titre_questions=data[0].strip().split(';')[4:]
    moyenne=0
    for ligne in data[1:]:
        ligne=ligne.strip().split(';')
        #pdb.set_trace()
        #print(ligne)
        alpha=int(ligne[1])
        #alpha=int(ligne[1][1:-1])
        #nom=ligne[2][1:-1]
        nom=ligne[2]
        #classe=ligne[4][1:-1]
        classe=ligne[4]
        if '1' in classe:
            erreur=erreur1
        else:
            erreur=erreur2
        note=[nom,classe]
        note_valeurs=note.copy()
        bonnes_reponses=corrige(alpha)[:]
        # bonnes_reponses=corrige(alpha)[1:5]
        # bonnes_reponses+=[corrige(alpha)[5][0]]
        # bonnes_reponses+=[corrige(alpha)[5][1]]
        # bonnes_reponses+=[corrige(alpha)[5][2]]
        # bonnes_reponses+=corrige(alpha)[6:]
        for x in bonnes_reponses:
            note_valeurs.append(conv(x))
        for i,x in enumerate(bonnes_reponses[1:]):
            #print(type(x),x,i)
            #pdb.set_trace()
            if type(x)==str:
                #pdb.set_trace()
                res=ligne[5+i]
                note.append(int(res==x))
            # else:
            #     for j,reponse in enumerate(ligne[5:]):
            #         car1=''
            #         if reponse=='oajwi':
            #             pdb.set_trace()
            #         for car in reponse:
            #             #print(car,car.isnumeric())
            #             if car.isnumeric() or car=='.' or car=='[' or car==']' or car==',' or car=='-':
            #                 car1+=car
            #         #print(ligne,car1)
            #         ligne[5+j]=car1
            #
            #     # if 5+i==16:
            #     #     pdb.set_trace()
            #     #
            #     # print(5+i)
            elif ligne[5+i]=="" or ('[' in ligne[5+i] and (type(x)!=np.ndarray or type(x)!=list)):
                note.append(0)
                #res='0'
            elif type(x)==np.ndarray or type(x)==list:
                # if 'ADAMCZAK' in nom.upper():
                #     pdb.set_trace()
                res=ligne[5+i]
                note.append(int(str(x.tolist()).replace(' ','') in res or str(x.tolist()).replace(' ','') in res.replace(' ','') or str(x) in res or str(x).replace(' ',',') in res))
            elif type(x)==int:
                if ligne[5+i]=='.' or ligne[5+i].isalpha():
                    res=0
                else:
                    res=float(ligne[5+i])
                note.append(int(x==res))
            elif type(x)==float or type(x)==np.float64:
                res=ligne[5+i]
                if ',' in res:
                    res=float(res.replace(',','.'))
                # elif '^' in res:
                #     res=float(res.replace('^','**'))
                else:
                    try:
                        float(res)
                    except:
                        res=x+1
                    res=float(res)
                note.append(int(abs(x-res)<=erreur))
            # elif type(x)==str:
            #     pdb.set_trace()
            else:
                res=float(ligne[5+i][:].copy())
                note.append(int(abs(x-res)<=erreur))
            note_valeurs.append(res)
            #pdb.set_trace()
        #coeffs=(len(note)-2)*[1]
        coeffs=[2,2,2,2,2,2,2,2,2,2,2,2]
        note_globale=np.dot(np.array(note[2:]),np.array(coeffs))*20/sum(coeffs)
        note.append(note_globale)
        notes.append(note)
        notes_valeurs.append(note_valeurs)
        moyenne+=note_globale
    moyenne=moyenne/len(notes)
    return moyenne,notes,coeffs,titre_questions,notes_valeurs




# def exporter_notes(notes,file,delimiter):
#

def remplacer_dans_fichier(fichier0,fichier,carac0,carac1):
  with open(fichier0,'r',encoding='utf-8') as f:
    texte0=f.read()
    texte=texte0.replace(carac0,carac1)
  with open(fichier,'w',encoding='utf-8') as f:
    f.write(texte)



#######
#Generer sujet
#######

# reponses()
# main()
# generer_tableau_sol(99)

# ####Correction
####Correction
# fichier_resultats0='/Users/emiliendurif/Dropbox/cpge/ipt_mpsi_ds/DS05/DS5_machine_ipt_2021_2022.csv'
# remplacer_dans_fichier(fichier_resultats0,fichier_resultats0.split('.csv')[0]+'2.csv','","','";"')
#
# fichier_resultats=fichier_resultats0.split('.csv')[0]+'2.csv'
# import numpy as np
# erreur=1e-4
# erreur1=1e-4
# erreur2=1e-4
# #pdb.set_trace()
# moyenne,notes,coeffs,titre_questions,notes_valeurs=generer_note(fichier_resultats,erreur1,erreur2)
#
#
# ###Calcul du rang
#
# notes_array=np.array(notes)[:,-1]
#
#
# def calculate_rank(vector):
#   a={}
#   rank=1
#   for num in sorted(vector):
#     if num not in a:
#       a[num]=rank
#       rank=rank+1
#   return[a[i] for i in vector]
#
# rang=calculate_rank(notes_array)
#
#
#
# file='Notes_DS5_machine_ipt_2021_2022.csv'
# file_valeurs=file.split('.csv')[0]+'_valeurs.csv'
#
# with open(file,'w',encoding='utf-8') as f:
#     f.write('Nom;'+renvoie_line(titre_questions)+'\n')
#     f.write(';;'+renvoie_line(coeffs)+'\n')
#     for note in notes:
#         f.write(renvoie_line(note)+'\n')
#
#
# with open(file_valeurs,'w',encoding='utf-8') as f:
#     ligne=''
#     for note in notes_valeurs:
#         #f.write(renvoie_line(note)+'\n')
#         for i,x in enumerate(note):
#             # if i==len(note)-1:
#             #     ligne+=str(x)+','+str(rang[i])+'\n'
#             # else:
#             #     ligne+=str(x)+','+str(rang[i])+';'
#             if i==len(note)-1:
#                 ligne+=str(x)+'\n'
#             else:
#                 ligne+=str(x)+';'
#         print(ligne)
#     f.write(ligne)
