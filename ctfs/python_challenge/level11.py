from PIL import Image

url = 'http://www.pythonchallenge.com/pc/return/5808.html'

img = Image.open('static/cave.jpg')
width, height = img.size
pixels = list(img.getdata())

even = [pixels[i] for i in range(0, len(pixels), 2)]
odd = [pixels[i] for i in range(1, len(pixels), 2)]


o = Image.new(img.mode, img.size)
o.putdata(odd + even)
o.show()
