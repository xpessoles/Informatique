# alias make='gmake --warn-undefined-variables --no-builtin-rules'

.PHONY: clean

LATEXMK	= latexmk

GOAL 	= main_info-tronc-commun
HELPER_FILES	= $(wildcard *.tex [Mm]akefile)

$(GOAL).pdf: $(HELPER_FILES) ../technique.tex
	$(LATEXMK) -pdflua -silent $(GOAL)

clean: 
	$(LATEXMK) -pdflua -C
