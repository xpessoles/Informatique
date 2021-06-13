from random import randrange, seed

def lire_texte_brut(nom_de_fichier1,nom_de_fichier2):
    """Lit le texte 1 et le transforme en texte 2"""
    with open(nom_de_fichier1,'r') as f :
        texte = f.read()
    texte = texte.replace('.',' point').replace(',', ' virgule').replace(';', 'point virgule').replace('œ','oe').replace("'"," ").replace("-"," ").replace("’"," ")
    accents = {'a' : ['à','â'],
               'e' : ['é','è','ê'],
               'i' : ['î'],
               'u' : ['ù','û'],
               'o' : ['ô']}
    for lettre in accents :
        for acc in accents[lettre] :
            texte = texte.replace(acc,lettre)
    with open(nom_de_fichier2,'w') as f :
        f.write(texte.lower())
    return None

alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
alphabet_dico = {}
for i in range(26):
    alphabet_dico[alphabet_str[i]] = i


def tableau_frequences_fic(nom_de_fichier):
    """Tableau des fréquences d'un texte"""
    with open(nom_de_fichier,'r') as f :
        texte = f.read().split()
    L = [0]*26
    for mot in texte :
        for lettre in mot :
            L[alphabet_dico[lettre]] += 1
    return L

def tableau_frequences(texte):
    """Tableau des fréquences d'un texte"""
    t = texte.split()
    L = [0]*26
    nb = 0
    for mot in t :
        for lettre in mot :
            L[alphabet_dico[lettre]] += 1
            nb += 1
    for i in range(26) :
        L[i] = L[i] / nb
    return L

def codage_texte(texte,clef):
    """Code un texte par décalage"""
    code = {}
    t = list(texte)
    for lettre in alphabet_dico :
        code[lettre] = alphabet_str[(alphabet_dico[lettre] + clef) % 26]
    for i in range(len(t)):
        if t[i] in code :
            t[i] = code[t[i]]
    return ''.join(t)

def transforme(n):
    """Ajoute un 0 devant les nombres entre 1 et 10"""
    if n<10 :
        return '0'+str(n)
    else :
        return str(n)

def tous_les_codages(nom_de_fichier1,nom_de_fichier2):
    """Calcule tous les codages possibles"""
    with open(nom_de_fichier1,'r') as f :
        texte = f.read()
    for clef in range(26):
        texte_code = codage_texte(texte,clef)
        with open(nom_de_fichier2+'_{}'.format(transforme(clef))+'.txt','w') as f :
            f.write(texte_code)
    return None

def ecrit_alpha(nom_de_fichier,graine=1):
    """Écris tous les textes"""
    with open(nom_de_fichier,'r') as f :   
        texte = f.read()
    seed(graine)
    clef = 1
    for alpha in range(1,100):
        # print('Clef = {}'.format(clef))
        texte_code = codage_texte(texte,clef)
        with open('texte_{}.txt'.format(transforme(alpha)),'w') as f :
            f.write(texte_code)
        clef = (clef + randrange(2,4)) % 26
        if clef == 0 or clef == 1 or clef == 2:
            clef = randrange(3,5)
    return None

def distance(t1,t2):
    """Distance entre deux tableaux de fréquences t1 et t2"""
    S = 0
    for i in range(len(t1)):
        S = S + (t1[i]-t2[i])**2
    return S

def decodage(nom_de_fichier,fichier_frequences = "frequences.txt"):
    """Calcule la meilleure clef de décodage"""
    with open(nom_de_fichier,'r') as f :   
        texte = f.read()
    with open(fichier_frequences,'r') as f :
        frequences = [float(s.strip()) for s in f.readlines()]
    tableau_distances = [0]*26
    for clef in range(26):
        texte_code = codage_texte(texte,clef)
        tf = tableau_frequences(texte_code)
        tableau_distances[clef] = distance(frequences,tf)
    m = min(tableau_distances)
    for clef in range(26) :
        if tableau_distances[clef] == m :
            return clef
    

def teste_texte():
    """Décode chaque texte et affiche son premier mot"""
    premier_mot = []
    for alpha in range(1,100):
        clef = decodage('texte_{}.txt'.format(transforme(alpha)))
        with open('texte_{}.txt'.format(transforme(alpha)),'r') as f :   
            texte = f.read()
        texte_decode = codage_texte(texte,clef).split()
        premier_mot.append(texte_decode[0])    
    return premier_mot

if __name__ == '__main__':
    lire_texte_brut('texte_brut.txt','texte.txt')
    ecrit_alpha('texte.txt')
    # tous_les_codages('texte.txt','texte_code')
