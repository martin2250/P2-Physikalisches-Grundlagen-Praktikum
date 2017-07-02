.PHONY: data low-freq-stuff

PLT := ./curve-plotter.py

data: low-freq-stuff plots/tempco.pdf

plots:
	mkdir plots

plots/tempco.pdf: tempco.py plots
	./$< $@


low-freq-stuff: plots/diodes-low-freq.pdf plots/photodiode-low-freq.pdf plots/varistor-low-freq.pdf plots/ldr-low-freq.pdf plots/z-diode-low-freq.pdf plots/leds-low-freq.pdf

plots/diodes-low-freq.pdf: $(PLT) plots
	$(PLT) $@ scope-src/20Hz/si-diode.npz "Si-Diode" scope-src/20Hz/ge-diode.npz "Ge-Diode"

plots/photodiode-low-freq.pdf: $(PLT) plots
	$(PLT) $@ scope-src/20Hz/photodiode-with-light.npz "Photodiode"

plots/varistor-low-freq.pdf: $(PLT) plots
	$(PLT) $@ scope-src/20Hz/varistor-3v3.npz "Varistor (3.3V)"

plots/ldr-low-freq.pdf: $(PLT) plots
	$(PLT) $@ scope-src/20Hz/ldr.npz "LDR"

plots/z-diode-low-freq.pdf: $(PLT) plots
	$(PLT) $@ scope-src/20Hz/z-diode-5v1.npz "Z-Diode (5.1V)"

plots/leds-low-freq.pdf: $(PLT) plots
	$(PLT) $@ scope-src/20Hz/led-red.npz "<r>LED red" scope-src/20Hz/led-yellow.npz "<#e8e81b>LED yellow" scope-src/20Hz/led-orange.npz "<#ff9933>LED orange" scope-src/20Hz/led-green.npz "<g>LED green"

clean:
	git clean -Xf
