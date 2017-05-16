.PHONY: data clean

data: plots/1_4.pdf plots/1_1.pdf plots/2.pdf plots/3.pdf plots/4_1.pdf plots/4_2.pdf

clean:
	git clean -Xf

plots:
	mkdir plots

plots/1_4.pdf: $(wildcard source/%.dat) 1_4.py plots
	./1_4.py $@

plots/1_1.pdf: source/1.1.dat 1_1.py plots
	./1_1.py $@

plots/2.pdf: source/2.dat 2.py plots
	./2.py $@

plots/4_1.pdf: source/4.1.dat 4_1.py plots
	./4_1.py $@

plots/4_2.pdf: source/4.2.dat 4_2.py plots
	./4_2.py $@

plots/3.pdf: source/3.dat 3.py plots
	./3.py $@
