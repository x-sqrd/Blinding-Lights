# created by Shad0w7 + ChickenAgent2227

# ///////////////       |||||||||    //\\    \\\\\\ \\\\\\ \\\\\\ \\\\\\\\\
# //         //         ||          //  \\       \\     \\     \\       \\
# //////    //          ||         //    \\   \\\\\  \\\\\  \\\\\      \\
#     //   //           ||        //      \\  \\     \\     \\        \\
# //////  //            |||||||||//        \\ \\\\\\ \\\\\\ \\\\\\   \\


#TODO needs major debugging heck

# Shared Framework - (NOTE Do NOT make substantial changes to, or make new functions, as these base utilites are used by both editors/frameworks)



# Blinding BorderOccurence.py

import math
import time
import datasets as DS

# to use, check out the dataset you want to use, such as c.png, and the corresponding function, in this case, imageC(), in datasets, and run that
# for instance: >> print(DS.imageC()) to get the hexValue, check other ImageC functions for more!


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

# CHICKENAGENT2227
# Daniel's Framework
#


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
    """
        Purpose: Trace the inner edge of the black border, starting from borderStart
        Return: A list of tuples representing the inner edge of the black border, if found.
                If the path it follows just ends abruptly, return None.
                If it times out, return None.
    """
    # The maximum time the program is allowed to run until it force-exits. Tweak as needed.
    maxTime = 0.015

    startX = borderStart[0]
    startY = borderStart[1]
    currentX = startX
    currentY = startY
    borderList = [(startX, startY)]
    startTime  = time.time()
    while True:
        # print("–––––––––––––––––––––––––––––––––––")
        # print("Current coordinates: (%d, %d)" % (currentX, currentY))
        prevCheckingX = currentX + 2
        prevCheckingY = currentY
        checkingX = prevCheckingX
        checkingY = prevCheckingY + 1
        FIRST_TIME = True

        while True: # Find next point
            try:
                # print("Trying to check coordinates: (%d, %d)" % (checkingX, checkingY))
                # print("Previous coordinates: (%d, %d)" % (prevCheckingX, prevCheckingY))
                # print("That has color %s" % coordinates[checkingX][checkingY])
                if hexIsBlack(coordinates[checkingX][checkingY]) and not hexIsBlack(coordinates[prevCheckingX][prevCheckingY]) and not (checkingX, checkingY) == borderList[len(borderList) - 2]:
                    # The current point is black, but the previous point isn't. Bingo!
                    FIRST_TIME = False
                    currentX = checkingX
                    currentY = checkingY
                    borderList.append((currentX, currentY))
                    # print("Checking: (%d, %d) works!" % (checkingX, checkingY))
                    # print("Previous Checking: (%d, %d) has color %s" % (prevCheckingX, prevCheckingY, coordinates[prevCheckingX][prevCheckingY]))
                    break
                elif checkingX == currentX + 2 and checkingY == currentY + 1 and not FIRST_TIME:
                    # We did a full loop and didn't find anything useful. Something is off.
                    return None
                    # return None
                else:
                    # Didn't work, so we'll check different points and run the process again.
                    FIRST_TIME = False
                    prevCheckingX = checkingX
                    prevCheckingY = checkingY
                    deltaX = checkingX - currentX
                    deltaY = checkingY - currentY
                    deltaX, deltaY = calcNextPoint(deltaX, deltaY)
                    checkingX = currentX + deltaX
                    checkingY = currentY + deltaY
                    # print("Typical not work, moving onto checking (%d, %d)" % (checkingX, checkingY) )
                    # print("Previous coordinates: (%d, %d)" % (prevCheckingX, prevCheckingY))
            except IndexError:
                FIRST_TIME = False
                prevCheckingX = checkingX
                prevCheckingY = checkingY
                deltaX = checkingX - currentX
                deltaY = checkingY - currentY
                deltaX, deltaY = calcNextPoint(deltaX, deltaY)
                checkingX = currentX + deltaX
                checkingY = currentY + deltaY
                # print("Out of range, moving onto checking (%d, %d)" % (checkingX, checkingY) )
                # print("Previous coordinates: (%d, %d)" % (prevCheckingX, prevCheckingY))


        # Check if we've completed the loop
        if abs(startX - currentX) <= 1 and abs(startY - currentY) <= 1:
            return borderList

        if time.time() - startTime > maxTime:
            return None


