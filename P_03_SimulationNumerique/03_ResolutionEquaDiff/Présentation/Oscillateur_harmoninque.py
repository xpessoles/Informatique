from scipy import *
from pylab import *
from math import sqrt
from scipy.integrate import odeint 

k = 20
m = 1
om_0 = math.sqrt(k/m)




def solve_euler_explicite(ti,tf,nb):
    h = (tf-ti)/nb
    res_x = [0.1]
    res_v = [0]
    tps = [ti]
    t=ti
    while t<=tf:
        t = t+h
        res_x.append(h*res_v[-1]+res_x[-1])
        res_v.append(-h*om_0*om_0*res_x[-2]+res_v[-1])
        tps.append(t)
    return tps,res_x


def solve_euler_implicite(ti,tf,nb):
    h = (tf-ti)/nb
    res_x = [0.1]
    res_v = [0]
    tps = [ti]
    t=ti
    while t<=tf:
        t = t+h
        res_x.append((h*res_v[-1]+res_x[-1])/(1+h*h*om_0*om_0))
        res_v.append(-h*om_0*om_0*res_x[-1]+res_v[-1]) 
        tps.append(t)
    return tps,res_x
    

nb,ti,tf = 1000,0,20
temps,res_x = solve_euler_implicite(ti,tf,nb)
plot(temps,res_x,label="N=10000,20s")


def deriv(syst, t):
    x = syst[0]                         # Variable1 x
    v = syst[1]                         # Variable2 v
    dxdt = v                            # Equation différentielle 1
    dvdt = -om_0**2*x                 # Equation différentielle 2
    return [dxdt,dvdt]                  # Dérivées des variables

t = linspace(ti,tf,nb)
# Conditions initiales et résolution
x0=0.1
v0=0
syst_CI=array([x0,v0])                  # Tableau des CI
Sols=odeint(deriv,syst_CI,t)            # Résolution numérique des équations différentielles

# Récupération des solutions
x = Sols[:, 0]
v = Sols[:, 1]
plot(t,x,label="Odeint")

legend()
show()

"""
nb,ti,tf = 2000,0,20
temps,res_x = solve_euler_explicite(ti,tf,nb)
plot(temps,res_x,label="N=2000,20s")

nb,ti,tf = 50000,0,20
temps,res_x = solve_euler_explicite(ti,tf,nb)
plot(temps,res_x,label="N=50000,20s")
"""

"""
nb,ti,tf = 1000,0,20
temps,res_x = solve_euler_implicite(ti,tf,nb)
plot(temps,res_x,label="N=1000,20s")

nb,ti,tf = 2000,0,20
temps,res_x = solve_euler_implicite(ti,tf,nb)
plot(temps,res_x,label="N=2000,20s")

nb,ti,tf = 50000,0,20
temps,res_x = solve_euler_implicite(ti,tf,nb)
plot(temps,res_x,label="N=50000,20s")
"""


"""
"""

    
    