all:
	./latexrun --latex-cmd='lualatex' --latex-args='--enable-write18 \
	  -shell-escape' --bibtex-cmd='biber' -W no-overfull dissertation.tex 
	# cd latex.out; make -f dissertation.makefile
clean:
	./latexrun --clean-all
