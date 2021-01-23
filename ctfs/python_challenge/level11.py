from PIL import Image
import pprint

url = 'http://www.pythonchallenge.com/pc/return/5808.html'

img = Image.open('static/cave.jpg')
width, height = img.size
pixels = list(img.getdata())

pprint.pprint(pixels[:100])

even = [pixels[i] for i in range(0, len(pixels), 2)]
odd = [pixels[i] for i in range(1, len(pixels), 2)]


e = Image.new(img.mode, img.size)
e.putdata(even)
e.show()

o = Image.new(img.mode, img.size)
o.putdata(odd)
o.show()
