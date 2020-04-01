# created by Shad0w7 + ChickenAgent2227
# needs major de

# Blinding BorderOccurence.py
import Random
from PIL import Image

def imagetoCartesian(path): # from a different package only here for testing purposes
    try:
        im = Image.open(path, 'r').convert('RGB')
    except FileNotFoundError:
        print('Not Running, Image Path Incorrect!')
        print('Exiting...')
        exit(1)
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
    return output


def hexToRGB(hex): # This is a CORE Package
    hex = hex.lstrip('#')
    rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    return rgb


def isBlack(rgb): # This is a CORE Package DO NOT REMOVE
    """
    Purpose: Check if a color is sufficiently black.
    """
    if int(rgb[0]) < 25 and int(rgb[1]) < 25 and int(rgb[2]) < 25:
        return True
    else:
        return False

def hexIsBlack(hex):
    return isBlack(hexToRGB(hex))

def findBorderStart(coordinates, startX=-1, startY=-1):
    """
    Purpose: Literally find the border, or return that it doesn't exist.
    Return: List of coordinates on inner boundary of border. Return if can't find it.
    """

    width = len(coordinates)
    height = len(coordinates[0])
    if startX == -1: startX = width//2
    if startY == -1: startY = height//2
    while True:
        #lefty loosey
        if hexIsBlack(coordinates[startX][startY]):
            borderStart = [startX, startY]
            break
        elif startX < width - 1:
            startX += 1
        else:
            borderStart = None
            break

    return borderStart

def calcNextPoint(deltaX, deltaY):
    if deltaX == 2:
        if deltaY < 1:
            deltaY += 1
        else:
            deltaX = 1
            deltaY = 2
    elif deltaX == -2:
        if deltaY > -1:
            deltaY -= 1
        else:
            deltaX = -1
            deltaY = -2
    elif deltaY == 2:
        if deltaX > -1:
            deltaX -= 1
        else:
            deltaX = -2
            deltaY = 1
    else:
        if deltaX < 1:
            deltaX += 1
        else:
            deltaX = 2
            deltaY = -1

    return deltaX, deltaY


def borderTrace(borderStart, coordinates):
    startX = borderStart[0]
    startY = borderStart[1]
    previousX = startX
    previousY = startY
    currentX = startX
    currentY = startY
    borderList = []
    while True:
        prevCheckingX = currentX + 2
        prevCheckingY = currentY
        checkingX = prevCheckingX
        checkingY = prevCheckingY + 1

        while True: # Find next point
            if isBlack[checkingX][checkingY] and not isBlack[prevCheckingX, prevCheckingY]:
                # The current point is black, but the previous point isn't. Bingo!
                previousX = currentX    # Move along the border.
                previousY = currentY    # which means updating coordinates
                currentX = checkingX
                currentY = checkingY
                borderList.append([currentX], [currentY])
                break
            elif checkingX == currentX + 2 and checkingY == currentY + 2:
                # We did a full loop and didn't find anything useful. Something is off.
                return None
            else:
                # Didn't work, so we'll check different points and run the process again.
                prevCheckingX = checkingX
                prevCheckingY = checkingY
                deltaX = checkingX - currentX
                deltaY = checkingY - currentY
                deltaX, deltaY = calcNextPoint(deltaX, deltaY)
                checkingX = currentX + deltaX
                checkingY = currentY + deltaY

        # Check if we've completed the loop
        if currentY > startY and previousY < startY:
            return borderList


# The AYUSH Framework !!!! YAY!

# ///////////////
# //         //
# //////    //
#     //   //
# //////  //

def borderBashed(coordinates): #Part of @bashingit
    blacklist = []
    height = len(coordinates)
    width = len(coordinates[0])
    x = 0
    y = 0
    while y < height:
        while x < width:
            if hexIsBlack(coordinates[y][x]):
                blacklist.append((x, y))
            x += 1
        x = 0
        y += 1
    return blacklist

def bashFlatten(coordinates, blacklist):
    # Because of the nature of the way blacklist was constructed in borderTraceBashed, it is not neccesary






'''
[
[asdf, asdf, asdf, asdf]
[asdf, asdf, asdf, asdf]
[asdf, asdf, asdf, asdf]
]
'''
def smoothBorder():
    """
    Purpose: Literally smoothen the border.
    Return: Coordinates of the 4 corners
    """
    pass


if __name__ == "__main__":
   pass
