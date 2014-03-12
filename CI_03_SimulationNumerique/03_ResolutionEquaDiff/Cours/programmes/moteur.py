# -*- coding: utf-8 -*-
"""
@author: Xavier Pessoles
"""

import numpy as np
import matplotlib.pyplot as plt
from math import exp


ti=0
tf=2
pas=0.15


def omega_n(ti,tf,pas,omega_0,tau):
    """
    omega_n premiere approche
    """
    res=[]
    temps=[ti]
    res=[omega_0]
    for i in range(1,int((tf-ti)/pas)):
        res.append(pas*528/tau+res[i-1]*(1-pas/tau))
        temps.append(ti+i*pas)
    return temps,res


def omega_n_euler_explicite_recurrence(ti,tf,pas,omega_0,omega_c,tau):
    """
    omega_n euler explicite par recurrence
    """
    res=[]
    temps=[ti]
    res=[omega_0]
    for i in range(1,int((tf-ti)/pas)):
        omega=res[i-1]*(1-pas/tau)+omega_c*pas/tau
        print(omega)
        res.append(omega)
        temps.append(ti+i*pas)
    return temps,res

def omega_n_euler_explicite_terme_general(ti,tf,pas,omega_0):
    """
    omega_n euler explicite par utilisation d'un terme général
    """
    res=[]
    temps=[ti]
    res=[omega_0]
    for i in range(1,int((tf-ti)/pas)):
        res.append(omega_0*((1-pas/0.2)**i)+528*(1-((1-pas/0.2)**i)))
        temps.append(ti+i*pas)
    return temps,res

        
def omega_t(ti,tf,pas,tau):
    """
    Expression théorique de omega demarrage
    """
    pas=pas/100
    res=[]
    temps=[ti]
    res=[0]
    for i in range(1,int((tf-ti)/pas)):
        res.append(528*(1-exp(-i*pas/tau)))
        temps.append(ti+i*pas)
    return temps,res
    
    
def omega_t_arret(ti,tf,pas):
    """
    Expression théorique de omega arret
    """
    pas=pas/100
    res=[]
    temps=[ti]
    res=[528]
    for i in range(1,int((tf-ti)/pas)):
        res.append(528*(exp(-i*pas/0.2)))
        temps.append(ti+i*pas)
    return temps,res

def figure_premiere_approche():
    omega_0=0
    temps,omegan=omega_n(ti,tf,pas,omega_0)
    temps2,omegat=omega_t(ti,tf,pas)
    plt.plot(temps,omegan,linewidth=3,marker='v')
    plt.plot(temps2,omegat,linewidth=3)
    plt.grid(True, which="both", linestyle="dotted")
    plt.legend(["Solution approchée","Solution exacte"],loc='lower right', fancybox=True, shadow=True, prop=dict(size=10))
    #plt.xlabel("Temps en $s$")
    #plt.ylabel("Position en $m$")
    #plt.axis([0,xf,-1.2,1.2])
    plt.show()

def figure_moteur_seul():
    pas = 0.1
    temps2,omegat=omega_t(ti,tf,pas)
    #temps2,omegat=omega_t_arret(ti,tf,pas)
    plt.plot(temps2,omegat,linewidth=3)
    plt.grid(True, which="both", linestyle="dotted")
    plt.xlabel("Temps en $s$")
    plt.ylabel("Vitesse angulaire en $rad/s$")
    plt.title("Démarrage du moteur")
    #plt.title("Arrêt du moteur")
    #plt.axis([0,xf,-1.2,1.2])
    plt.show()
    
    
