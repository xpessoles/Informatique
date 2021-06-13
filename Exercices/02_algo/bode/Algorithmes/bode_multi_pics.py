import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

# Fonction de transfert sous la forme den(p)/num(p)
# Coefficients au numerateur
# du plus grand ordre au plus petit, exemple : 1*p^0
num = [1]
# Coefficients au denominateur
# du plus grand ordre au plus petit, exemple : 1*p^2 + 0.1*p^1 + 1*p^0
# den = [1, 0.1, 1]
 
#plt.subplot(2, 1, 1)
for i in range(1):
    den1 = [3,0.05+i/5,1]
    den2 = [0.3,0.002+i/5,1]
    #definition de la fonction de transfert
    s1 = signal.lti(num, den1)
    s2 = signal.lti(num, den2) 
    # Specification de la plage de pulsations :
    # 0.1 a 100 non inclus par pas de 0.02
    # w, gain, phase : listes de nombres (pulsations, gains, phases)
    w, gain1, phase1 = signal.bode(s1, np.arange(0.1, 10, 0.02))
    w, gain2, phase2 = signal.bode(s2, np.arange(0.1, 10, 0.02))
    gain=[gain1[i]+gain2[i] for i in range(len(gain1))]
    # Trace du graphe en semilog
    plt.semilogx (w, gain, color="blue", linewidth="1")
#plt.xlabel ("Pulsation $\omega$",size=16)
plt.ylabel (r"Gain $G_{dB}(\omega)$",size=16)
plt.xscale('log')
plt.grid(True,which="both")

"""
plt.subplot(2, 1, 2)
for i in range(1):
    den1 = [3,0.05+i/5,1]
    den2 = [0.3,0.002+i/5,1]
    s1 = signal.lti(num, den1)
    s2 = signal.lti(num, den2)
    w, gain1, phase1 = signal.bode(s1, np.arange(0.1, 10, 0.02))
    w, gain2, phase2 = signal.bode(s2, np.arange(0.1, 10, 0.02))
    phase=[phase1[i]+phase2[i] for i in range(len(gain1))]
    plt.semilogx (w, phase, color="red", linewidth="1.1")
plt.xlabel ("Pulsation $\omega$")
plt.ylabel (r"Phase $\phi(\omega)$")
plt.xscale('log')
plt.grid(True,which="both")
"""
plt.show()
"""
f=open("bode.txt","w")
f.write("pulsation"+";"+"gain"+";"+"phase"+"\n")
for i in range(len(w)):
    f.write(str(w[i])+";"+str(gain[i])+";"+str(phase[i])+"\n")
f.close()

def picResonance(w,gain,phase):
    n=len(w)
    gr=gain[0]
    L=[]
    i=1
    while i<n:
        if gain[i-1]<=gain[i]:
            i+=1
            while i<n and gain[i-1]<=gain[i]:
                i+=1
            if i<n:
                L.append((w[i-1],gain[i-1],phase[i-1]))
        i+=1 
    return L

print(picResonance(w,gain,phase))
"""
