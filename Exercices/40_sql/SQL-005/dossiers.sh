liste=$(ls | grep .py | sed 's/.py//g')

for eleve in $liste

do
mkdir $eleve
cp $eleve.py $eleve/
cp ../mypdf $eleve/mypdf
cp ../tops $eleve/tops
cp ../topdf $eleve/topdf
cp ../export_pdf.py export_pdf.py
cp ../correction_auto.sh correction_auto.sh
cp ../blank.pdf blank.pdf
done

rm -rf ./test_TP || echo 'Pensez à mettre le fichier test_TP.py dans ce dossier' 
