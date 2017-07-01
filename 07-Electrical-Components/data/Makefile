.PHONY: data

PLT := ./curve-plotter.py

data: plots/diodes-low-freq.pdf plots/leds-low-freq.pdf plots/tempco.pdf

plots:
	mkdir plots

plots/tempco.pdf: tempco.py plots
	./$< $@

plots/diodes-low-freq.pdf: $(PLT) plots
	$(PLT) $@ scope-src/20Hz/si-diode.npz "Si-Diode" scope-src/20Hz/ge-diode.npz "Ge-Diode"

plots/leds-low-freq.pdf: $(PLT) plots
	$(PLT) $@ scope-src/20Hz/led-red.npz "<r>LED red" scope-src/20Hz/led-yellow.npz "<#e8e81b>LED yellow" scope-src/20Hz/led-orange.npz "<#ff9933>LED orange" scope-src/20Hz/led-green.npz "<g>LED green"

clean:
	git clean -Xf
