.PHONY: data

data: 2_img.pdf plots/4_enth.pdf plots/4_vapor.pdf

%.pdf:	%.py
	./$< $@

plots/4_enth.pdf:	plots/%.pdf: %.py source/4_a.dat source/4_b.dat plots
	./$< $@

plots/4_vapor.pdf:	plots/%.pdf: %.py source/4_a.dat source/4_b.dat plots
	./$< $@

clean:
	git clean -Xf
