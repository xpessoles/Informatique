import matplotlib.pyplot as plt
import matplotlib . image as img # import de la bibliotheque image
import numpy as np

##PARTIE 1 Accentuation d’une composante de couleur

#Question 1

imV=img.imread("vague.png")
plt.figure("Vague")
plt.imshow(imV)

#Question 2
def accentuation(im,k):
    '''accentue la composante rouge d'une valeur k'''
    nb_lig,nb_col,nb_coul=im.shape
    im2=np.zeros((nb_lig,nb_col,nb_coul))
    for i in range(nb_lig):
        for j in range(nb_col):
            R=im[i,j,0]
            if R+k>1 :
                im2[i,j,0]=1
            else:
                im2[i,j,0]=R+k
            im2[i,j,1]=im[i,j,1] #Recopie de G
            im2[i,j,2]=im[i,j,2]
    return(im2)


imV_rouge=accentuation(imV,0.2)
plt.figure("Vague rougie")
plt.imshow(imV_rouge)

##PARTIE 2 Conversion d'une image couleur en niveau de gris
#Question 3
def niveau_gris(matB):
    '''convertit une image rgb en niveau de gris en faisant une moyenne des composantes'''
    nb_lig,nb_col,nb_coul=matB.shape
    matC=np.zeros((nb_lig,nb_col))
    for i in range(nb_lig):
        for j in range(nb_col):
            sum=0
            for k in range(nb_coul):
                sum+=matB[i,j,k]
            moy=sum/nb_coul
            matC[i,j]=moy
    return matC

imV_NG=niveau_gris(imV)
plt.figure("Vague grise _ moyenne")
plt.imshow(imV_NG,cmap='gray',vmin=0, vmax =1)

#Question 4
def niveau_gris2(matB):
    '''convertit une image rgb en niveau de gris en utilisant la norme 709'''
    nb_lig,nb_col,nb_coul=matB.shape
    matC=np.zeros((nb_lig,nb_col,nb_coul))
    for i in range(nb_lig):
        for j in range(nb_col):
            sum=0
            for k in range(nb_coul):
                sum+=int(matB[i,j,k])
            moy=sum//nb_coul
            for k in range(nb_coul):
                matC[i,j,k]=moy
    return matC




imV_NG2=niveau_gris(imV)
plt.figure("Vague grise _ norme 709")
plt.imshow(imV_NG2,cmap='gray',vmin=0, vmax =1)



##PARTIE 3 Flou

#Question 5
imG=img.imread("groupe.png")
plt.figure("Groupe : image initiale")
plt.imshow(imG)

#Question 6
def flou3(im):
    """realise un flou avec une matrice 3*3"""
    b=3//2 #pixels à enlever pour la bordure
    nb_lig ,nb_col,comp = im. shape
    im2 =np. zeros (( nb_lig ,nb_col,comp))
    for i in range (b,nb_lig-b):
        for j in range (b, nb_col-b):
            for c in range(comp):
                im2[i,j,c]=(im[i-1,j,c]+im[i-1,j-1,c]+im[i-1,j+1,c]+im[i,j,c]+im[i,j-1,c]+im[i,j+1,c]+im[i+1,j,c]+im[i+1,j-1,c]+im[i+1,j+1,c])/9

    return(im2)

#Question 7
imG_F1=flou3(imG)
plt.figure("Groupe : flou avec matrice 3x3")
plt.imshow(imG_F1)

#Question 8
def flou(im,n):
    """realise un flou avec une matrice n*n"""
    b=n//2 #pixels à enlever pour la bordure
    nb_lig ,nb_col,comp = im. shape
    im2 =np. zeros (( nb_lig ,nb_col,comp))
    for i in range (b,nb_lig-b):
        for j in range (b, nb_col-b):
            for c in range(comp):
                s=0
                for k in range(n):
                    for l in range(n):
                        s=s+im[i+k-n//2,j+l-n//2,c]
                im2[i,j,c]=s/(n*n)
    return(im2)

#Question 9
imG_F2=flou(imG,7)
plt.figure("Groupe : flou avec matrice 7x7")
plt.imshow(imG_F2)

#Question 10
nb_lig ,nb_col,comp = imG. shape
#Création d'une image noire
im_M =np. zeros (( nb_lig ,nb_col,comp))
for i in range(nb_lig):
      for j in range(nb_col):
            im_M[i,j]=[0,0,0,1]
for i in range(80,180):
      for j in range(370,450):
            im_M[i,j]=[1,1,1,1]


plt.figure("Masque seuil")
plt.imshow(im_M)

#Question 11
#mise en place de l'image floutée
im_finale=im_M*imG_F2+(1-im_M)*imG
plt.figure()
plt.imshow(im_finale)



##Pour aller + loin : Imagerie médicale
#
# def moyenne(mat):
#     '''réalise la moyenne de tous les pixels d'une matrice'''
#     nb_lig ,nb_col  = mat . shape
#     s=0
#     n=nb_lig*nb_col
#
#     for i in range ( nb_lig ):
#         for j in range ( nb_col ):
#             s=s+mat[i,j]
#     moy=s/n
#     return(moy)
#
# def ecart_type(mat):
#     '''réalise la moyenne de tous les pixels d'une matrice'''
#     m=moyenne(mat)
#     nb_lig ,nb_col  = mat . shape
#     n=nb_lig*nb_col
#     s=0
#     for i in range ( nb_lig ):
#         for j in range ( nb_col ):
#             s=s+(mat[i,j]-m)**2
#     e_type=(s/n)**(1/2)
#
#     return(e_type)
#
# def carte_texture(im,T):
#     '''realise la carte de texture, voisins considérés dans une image de T*T'''
#     nb_lig ,nb_col = im . shape
#     max=0
#     maxstd=0
#     im2 =np. zeros (( nb_lig ,nb_col ))
#     for i in range (T//2, nb_lig -T//2):
#         for j in range (T//2, nb_col -T//2):
#             extrait=im[i-T//2:i+T//2, j-T//2: j+T//2]
#             moy=moyenne(extrait)
#             if moy>max:
#                 max=moy
#             std=ecart_type(extrait)
#             v= 10*moy-30*std
#             if v<0:
#                 v=0
#             im2[i,j]=v
#     return(im2)
#
# imIRM=img.imread("IRM.png")
# imIRM=niveau_gris(imIRM)
# plt.figure("EX3 : imagerie : image initiale")
# plt.imshow(imIRM,cmap="gray")
#
# im_B=carte_texture(imIRM,11)
# plt.figure("EX3 : après carte texture")
# plt.imshow(im_B,cmap="gray")
#
# im_c=contour(im_B,0.25)
# plt.figure("EX3 : imagerie : contour endocardique")
# plt.imshow(im_c[160:310,100:250],cmap="gray")
plt.show()


