### dictionnaire compter les lettres d'un texte

texte="""il est parvenu à la maturité de l’enfance, il a vécu de la vie d’un enfant, il n’a point acheté sa perfection aux dépens de son bonheur ; au contraire, ils ont concouru l’un à l’autre. en acquérant toute la raison de son âge, il a été heureux et libre autant que sa constitution lui permettait de l’être. si la fatale faux vient moissonner en lui la fleur de nos espérances, nous n’aurons point à pleurer à la fois sa vie et sa mort, nous n’aigrirons point nos douleurs du souvenir de celles que nous lui aurons causées ; nous nous dirons : au moins il a joui de son enfance ; nous ne lui avons rien fait perdre de ce que la nature lui avait donné. le grand inconvénient de cette première éducation est qu’elle n’est sensible qu’aux hommes clairvoyants et, que, dans un enfant élevé avec tant de soin, des yeux vulgaires ne voient qu’un polisson. un précepteur songe a son interêt plus qu’à celui de son disciple ; il s’attache à prouver qu’il ne perd pas son temps, et qu’il gagne bien l’argent qu’on lui donne ; il le pourvoit d’un acquis de facile étalage et qu’on puisse montrer quand on veut ; il n’importe que ce qu’il lui apprend soit utile, pourvu qu’il se voie aisé-ment. il accumule, sans choix, sans discernement, cent fatras dans sa mémoire. quand il s’agit d’examiner l’enfant, on lui fait déployer sa marchandise ; il l’étale, on est content ; puis il replie son ballot, et s’en va. mon élève n’est pas si riche, il n’a point de ballot à déployer, il n’a rien à montrer que lui-même. or un enfant, non plus qu’un homme, ne se voit pas en un moment. où sont les observateurs qui sachent saisir au premier coup d’oeil les traits qui le caractérisent ? il en est, mais il en est peu ; et sur cent mille pères, il ne s’en trouvera pas un de ce nombre."""


def compterLettre(texte:str):
    dictionnaire={}
    for lettre in texte:
        if lettre in 'azertyuiopqsdfghjklmwxcvbn':
            if lettre in dictionnaire.keys():
                dictionnaire[lettre]+=1
            else:
                dictionnaire[lettre]=1
    return dictionnaire


### tests
# >>> compterLettre(texte)
res = {'i': 105, 'l': 84, 'e': 175, 's': 102, 't': 93, 'p': 39, 'a': 102, 'r': 75, 'v': 24, 'n': 139, 'u': 99, 'm': 30, 'd': 40, 'f': 15, 'c': 40, 'o': 87, 'h': 10, 'x': 7, 'b': 8, 'q': 23, 'g': 10, 'j': 1, 'y': 4}

# >>> res=compterLettre(texte)
#
# >>> len(res)
# 23

def sommeLettre(fleur:dict):
    s=0
    for element in fleur.values():
        s=s+element
    return s


 ### tests
# >>> sommeLettre(compterLettre(texte))
# 1312
# >>> sommeLettre(res)
# 1312

def frequenceLettre(truc:dict):
    D={}
    total=sommeLettre(truc)
    for cle,valeur in truc.items():
        D[cle]=valeur*100/total
    return D

# >>> frequenceLettre(res)
# {'i': 8.003048780487806, 'l': 6.402439024390244, 'e': 13.338414634146341, 's': 7.774390243902439, 't': 7.088414634146342, 'p': 2.972560975609756, 'a': 7.774390243902439, 'r': 5.716463414634147, 'v': 1.829268292682927, 'n': 10.59451219512195, 'u': 7.545731707317073, 'm': 2.2865853658536586, 'd': 3.048780487804878, 'f': 1.1432926829268293, 'c': 3.048780487804878, 'o': 6.6310975609756095, 'h': 0.7621951219512195, 'x': 0.5335365853658537, 'b': 0.6097560975609756, 'q': 1.7530487804878048, 'g': 0.7621951219512195, 'j': 0.07621951219512195, 'y': 0.3048780487804878}





