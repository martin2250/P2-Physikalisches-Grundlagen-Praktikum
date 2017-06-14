.PHONY: data

data:plots/1_4.pdf

clean:
	git clean -Xf

plots:
	mkdir plots

plots/1_4.pdf: plots/%.pdf: %.py source/%.dat plots
	./$< $@
