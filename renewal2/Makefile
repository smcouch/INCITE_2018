NAME=Achievements
TARGET=$(NAME).pdf
SOURCE=$(NAME).tex
AUX=$(NAME).aux

#FIGS=$(wildcard fig/*.pdf)
#BIBS=$(shell find bibliography/ -name \*.bib)
#PLTS=$(shell find fig -name \*.py -perm +111)

JUNK=.aux .bbl .blg .dvi .log .nav .out .ps .snm .tex.backup .toc Notes.bib

all: $(TARGET)

$(TARGET): $(SOURCE) $(FIGS) .FORCE
	@pdflatex $(SOURCE)
	@bibtex $(NAME)
	@pdflatex $(SOURCE)
	@pdflatex $(SOURCE)

bib1: Achievements.tex .FORCE
	@pdflatex Achievements.tex
	@bibtool -x Achievements.aux -i $(PTOOLSDIR)/masterDB.bib -o Achievements.bib
	@bibtex Achievements

bib2: Plans.tex .FORCE
	@pdflatex Plans.tex
	@bibtool -x Plans.aux -i $(PTOOLSDIR)/masterDB.bib -o Plans.bib
	@bibtex Plans

clean:
	@for ext in $(JUNK); do\
	    rm -f $(NAME)$$ext;\
	done

quick:  $(SOURCE) $(FIGS) $(BIBS) .FORCE
	@pdflatex $(SOURCE)

milestones: .FORCE
	@pdflatex incite_ccsn_milestones.tex 

.FORCE:
