# -*- coding: utf-8 -*-
"""
@author: Xavier Pessoles
http://matplotlib.org/examples/showcase/integral_demo.html
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def func(x):
    return (x - 3) * (x - 5) * (x - 7) + 200



x = np.linspace(-1, 11)
y = func(x)

fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)
plt.ylim(ymin=0)

# Make the shaded region
a, b = 0, 2 # integral limits
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0)] +[(a,func(a))] + [(b,func(b))] + [(b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

a, b = 2, 4 # integral limits
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0)] +[(a,func(a))] + [(b,func(b))] + [(b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

a, b = 4, 6 # integral limits
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0)] +[(a,func(a))] + [(b,func(b))] + [(b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

a, b = 6, 8 # integral limits
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0)] +[(a,func(a))] + [(b,func(b))] + [(b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)


a, b = 8,10 # integral limits
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0)] +[(a,func(a))] + [(b,func(b))] + [(b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)


#plt.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
#        horizontalalignment='center', fontsize=14)

plt.plot(0,func(0),marker='o',color='b')
plt.plot(2,func(2),marker='o',color='b')
plt.plot(4,func(4),marker='o',color='b')
plt.plot(6,func(6),marker='o',color='b')
plt.plot(8,func(8),marker='o',color='b')
plt.plot(10,func(10),marker='o',color='b')

plt.figtext(0.9, 0.05, '$x$')
plt.figtext(0.1, 0.9, '$y$')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((0, 2, 4, 6, 8, 10))
ax.set_xticklabels(('$x_0$', '$x_1$', '$x_2$', '$x_3$', '$x_4$', '$x_5$'))

ax.set_yticks((0,50,100,150,200,250,300,350,400))
ax.set_yticklabels(('','','','','','','','',''))
plt.grid(True)
plt.show()
