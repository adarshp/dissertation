all:
	latexrun --latex-cmd='lualatex' --latex-args='--enable-write18 \
	  -shell-escape' --bibtex-cmd='biber' -W no-overfull dissertation.tex 
clean:
	./latexrun --clean-all
