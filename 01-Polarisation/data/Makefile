.PHONY: data clean

sources := $(wildcard source/*.dat)
targets := $(patsubst %.dat,%.pdf,$(sources))
targets := $(patsubst source/%,plots/%,$(targets))

data: $(targets)

plots:
	mkdir plots

#plots/%.pdf: source/%.dat plots plot.py
#	./plot.py $< $@

plots/%.pdf: source/%.dat plots plot.gnu
	gnuplot plot.gnu "$<" "$@"

clean:
	git clean -Xf
