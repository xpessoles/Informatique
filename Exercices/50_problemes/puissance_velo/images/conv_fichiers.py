import os
import sh

fichier_note='Notes_DS5_mpsi_2017_2018.pdf'
fichier_bilan='DS5_bilan.pdf'

for k in range(16):
    if k<10:
        num='0'+str(k)
    else:
        num=str(k)
    os.system('/usr/local/bin/pdftk A='+fichier_bilan+' B='+fichier_note+' C=blank.pdf cat A1 B'+str(k*2+1)+'-'+str(2*k+2)+' C1 output pdf/bilan_DS5_'+num+'.pdf')
    
os.system('/usr/local/bin/pdftk pdf/bilan_DS5_*.pdf cat output bilan_DS5_.pdf')


        
        


