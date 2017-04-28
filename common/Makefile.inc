BUILD = latexmk -pdf -interaction=nonstopmode -synctex=1
FILE = P2-$(shell basename $(CURDIR))

.PHONY: all build show upload share clean data

all: build show

data:
	make -C data

build: data main.tex ../common/emails.tex bibliography.ag.tex titlepage.ag.tex
	$(BUILD) -jobname=$(FILE) main.tex

show:
	xdg-open $(FILE).pdf > /dev/null 2>&1 &

upload: build
	../common/upload.sh $(FILE).pdf

share: build
	curl -H "Max-Days: 1" --upload-file ./$(FILE).pdf https://transfer.sh/$(FILE).pdf

../common/emails.tex:
	printf '\\newcommand{\\emailadressen}{TODO: umut@dick.butt, martin@dick.butt}' > ../common/emails.tex

#titlepage and bibliography have to be copied, because \include only works in subdirectories of $PWD
titlepage.ag.tex:
	cp ../praktikum-protokollvorlage-latex/include/titlepage.tex titlepage.ag.tex
bibliography.ag.tex:
	cp ../common/bibliography.tex bibliography.ag.tex

clean:
	git clean -Xf
