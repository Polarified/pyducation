import pprint
from PIL import Image

url = 'http://www.pythonchallenge.com/pc/return/evil.html'

img = Image.open('static/evil1.jpg')
width, height = img.size
pixels = img.load()

pprint.pprint([pixels[x, y] for x in range(width) for y in range(height)])
