import os
os.chdir(r'F:\Github\Informatique\P_05_AlgorithmiqueProgrammation\03_Tris\TD_02_Arbre\programmes')

import sys
sys.setrecursionlimit(1000000)

from tris import *
from random import randint
from time import time
# 
# 
# n = 8000
# liste = [randint(0,n) for x in range(n)]
# liste.sort()
# 
# # t1=time()
# # tri_insertion(liste)
# # t1=time()-t1
# # print("Insertion "+str(t1))
# # 
# # liste.reverse()
# # 
# # t1=time()
# # tri_insertion(liste)
# # t1=time()-t1
# # print("Insertion "+str(t1))
# 
# t1=time()
# tri_quicksort(liste,0,n-1)
# t1=time()-t1
# print("Rapide "+str(t1))
# 
# liste.reverse()
# t1=time()
# tri_quicksort(liste,0,n-1)
# t1=time()-t1
# print("Rapide "+str(t1))

file = "classement_general.txt"
fid = open(file,'r')
tab = []
for ligne in fid:
    tab.append(ligne.split("\t"))
fid.close()