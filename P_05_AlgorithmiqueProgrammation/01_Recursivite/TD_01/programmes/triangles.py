
import matplotlib.pyplot as plt
import numpy as np
    
from numpy import sqrt

def polygon(*args):
    X, Y = [], []
    for arg in args:
        X.append(arg[0])
        Y.append(arg[1])
    plt.fill(X, Y, 'b')

    
def sierpinski(n, a=[0, 0], b=[1, 0], c=[.5, sqrt(3)/2]):
    if n == 1:
        polygon(a, b, c)
    else:
        u = [(b[0]+c[0])/2, (b[1]+c[1])/2]
        v = [(c[0]+a[0])/2, (c[1]+a[1])/2]
        w = [(a[0]+b[0])/2, (a[1]+b[1])/2]
        sierpinski(n-1, a, w, v)
        sierpinski(n-1, w, b, u)
        sierpinski(n-1, v, u, c)
        
sierpinski(7)
plt.axis("equal")
