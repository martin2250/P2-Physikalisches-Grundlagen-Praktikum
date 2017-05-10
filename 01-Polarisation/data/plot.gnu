set polar
set angles degree
unset key
set grid polar 30
set rtics textcolor rgb "white"
set rtics scale 0
unset raxis
#set size square
set size ratio -1

set border 2
unset xtics
set ytics nomirror


set ylabel "Spannung in V"

########################################## Doesn't work somehow
#set_label(x, text) = sprintf("set label '%s' at (6500*cos(%f)), (6500*sin(%f)) center", text, x, x)

#eval set_label(0, "0")
#eval set_label(30, "30")
#eval set_label(60, "60")
#eval set_label(90, "90")
#eval set_label(120, "120")
#eval set_label(150, "150")
#eval set_label(180, "180")
#eval set_label(210, "210")
#eval set_label(240, "240")
#eval set_label(270, "270")
#eval set_label(300, "300")
#eval set_label(330, "330")
###########################################
set terminal pdf
set output ARG2

plot ARG1 with lines
