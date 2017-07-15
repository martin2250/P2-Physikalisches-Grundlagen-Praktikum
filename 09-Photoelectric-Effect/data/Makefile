.PHONY: data

data: plots/photocurrent.pdf

plots:
	mkdir plots

plots/photocurrent.pdf: photocurrent.py source/33.dat plots
	./$< $@

clean:
	git clean -Xf
