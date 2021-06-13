import matplotlib.pyplot as plt
import numpy as np

## Q1

def g(x) :
    """ renvoie la valeur de g(x) """
    return(1)
    
def f(x) :
    """ renvoie la valeur de f(x) """
    
    if x>= 0 and x<1 :
        return(g(x))
    elif x>1 :
        return(x*f(x-1))
    
def H(x) :
    """ prolongement de f(x) à ]-1,0] """
    if x >= 0 :
        return(f(x))
    elif x > -1 :
        return(f(-x))
    
## Q3

les_x = np.arange(-0.99,4.01,0.01)
les_y = []

for x in les_x :
 les_y.append(H(x))

plt.plot(les_x,les_y, 'b',label = 'H(x)')

## Q4

#On approxime la dérivée avec Euler :
# yi' = (yi+1-yi)/dx


def derivation(les_x,les_y) :
    """ dérive une fonction f, sous la forme de deux listes avec euler """
    return([ (les_y[i+1]-les_y[i])/(les_x[i+1]-les_x[i]) for i in range(len(les_x) -1) ])

les_yp = derivation(les_x,les_y)

plt.plot(les_x[:len(les_x)-1],les_yp,'r', label = "f'(x)")

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.figure()

## Q5 
#Même chose avec g = cos(x)
def g2(x) :
    """ renvoie la valeur de g(x) """
    return(np.cos(x))

def f2(x) :
    """ renvoie la valeur de f(x) """
    
    if x>= 0 and x<1 :
        return(g2(x))
    elif x>1 :
        return(x*f2(x-1))
    
def H2(x) :
    """ prolongement de f(x) à ]-1,0] """
    if x >= 0 :
        return(f2(x))
    elif x > -1 :
        return(f2(-x))

les_x2 = np.arange(-0.99,4.01,0.01)
les_y2 = []

for x in les_x2 :
 les_y2.append(H2(x))

plt.plot(les_x2,les_y2, 'b',label = 'H2(x)')
les_yp2 = derivation(les_x2,les_y2)

plt.plot(les_x2[:len(les_x2)-1],les_yp2,'r', label = "f'2(x)")

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()




