.PHONY: data

data: plots/calorimeter.agtex

plots:
	mkdir plots

plots/calorimeter.agtex: calorimeter.py plots source/calorimeter.dat
	./$< > $@

clean:
	git clean -Xf
