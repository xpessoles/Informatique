#question 26
def consigne(distance,distance_verin):
    ecart=distance-distance_verin #écart en cm
    if ecart>1:
        res=rapide
    else : 
        res=lente
    return res


#question 27
def setup():
  
    pinMode(2,OUTPUT)
    pinMode(4,INPUT)
    digitalWrite(2,LOW)
    
#question 28
de impulsion(S):
    digitalWrite(S,HIGH)
    time.sleep(2e-5)
    digitalWrite(S,LOW)

#question 29
def calcul_distance(E):
    # détection du front montant de E avec mémorisation de la date d'apparition
    while (digitalRead(E) == 0) :
        pulse_start = time.time()
    # détection du front descendant de E avec mémorisation de la date d'apparition
    while (digitalRead(E)  == 1):
        pulse_end = time.time()
    # calcul de tc
    pulse_duration = pulse_end - pulse_start
    # calcul de la distance  (en cm) à partir de tc
    distance = pulse_duration * 17150
    # retour du résultat, la distance
    return (distance)
    
#Il faut prendre E=4, la sortie du capteur, l'entrée de l'arduino

#question 30
def mesure():
    #envoie d'une impulsion 
    impulsion(2)
    mes=calcul_distance(4)
    return mes 
#mes est un nombre flottant (type float)  tout comme distance dans la fonction cacul_distance

#question 31
"""
Clefs primaires : élément souligné du schéma relationnel
-attribut Mesure pour la table Sismique
-attribut Id_LB pour la table LargeBande
-attribut Id_CB pour la table Courte bande
"""
#question 32
"""
SELECT Date FROM CourteBande ORDER BY MCBx;
Date par ordre croissant des MCBx
18.02.2019_09H52
15.02.2019_04H02
16.02.2019_15H15
16.02.2019_22H47
"""

#question 33
SELECT MCBz FROM CourteBande WHERE MCBz > 0.2 ORDER by Date ASC;

#question 34
Select MLBx, MLBy, MLBz FROM Sismique JOIN LargeBande ON Mesure=Id_LB WHERE Température > -30;



