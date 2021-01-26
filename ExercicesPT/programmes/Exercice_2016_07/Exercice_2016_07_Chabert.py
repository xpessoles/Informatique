##Q1

# 400 Zholty : Impossible !
# 400 divisible par 10 => Si on veut faire avec ces billets, il en faudra 5 ou 10
# Si on en prend 5, on sera en dessous et la valeur à combler sera trop petite, 
# Si on en prend 10 on est forcément au desssus (10*52 > 400 )

##Q2

Billets = [52,62,72]

def somme(p) :
    """ p = [a,b,c], renvoie la somme de a billets de 52 etc... """
    return(p[0]*Billets[0] + p[1]*Billets[1] + p[2]*Billets[2])
    
#print(somme([0,0,0]))
#print(somme([4,2,1]))
#0
#404
    
def compte(n) :
    """ Donne les possibilités pour obtenir n avec des triplets de bilets """
    Poss = []
    a,b,c = 0,0,0
    p = [a,b,c]
    
    while somme(p) < n : 
        #On incrémente d'abord sur le a, après avoir testé toutes les combinaisons pour une valeur de a 
        
        while somme(p) < n :
            #Id. pour b et c
            
            while somme(p) < n :
                c += 1
                p = [a,b,c]
                
            if somme(p) == n :
                Poss.append(p)
            
            c = 0
            b += 1
            p = [a,b,c]
            
        b = 0
        a += 1
        p = [a,b,c]
    
    return(Poss)
    
#print(compte(600))
#print(compte(400))
#[[3, 6, 1], [4, 4, 2], [5, 2, 3], [6, 0, 4]]
#[]

##Q3

res = []


for i in range(72, 600) :
    #On cherche les possibilités entre 72z et 600z avec 4z d'écarts
    
    if compte(i) != [] :
        if compte(i-4) != []:
            res.append(i)
            

#print(res)
#[436, 488, 498, 508, 540, 550, 560, 570, 580, 592]

for val in res :
    print(compte(val),compte(val-4))
                
                
# [[7, 0, 1]] [[0, 0, 6]]
# [[8, 0, 1]] [[0, 2, 5], [1, 0, 6]]
# [[7, 1, 1]] [[0, 1, 6]]
# [[6, 2, 1], [7, 0, 2]] [[0, 0, 7]]
# [[9, 0, 1]] [[0, 4, 4], [1, 2, 5], [2, 0, 6]]
# [[8, 1, 1]] [[0, 3, 5], [1, 1, 6]]
# [[7, 2, 1], [8, 0, 2]] [[0, 2, 6], [1, 0, 7]]
# [[6, 3, 1], [7, 1, 2]] [[0, 1, 7]]
# [[5, 4, 1], [6, 2, 2], [7, 0, 3]] [[0, 0, 8]]
# [[10, 0, 1]] [[0, 6, 3], [1, 4, 4], [2, 2, 5], [3, 0, 6]]
#A chaque fois, on à au moins deux billets différents
#Il faudrait eventuellement eliminier les cas incohérent  ou l'enfant récupère des billets qu'il avait déjà
