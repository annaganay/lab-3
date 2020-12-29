import numpy as np
from tkinter import *

print('Введите ширину файла в пиксилях(не меньше 600):')
h = int(input())

min = 600

if h < min:
    h = min

root = Tk()

c = Canvas(root, width=h, height=h, bg='white')
c.pack()

c.create_line(h/2, h, h/2, 0, arrow=LAST)
c.create_line(0, h/2, h, h/2, arrow=LAST)

for x in range(10):
    c.create_line(h/2-6, x/10*h, h/2+7, x/10*h)
    c.create_line(x/10*h, h/2-6, x/10*h, h/2+7)


t = np.linspace(0, 4 * np.pi, 600)
x = 2*(np.cos(2*t) - np.cos(4*t)/2)*h/10
y = 2*(np.cos(2*t) - np.sin(4*t)/2)*h/10
x = [round(v, 5) for v in x]
y = [round(v, 5) for v in y]


for i in range(599):
    c.create_line(x[i]+h/2, -y[i]+h/2, x[i+1]+h/2, -y[i+1]+h/2, width=2, fill='red')
y.sort()

c.update()
c.postscript(file="picture.bmp")

root.mainloop()
