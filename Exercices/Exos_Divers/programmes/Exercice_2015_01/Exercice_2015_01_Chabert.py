import numpy as np
import matplotlib.pyplot as plt

# Précision sur l'énoncé : tracé dans le plan complexe des points de module
# k/12 et d'argument k*pi/6, k entre 0 et 12 

les_z = [ ((k/12)*np.exp((k*np.pi/6)*1j)) for k in range(0,13) ]
print(les_z)

les_abs = [ z.real for z in les_z ]
les_ord = [ z.imag for z in les_z ]

plt.plot(les_abs,les_ord, label = ' les points ' )

plt.xlabel( 'partie réelle' )
plt.ylabel( 'partie imaginaire' )

plt.legend()
plt.show()
