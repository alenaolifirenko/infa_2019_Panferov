from graph import *

windowSize(500, 1000)
penSize(0)

sky = (152,161,158)
asphalt = (32,54,47)

brushColor(asphalt)
rectangle(0,300,500,1000)

brushColor(sky)
rectangle(0,0,500,300)

brushColor(163,176,172)
oval(100,100,40,4)


brushColor(191,203,200)
circle(300,1020,550)

brushColor(sky)
rectangle(20,350,130,300)
penColor(80,171,168)
for i in range(55):
	line(20+2*i,350,20+2*i,40)

rectangle(140,370,250,300)
penColor(125,154,145)
for i in range(55):
	line(140+2*i,370,140+2*i,65)



brushColor(56,71,71)
rectangle(100,380,210,80)



brushColor(198,218,212)
rectangle(350,310,460,80)



brushColor(117,142,135)
rectangle(300,390,410,150)

brushColor("black")
oval(200,530,5,3)

brushColor(77,210,210)
rectangle(200,500,400,550)
rectangle(250,500,320,470)

brushColor("white")
rectangle(260,492,280,475)
rectangle(285,492,310,475)

brushColor("black")
circle(240,550,20)
circle(375,550,20)


penColor(163,176,172)
for i in range(40):
	hui = ((80**2-(2*i)**2)/16)**(1/2)
	line(100-2*i, 520-hui, 100-2*i, 520+hui)
for i in range(40):
	hui = ((80**2-(2*i)**2)/16)**(1/2)
	line(100+2*i, 520-hui, 100+2*i, 520+hui)

for i in range(100):
	hui = ((200**2-(2*i)**2)/16)**(1/2)
	line(350+2*i, 200-hui, 350+2*i, 200+hui)
for i in range(100):
	hui = ((200**2-(2*i)**2)/16)**(1/2)
	line(350-2*i, 200-hui, 350-2*i, 200+hui)

brushColor(97,115,110)
oval(50,475,15,4)
oval(0,400,22,4)


run()