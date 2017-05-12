.PHONY: data

data: 1_4.pdf

clean:
	git clean -Xf


1_4.pdf: $(wildcard source/%.dat) 1_4.py
	./1_4.py $@
