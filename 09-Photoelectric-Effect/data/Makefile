.PHONY: data

data: plots/photocurrent.pdf plots/3-1.pdf plots/3-2.pdf plots/3-5.pdf

plots:
	mkdir plots

plots/3-1.pdf: 3_1.py source/31.dat plots
	./$< $@

plots/3-2.pdf: 3_2+5.py source/32.dat plots
	./$< source/32.dat $@

plots/3-5.pdf: 3_2+5.py source/35.dat plots
	./$< source/35.dat $@

plots/photocurrent.pdf: photocurrent.py source/33.dat plots
	./$< $@

clean:
	git clean -Xf
