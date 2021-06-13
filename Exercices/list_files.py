import os

ld = os.listdir()

tmp = []
# On supprime les fichiers .py
for dir in ld :
    if ".py" in dir:
        tmp.append(dir)

print(ld,tmp)
for dir in tmp :
    ld.remove(dir)
    ld.remove("consignes")
    ld.remove("Exos_Divers")
    

for dir in ld :
    liste_exos = os.listdir(dir)
    file = dir+".tex"
    fid = open(file,"w")
    
    fid.write("\\renewcommand{\\repExo}{../../Informatique/Exercices/"+dir+"} \n \n")

    for exo in liste_exos :
        if not "cor" in exo :
            ex = exo[:-4]
            fid.write("\\renewcommand{\\td}{"+ex+"}\n")
            fid.write("\\graphicspath{{\\repStyle/png/}{\\repExo/\\td/}}\n")
            fid.write("\\input{\\repExo/\\td.tex} \n \n")
    fid.close()
            
        
    