def distBetween(aPoint, aNotherPoint):
    """ Uses the distance formula to find the distance between 2 points """
    deltaX = aNotherPoint[0] - aPoint[0]
    deltaY = aNotherPoint[1] - aPoint[1]
    dist = math.sqrt(deltaX**2 + deltaY**2)
    return dist

def smoothenBorder(borderList):
    """
    Finds the topmost, leftmost, bottommost, and rightmost points in a given list of points
    """
    top = borderList[0]
    bottom = borderList[0]
    left = borderList[0]
    right = borderList[0]

    for point in borderList:
        # Looking for topmost point
        if point[1] > top[1]:
            top = point
        elif point[1] == top[1] and point[0] > top[0]:
            # When in doubt, pick the rightmost one
            top = point

        # Looking for bottommost point
        if point[1] < bottom[1]:
            bottom = point
        elif point[1] == bottom[1] and point[0] < bottom[0]:
            # When in doubt, pick the leftmost one
            bottom = point

        # Looking for rightmost point
        if point[0] > right[0]:
            right = point
        elif point[0] == right[0] and point[1] < right[1]:
            # When in doubt, pick the bottommost one
            right = point

        # Looking for leftmost point
        if point[0] < left[0]:
            left = point
        elif point[0] == left[0] and point[1] > left[1]:
            # When in doubt, pick the topmost one
            left = point

    return top, bottom, left, right


def findScreenPos(top, bottom, left, right):
    """
    Interprets the output of smoothenBorder to figure out the screen's orientation.
    """
    BL = left       # Bottomleft point of the screen
    TL = top        # Topleft point of the screen
    TR = right      # Topright point of the screen
    BR = bottom     # Bottomright point of the screen
    if distBetween(bottom, left) >= distBetween(bottom, right):
        BL = bottom
        TL = left
        TR = top
        BR = right

    return BL, TL, TR, BR


def inverseSkew(x, y, skewConstantX, skewConstantY):
    # skewConstantX = ( BL[0] - TL[0] ) / ( BL[1] - TL[1] )
    # skewConstantY = ( BL[1] - BR[1] ) / ( BL[0] - BR[0] )
    newX = x + skewConstantX * y
    newY = y - skewConstantX * x
    return newX, newY

def sqrToCoord(xSqr, ySqr, widthSqr, heightSqr, BL, BR, TL):
    """
    Find the color of the square on the screen, that is xSqrth from the left and
    ySqrth from the bottom (starting from 0). The number of columns and rows in the
    UI are passed as widthSqr and heightSqr respectively.
    """
    # widthPixel and heightPixel are the width and height of the screen after skewing
    widthPixel = BR[0]
    heightPixel = TL[1]

    x = (xSqr + 0.5) * (widthPixel / widthSqr)
    y = (ySqr + 0.5) * (heightPixel / heightSqr)

    try:
        skewConstantX = ( BL[0] - TL[0] ) / ( BL[1] - TL[1] )
        skewConstantY = ( BL[1] - BR[1] ) / ( BL[0] - BR[0] )
    except ZeroDivisionError:
        return None # Something wack going on with the coordinates

    x, y = inverseSkew(x, y, skewConstantX, skewConstantY)

    x += BL[0]
    y += BL[1]

    return int(x), int(y) # The coordinates you need to check to find your desired square



if __name__ == "__main__":
    ### THE FOLLOWING IS DANIEL'S TEST CODE FOR REFERENCE ###
    # Assumes coordinates is already defined lol don't mess up there

    # borderStart = findBorderStart(coordinates)
    # # print(borderStart)
    # borderList = borderTrace(borderStart, coordinates)
    # # print(borderList)
    # # print("–––––––––––––––––––––")
    # top, bottom, left, right = smoothenBorder(borderList)
    # # print("Top: (%d, %d)" % top)
    # # print("Bottom: (%d, %d)" % bottom)
    # # print("Left: (%d, %d)" % left)
    # # print("Right: (%d, %d)" % right)
    #
    # BL, TL, TR, BR = findScreenPos(top, bottom, left, right)
    # print("BL: (%d, %d)" % BL)
    # print("TL: (%d, %d)" % TL)
    # print("BR: (%d, %d)" % BR)
    # print("TR: (%d, %d)" % TR)
    #
    # x, y = sqrToCoord(1, 1, 3, 3, BL, BR, TL)
    # print(x, y)
    pass
