.PHONY: data

data: plots/1-1-blue.pdf plots/1-1-yellow.pdf

plots:
	mkdir plots

plots/1-%.pdf: source/1-%.dat newton.py plots
	./newton.py $< $@

clean:
	git clean -Xf
