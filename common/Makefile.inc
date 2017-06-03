BUILD = latexmk -pdf -interaction=nonstopmode -synctex=1
FILE = $(shell basename $(CURDIR))
svgimgs := $(wildcard img/*.svg)
svgimtargets := $(patsubst %.svg,%.pdf,$(svgimgs))

.PHONY: all build show upload share clean data

all: build show

data:
	make -C data

build: data $(FILE).tex ../common/emails.tex bibliography.ag.tex titlepage.ag.tex $(svgimtargets)
	$(BUILD) $(FILE).tex

show:
	xdg-open $(FILE).pdf > /dev/null 2>&1 &

share: build
	curl -H "Max-Days: 1" --upload-file ./$(FILE).pdf https://transfer.sh/$(FILE).pdf

../common/emails.tex:
	printf '\\newcommand{\\emailadressen}{TODO: umut@dick.butt, martin@dick.butt}' > ../common/emails.tex

img/%.pdf: img/%.svg
	inkscape $< --export-pdf=$@

#titlepage and bibliography have to be copied, because \include only works in subdirectories of $PWD
titlepage.ag.tex:
	cp ../praktikum-protokollvorlage-latex/include/titlepage.tex titlepage.ag.tex
bibliography.ag.tex:
	cp ../common/bibliography.tex bibliography.ag.tex

clean:
	git clean -Xf
