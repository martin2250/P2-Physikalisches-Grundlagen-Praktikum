.PHONY: data clean

data:

clean:
	git clean -Xf

plots:
	mkdir plots

plots/%.pdf: source/%.dat evalkafe.py plots
	./evalkafe.py $< $@
