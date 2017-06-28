.PHONY: data

data: plots/2_img.pdf plots/4_enth.pdf plots/4_vapor.pdf

plots:
	mkdir plots

plots/2_img.pdf: 2_img.py plots
	./$< $@

plots/4_vapor.pdf plots/4_enth.pdf:	plots/%.pdf: %.py source/4_a.dat source/4_b.dat plots
	./$< $@

clean:
	git clean -Xf
