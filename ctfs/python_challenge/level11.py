from PIL import Image
from pprint import pprint

img = Image.open('cave.jpg')
width, height = img.size
pixels = img.load()

pixlist = []
for x in range(width):
    row = [pixels[x, y] for y in range(height)]
    pixlist.append(row)
    print(row)
