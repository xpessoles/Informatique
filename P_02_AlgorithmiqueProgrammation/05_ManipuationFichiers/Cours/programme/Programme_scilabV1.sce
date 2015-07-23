

// ouverture d'un fichier et lecture ligne à ligne

fic=mopen("Mesure_axe_Emericc.txt","r");

ligne=mgetl(fic,1)
// Découpage à la tabulation = caractère ascii 9
noms_grandeurs=strsplit(ligne,ascii(9))
noms_grandeurs=noms_grandeurs(2:3)

for i=1:10
    ligne = mgetl(fic,1);
end

ligne = mgetl(fic,1)
ligne_nbpoints=strsplit(ligne,ascii(9))
nb_points=int(ligne_nbpoints(2))
nb_points=msscanf(ligne_nbpoints(2),"%i")


numero=[];position=[];consigne=[];
for i=1:nb_points
    ligne = mgetl(fic,1);
    ligne = strsubst(ligne,",",".");
    [n,numero(i),position(i),consigne(i)]=msscanf(ligne,"%d\t%f\t%f");
end

mclose(fic);                    //close the file

plot(position)

// lecture de données formatées


fic=mopen("Mesure_axe_Emericc_formate.txt","r");

T=mfscanf(-1,fic,'%d\t%f\t%f')  

plot(T(:,1),[T(:,2),T(:,3)/10])

mclose(fic); //close the file

// Ecriture de données formatées ou non...


fic=mopen("monFichier.txt","w");

mfprintf(fic,"Voici mon fichier de point\n")
mfprintf(fic,"Nombre de points : %d\n",100)

x=-20:40/99:20;
y=sin(x)./x;

mfprintf(fic,'%d\t%f\t%f\n',[1:100]',x',y')  

mclose(fic); //close the file


