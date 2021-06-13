with open('sainte_lyon.csv','r',encoding='utf8') as f:
    _ = f.readline() # on ignore la première ligne
    d = f.readlines() # les données intéressantes
    resultat=''
    for ligne in d:
        ligne=ligne.strip()
        ligne=ligne.split(';')
        nom=ligne[2]
        chrono=ligne[-3]
        heure,minute,seconde=chrono.split(':')
        duree=3600*int(heure)+60*int(minute)+int(seconde)
        vitesse=72/(duree/3600)
        resultat=resultat+nom+';'+str(vitesse)+'\n'
        
with open('sainte_lyon2.csv','w',encoding='utf8') as f:
    f.write(resultat)