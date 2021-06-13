#utf8
# header = "\\documentclass[francais,a4paper,div=19,12 pt]{scrartcl}\n\\usepackage{enumitem}\n\\input{tp.tex}\n\\begin{document}\n\\pagestyle{empty}\n\\newcommand{\\rep}{\\fbox{\\phantom{\\raisebox{0pt}[.5cm][.3cm]{}\\makebox[9.5cm]{}}}}\n"
header = "\\documentclass[francais,a4paper,div=19,12 pt]{scrartcl}\n\\usepackage{enumitem}\n\\begin{document}\n\\pagestyle{empty}\n\\newcommand{\\rep}{\\fbox{\\phantom{\\raisebox{0pt}[.5cm][.3cm]{}\\makebox[9.5cm]{}}}}\n"
footer = "\\end{document}"

fichedeb = "\\begin{center}\n \\textbf{Informatique tronc commun, Devoir 03}\\\\\n \\textbf{Fiche réponse}\n\\end{center}\n\n\\medskip{}\n Nom  et prénom : \\hfill \n\n\\bigskip{}\n\n\\centerline{\\fbox{\\huge{$\\mathbf{\\alpha="
fichefin = "}$}}}\n\\medskip{}\n"
question = "\\rep{}\n"

r = ["R1 ", "R2 :", "R3 :", "R4 :", "R5 :", "R6 :", "R7 :", "R8 :", "R9 :", "R10 :", "R11 :", "R12 :"]

reponses = "\\begin{center}\n\\begin{tabular}{rc}\n"
for x in r:
    reponses += (x + " & \\rep \\\\[1 em] \n")
reponses += "\\end{tabular}\n\\end{center}"

def fiches():
    with open("fiches.tex","w",encoding='utf8') as f:
        f.write(header)
        for alpha in range(1,100):
            f.write(fichedeb)
            f.write(str(alpha))
            f.write(fichefin)
            f.write(reponses)
            f.write('\\newpage\n')
        f.write(footer)
    return None


if __name__ == '__main__':
    fiches()
