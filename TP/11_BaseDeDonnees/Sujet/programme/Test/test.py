'''script de http://apiolaza.net/code/dynamic-maps-python.html,légèrement modifié'''

from GChartWrapper import *
 
# création d'un graphique Google Chart et renvoi de l'URL
def macharte(data):
    G = Line(data)
    G.size(250,100)
    G.color('76A4FB') 
    G.axes.type('xy')
    G.grid(20.0,25.0,1,0) 
    return G.url
    
f = open('test3.csv')
stations = f.readlines()

import random
 
#création du fichier kml
kmlBody = ('')
for s in stations:
    data = s.split(',')
    # Géneration de données aléatoires
    a = []
    for r in range(60):
        a.append(round(random.gauss(50,10), 1))
    chart = macharte(a)
    kml = (
        '<Placemark>\n'
        '<name>%s</name>\n'
        '<description>\n'
        '<![CDATA[\n'
        '<p>Valeur: %s</p>\n'
        '<p><img src="%s" width="250" height="100" /></p>\n'
        ']]>\n'
        '</description>\n'
        '<Point>\n'
        '<coordinates>%f,%f</coordinates>\n'
        '</Point>\n'
        '</Placemark>\n'
        ) %(data[0], data[3], chart, float(data[1]), float(data[2]))
 
    kmlBody = kmlBody + kml
 
 
#"morceaux" du fichier KML 
kmlHeader = ('<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n'
             '<kml xmlns=\"http://earth.google.com/kml/2.2\">\n'
             '<Document>\n')
 
kmlFooter = ('</Document>\n'
             '</kml>\n')
 
kmlfinal = kmlHeader + kmlBody + kmlFooter
print(kmlfinal)
fid = open('mon.kml','wb')
fid.write(bytes(kmlfinal, 'UTF-8'))
fid.close()

import webbrowser
url="http://maps.google.com/maps?q=http://dl.dropbox.com/u/678636/"+"mon.kml"
import webbrowser
webbrowser.open_new(url)