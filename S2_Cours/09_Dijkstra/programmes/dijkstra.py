# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 10:52:36 2022

@author: xpess
"""
def cherche_min(d, traites):
    """ Renvoie le sommet i vérifiant d[i] minimal et traites[i] faux, 
    s'il existe un tel sommet tel que d[i] != inf. 
    Sinon, renvoie -1 """
    n=len(d)
    x=-1
    for i in range(n):
        if not traites[i] and d[i] != float('inf') and (x==-1 or d[x]>d[i]):
            print("i",i)
            x=i
    print(x)
    return x


def dijkstra_mat(G,s):
    """ 
    G donné par matrice d'adjacence. 
    Renvoie les poids chemins de plus petits poids depuis s. 
    """
    n=len(G)
    d = [float('inf')]*n
    d[s]=0
    traites = [False]*n
    while True:
        print()
        print(d,traites)
        
        x=cherche_min(d,traites)

        if x==-1:
            return d
        for i in range(n):
            d[i]=min(d[i], d[x]+G[x][i])
        traites[x]=True
    

G = [[0,1,2,float("inf"),float("inf")],
     [2,0,2,1,float("inf")],
     [float("inf"),float("inf"),0,float("inf"),3],
     [3,float("inf"),float("inf"),0,1],
     [float("inf"),float("inf"),float("inf"),float("inf"),0]]

GG = [[0,9,float("inf"),5,float("inf")],
      [float("inf"),0,1,2,float("inf")],
      [float("inf"),float("inf"),0,float("inf"),4],
      [float("inf"),3,9,0,2],
      [7,float("inf"),6,float("inf"),0]]

       
