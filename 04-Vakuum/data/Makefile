.PHONY: data

data: plots/5.pdf plots/6.pdf

clean:
	git clean -Xf

plots:
	mkdir plots

plots/5.pdf plots/6.pdf: plots/%.pdf: %.py source/%.dat plots
	./$< $@
