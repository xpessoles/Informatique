##===============
while y2>0:         #ZONEA
    t=t+h
    ##=====
    ##Euler
                #Debut Zone B
    y2n=y2-h*(a+b*exp(-y2/Vref))*g
    y1n=y1+h*y2
                
                
                #Fin Zone B
    ##=====
    y1=y1n
    y2=y2n
##===============
#Debut de la zone C
DA=y1
Vf=y2
tf=t