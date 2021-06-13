## Q1 - Configurations

#yi dans [|0,xi|], donc pour chaque yi il y a xi + 1 valeurs possibles
#Soit pour le nombre de configuration : Produit(xi + 1); 1<= i <= m :
# Avec 4 fruits dans 6 vases : 15625 configurations
#Grand nb de config => Intérêt de l'informatique

## Q2- G(10,5,2,4)

#10 : 1010
#5:   0101
#2:   0010
#4:   0100
#__________________
#     1001 = 9

#G(10,5,2,4) = 9


## Q3 - taille 

def taille(x):
    """ renvoie la taille du codage binaire minimal pour x"""
    n = 0
    
    while (2**n) -1 < x :
        n+=1
    
    return(n)
    
#print(taille(128))
#8

# Complexité : p tq 2^(p-1)< x <= 2^p
# p ~= log2(x); p correspond au nombre de tour de boucle => O(log(x)) : logarithmique

## Q4 - binaire

def binaire(x,n):
    """ Convertit x en binaire sur n bits """
    a,q = [],0
    
    for i in range(n):
        q = x%2
        x //=2
        a = [q] + a
    
    return(a)
    
#print(binaire(128,8))
#[1, 0, 0, 0, 0, 0, 0, 0]

#Complexité O(n), ie  O(log(x)) : Linéaire / n; Logarithmique/x 
#

## Q5 - decimal

def decimal(a):
    """ renvoie l'expression décimale de a binaire """
    
    s = 0
    for i in range(len(a)):
        s+= a[i]*(2**(len(a)-1-i))
    
    return(int(s))
    
#print(decimal([1,0,1,0,1,0,1,0]))
#170

# n = len(a) : Complexité en O(n)

## Q6 - Grundy

def Grundy(x):
    """ renvoie la valeur de la fonction de grundy pour la liste x = (x1,...,xm) """
    # n taille bianire max des xi; m longeur de x
    
    # Calcul de la longueur binaire utilisée
    # Complexité en O(m)
    
    n = 0
    
    for val in x :
        t = taille(val)
        if n < t :
            n = t
    
    
    
    # Ecriture de la liste x en binaire
    # Complexité en O(m*n) car binaire(x,n) en O(n)
    
    b = [binaire(val,n) for val in x ]
    
    # Calcul de la somme binaire mod 2 :
    # Complexité en O(m*n) : m valeur dans b; n tours de boucle
    
    a = []
    
    for i in range(n):
        
        s = 0
        
        for val in b :
            s+= val[i]
            
        a.append(s%2)
    
    return(decimal(a))

#print(Grundy([10,5,2,4]))
#9

#Complexité de la fonction en O(m*n)


## Q7 - Jouer_coup

def jouer_coup(x,i,z):
    """ modifie la configuration x en enlevant z fruits dans le i-ème vase """
    
    y = x [:]
    y[i-1] = x[i-1] - z
    
    return(y)
    

## Q8 - x dans Y0 => x suivant dans Y1

# Soit x une config (x1,...,xm), et G(x) = 0
# Soit j le vase dans lequel on enlève des fruits
# Soit i le i-ème bit de l'écriture binaire de xj, qui se trouve modifié (il en existe au moins un, à cause de l'écriture binaire)
# Comme avant la modif a[i] = 0, on obtient donc a[i] = 1
# Donc a != 0 en décimal
# Donc la config suivant x est telle que G(x) != 0; ie x suivant dans Y1

## Q9 - x dans Y1 il existe un coup pour que x suivant soit dans Y0

# Soit x une config (x1,...,xm), et G(x) != 0
# Soit j le vase dont l'écriture biniare porte un bit de poids fort dans a
# On modifie x de telle sorte que a = 0 en binaire ( le x ainsi trouvé sera forcément inférieur puisqu'on modifie le bit de poirds fort)
# On a donc alors le x suivant tel que G(x) = 0, ie x suivant dans Y0

## Q10 - Conclusion et stratégie

# x, x' deux config consécutives
# x dans Y1 <=> x' dans Y0
# donc G(x) != 0 <=> G(x') = 0
# G nulle toujours pour le même joueur
# Or G(x) = 0 correspond en particulier au cas ou x = (0,...,0), ie le joueur à perdu
# D'ou l'équivalence demandée

# Stratégie :
# x dans Y0 : perdu
# x dans Y1 : modifier la config de telle sorte que G = 0

## Q11 -  Stratégie 

def stratégie(x):
    """ Définit une stratégie à jouer pour le joueur avec la configuration x """
    
    a = Grundy(x)
    
    if a!= 0 :
        n = taille(a)
        b = binaire(a,n)
        
        i = 0
        while i<n and taille(x[i]) < n:
            i +=1
        
        y = binaire(x[i],n)
        
        z = y[:]
        
        for j in range(len(y)) :
            
            if b[j] == 1 :
                z[j] = 1 - z[j]
            
        return((i+1,decimal(y)-decimal(z)))
    
#print(stratégie([0,1,0,0]))
#print(stratégie([0,1,1,0]))
#(2, 1)
#None