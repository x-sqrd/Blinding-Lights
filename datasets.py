# Blinding Lights Media
import FunctionVersions.imageDataToCartesian as ID
from PIL import Image

def imageA():
    return ID.imagetoCartesian("TestData/a.png")

def imageB():
    return ID.imagetoCartesian("TestData/b.png")

def imageC():
    return ID.imagetoCartesian("TestData/c.png")

def imageD():
    return ID.imagetoCartesian("TestData/d.png")

def largeImage(path, decompress=500, create=False):
    im = Image.open(path)
    im.thumbnail((decompress,decompress), Image.BICUBIC)

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

    while county < height:
        global list1
        list1 = []
        while countx < width:

            list1.append(hexArr[countHex])
            countHex+=1
            countx+=1
        #now countx = 100
        output.append(list1)
        countx = 0
        county += 1
    
    if create: im.save('compressed.jpg', 'JPEG', progressive=True, quality=100)
    return output 


def image12():
    return largeImage("TestData/IMG_0012.jpg")

def image13():
    return largeImage("TestData/IMG_0013.jpg")

def image14():
    return largeImage("TestData/IMG_0014.jpg")

def image15():
    return largeImage("TestData/IMG_0015.jpg")

def image16():
    return largeImage("TestData/IMG_0016.jpg")

def image17():
    return largeImage("TestData/IMG_0017.jpg")


