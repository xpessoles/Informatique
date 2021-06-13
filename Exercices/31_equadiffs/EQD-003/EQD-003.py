from math import pi, sin
from numpy import array
from scipy.integrate import odeint
import matplotlib.pyplot as plt

R = 1E-2 # m, rayin maximum du bouchon de révolution
H = 4.5*1E-2 # m, Hauteur du bouchon
N = 1000 # nb de trapèzes
rho_eau = 1000 # kg / m**3 masse volumique de l'eau
rho_b = 240 # kg / m**3, masse volumique du liège
g = 9.81 # m / s**2, accélération de la pesanteur en
Cx=1#Coefficient de trainée aérodynamique

def euler_for(F, tmin, tmax, Z0, n):
    """Solution de Z'=F(Z,t) sur [tmin,tmax], Z(tmin) = Z0,"""
    h=(tmax-tmin)/n
    Z = Z0
    t = tmin
    z_list = [Z0] # la liste des valeurs renvoyées
    t_list = [tmin] # la liste des temps
    for i in range(n):
        # Variant : floor((tmax-t)/h)
        # Invariant : au tour k, z_list = [Z_0,...,Z_k], t_list = [t_0,...,t_k]
        Z = Z + h * F(Z, t)
        z_list.append(Z)
        t = t + h
        t_list.append(t)
    return t_list, z_list

def euler(F, tmin, tmax, Z0, h):
    """Solution de Z'=F(Z,t) sur [tmin,tmax], Z(tmin) = Z0,"""
    Z = Z0
    t = tmin
    z_list = [Z0] # la liste des valeurs renvoyées
    t_list = [tmin] # la liste des temps
    while t+h <= tmax : 
        # Variant : floor((tmax-t)/h)
        # Invariant : au tour k, z_list = [Z_0,...,Z_k], t_list = [t_0,...,t_k]
        Z = Z + h * F(Z, t)
        z_list.append(Z)
        t = t + h
        t_list.append(t)
    return t_list, z_list

def T(f,a,b,N):
    """Approximation de l'intégrale de a à b de f 
    Méthode des trapèzes, N trapèzes"""
    S = 0.5*(f(a) + f(b))
    h = (b-a)/N
    for k in range(1,N) : 
        S = S + f(a + k*h)
    return S*h

def r(z):
    """Rayon du bouchon à la hauteur z"""
    return R*(1+0.1*sin(pi*z/H))

def r2(z):
    """Carré du rayon du bouchon à la hauteur z"""
    return r(z)**2

def volume_immerge(z):
    """Renvoie le volume immergé du bouchon.
    z : profondeur du bas du bouchon"""
    if z <= 0 :
        # bouchon hors de l'eau
        return 0
    elif z <= H :
        # bouchon immergé jusqu'à la hauteur z
        return pi*T(r2,0,z,N)
    else :
        # bouchon totalement immergé
        return pi*T(r2,0,H,N)

V = volume_immerge(H)



def Fv(z,zp):
    """renvoie la force de frottement visqueux"""
    if zp==0 or z<0:
        return 0
    else:
        alpha=-0.5*Cx*rho_eau*zp**2*zp/abs(zp)
        if zp>0 :#Le bouchon descend
            if 0<=z<H/2:
                return alpha*pi*r(z)**2
            else: #if z>=H/2:
                return alpha*pi*r(H/2)**2
        else:#Le bouchon remonte
            if 0<=z<H/2:
                return 0
            elif H/2<=z<=H:
                return alpha*pi*(r(H/2)**2-r(z)**2)
            else:# z>H:
                return alpha*pi*r(H/2)**2
        

def F0(Z,t):
    """Sans frottement visqueux"""
    z,zp = Z
    zpp = - rho_eau*g*volume_immerge(z) / (rho_b*volume_immerge(H)) + g
    return array([zp,zpp])

def F(Z,t):
    """Avec frottement visqueux"""
    z,zp = Z
    zpp = (Fv(z,zp)- rho_eau*g*volume_immerge(z)) / (rho_b*volume_immerge(H)) + g
    return array([zp,zpp])

