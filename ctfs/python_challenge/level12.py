from PIL import Image
import numpy as np
import pprint

url = 'http://www.pythonchallenge.com/pc/return/evil.html'

img = Image.open('static/evil1.jpg')
width, height = img.size
pixels = list(img.getdata())

rows = [pixels[x:width + x] for x in range(0, len(pixels), width)]

print(len(rows), len(rows[0]))

greens = [rows[x: x + 2] for x in range(1, len(rows), 6)]
blues = [rows[x: x + 2] for x in range(2, len(rows), 6)]
reds = [rows[x: x + 2] for x in range(0, len(rows), 6)]

print(len(greens), len(greens[0]), len(greens[0][0]))

fr = [item for sublist in reds for item in sublist]
fg = [item for sublist in greens for item in sublist]
fb = [item for sublist in blues for item in sublist]

e = Image.new(img.mode, img.size)
e.putdata(fr + fg + fb)
e.show()
e.save('static/triple.jpg')
