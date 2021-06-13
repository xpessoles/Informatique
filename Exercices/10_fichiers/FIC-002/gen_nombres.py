"""Génère le fichier nombres.txt du d02m"""

from random import randrange

def gen_nombres(nom_de_fichier,p=5,n=50,a=0,b=50):
    """Génère le fichier demandé, p nombres par lignes, n lignes, nombres dans [a,b["""
    with open(nom_de_fichier,'w') as f :
        for i in range(n):
            for j in range(randrange(p,2*p)):
                x = randrange(a,b)
                f.write(str(x)+' ')
            f.write('\n')
    return None

if __name__ == '__main__':
    gen_nombres('nombres.txt')
