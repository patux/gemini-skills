CMD_SEP = "========================================"
CMD_DONE = "Done."
CLEAN_CMD = rm -f *.aux *.log *.out *.ilg *.idx *.ent *.toc *.ind *.epub cover-*.pdf cover-*.png temp_epub.tex

all: full epub

full: 
	@echo "FULL BUILD"
	@echo
	@echo $(CMD_SEP)
	@echo "Building the_prince-machiavelli-en (1st time)..."
	pdflatex -jobname=the_prince-machiavelli-en main-en.tex
	@echo $(CMD_DONE)
	@echo $(CMD_SEP)
	@echo
	@echo $(CMD_SEP)
	@echo "Building the_prince-machiavelli-en (2nd time)..."
	pdflatex -jobname=the_prince-machiavelli-en main-en.tex
	@echo $(CMD_DONE)
	@echo $(CMD_SEP)
	@echo
	@echo $(CMD_SEP)
	@echo "Rebuilding the_prince-machiavelli-en (3rd time)..."
	pdflatex -jobname=the_prince-machiavelli-en main-en.tex
	@echo $(CMD_DONE)
	@echo $(CMD_SEP)
	@echo
	@echo $(CMD_SEP)
	@echo "Rebuilding the_prince-machiavelli-en (last time)..."
	pdflatex -jobname=the_prince-machiavelli-en main-en.tex
	@echo $(CMD_DONE)
	@echo $(CMD_SEP)
	@echo

epub:
	@echo "EPUB BUILD"
	@echo
	@echo $(CMD_SEP)
	@echo "Building the_prince-machiavelli-en.epub..."
	@cat info-en.tex > temp_epub.tex
	@echo "" >> temp_epub.tex
	@cat dedication.tex >> temp_epub.tex
	@echo "" >> temp_epub.tex
	@perl -ne 'BEGIN{ %r=(1=>"I",2=>"II",3=>"III",4=>"IV",5=>"V",6=>"VI",7=>"VII",8=>"VIII",9=>"IX",10=>"X",11=>"XI",12=>"XII",13=>"XIII",14=>"XIV",15=>"XV",16=>"XVI",17=>"XVII",18=>"XVIII",19=>"XIX",20=>"XX",21=>"XXI",22=>"XXII",23=>"XXIII",24=>"XXIV",25=>"XXV",26=>"XXVI"); $$i=1} s/\\chapter\[(.*?)\]\{\}/"\\chapter{Chapter $$r{$$i}: $$1}" . ($$i++ ? "" : "")/e; s/\\subtitle\{.*?\}//g; print' chapters-en.tex >> temp_epub.tex
	@pandoc temp_epub.tex -o the_prince-machiavelli-en.epub \
		--toc --toc-depth=1 \
		--metadata title="The Prince" \
		--metadata author="Niccolò Machiavelli" \
		--metadata lang="en"
	@rm temp_epub.tex
	@echo $(CMD_DONE)
	@echo $(CMD_SEP)
	@echo

clean:
	@echo $(CMD_SEP)
	@echo "Cleaning '.' folder..."
	@-$(CLEAN_CMD)
	@echo $(CMD_DONE)
	@echo $(CMD_SEP)
	@echo
