import matplotlib.pyplot as plt
import matplotlib . image as img # import de la bibliotheque image
import numpy as np

##Question 1 : création d'une image noire
def image_noire(n,p):
    '''construit la matrice n*p d'une image noire'''
    img =[0]*n    #construit une liste contenant A COMPLETER
    for i in range(n): # n sera le nombre de colonne/ de lignes A COMPLETER
        img[i]=[0]*p #construit une liste contenant A COMPLETER et l'affecte à A COMPLETER
    return img   #img sera une image noire de hauteur : ??? pixels et de largeur ??? pixels  (A COMPLETER EN INDIQUANT LE NB DE PIXELS)

imN_3_6=image_noire(3,6)


##Question 2 : affichage
print (imN_3_6)
plt.figure("Image noire")
plt.imshow(imN_3_6,cmap='gray',vmin=0, vmax=1)

##Question 3 : création d'images en noir et blanc rayées
def rayure_hor(n,p):
    '''construit la matrice n*p d'une image rayée horizontalement'''
    img =[0]*n
    for i in range(0,n,2):
        img[i]=[0]*p
    for i in range(1,n,2):
        img[i]=[1]*p
    return(img)


def rayure_ver(n,p):
    '''construit la matrice n*p d'une image rayée horizontalement'''
    img =[0]*n
    for i in range(n):
        im=[]
        for j in range(n):
            im.append(j%2)
        img[i]=im
    return(img)

imRH=rayure_hor(9,14)
imRV=rayure_ver(9,14)
plt.figure("Image rayée horizontale")
plt.imshow(imRH,cmap='gray',vmin=0, vmax=1)
plt.figure("Image rayée verticale")
plt.imshow(imRV,cmap='gray',vmin=0, vmax=1)
plt.show()

##Question3bis (optionnelle) : création d'un échiquier

def echiquier(n,p):
    '''crée un motif échiquier sur une image de taille n par p'''
    im=image_noire(n,p)
    for i in range(n) :
        for j in range(p):
            if (i%2 and not(j%2)) or not(i%2) and j%2:
                im[i][j]=1
    return(im)


imE=echiquier(8,15)
plt.figure("Equiquier")
plt.imshow(imE,cmap='gray',vmin=0, vmax=1)

##Question 4 : modifier une image pour l'éclaircir
def eclaircir(im,k):
    '''modifie l'image im en augmentant de k la valeur de chaque pixel, attention l'image im est modifiée sur place'''
    n=len(im)
    p=len(im[0])
    for i in range(n):
        for j in range(p):
            gris=im[i][j]+k
            if gris>1:
                gris=1
            im[i][j]=gris
    return(im)

#im2=eclaircir(imRH,0.5)
#plt.figure("Image rayée horizontale éclaircie")
#plt.imshow(im2,cmap='gray',vmin=0, vmax=1)
#plt.figure("Image rayée horizontale initiale")
#plt.imshow(imRH,cmap='gray',vmin=0, vmax=1)

##Question 5 : modifier une image pour l'éclaircir en faisant une copie indépendante
def eclaircir2(im0,k):
    '''modifie l'image im0 en augmentant de k la valeur de chaque pixel, une copie indépendante est réalisée'''
    n=len(im0)
    im=[]
    for i in range(n):
         im.append(list(im0[i]))

    p=len(im[0])
    for i in range(n):
        for j in range(p):
            gris=im[i][j]+k
            if gris>1:
                gris=1
            im[i][j]=gris
    return(im)

im2=eclaircir2(imRH,0.5)
plt.figure("Image rayée horizontale éclaircie")
plt.imshow(im2,cmap='gray',vmin=0, vmax=1)
plt.figure("Image rayée horizontale initiale")
plt.imshow(imRH,cmap='gray',vmin=0, vmax=1)

##Question 6 : lecture d'un fichier image et appel de la fonction éclaircir

imF=img.imread("allium.png")
imFF=eclaircir2(imF,0.2)
plt.figure("Image lue")
plt.imshow(imF,cmap='gray',vmin=0, vmax=1)

plt.figure("Image lue éclaircie")
plt.imshow(imFF,cmap='gray',vmin=0, vmax=1)

##Question 7 : lecture et affichage de l'image ciel
imC=img.imread("ciel.png")
plt.figure("Ciel")
plt.imshow(imC,cmap='gray',vmin=0, vmax=1)


##Question 8 : détection de contour d'une image

def contour (im, seuil):
    """im : image en niveau de gris
    renvoie une image en niveau de gris"""
    nb_lig ,nb_col = im. shape
    im2 =np. zeros (( nb_lig ,nb_col))
    for i in range (1, nb_lig -1):
        for j in range (1, nb_col -1):
            p1= im [i-1,j]
            p2= im [i,j-1]
            p3= im [i+1,j]
            p4= im [i,j+1]
            norme =np.sqrt ((p1-p3 )**2+( p2-p4 )**2)
            if norme > seuil :
                im2 [i,j]=1
    return im2

##Question 9 : test
im_contour=contour(imC,0.2)
plt.figure("Ciel : contour")
plt.imshow(im_contour,cmap='gray')



plt.show()