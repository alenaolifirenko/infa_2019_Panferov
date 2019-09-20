from graph import *

windowSize(2000,1000)
canvasSize(2000,1000)

def mkcar(x,y,sc):
	brushColor("black")
	oval(x,y+30*sc,5*sc,3)

	brushColor(77,210,210)
	rectangle(x,y,x+200*sc,y+50*sc)
	rectangle(x+50*sc,y,x+120*sc,y-30*sc)

	brushColor("white")
	rectangle(x+60*sc,y-8*sc,x+80*sc,y-25*sc)
	rectangle(x+85*sc,y-8*sc,x+110*sc,y-25*sc)

	brushColor("black")
	circle(x+40*sc,y+50*sc,20*sc)
	circle(x+175*sc,y+50*sc,20*sc)

penSize(0)
sky = (152,161,158)
asphalt = (32,54,47)

brushColor(asphalt)
rectangle(0,700,2000,1000)

mkcar(800,800,1)
mkcar(1500,820,1.2)
mkcar(500,900,1.5)
mkcar(50,950,1.6)

run()