def trace(z0,zp0,n,b,nom_traj,nom_phase):
    """Trace trajectoire et portrait de phase, euler et odeint"""
    X0 = array([z0,zp0])
    h=b/n
    t_list,X_list = euler(F,0,b,X0,n)
    z_list = [X[0] for X in X_list]
    zp_list = [X[1] for X in X_list]
    odeint_list = odeint(F,X0,t_list)
    zode_list = [X[0] for X in odeint_list]
    zpode_list = [X[1] for X in odeint_list]
    plt.clf()
    plt.plot(t_list,z_list,label="Méthode d'Euler")
    plt.plot(t_list,zode_list,label="Odeint")
    plt.xlabel("Temps en $s$")
    plt.ylabel("Profondeur en $m$")
    plt.title("Trajectoire du bouchon, $z_0="+str(z0)+"$, $z_0'="+str(zp0)+"$, pas $h="+str(h)+"$")
    plt.legend()
    plt.savefig(nom_traj)
    plt.clf()
    plt.plot(z_list,zp_list,label="Méthode d'Euler")
    plt.plot(zode_list,zpode_list,label="Odeint")
    plt.xlabel("Profondeur en $m$")
    plt.ylabel("Vitesse en $ms^{-1}$")
    plt.title("Trajectoire du bouchon, $z_0="+str(z0)+"$, $z_0'="+str(zp0)+"$, pas $h="+str(h)+"$")
    plt.legend()
    plt.savefig(nom_phase)

def trace_euler(z0,zp0,h,tmax,nom_traj,nom_phase):
    """Trace trajectoire et portrait de phase, euler et odeint"""
    X0 = array([z0,zp0])
    t_list,X_list = euler(F,0,tmax,X0,h)
    z_list = [X[0] for X in X_list]
    zp_list = [X[1] for X in X_list]
    plt.clf()
    plt.plot(t_list,z_list,label="Méthode d'Euler")
    plt.xlabel("Temps en $s$")
    plt.ylabel("Profondeur en $m$")
    plt.title("Trajectoire du bouchon, $z_0="+str(z0)+"$, $z_0'="+str(zp0)+"$, pas $h="+str(h)+"$")
    plt.legend()
    plt.savefig(nom_traj)
    plt.clf()
    plt.plot(z_list,zp_list,label="Méthode d'Euler")
    plt.xlabel("Profondeur en $m$")
    plt.ylabel("Vitesse en $ms^{-1}$")
    plt.title("Trajectoire du bouchon, $z_0="+str(z0)+"$, $z_0'="+str(zp0)+"$, pas $h="+str(h)+"$")
    plt.legend()
    plt.savefig(nom_phase)

##if __name__ == '__main__':
##    trace(0,0,20,1,"trajectoire_1.png","phase_1.png")
##    trace(-0.1,0,100,1,"trajectoire_2.png","phase_2.png")
##    trace(-0.1,0,1000,1,"trajectoire_3.png","phase_3.png")
##    trace(-0.1,0,10000,1,"trajectoire_4.png","phase_4.png")

if __name__ == '__main__':
    trace_euler(-.2,0,.015,1,"trajectoire.png","phase.png")



##z0=-0.05
##zp0=0
##n=10000
##Z0 = array([z0,zp0])
##b=1
##h=b/n
##t_list,Z_list = euler(F,0,b,Z0,n)
##z_list = [Z[0] for Z in Z_list]
##zp_list = [Z[1] for Z in Z_list]
##plt.clf()
##plt.plot(t_list,z_list)
##plt.xlabel("Temps en $s$")
##plt.ylabel("Profondeur en $m$")
##plt.title("Trajectoire du bouchon au cours du temps, $z_0="+str(z0)+"$, $z_0'="+str(zp0)+"$, pas $h="+str(h)+"$")
##plt.legend()
##plt.savefig("z_t")
##plt.clf()
##plt.plot(z_list,zp_list)
##plt.xlabel("Profondeur en $m$")
##plt.ylabel("Vitesse en $ms^{-1}$")
##plt.title("Portrait de phase de la trajectoire du bouchon, $z_0="+str(z0)+"$, $z_0'="+str(zp0)+"$, pas $h="+str(h)+"$")
##plt.legend()
##plt.savefig("portrait_de_phase")
