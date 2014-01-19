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


a, b = 0, 1 # integral limits
x = np.linspace(0, 1)
y = func(x)

fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)
plt.ylim(ymin=0)

# Make the shaded region
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0)] + list(zip(ix, iy)) + [(b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

#plt.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
#         horizontalalignment='center', fontsize=14)

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
