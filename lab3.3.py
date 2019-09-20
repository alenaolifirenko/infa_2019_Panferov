from graph import *
import random
import math

windowSize(2000,1000)
canvasSize(2000,1000)

def smoke(x1,y1,x2,y2,n):
	c = (163,176,172)
	for i in range(x2-x1):
		for j in range(y2-y1):
			if random.random() < n*(1-(((x2-x1)/2-i)/(x2-x1)*2)**2)*(1-(((y2-y1)/2-j)/(y2-y1)*2)**2):
				point(x1+i,y1+j,c)

def shadow(x1,y1,x2,y2,n):
	c = (0,0,0)
	for i in range(x2-x1):
		for j in range(y2-y1):
			if random.random() < n:
				point(x1+i,y1+j,c)

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

def mkcor(x,y,sc):
	brushColor("black")
	oval(x,y+30*sc,5*sc,3)

	brushColor(77,210,210)
	rectangle(x,y,x-200*sc,y+50*sc)
	rectangle(x-50*sc,y,x-120*sc,y-30*sc)

	brushColor("white")
	rectangle(x-60*sc,y-8*sc,x-80*sc,y-25*sc)
	rectangle(x-85*sc,y-8*sc,x-110*sc,y-25*sc)

	brushColor("black")
	circle(x-40*sc,y+50*sc,20*sc)
	circle(x-175*sc,y+50*sc,20*sc)

def mkcloud(x,y,r,e):
	penColor(30,30,30)
	for i in range(r):
		hui = (((2*r)**2-(2*i)**2)/e**2)**(1/2)
		line(x-2*i, y-hui, x-2*i, y+hui)
	for i in range(r):
		hui = (((2*r)**2-(2*i)**2)/e**2)**(1/2)
		line(x+2*i, y-hui, x+2*i, y+hui)





penSize(0)
sky = (50,50,50)
asphalt = (32,54,47)
h1 = (113,135,129)
h2 = (76,91,87)
h3 = (106,125,120)
h4 = (109,115,114)
h5 = (87,119,111)

brushColor(asphalt)
rectangle(0,700,2000,1000)
brushColor(sky)
rectangle(0,0,2000,700)

shadow(0,0,150,700,0.7)
shadow(400,200,600,700,0.8)
shadow(550,100,700,700,0.9)
shadow(1000,50,1500,700,0.7)
shadow(1400,20,1700,700,0.8)

brushColor(h2)
rectangle(750,200,1500,700)
brushColor(h1)
rectangle(0,300,800,800)
mkcloud(1200,500,300,4)
brushColor(h4)
rectangle(1400,250,2000,850)

mkcor(400,840,1)
mkcar(800,800,1)
mkcar(1500,820,1.2)
mkcar(500,900,1.5)
mkcar(50,950,1.6)
mkcar(0,800,0.8)
mkcor(1400,900,1.5)
mkcor(1390,750,0.7)

smoke(0,700,2000,1000,0.5)

mkcloud(1000,200,100,10)
mkcloud(200,150,150,9)
mkcloud(1700,50,150,8)
run()