#Importation des modules
import matplotlib.pyplot as plt


def dessiner(n,s):
    if n==0:
        tracer_segment()
    else:
        dessiner(n-1)
        tourner()    
    return
    
def tracer_segment():
    
    