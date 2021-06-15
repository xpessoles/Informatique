import os

ld = os.listdir()

tmp = []
# On supprime les fichiers .py
for dir in ld :
    if (".py" in dir) or (".tex" in dir) :
        print("del dir",dir)
        tmp.append(dir)

print(ld,tmp)
for dir in tmp :
    ld.remove(dir)
ld.remove("consignes")
ld.remove("Exos_Divers")
    

for dir in ld :
    liste_exos = os.listdir(dir)
    liste_exos2 = []
    for exo in liste_exos :
        if ".tex" in exo : 
            liste_exos2.append(exo) 
        
        
    file = dir+".tex"
    fid = open(file,"w")
    
    fid.write("\\renewcommand{\\repExo}{../../Informatique/Exercices/"+dir+"} \n \n")

    for exo in liste_exos2 :
        if not "cor" in exo :
            ex = exo[:-4]
            print(exo,ex)
            fid.write("\\renewcommand{\\td}{"+ex+"}\n")
            fid.write("\\graphicspath{{\\repStyle/png/}{\\repExo/\\td/}}\n")
            fid.write("\\input{\\repExo/\\td.tex} \n \n")
    fid.close()
            
        
    