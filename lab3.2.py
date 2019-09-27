from graph import * #измененный graph


def mkcar(x, y, sc):
    brushColor("black")
    oval(x, y + 30 * sc, 5 * sc, 3)

    brushColor(77, 210, 210)
    rectangle(x, y, x + 200 * sc, y + 50 * sc)
    rectangle(x + 50 * sc, y, x + 120 * sc, y - 30 * sc)

    brushColor("white")
    rectangle(x + 60 * sc, y - 8 * sc, x + 80 * sc, y - 25 * sc)
    rectangle(x + 85 * sc, y - 8 * sc, x + 110 * sc, y - 25 * sc)

    brushColor("black")
    circle(x + 40 * sc, y + 50 * sc, 20 * sc)
    circle(x + 175 * sc, y + 50 * sc, 20 * sc)

windowSize(500, 600)
canvasSize(500, 600)
penSize(0)

sky = (152, 161, 158)
asphalt = (32, 54, 47)

brushColor(asphalt)
rectangle(0, 300, 500, 1000)

brushColor(sky)
rectangle(0, 0, 500, 350)

brushColor(sky)
rectangle(20, 350, 130, 300)

brushColor(204, 255, 255)
penColor('white')
penSize(5)
rectangle(0, 10, 250, 350)
rectangle(230, 20, 500, 350)

penSize(0)
penColor(80, 171, 168)
for i in range(55):
    line(20 + 2 * i, 350, 20 + 2 * i, 40)

rectangle(140, 370, 250, 350)
penColor(125, 154, 145)
for i in range(55):
    line(140 + 2 * i, 350, 140 + 2 * i, 65)

brushColor(56, 71, 71)
rectangle(100, 380, 210, 80)

brushColor(198, 218, 212)
rectangle(350, 310, 460, 80)

brushColor(117, 142, 135)
rectangle(300, 390, 410, 150)

mkcar(200, 500, 1)
mkcar(350, 450, 0.5)
mkcar(75, 450, 0.3)
mkcar(175, 400, 0.7)
mkcar(430, 400, 0.3)
mkcar(50, 400, 0.4)

penColor(163, 176, 172)
for i in range(40):
    hui = ((80 ** 2 - (2 * i) ** 2) / 16) ** (1 / 2)
    line(100 - 2 * i, 520 - hui, 100 - 2 * i, 520 + hui)
for i in range(40):
    hui = ((80 ** 2 - (2 * i) ** 2) / 16) ** (1 / 2)
    line(100 + 2 * i, 520 - hui, 100 + 2 * i, 520 + hui)

for i in range(100):
    hui = ((200 ** 2 - (2 * i) ** 2) / 16) ** (1 / 2)
    line(350 + 2 * i, 200 - hui, 350 + 2 * i, 200 + hui)
for i in range(100):
    hui = ((200 ** 2 - (2 * i) ** 2) / 16) ** (1 / 2)
    line(350 - 2 * i, 200 - hui, 350 - 2 * i, 200 + hui)

run()