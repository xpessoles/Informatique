# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:53:52 2014

@author: Alain
"""
import matplotlib.pyplot as plt
import numpy as np

### Euler explicite
def euler(f,x0,h,N):
    y = np.zeros(N)
    y[0] = x0
    for i in range(len(y)-1):
        
        y[i+1] = f(y[i],h*i) * h + y[i]
    return y

def f1(y,t):
    return -y

    
#########Euler explicite - courbes
#t=linspace(0,10,1000)
#plot(t,exp(-t))
#leg=['solution exacte']
#hh = [2.1,2,1.5,1,0.8,0.5,.1]
#for h in hh:
#    T = 10
#    leg+=[str(h)]
#    t=arange(0,T,h)
#    print(t)
#    
#    
#    y=euler(f1,1,h,len(t))
#    plot(t,y,'-+')
#
#
#legend(leg,loc=4)
#xlabel('temps (s)')


########Euler explicite - performance
#import time
#t=linspace(0,2,1000)
#leg=['solution exacte']
#hh = [.1,1e-2,1e-3,1e-4,1e-5,1e-6]
#erreur=[]
#temps=[]
#for h in hh:
#    T = 10
#    t=arange(0,T,h)
#    yex = exp(-t)
#    tic = time.time()
#    y=euler(f1,1,h,len(t))
#    temps += [time.time()-tic]    
#    erreur += [max(abs((y-yex))/yex)]
#    print(erreur)
#    print(temps)


########Euler implicite
import scipy.optimize as opt
def euler_implicite(f,x0,h,N):
    y = zeros(N)
    y[0] = x0
    for i in range(len(y)-1):
        y[i+1] = opt.newton(g,1,args=(h*(i+1),y[i],f))
    return y


def g(x,t,xp,f):
    return x - f(x,t) * h - xp
#
#########Euler implicite - courbes
#t=linspace(0,10,1000)
#plot(t,exp(-t))
#leg=['solution exacte']
#hh = [2.1,2,1.5,1,0.8,0.5,.1]
#for h in hh:
#    T = 10
#    leg+=[str(h)]
#    t=arange(0,T,h)
#    print(t)
#    
#    
#    y=euler_implicite(f1,1,h,len(t))
#    plot(t,y,'-+')
#
#
#legend(leg,loc=0)
#xlabel('temps (s)')

########Euler implicite - performance
#import time
#t=linspace(0,10,1000)
#leg=['solution exacte']
#hh = [.1,1e-2,1e-3,1e-4,1e-5,1e-6]
#erreur=[]
#temps=[]
#for h in hh:
#    T = 10
#    t=arange(0,T,h)
#    yex = exp(-t)
#    tic = time.time()
#    y=euler_implicite(f1,1,h,len(t))
#    temps += [time.time()-tic]    
#    erreur += [max(abs((y-yex))/yex)]
#    print(erreur)
#    print(temps)
#
#
##### Méthode de Heun
def heun(f,x0,h,N):
    y = zeros(N)
    y[0] = x0
    for i in range(len(y)-1):
        k1 = f(y[i],h*i)
        k2 = f(y[i]+h*k1,i*h+h)
        y[i+1] = y[i] + h/2*k1 + h/2*k2
    return y

##### Méthode de Heun - courbes
#t=linspace(0,10,1000)
#plot(t,exp(-t))
#leg=['solution exacte']
#hh = [1.5,1,0.8,0.5,.1]
#for h in hh:
#    T = 10
#    leg+=[str(h)]
#    t=arange(0,T,h)
#    print(t)
#    
#    
#    y=heun(f1,1,h,len(t))
#    plot(t,y,'-+')
#
#
#legend(leg,loc=0)
#xlabel('temps (s)')
#
#
#########Méthode de Heun - performance
#import time
#t=linspace(0,10,1000)
#leg=['solution exacte']
#hh = [.1,1e-2,1e-3,1e-4,1e-5,1e-6]
#erreur=[]
#temps=[]
#for h in hh:
#    T = 10
#    t=arange(0,T,h)
#    yex = exp(-t)
#    tic = time.time()
#    y=heun(f1,1,h,len(t))
#    temps += [time.time()-tic]    
#    erreur += [max(abs((y-yex))/yex)]
#    print(erreur)
#    print(temps)



##### Méthode de RK4
def rk4(f,x0,h,N):
    if str(type(x0))== "<class 'numpy.ndarray'>":
        y = zeros((N,len(x0)))
        y[0,:] = x0
        for i in range(len(y)-1):
            k1 = f(y[i,:],h*i)
            k2 = f(y[i,:]+h/2*k1,i*h+h/2)
            k3 = f(y[i,:]+h/2*k2,i*h+h/2)
            k4 = f(y[i,:]+h*k3,i*h+h)
            y[i+1,:] = y[i,:] + h/6*(k1+2*k2+2*k3+k4)
        return y
    else:
        y = zeros(N)
        y[0] = x0
        for i in range(len(y)-1):
            k1 = f(y[i],h*i)
            k2 = f(y[i]+h/2*k1,i*h+h/2)
            k3 = f(y[i]+h/2*k2,i*h+h/2)
            k4 = f(y[i]+h*k3,i*h+h)
            y[i+1] = y[i] + h/6*(k1+2*k2+2*k3+k4)
        return y

##### Méthode de RK4 - courbes
#t=linspace(0,10,1000)
#plot(t,exp(-t))
#leg=['solution exacte']
#hh = [1.5,1,0.8,0.5,.1]
#for h in hh:
#    T = 10
#    leg+=[str(h)]
#    t=arange(0,T,h)
#    print(t)
#    
#    
#    y=rk4(f1,1,h,len(t))
#    plot(t,y,'-+')
#
#
#legend(leg,loc=0)
#xlabel('temps (s)')
#
#########Méthode de RK4 - performance
#import time
#t=linspace(0,10,1000)
#leg=['solution exacte']
#hh = [.1,1e-2,1e-3,1e-4]
#erreur=[]
#temps=[]
#for h in hh:
#    T = 10
#    t=arange(0,T,h)
#    yex = exp(-t)
#    tic = time.time()
#    y=rk4(f1,1,h,len(t))
#    temps += [time.time()-tic]    
#    erreur += [max(abs((y-yex))/yex)]
#    print(erreur)
#    print(temps)

#


##### fonction pour y" + omega² y = 0
def f2(y,t):
    return array([y[1],-w0**2*y[0]])
##### fonction pour y" + 2*xiomega*y' + omega² y = 0
def f3(y,t):
    return array([y[1],-w0**2*y[0]-2*xi*w0*y[1]])
##### fonction pour y" + 2*xiomega*y' + omega² y = w0**2*e0 sin(w t)
def f4(y,t):
    return array([y[1],-w0**2*y[0]-2*xi*w0*y[1]+w0**2*e0*sin(w*t)])

##### pb de chimie
def f5(y,t):
    x1=y[0]
    x2=y[1]
    return array([k1*(c-x1-x2)*(cc-x1),k2*(c-x1-x2)*(x1-x2)])

#w0 = 2*pi/2
#xi = 0.015
#w  = 2*pi/5
#e0 = 0.2
#
#h=0.01
#t = arange(0,120,h)
#y = rk4(f4,array([1,0]),h,len(t))
#plot(t,y[:,0])


#c=1
#cc=1
#k1=0.9
#k2=5*k1
#
#h=0.01
#t = arange(0,10,h)
#y = rk4(f5,array([0,0]),h,len(t))
#plot(t,y[:,1])
#plot(t,y[:,0]-y[:,1])
#legend(['x2','x1-x2')





####### y'-y=0 
def f6(y,t):
    return y/2+t


plt.close('all')

fig1=plt.figure(1)
T = 2.
h=.5
t=np.linspace(0,T,T/h+1)

amp = 3
x,y = meshgrid(linspace(0,2.,9),linspace(1,6,15))
yv = f6(y,x) / sqrt(1+f6(y,x)**2) * amp
xv =    1    / sqrt(1+f6(y,x)**2) * amp
quiver(x,y,xv,yv,headwidth=0,units='width',angles='xy',width=0.002)
quiver(x,y,-xv,-yv,headwidth=0,units='width',angles='xy',width=0.002)

y1 = euler(f6,1,h,len(t))
plt.plot(t,y1,'-+',linewidth=2)
t = np.linspace(0,T,1000)

plt.plot(t,euler(f6,1,t[1]-t[0],len(t)),linewidth=2)
#plt.plot(t,5*np.exp(t/2)-4-2*t,linewidth=2)

fig2=figure(2)
T = 2.
h=.5
t=np.linspace(0,T,T/h+1)

amp = 3
x,y = meshgrid(linspace(0,2.,9),linspace(1,8,15))
yv = f6(y,x) / sqrt(1+f6(y,x)**2) * amp
xv =    1    / sqrt(1+f6(y,x)**2) * amp
quiver(x,y,xv,yv,headwidth=0,units='width',angles='xy',width=0.002)
quiver(x,y,-xv,-yv,headwidth=0,units='width',angles='xy',width=0.002)

y1 = euler_implicite(f6,1,h,len(t))
plt.plot(t,y1,'-+',linewidth=2)
t = np.linspace(0,T,1000)

plt.plot(t,euler(f6,1,t[1]-t[0],len(t)),linewidth=2)




#T=1
#h=.3
#t=arange(0,T,h)
#y2 = euler_implicite(f6,1,h,len(t))
#plot(t,y2,'-+')
#t = linspace(0,T,1000)
#plot(t,exp(t))
#
#
#fig3=figure(3)
#T=6
#h=1.9
#t=arange(0,T,h)
#y3 = rk4(f6,1,h,len(t))
#plot(t,y3,'-+')
#t = linspace(0,T,1000)
#plot(t,exp(t))



#legend(['euleur expl','euler impl','rk4','sol exacte'])





#
#from scipy.integrate import odeint
#yt=odeint(f1,1,t)
#
#
#yex = exp(-t)
#
#erreur = max(abs(y-yex))
#
#plot(t,y)
#plot(t,yt)
#t=linspace(0,N*h,1000)
#plot(t,exp(-t))


#def f2(y,t):
#    return -t*y
#
#h = 2
#N = 100
#t=arange(0,N*h,h)
#
#
#y=euler(f2,1,h,len(t))
#yt=odeint(f2,1,t)
#yex = exp(-t**2/2)
#erreur = max(abs(y-yex))
#
#plot(t,y)
#plot(t,yt)
#t=linspace(0,N*h,1000)
#plot(t,exp(-t**2/2))
