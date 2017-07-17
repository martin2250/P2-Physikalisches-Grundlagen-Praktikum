.PHONY: data

data: plots/photocurrent.pdf plots/3-1.pdf

plots:
	mkdir plots

plots/3-1.pdf: 3_1.py source/31.dat plots
	./$< $@

plots/photocurrent.pdf: photocurrent.py source/33.dat plots
	./$< $@

clean:
	git clean -Xf
