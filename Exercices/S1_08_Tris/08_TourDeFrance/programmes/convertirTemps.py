def convertirTemps(temps:str):
    '''temps est un str de la forme "06h 09' 39''" '''
    t_course=temps.split('h') #on peut aussi couper a h
    heure=int(t_course[0])
    t_course2=t_course[1].split("'")
    duree=int(t_course2[1])+60*int(t_course2[0])+3600*heure
    return duree