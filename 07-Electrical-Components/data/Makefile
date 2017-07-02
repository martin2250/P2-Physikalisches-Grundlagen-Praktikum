.PHONY: data low-freq-stuff phototransistor-stuff

PLT := ./curve-plotter.py

data: low-freq-stuff phototransistor-stuff plots/tempco.pdf

plots:
	mkdir plots

plots/tempco.pdf: tempco.py plots
	./$< $@

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
low-freq-stuff: plots/diodes-low-freq.pdf plots/photodiode-low-freq.pdf plots/varistor-low-freq.pdf plots/ldr-low-freq.pdf plots/z-diode-low-freq.pdf plots/leds-low-freq.pdf

plots/diodes-low-freq.pdf: $(PLT) plots
	$< $@ scope-src/20Hz/si-diode.npz "&dSilicon Diode" scope-src/20Hz/ge-diode.npz "&dGermanium Diode"

plots/photodiode-low-freq.pdf: $(PLT) plots
	$< $@ scope-src/20Hz/photodiode-with-light.npz "Photodiode"

plots/varistor-low-freq.pdf: $(PLT) plots
	$< $@ scope-src/20Hz/varistor-3v3.npz "&d&zVaristor (3.3V)"

plots/ldr-low-freq.pdf: $(PLT) plots
	$< $@ scope-src/20Hz/ldr.npz "LDR"

plots/z-diode-low-freq.pdf: $(PLT) plots
	$< $@ scope-src/20Hz/z-diode-5v1.npz "&d&zZ-Diode (5.1V)"

plots/leds-low-freq.pdf: $(PLT) plots
	$< $@ scope-src/20Hz/led-red.npz "<r>LED red" scope-src/20Hz/led-yellow.npz "<#e8e81b>LED yellow" scope-src/20Hz/led-orange.npz "<#ff9933>LED orange" scope-src/20Hz/led-green.npz "<g>LED green"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
phototransistor-stuff: plots/phototranny.pdf plots/phototranny_curve.pdf

plots/phototranny.pdf: ./phototranny.py plots
	$< $@ scope-src/phototransistor/0v.npz 0 scope-src/phototransistor/5v.npz 200 scope-src/phototransistor/6v.npz 600  scope-src/phototransistor/7.5v.npz 1550  scope-src/phototransistor/8.5v.npz 2550 scope-src/phototransistor/9.5v.npz 3950 scope-src/phototransistor/10.5v.npz 5800 scope-src/phototransistor/11v.npz 6850 scope-src/phototransistor/11.5v.npz 7850 scope-src/phototransistor/12v.npz 9100

plots/phototranny_curve.pdf: ./phototranny_curve.py plots
	$< $@
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

clean:
	git clean -Xf
