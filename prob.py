from graph import *

penColor("black")
penSize(1)
brushColor("yellow")

circle(300, 300, 100)

brushColor("red")
circle(260, 270, 21)
circle(340, 270, 18)

brushColor("black")
circle(260,270,10)
circle(340,270,10)

brow1 = [(280,250),(290,240),(230,180),(220,190)]
polygon(brow1)
brow2 = [(320,250),(380,220),(375,210),(315,240)]
polygon(brow2)

rectangle(270,320,330,330) 

run()
