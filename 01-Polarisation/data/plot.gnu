set polar
set angles degree
unset key
set grid polar
set rtics textcolor rgb "white"
set rtics scale 0
unset raxis
set size square


set border 2
unset xtics
set ytics nomirror


set ylabel "Spannung in V"

plot 'zirkular.dat' with lines
