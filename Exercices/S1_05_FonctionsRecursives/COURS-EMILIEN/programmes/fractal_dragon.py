#importation des modules
import turtle as t



#Deckaration des fonctions
def dessiner_dragon(n,s,L):
    if n==1:
        tracer_segment(L)
    else:
        dessiner_dragon(n-1,1,L)
        tourner_plume(s)
        dessiner_dragon(n-1,-1,L)
        
def tourner_plume(s):
    if s==1:
        t.left(90)
    if s==-1:
        t.right(90)
        
def tracer_segment(L):
    t.forward(L)
#Programme principal
k=6
L=320/(1.414)**(k-1)
t.up()

t.down()
dessiner_dragon(k,1,L)

