import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

# Fonction de transfert sous la forme num(p)/den(p)
# Coefficients au numerateur
# du plus grand ordre au plus petit, exemple : 1*p^0
num = [1]
# Coefficients au denominateur
# du plus grand ordre au plus petit, exemple : 1*p^2 + 0.1*p^1 + 1*p^0
# den = [1, 0.1, 1]
 
plt.subplot(2, 1, 1)
for i in range(5):
    den = [1,0.1+i/5,1]
    #definition de la fonction de transfert
    s1 = signal.lti(num, den) 
    # Specification de la plage de pulsations :
    # 0.1 a 10 non inclus par pas de 0.02
    # w, gain, phase : listes de nombres (pulsations, gains, phases)
    w, gain, phase = signal.bode(s1, np.arange(0.1, 10, 0.02))
    # Trace du graphe en semilog
    plt.semilogx (w, gain, color="blue", linewidth="1")
plt.xlabel ("Pulsation $\omega$")
plt.ylabel (r"Gain $G_{dB}(\omega)=20 \times \log_{10}(|H(j\omega)|)$",size=16)
plt.xscale('log')
plt.grid(True,which="both")

 
plt.subplot(2, 1, 2)
for i in range(5):
    den = [1,0.1+i/5,1]
    s1 = signal.lti(num, den)
    w, gain, phase = signal.bode(s1, np.arange(0.1, 10, 0.02))
    plt.semilogx (w, phase, color="red", linewidth="1.1")
plt.xlabel ("Pulsation $\omega$")
plt.ylabel (r"Phase $\phi(\omega)=arg(H(j\omega))$",size=16)
plt.xscale('log')
plt.grid(True,which="both")

plt.show()

