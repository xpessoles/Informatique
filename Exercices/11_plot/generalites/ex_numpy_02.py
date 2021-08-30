import matplotlib.pyplot as plt
from numpy import linspace

x = linspace(0,1,101)
y = [t**3 for t in x]

plt.clf()
plt.plot(x,y)
plt.xlabel('$t$')
plt.ylabel('$t^3$')
plt.savefig('ex_numpy_02.png')
