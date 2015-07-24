# -*- coding: utf-8 -*-
"""
@author: Xavier Pessoles
http://matplotlib.org/examples/showcase/integral_demo.html
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def func(x):
    return np.sqrt(1-x*x)



x = np.linspace(0, 1)
y = func(x)

fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)
plt.ylim(ymin=0)

# Make the shaded region
a, b = 0, 1 # integral limits
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0)] +[(a,func(a))] + [(b,func(b))] + [(b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)



#plt.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
#        horizontalalignment='center', fontsize=14)

plt.plot(0,func(0),marker='o',color='b')
"""plt.plot(0.2,func(0.2),marker='o',color='b')
plt.plot(0.4,func(0.4),marker='o',color='b')
plt.plot(0.6,func(0.6),marker='o',color='b')
plt.plot(0.8,func(0.8),marker='o',color='b')"""
plt.plot(1,func(1.0),marker='o',color='b')

#plt.figtext(0.9, 0.05, '$x$')
#plt.figtext(0.1, 0.9, '$y$')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((0, 0.2, 0.4, .6, .8, 1))
#ax.set_xticklabels(('$x_0$', '$x_1$', '$x_2$', '$x_3$', '$x_4$', '$x_5$'))

ax.set_yticks((0, 0.2, 0.4, .6, .8, 1))
#ax.set_yticklabels(('','','','','','','','',''))
plt.axis('equal')
plt.grid(True)

plt.show()

def trap(n):
    I = 0
    for  i in range(n):
        a=i/n
        b=a+1/n
        I = I + (b-a)*0.5*(func(b)+func(a))
    print(4*I)
    return I
