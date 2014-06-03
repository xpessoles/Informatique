# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 23:39:30 2014

@author: Xavier
"""

from random import randrange

def generateCouple(n):
    i=0
    tab = []
    while i<n:
        i+=1
        tab.append([(randrange(0,2000)-1000)/1000,
                   (randrange(0,2000)-1000)/1000])
    return tab


def sortCouple(couples):
    resT=[] # resultats True (dans la cible)
    resF=[] # resultats False (hors la cible)
    for i in range(len(couples)):
        if (couples[i][0]**2+couples[i][1]**2)>1:
            resF.append(couples[i])
        else :
            resT.append(couples[i])
    return resT,resF

#Affichage
resT,resF = sortCouple(generateCouple(10000))

def generateXY(tab):
    #remise en forme des points
    ptx,pty=[],[]
    for i in range(len(tab)):
        ptx.append(tab[i][0])
        pty.append(tab[i][1])
    return ptx,pty
    
xTrue,yTrue= generateXY(resT)
xFalse,yFalse= generateXY(resF)
plt.plot(xTrue,yTrue,'.g')
plt.plot(xFalse,yFalse,'.r')

xx = linspace(0,2*pi,200)
#plt.plot(cos(xx), sin(xx),'-k',linewidth=2)

plt.xlim([-1.5,1.5])
plt.ylim([-1.5,1.5])

plt.axis("equal")
plt.show()