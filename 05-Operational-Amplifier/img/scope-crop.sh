for f in *.JPG; do convert $f -crop 628x425+0+24 -quality 20 outp/${f%.JPG}.jpg ; done
