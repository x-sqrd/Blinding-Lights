# Blinding Lights Image to Cartesian Coordinates [Python 3.8.2]

# Created by Ayush Nayak in 2020
from PIL import Image

im = Image.open('TestData/a.png', 'r').convert('RGB')
redPix = list(im.getdata(0))
greenPix = list(im.getdata(1))
bluePix = list(im.getdata(2))
pixArr = []
for l in range(0, len(redPix)):
    pixArr.append((redPix[l], greenPix[l], bluePix[l]))

def rgbToHex(RGBtuple):
    return '#%02x%02x%02x' % (RGBtuple[0], RGBtuple[1], RGBtuple[2])

hexArr = []

for m in range(0, len(pixArr)):
    hexArr.append(rgbToHex(pixArr[m]))

width, height = im.size

countx = 0
county = 0

output = []

countHex = 0

while county < 100:
    while countx < 100:
        output.append((countx, county, hexArr[countHex]))
        countHex+=1
        countx+=1
    #now countx = 100
    countx = 0
    county += 1
