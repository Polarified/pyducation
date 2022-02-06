import pprint
import sys

from PIL import Image

# I cheated on this one. Couldn't get past it.
# 1, I didnt think there were more images.
# 2, I didn't think of splitting into 5 because there were 5 piles.
url = 'http://www.pythonchallenge.com/pc/return/evil.html'

with open("static/evil2.gfx", "rb") as f1:
    data = f1.read()

for i in range(5):
    with open('{filename}.jpg'.format(filename=i), 'wb') as f2:
        f2.write(data[i::5])

