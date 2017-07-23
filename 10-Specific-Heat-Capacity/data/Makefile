.PHONY: data

data: plots/calorimeter.agtex plots/al_heater.pdf plots/al_no_heater.pdf plots/cap_over_T.pdf

plots:
	mkdir plots

plots/calorimeter.agtex: calorimeter.py plots source/calorimeter.dat
	./$< > $@

plots/al_heater.pdf: al_heater.py plots source/al-warm-up-no-shitty-encoding-errors.dat
	./$< $@

plots/al_no_heater.pdf: al_no_heater.py plots source/al-warm-up-no-heater-and-no-shitty-encoding-errors.dat
	./$< $@

plots/cap_over_T.pdf: cap_over_T.py plots
	./$< $@
clean:
	git clean -Xf
