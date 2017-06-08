.PHONY: data

data: plots/5.pdf plots/6.pdf plots/2.pdf plots/3.pdf plots/4.pdf

clean:
	git clean -Xf

plots:
	mkdir plots

plots/5.pdf plots/6.pdf plots/2.pdf plots/3.pdf plots/4.pdf: plots/%.pdf: %.py source/%.dat plots
	./$< $@
