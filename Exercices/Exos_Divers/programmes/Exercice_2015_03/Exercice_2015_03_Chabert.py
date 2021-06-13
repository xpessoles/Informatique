## Q1

def est_cube(n) :
    """ vérifie qu'un nombre est un cube """
    return(int(n**(1/3))**3 == n )

#print(est_cube(8))
#print(est_cube(27))
#print(est_cube(12))

#True
#True
#False

Lcube = []

for i in range(251):
    if est_cube(i):
        Lcube.append(i)

# print(Lcube)
# [0, 1, 8, 27, 125]

        
## Q2

def S2cube(n) :
    """ vérifie qu'un nombre est la somme de deux cubes """
    
    res = False
    i = 0
    
    while i <= (n-1) and not(res) :
        if est_cube(n-i) and est_cube(i) :
            res = True
        i+=1
        
    return(res)

#print(S2cube(35))
#print(S2cube(30))

#True
#False



# Entier inférieur à 250 somme de 2 cubes :

##L2cube = []
##
##for i in range(251):
##    if S2cube(i):
##        L2cube.append(i)

#print(L2cube)
#[1, 2, 8, 9, 16, 27, 28, 35, 54, 125, 126, 133, 152, 250]


## Q3

def S4cube(n) :
    """ vérifie qu'un nombre est la somme de 4 cubes """
    
    res = False
    i = 0
    
    while i <= (n-1) and not(res) :
        if S2cube(n-i) and S2cube(i) :
            res = True
        i+=1
        
    return(res)

##
##L4cube = []
##
##for i in range(251):
##    if S4cube(i):
##        L4cube.append(i)

#print(L4cube)
#[2, 3, 4, 9, 10, 11, 16, 17, 18, 24, 25, 28, 29, 30, 32, 35, 36, 37, 43, 44, 51, 54, 55, 56, 62, 63, 70, 81, 82, 89, 108, 126, 127, 128, 133, 134, 135, 141, 142, 149, 152, 153, 154, 160, 161, 168, 179, 180, 187, 206, 250]


## Q4

def S8cube(n) :
    """ vérifie qu'un nombre est la somme de 8 cubes """
    
    res = False
    i = 0
    
    while i <= (n-1) and not(res) :
        if S4cube(n-i) and S4cube(i) :
            res = True
        i+=1
        
    return(res)


##L8cube = []
##
##for i in range(251):
##    if S8cube(i):
##        L8cube.append(i)
##    print(i)
##
##print(L8cube)
##
###[4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 18, 19, 20, 21, 22, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98, 99, 100, 102, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 116, 117, 118, 119, 121, 124, 125, 126, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 142, 143, 144, 145, 146, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 195, 196, 197, 198, 200, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 214, 215, 216, 217, 219, 222, 223, 224, 230, 231, 233, 234, 235, 236, 238, 241, 242, 243, 249, 250]
