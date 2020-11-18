from PIL import Image

img = Image.open('oxygen.png')
img = img.convert('RGB')
Y = 45

answer = ''.join([chr(img.getpixel((x, Y))[0]) for x in range(0, 605, 7)])
print(answer)
next_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join(chr(x) for x in next_level))