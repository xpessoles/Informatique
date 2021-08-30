# alias make='gmake --warn-undefined-variables --no-builtin-rules'

.PHONY: clean

LATEXMK	= latexmk

GOAL 	= main_mp-option-info
HELPER_FILES	= $(wildcard *.tex [Mm]akefile)

$(GOAL).pdf: $(HELPER_FILES) ../technique.tex
	$(LATEXMK) -pdflua -silent $(GOAL)

clean: 
	$(LATEXMK) -pdflua -C