def figure_euler_explicite():
    pas = 0.1
    #omega_0 = 0
    omega0 = 528
    omegac=0
    temps,omegan=omega_n_euler_explicite_recurrence(ti,tf,pas,omega0,omegac)
    #temps2,omegat=omega_t(ti,tf,pas)
    temps2,omegat=omega_t_arret(ti,tf,pas)
    #temps3,omegann = omega_n_euler_explicite_terme_general(ti,tf,pas,omega0)
    plt.plot(temps,omegan,linewidth=3,marker='v')
    plt.plot(temps2,omegat,linewidth=3)
    #plt.plot(temps3,omegann,linewidth=3)
    plt.grid(True, which="both", linestyle="dotted")
    plt.legend(["Euler explicite","Solution exacte"],loc='lower right', fancybox=True, shadow=True, prop=dict(size=10))
    plt.xlabel("Temps en $s$")
    plt.ylabel("Vitesse angulaire en $rad/s$")
    #plt.title("Démarrage du moteur")
    plt.title("Arrêt du moteur")
    #plt.axis([0,xf,-1.2,1.2])
    plt.show()


def figure_euler_explicite_pas():
    temps2,omegat=omega_t(ti,tf,0.1)
    plt.plot(temps2,omegat,linewidth=3)
    
    omega0 = 0
    omegac = 528
    pas=0.25
    temps,omegan=omega_n_euler_explicite_recurrence(ti,tf,pas,omega0,omegac)
    plt.plot(temps,omegan,linewidth=1,marker='v')
    
    pas=0.1
    temps,omegan=omega_n_euler_explicite_recurrence(ti,tf,pas,omega0,omegac)
    plt.plot(temps,omegan,linewidth=1,marker='x')
    
    pas=0.05
    temps,omegan=omega_n_euler_explicite_recurrence(ti,tf,pas,omega0,omegac)
    plt.plot(temps,omegan,linewidth=1,marker='.')
    
    plt.grid(True, which="both", linestyle="dotted")
    plt.legend(["Solution exacte",
    "Euler explicite -- Pas 0,25 s.",
    "Euler explicite -- Pas 0,1 s.",
    "Euler explicite -- Pas 0,05 s.",
    ],loc='lower right', fancybox=True, shadow=True, prop=dict(size=10))
    plt.xlabel("Temps en $s$")
    plt.ylabel("Vitesse angulaire en $rad/s$")
    #plt.title("Démarrage du moteur")
    plt.title("Arrêt du moteur")
    #plt.axis([0,xf,-1.2,1.2])
    plt.show()
    
def figure_euler_explicite_pas_tau():
    omega0 = 0
    omegac = 528
    pas = 0.1
    tau=pas/1.5
    temps2,omegat=omega_t(ti,tf,0.1,tau)
    plt.plot(temps2,omegat,'b-',linewidth=3)
    
    temps,omegan=omega_n_euler_explicite_recurrence(ti,tf,pas,omega0,omegac,tau)
    plt.plot(temps,omegan,'bv-')
    
    tau=pas/0.5
    temps2,omegat=omega_t(ti,tf,0.1,tau)
    plt.plot(temps2,omegat,'g-',linewidth=3)
    
    temps,omegan=omega_n_euler_explicite_recurrence(ti,tf,pas,omega0,omegac,tau)
    plt.plot(temps,omegan,'gs-')
    
     
    tau=pas/0.1
    temps2,omegat=omega_t(ti,tf,0.1,tau)
    plt.plot(temps2,omegat,'r-',linewidth=3)
    
    temps,omegan=omega_n_euler_explicite_recurrence(ti,tf,pas,omega0,omegac,tau)
    plt.plot(temps,omegan,'r*-')
    
    
    plt.grid(True, which="both", linestyle="dotted")
    plt.legend(["Solution exacte",
    "Euler explicite - $h/\\tau=0.07$",
    "Solution exacte",
    "Euler explicite - $h/\\tau=0.2$",
    "Solution exacte",
    "Euler explicite - $h/\\tau=1$",
    ],loc='lower right', fancybox=True, shadow=True, prop=dict(size=10))
    plt.xlabel("Temps en $s$")
    plt.ylabel("Vitesse angulaire en $rad/s$")
    #plt.title("Démarrage du moteur")
    plt.title("Arrêt du moteur")
    #plt.axis([0,xf,-1.2,1.2])
    plt.show()
    
# figure_premiere_approche()
# figure_moteur_seul()
#figure_euler_explicite()
#figure_euler_explicite_pas()
figure_euler_explicite_pas_tau()