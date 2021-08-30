TEX=algorithmique.tex bd.tex calculabilite.tex intro.tex langage_c.tex langage_ocaml.tex langage.tex logique.tex programmation.tex recursivite.tex structuresdonnees.tex systeme.tex


LATEXMK_AVAILABLE := $(shell which latexmk)

main_mpi.pdf: $(TEX) main_mpi.tex ../technique.tex
ifdef LATEXMK_AVAILABLE
	latexmk -cd -pdflua -recorder- -silent -bibtex-cond -synctex=0 -interaction=batchmode -halt-on-error -file-line-error -e '$$hash_calc_ignore_pattern{"luc"}="^";' main_mpi.tex
else
	lualatex main_mpi.tex
endif

	
clean: 
	latexmk -pdflua -C
