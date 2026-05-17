CMD_SEP = "========================================"
CMD_DONE = "Done."
CLEAN_CMD = rm -f *.aux *.log *.out *.ilg *.idx *.ent *.toc *.ind cover-*.pdf cover-*.png temp_epub.tex

# Default target
all: en es

# Language Aliases
english: en
spanish: es

# Format Aliases
pdfs: en-pdf es-pdf
epubs: en-epub es-epub

# Granular Targets
english-pdf: en-pdf
english-epub: en-epub
spanish-pdf: es-pdf
spanish-epub: es-epub

en: en-pdf en-epub
es: es-pdf es-epub

# Build Logic
en-pdf:
	@echo "ENGLISH PDF BUILD"
	@echo $(CMD_SEP)
	@echo "Building PDF (multiple passes)..."
	pdflatex -jobname=book-en main-en.tex
	pdflatex -jobname=book-en main-en.tex
	pdflatex -jobname=book-en main-en.tex
	@echo $(CMD_DONE)
	@echo $(CMD_SEP)
	@echo

es-pdf:
	@echo "SPANISH PDF BUILD"
	@echo $(CMD_SEP)
	@echo "Building PDF (multiple passes)..."
	pdflatex -jobname=book-es main-es.tex
	pdflatex -jobname=book-es main-es.tex
	pdflatex -jobname=book-es main-es.tex
	@echo $(CMD_DONE)
	@echo $(CMD_SEP)
	@echo

en-epub:
	@echo "ENGLISH EPUB BUILD"
	@echo $(CMD_SEP)
	@echo "Building EPUB..."
	@cat info-en.tex > temp_epub.tex
	@echo "" >> temp_epub.tex
	@cat dedication-en.tex >> temp_epub.tex
	@echo "" >> temp_epub.tex
	@perl -ne 'BEGIN{ %r=(1=>"I",2=>"II",3=>"III",4=>"IV",5=>"V",6=>"VI",7=>"VII",8=>"VIII",9=>"IX",10=>"X",11=>"XI",12=>"XII",13=>"XIII",14=>"XIV",15=>"XV",16=>"XVI",17=>"XVII",18=>"XVIII",19=>"XIX",20=>"XX",21=>"XXI",22=>"XXII",23=>"XXIII",24=>"XXIV",25=>"XXV",26=>"XXVI"); $$i=1} s/\\chapter\[(.*?)\]\{\}/"\\chapter{Chapter $$r{$$i}: $$1}" . ($$i++ ? "" : "")/e; s/\\subtitle\{.*?\}//g; print' chapters-en.tex >> temp_epub.tex
	@pandoc temp_epub.tex -o book-en.epub \
		--toc --toc-depth=1 \
		--metadata title="Book Title" \
		--metadata author="Author Name" \
		--metadata lang="en"
	@rm temp_epub.tex
	@echo $(CMD_DONE)
	@echo $(CMD_SEP)
	@echo

es-epub:
	@echo "SPANISH EPUB BUILD"
	@echo $(CMD_SEP)
	@echo "Building EPUB..."
	@cat info-es.tex > temp_epub.tex
	@echo "" >> temp_epub.tex
	@cat dedication-es.tex >> temp_epub.tex
	@echo "" >> temp_epub.tex
	@perl -ne 'BEGIN{ %r=(1=>"I",2=>"II",3=>"III",4=>"IV",5=>"V",6=>"VI",7=>"VII",8=>"VIII",9=>"IX",10=>"X",11=>"XI",12=>"XII",13=>"XIII",14=>"XIV",15=>"XV",16=>"XVI",17=>"XVII",18=>"XVIII",19=>"XIX",20=>"XX",21=>"XXI",22=>"XXII",23=>"XXIII",24=>"XXIV",25=>"XXV",26=>"XXVI"); $$i=1} s/\\chapter\[(.*?)\]\{\}/"\\chapter{Capítulo $$r{$$i}: $$1}" . ($$i++ ? "" : "")/e; s/\\subtitle\{.*?\}//g; print' chapters-es.tex >> temp_epub.tex
	@pandoc temp_epub.tex -o book-es.epub \
		--toc --toc-depth=1 \
		--metadata title="Título del Libro" \
		--metadata author="Nombre del Autor" \
		--metadata lang="es"
	@rm temp_epub.tex
	@echo $(CMD_DONE)
	@echo $(CMD_SEP)
	@echo

clean:
	@echo $(CMD_SEP)
	@echo "Cleaning workspace..."
	@-$(CLEAN_CMD)
	@echo $(CMD_DONE)
	@echo $(CMD_SEP)
	@echo
