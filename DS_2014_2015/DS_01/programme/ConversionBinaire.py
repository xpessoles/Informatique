# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 15:31:08 2014

@author: Xavier
"""

print()

def conversionBinaireZ(nb,nb_bits):
    """
    Conversion d'un nombre entier relatif
     * nb : nombre à convertir appartenant à Z donné dans le système décimal
     * nb_bits : nombre de bits du codage
    """

    # On regarde si on dépasse la capacité de stockage    
    if nb>(2**(nb_bits-1)-1) or nb<-(2**(nb_bits-1)):
        print("Le nombre donné dépasse les capacités de l'espace de stockage.")
    
    else :
        # Si le nombre est positif on le convertit en binaire
        if nb>0:        
            res = conversionBinaireN(nb)
            while(len(res)!=nb_bits):
                res = "0"+res
            return res
        else :
            # On convertit le nombre en binaire
            res_cv = conversionBinaireN(abs(nb))
            # On complete pour avoir un nombre sur 8 bits
            while(len(res_cv)!=nb_bits):
                res_cv = "0"+res_cv
                
            # Inversion des bits
            res_inv = ""
            for i in range(len(res_cv)):
                if res_cv[i]=="0":
                    res_inv=res_inv+"1"
                else :
                    res_inv=res_inv+"0"
            # On ajoute +1
            # Initialisation
            retenue="1"
            res=""
            for i in range(len(res_inv)-1,-1,-1):
                if retenue=="0" and res_inv[i]=="0":
                    retenue=="0"
                    res = "0"+res
                elif retenue=="0" and res_inv[i]=="1":
                    retenue ="0"
                    res = "1"+res
                elif retenue=="1" and res_inv[i]=="0":
                    retenue ="0"
                    res = "1"+res
                elif retenue=="1" and res_inv[i]=="1":
                    retenue ="1"
                    res = "0"+res
            return res_inv
            
            
            
            

def conversionBinaireN(nb):
    """
    Conversion d'un nombre entier de la base 10 vers la base 2.
     * nb : nombre entier
    """
    dividende = nb
    diviseur = 2
    resultat = ""
    quotient = -nb
    
    while quotient != 0 :
        quotient = int(dividende/diviseur)
        reste = dividende - diviseur * quotient        
        dividende = quotient
        resultat = resultat + str(reste)
    
    res=""
    for i in range(len(resultat)-1,-1,-1):
        res=res+resultat[i]
        
    return res
    
    
#print(conversionBinaireN(16))


def decodageBinaireZ(nb):
    print("Cc")
    if nb[0]=="0" :
        #Le nombre est positif : 
        res = 0
        for i in range(1,len(nb)):
            exp=len(nb)-1-i
            res = res+(2**exp)*int(nb[i])
            print(i,exp,res)
    else :
        # On enlève 1
    
        return res

res_cv = "1010"
nb_bits = 8
while(len(res_cv)!=nb_bits):
    res_cv = "0"+res_cv

res_cv = "1010"
res_inv = ""
for i in range(len(res_cv)):
    if res_cv[i]=="0":
        res_inv=res_inv+"1"
    else :
        res_inv=res_inv+"0"
#print(conversionBinaireZ(1,3))
#print(decodageBinaireZ("0111"))
#print(conversionBinaireZ(-3,3))