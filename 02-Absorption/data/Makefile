.PHONY: data clean

data: plots/1_4.pdf plots/1_1.pdf

clean:
	git clean -Xf

plots:
	mkdir plots

plots/1_4.pdf: $(wildcard source/%.dat) 1_4.py plots
	./1_4.py $@

plots/1_1.pdf: source/1.1.dat 1_1.py plots
	./1_1.py $@
