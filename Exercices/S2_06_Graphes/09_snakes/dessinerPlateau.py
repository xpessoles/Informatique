import matplotlib.pyplot as plt

def position(case):
    j = (case-1) // 10 # ligne
    i = (case-1) % 10 # placement
    if j % 2 == 1: # j impair
        i = 9 - i # renversement 1 fois sur 2
    return i, j

dSeE = {  1: 38,  4: 14,  9: 31, 17:  7, 21: 42, 28: 84, 51: 67, 54: 34,
         62: 19, 64: 60, 71: 91, 80: 99, 87: 24, 93: 73, 95: 75, 98: 79}

for case in range(1, 101): # pour les cases 1 à 100
    i, j = position(case)
    plt.text(i, j, str(case),
        horizontalalignment='center', verticalalignment='center')

for caseD, caseA in dSeE.items(): # ligne 6
    iD, jD = position(caseD)
    iA, jA = position(caseA)
    if caseA > caseD : # ligne 9
        couleur = 'b'
    else:
        couleur = 'r'
    plt.plot(iA, jA, '^', color=couleur)
    plt.plot(iD, jD, 'o', color=couleur)
    plt.plot([iA, iD], [jA, jD], color=couleur)
plt.axis("equal")
plt.show()