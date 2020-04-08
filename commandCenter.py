# Command Wrapper for python code

# Standard Imports

import datasets as DS # datasets.py

import borderoccurence as BS # borderoccurence.py

# FunctionVersions Imports
'''
[Usage]: pkgname.function()
[Example]: encodeBitHex.encode(usr/bin/bash/asdf/adsf/asdf.txt)
'''
from FunctionVersions.decodeHexBit import *

from FunctionVersions.encodeBitHex import *

from FunctionVersions.imageDataToCartesian import *

Verbose = True #

# TODO: Write function to rasterize hex color data

def updatePage(page):
    """
    The top-left square is the page number. You input your current "page color"
    into this function, which outputs the next "page color."
    """
    # TODO: Move this into encode.py and update encode.py accordingly
    pass

def displayStuff():
    """
    The one function we will run on the transmitting side.
    """

def scanning(path):
    """
    Scan the grid and stash all of the data somewhere.
    """
    # Image to Coordinates
    coordinates = imagetoCartesian(path, notflipped=False)

    # Coordinates To cropped Straigtened Coordinates
    if Verbose: print("Keep scanning comrade")
    '''if USER_EXITS:
        # User decides to stop scanning
        break'''

    # Find a point on the border
    borderStart = BS.findBorderStart(coordinates)
    if borderStart == None: #border start fails
        break

    # Find points along the inner edge of the border
    borderList = BS.borderTrace(borderStart, coordinates)
    if borderList == None:
        break

    # Find the corners of the grid
    top, bottom, left, right = BS.smoothenBorder(borderList)
    BL, TL, TR, BR = BS.findScreenPos(top, bottom, left, right)

    # Find where the page color is
    widthSqr = len(coordinates)
    heightSqr = len(coordinates[0])
    x, y = BS.sqrToCoord(0, 0, widthSqr, heightSqr, BL, BR, TL)
    if x == None or y == None:
        break


    # Straightened to Bits
    pageCol = coordinates[x][y]
    if pageCol = currentPage:
        # We're looking at proper data
        currentPage = updatePage(currentPage)
        data = []
        for j in range(height):
            for i in range(width):
                x, y = BS.sqrToCoord(0, 0, widthSqr, heightSqr, BL, BR, TL)
                color = coordinates[x][y]
                data.append(color)
        saveTheDataIntoAFileCauseItsCorrect(data)

    if Verbose: print(data)



def readTheData(lotsOfData):
    """
    All the scanning is done, and the data is stashed in some file. Read it and
    reconstruct the orignial file.
    """
    pass
