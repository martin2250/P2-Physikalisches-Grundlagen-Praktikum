.PHONY: data

PLT := ./curve-plotter.py

tempco-stuff := plots/tempco-ntc.pdf plots/tempco-pt100.pdf
low-freq-stuff := plots/diodes-low-freq.pdf plots/photodiode-low-freq.pdf plots/varistor-low-freq.pdf plots/ldr-low-freq.pdf plots/z-diode-low-freq.pdf plots/leds-low-freq.pdf
phototransistor-stuff := plots/phototranny.pdf plots/phototranny_curve.pdf
hi-freq-stuff := plots/diodes-hi-freq.pdf plots/photodiode-hi-freq.pdf plots/varistor-hi-freq.pdf plots/ldr-hi-freq.pdf plots/z-diode-hi-freq.pdf plots/led-hi-freq.pdf
piezo-stuff := plots/piezo-finger-press.pdf plots/piezo-finger-snap.pdf plots/piezo-2kHz.pdf

data: $(low-freq-stuff) $(hi-freq-stuff) $(phototransistor-stuff) $(piezo-stuff) $(tempco-stuff) plots/superconductor.pdf

plots:
	mkdir plots


plots/tempco-%.pdf: tempco.py plots
	./$< $* $@

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
plots/diodes-low-freq.pdf: $(PLT) plots
	./$< $@ scope-src/20Hz/si-diode.npz "&dSilicon Diode" scope-src/20Hz/ge-diode.npz "&dGermanium Diode"

plots/photodiode-low-freq.pdf: $(PLT) plots
	./$< $@ scope-src/20Hz/photodiode-with-light.npz "Photodiode"

plots/varistor-low-freq.pdf: $(PLT) plots
	./$< $@ scope-src/20Hz/varistor-3v3.npz "&d&zVaristor (3.3V)"

plots/ldr-low-freq.pdf: $(PLT) plots
	./$< $@ scope-src/20Hz/ldr.npz "LDR"

plots/z-diode-low-freq.pdf: $(PLT) plots
	./$< $@ scope-src/20Hz/z-diode-5v1.npz "&d&zZ-Diode (5.1V)"

plots/leds-low-freq.pdf: $(PLT) plots
	./$< $@ scope-src/20Hz/led-red.npz "<r>&dLED red" scope-src/20Hz/led-yellow.npz "<#e8e81b>&dLED yellow" scope-src/20Hz/led-orange.npz "<#ff9933>&dLED orange" scope-src/20Hz/led-green.npz "<g>&dLED green"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

plots/diodes-hi-freq.pdf: $(PLT) plots
	./$< $@ scope-src/10kHz/si-diode.npz "Silicon Diode" scope-src/10kHz/ge-diode.npz "Germanium Diode"

plots/photodiode-hi-freq.pdf: $(PLT) plots
	./$< $@ scope-src/10kHz/photodiode-with-metric-shitton-of-light.npz "Photodiode"

plots/varistor-hi-freq.pdf: $(PLT) plots
	./$< $@ scope-src/10kHz/varistor-3v3.npz "Varistor (3.3V)"

plots/ldr-hi-freq.pdf: $(PLT) plots
	./$< $@ scope-src/10kHz/ldr.npz "LDR"

plots/z-diode-hi-freq.pdf: $(PLT) plots
	./$< $@ scope-src/10kHz/z-diode-5v1.npz "Z-Diode (5.1V)"

plots/led-hi-freq.pdf: $(PLT) plots
	./$< $@ scope-src/10kHz/led-red.npz "<r>LED red"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
plots/phototranny.pdf: ./phototranny.py plots
	./$< $@ scope-src/phototransistor/0v.npz 0 scope-src/phototransistor/5v.npz 200 scope-src/phototransistor/6v.npz 600  scope-src/phototransistor/7.5v.npz 1550  scope-src/phototransistor/8.5v.npz 2550 scope-src/phototransistor/9.5v.npz 3950 scope-src/phototransistor/10.5v.npz 5800 scope-src/phototransistor/11v.npz 6850 scope-src/phototransistor/11.5v.npz 7850 scope-src/phototransistor/12v.npz 9100

plots/phototranny_curve.pdf: ./phototranny_curve.py plots
	./$< $@
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
plots/piezo-finger-press.pdf: ./piezo-fucking-curve-plotter-motherfuckaaa.py plots
	./$< scope-src/piezo/finger-press.npz volt $@

plots/piezo-finger-snap.pdf: ./piezo-fucking-curve-plotter-motherfuckaaa.py plots
	./$< scope-src/piezo/finger-snap.npz volt $@

plots/piezo-2kHz.pdf: ./piezo-fucking-curve-plotter-motherfuckaaa.py plots
	./$< scope-src/piezo/2kHz.npz mV $@
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

plots/superconductor.pdf: ./superconductor.py plots
	./$< $@

clean:
	git clean -Xf
