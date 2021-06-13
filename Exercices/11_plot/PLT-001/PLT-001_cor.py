import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,6*np.pi,100)
y1=np.sin(x)
y2=np.exp(-0.1*x)
y3=y1*y2

plt.clf()
plt.plot(x,y1,'b--',label='$\\sin(x)$ en bleu',linewidth=2)
plt.plot(x,y2,'r-.',label='$\\exp(-0,1\cdot x)$ en rouge',linewidth=2)
plt.plot(x,-y2,'g-.',label='$-\\exp(-0,1\cdot x)$ en vert',linewidth=2)
plt.plot(x,y3,'k-',label='$\\sin(x)\\cdot \\exp(-0,1\\cdot x)$ en noir',linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=0)
plt.title('Fonction pseudo-périodique')
plt.savefig('pseudo_harmonique.png')
