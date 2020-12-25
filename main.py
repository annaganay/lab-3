from struct import pack
import numpy as np
import math

HEIGHT = 600
WIDTH = 600

file = open('result.bmp', 'wb')
file.write(b'BM')
file.write(pack('<LHHL', 62 + HEIGHT*WIDTH, 0, 0, 62))
file.write(pack('<LLLHHLLLLLL', 40, HEIGHT, WIDTH, 1, 8, 0, 0, 0, 0, 0, 0))
color_0 = (0, 0, 0, 0)
color_1 = (255, 255, 255, 0)
file.write(pack('<8B', *color_0, *color_1))

t = np.linspace(0, 4 * np.pi, 600)
x = 2*(np.cos(2*t) - np.cos(4*t)/2)
y = 2*(np.cos(2*t) - np.sin(4*t)/2)
x = [round(v, 5) for v in x]
y = [round(v, 5) for v in y]

picture = []

for i in range(600):
    picture.append([x[i], y[i]])
y.sort()

for i in y:
    x_in_function = []
    for pair in picture:
        if pair[1] == i:
            x_in_function.append(pair[0])
    x_pixels = []
    for cur_y in x_in_function:
        x_pixels.append(math.trunc(cur_y*106 + 300))
    for a in range(WIDTH):
        if a in x_pixels:
            file.write(pack('<B', 0))
        else:
            file.write(pack('<B', 1))
file.close()