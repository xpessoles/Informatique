#! /bin/sh

warn () { echo "$@" >&2; }
die () { echo "FATAL: $@" >&2; echo WD=$(pwd) >&2; exit 255; }

teste_dir () {
  d="$1"
  echo "$d"
  cd "$d" > /dev/null || die "cd $d : échec"
  rm -f prog.py test_TP.py || die "effacement de prog.py et test_TP.py: échec"
  test -f *.py || die "Un et un seul fichier .py attendu ici"
  cp *.py prog.py || die "pas réussi à créer prog.py"
  test -f prog.py.orig || cp prog.py prog.py.orig
  cp ../test_TP.py test_TP.py
  cp ../../tops tops
  echo 'RESULTAT DES TESTS' > testeur1.log
  echo '' >> testeur1.log
  pytest >> testeur1.log || true
  scode >> testeur1.log
  cat prog.py.orig | bash topdf $(basename "$d") > prog.py.orig.pdf echo ''
  cat testeur1.log | bash topdf $(basename "$d") > testeur1.pdf
  pdftk testeur1.pdf prog.py.orig.pdf cat output testeur2.pdf
  cat testeur2.pdf | bash mypdf make_even > testeur.pdf
}

scode () {
  if ! cmp -s prog.py.orig prog.py
  then
    echo ''
    echo "MODIFICATIONS EFFECTUEES SUR LE FICHIER RENDU"
    echo  =============================================
    echo ''
    diff -u prog.py.orig prog.py;
  fi
}

main () {
rm -f resultat.log
for d in */
do
  (teste_dir "$d") \
  && (echo "$d" >> resultat.log; cat "$d"/testeur1.log >> resultat.log)
done
pdftk */testeur.pdf output resultat.pdf
}

main
